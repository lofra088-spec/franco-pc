"""Lightweight, thread-safe TTL/LRU cache with explicit shutdown."""
import math
import threading
import time
from collections import OrderedDict, defaultdict
from typing import Any, Callable, Dict, Optional

CACHE_MAX_SIZE = 1000
CACHE_DEFAULT_TTL = 3600
CACHE_CLEANUP_INTERVAL = 600
__all__ = ["CacheManager"]

class CacheManager:
    """
    Sistema di caching intelligente con:
    - TTL (time-to-live) per ogni entry
    - LRU eviction policy
    - Limite dimensione configurabile
    - Pulizia automatica asincrona
    - Statistiche dettagliate
    - Thread-safe
    """
    
    def __init__(self, max_size: int = CACHE_MAX_SIZE,
                 default_ttl: int = CACHE_DEFAULT_TTL,
                 cleanup_interval: int = CACHE_CLEANUP_INTERVAL):
        if not isinstance(max_size, int) or isinstance(max_size, bool) or max_size < 1:
            raise ValueError("max_size deve essere un intero positivo")
        if not math.isfinite(cleanup_interval) or cleanup_interval <= 0:
            raise ValueError("cleanup_interval deve essere positivo e finito")
        self._stop_event = threading.Event()
        self._compute_locks = [threading.RLock() for _ in range(64)]
        self._cache: OrderedDict = OrderedDict()
        self._timestamps: Dict[str, float] = {}
        self._ttls: Dict[str, int] = {}
        self._hit_count: Dict[str, int] = defaultdict(int)
        self._lock = threading.RLock()
        self.max_size = max_size
        self.default_ttl = default_ttl
        self.cleanup_interval = cleanup_interval
        
        self._stats = {
            "hits": 0,
            "misses": 0,
            "evictions": 0,
            "expirations": 0,
            "sets": 0,
        }
        
        self._running = True
        self._cleanup_thread = threading.Thread(
            target=self._cleanup_loop, daemon=True, name="CacheCleanup"
        )
        self._cleanup_thread.start()
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get value from cache (with LRU update)"""
        with self._lock:
            if key not in self._cache:
                self._stats["misses"] += 1
                return default
            
            if self._is_expired(key):
                self._remove(key)
                self._stats["expirations"] += 1
                self._stats["misses"] += 1
                return default
            
            self._cache.move_to_end(key)
            self._stats["hits"] += 1
            self._hit_count[key] += 1
            return self._cache[key]
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        """Set value in cache with optional TTL"""
        with self._lock:
            if key not in self._cache and len(self._cache) >= self.max_size:
                self._cleanup_expired()
                if len(self._cache) >= self.max_size:
                    self._evict_lru()
            
            self._cache[key] = value
            self._cache.move_to_end(key)
            self._timestamps[key] = time.monotonic()
            self._ttls[key] = ttl if ttl is not None else self.default_ttl
            self._stats["sets"] += 1
    
    def delete(self, key: str) -> bool:
        with self._lock:
            if key in self._cache:
                self._remove(key)
                return True
            return False
    
    def clear(self):
        with self._lock:
            self._cache.clear()
            self._timestamps.clear()
            self._ttls.clear()
            self._hit_count.clear()
    
    def has(self, key: str) -> bool:
        with self._lock:
            if key not in self._cache:
                return False
            if self._is_expired(key):
                self._remove(key)
                self._stats["expirations"] += 1
                return False
            return True
    
    def _is_expired(self, key: str) -> bool:
        if key not in self._timestamps:
            return True
        ttl = self._ttls.get(key, self.default_ttl)
        if ttl <= 0:
            return False
        return (time.monotonic() - self._timestamps[key]) >= ttl
    
    def _remove(self, key: str):
        self._cache.pop(key, None)
        self._timestamps.pop(key, None)
        self._ttls.pop(key, None)
        self._hit_count.pop(key, None)
    
    def _evict_lru(self):
        if self._cache:
            key = next(iter(self._cache))
            self._remove(key)
            self._stats["evictions"] += 1
    
    def _cleanup_loop(self):
        while not self._stop_event.wait(self.cleanup_interval):
            self._cleanup_expired()
    
    def _cleanup_expired(self):
        with self._lock:
            expired_keys = [k for k in list(self._cache.keys()) if self._is_expired(k)]
            for key in expired_keys:
                self._remove(key)
                self._stats["expirations"] += 1
    
    def get_or_compute(self, key: str, compute_func: Callable,
                       ttl: Optional[int] = None) -> Any:
        """Get from cache, or compute and store if missing"""
        # Bounded lock stripes prevent duplicate concurrent work for the same key.
        # They are separate from the cache lock so other reads remain responsive.
        missing = object()
        with self._compute_locks[hash(key) % len(self._compute_locks)]:
            value = self.get(key, missing)
            if value is not missing:
                return value
            value = compute_func()
            self.set(key, value, ttl)
            return value
    
    def get_statistics(self) -> Dict:
        with self._lock:
            total = self._stats["hits"] + self._stats["misses"]
            hit_rate = (self._stats["hits"] / total * 100) if total > 0 else 0
            return {
                "size": len(self._cache),
                "max_size": self.max_size,
                "hits": self._stats["hits"],
                "misses": self._stats["misses"],
                "hit_rate": round(hit_rate, 2),
                "evictions": self._stats["evictions"],
                "expirations": self._stats["expirations"],
                "sets": self._stats["sets"],
                "top_keys": sorted(
                    self._hit_count.items(),
                    key=lambda x: x[1], reverse=True
                )[:10],
            }
    
    def shutdown(self):
        self._running = False
        self._stop_event.set()
        if threading.current_thread() is not self._cleanup_thread:
            self._cleanup_thread.join(timeout=2)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.shutdown()
