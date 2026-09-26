"""Regression tests without starting the assistant's services or loading SDKs.

Run: python -m unittest discover -s tests -p test_runtime_regressions.py -v
The legacy classes are compiled from their actual AST with only standard-library
dependencies, so the tests cannot start trading, voice, or mobile integrations.
"""
import ast
import asyncio
from concurrent.futures import ThreadPoolExecutor
import contextlib
import copy
from enum import IntEnum
import importlib
import io
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import time
import typing
import unittest
from unittest.mock import patch
import uuid
from collections import OrderedDict, defaultdict, deque

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


def load_classes(path):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names = {"CacheManager", "ConfigurationManager", "EventBus", "EventData", "merge_dicts", "atomic_write"}
    selected = [n for n in tree.body if isinstance(n, (ast.ClassDef, ast.FunctionDef)) and n.name in names]
    from dataclasses import dataclass, field
    from datetime import datetime
    class Priority(IntEnum):
        NORMAL = 1
        HIGHEST = 5
    namespace = dict(vars(typing), **globals())
    namespace.update(CACHE_MAX_SIZE=1000, CACHE_DEFAULT_TTL=3600, CACHE_CLEANUP_INTERVAL=600,
                     CONFIG_FILE=Path("unused.json"), __version__="6.0.0", WAKE_WORDS=["franco"],
                     UI_WIDTH=1200, UI_HEIGHT=800, USER_AGENT="test", Priority=Priority,
                     dataclass=dataclass, field=field, datetime=datetime, contextmanager=contextlib.contextmanager)
    exec(compile(ast.Module(body=selected, type_ignores=[]), str(path), "exec"), namespace)
    return namespace


class RuntimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.variants = [load_classes(ROOT / "src/franco/_monolith.py")]
        # The historical monolith lives beside the original checkout and is
        # intentionally not required in a clean GitHub clone.
        legacy = ROOT.parent / "francov6reall.py"
        if legacy.is_file():
            cls.variants.append(load_classes(legacy))
        cls.variants[0]["CacheManager"] = importlib.import_module("franco.core.cache").CacheManager

    def test_cache_none_and_single_concurrent_computation(self):
        for variant in self.variants:
            with self.subTest(variant=variant["CacheManager"].__module__), variant["CacheManager"]() as cache:
                calls = []
                def compute():
                    calls.append(1)
                    time.sleep(0.02)
                    return None
                with ThreadPoolExecutor(max_workers=8) as pool:
                    self.assertEqual(list(pool.map(lambda _: cache.get_or_compute("same", compute), range(20))), [None] * 20)
                self.assertEqual(len(calls), 1)

    def test_cache_expiration_and_lru(self):
        for variant in self.variants:
            with variant["CacheManager"](max_size=2) as cache, patch.object(time, "monotonic", return_value=100) as clock:
                cache.set("keep", 1, ttl=100)
                cache.set("expired", 2, ttl=1)
                clock.return_value = 101
                cache.set("new", 3)
                self.assertEqual(cache.get("keep"), 1)
                self.assertFalse(cache.has("expired"))
                self.assertEqual(cache.get_statistics()["expirations"], 1)
                self.assertEqual(cache.get_statistics()["evictions"], 0)
                cache.set("last", 4)
                self.assertFalse(cache.has("new"))

    def test_cache_shutdown_and_invalid_settings(self):
        for variant in self.variants:
            cache_type = variant["CacheManager"]
            for kwargs in ({"max_size": 0}, {"max_size": -1}, {"cleanup_interval": 0}, {"cleanup_interval": float("nan")}):
                with self.assertRaises(ValueError):
                    cache_type(**kwargs)
            cache = cache_type(cleanup_interval=600)
            cache.shutdown()
            cache.shutdown()
            self.assertFalse(cache._cleanup_thread.is_alive())

    def test_failed_compute_can_retry(self):
        for variant in self.variants:
            with variant["CacheManager"]() as cache:
                def fail():
                    raise RuntimeError("expected")
                with self.assertRaises(RuntimeError):
                    cache.get_or_compute("retry", fail)
                self.assertEqual(cache.get_or_compute("retry", lambda: 42), 42)

    def test_config_defensive_copies_and_persistence(self):
        for variant in self.variants:
            with tempfile.TemporaryDirectory() as directory:
                config = variant["ConfigurationManager"](str(Path(directory) / "config.json"))
                supplied = ["one"]
                config.set("custom.items", supplied)
                supplied.append("two")
                config.get("custom.items").append("three")
                self.assertEqual(config.get("custom.items"), ["one"])
                self.assertEqual(variant["ConfigurationManager"](config.config_path).get("custom.items"), ["one"])
                for key in ("", "a..b", ".a", "a."):
                    with self.assertRaises(ValueError):
                        config.set(key, 1)

    def test_invalid_config_keeps_last_good_state(self):
        for variant in self.variants:
            with tempfile.TemporaryDirectory() as directory:
                config = variant["ConfigurationManager"](Path(directory) / "config.json")
                config.set("voice.volume", 0.3)
                for content in ('{broken', '[]', '{"voice": false}'):
                    config.config_path.write_text(content, encoding="utf-8")
                    with contextlib.redirect_stdout(io.StringIO()):
                        self.assertFalse(config._load())
                    self.assertEqual(config.get("voice.volume"), 0.3)
                config.config_path.write_text('{"voice": {"volume": 0.7}}', encoding="utf-8-sig")
                # Atomic restores can carry older timestamps, which must also reload.
                os.utime(config.config_path, ns=(1_000_000_000, 1_000_000_000))
                self.assertTrue(config.reload())
                self.assertEqual(config.get("voice.volume"), 0.7)
                self.assertFalse(config.reload())

    def test_defaults_and_observers_are_isolated(self):
        for variant in self.variants:
            with tempfile.TemporaryDirectory() as directory:
                cls = variant["ConfigurationManager"]
                before = copy.deepcopy(cls.DEFAULT_CONFIG)
                config = cls(Path(directory) / "config.json")
                config._load()
                config.set("voice.enabled", False, save=False)
                def observer(key, old, value):
                    value.append("observer")
                config.add_observer(observer)
                config.set("custom.items", [], save=False)
                self.assertEqual(config.get("custom.items"), [])
                self.assertEqual(cls.DEFAULT_CONFIG, before)

    def test_async_unsubscribe(self):
        for variant in self.variants:
            bus = variant["EventBus"]()
            calls = []
            async def callback(event):
                calls.append(event)
            bus.subscribe_async("test", callback)
            bus.unsubscribe("test", callback)
            asyncio.run(bus.emit_async("test"))
            self.assertEqual(calls, [])

    def test_lightweight_import_and_doctor(self):
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONIOENCODING="utf-8")
        code = "import franco, sys; from franco.core.cache import CacheManager; assert franco.__version__; assert 'franco._monolith' not in sys.modules"
        subprocess.run([sys.executable, "-c", code], env=env, check=True, capture_output=True, timeout=10)
        result = subprocess.run([sys.executable, "-m", "franco", "--doctor", "--json"], env=env, check=True, capture_output=True, text=True, encoding="utf-8", timeout=10)
        report = json.loads(result.stdout)
        self.assertEqual(report["summary"]["error"], 0)
        self.assertGreater(len(report["checks"]), 10)
        result = subprocess.run([sys.executable, str(ROOT.parent / "avvia_franco.py"), "--version"], env=env, check=True, capture_output=True, text=True, timeout=10)
        self.assertEqual(result.stdout.strip(), "FRANCO 6.0.0 NEXUS")


if __name__ == "__main__":
    unittest.main()
