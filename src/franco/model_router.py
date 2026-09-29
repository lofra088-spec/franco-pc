"""Low-latency request router with cache, breakers and timing telemetry."""
from __future__ import annotations
from collections import OrderedDict
import json, os, re, threading, time, urllib.request

def openai_compatible_provider(url, api_key, model, extra_headers=None):
    """Create a small OpenAI-compatible provider without another dependency."""
    if not api_key:
        return None
    def call(prompt, system=None, max_tokens=450, temperature=.65, **_):
        messages = []
        if system: messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        request = urllib.request.Request(url, data=json.dumps({
            "model": model, "messages": messages, "max_tokens": max_tokens,
            "temperature": temperature,
        }).encode(), headers={"Authorization": f"Bearer {api_key}",
                              "Content-Type": "application/json", **(extra_headers or {})})
        with urllib.request.urlopen(request, timeout=float(os.environ.get("FRANCO_AI_TIMEOUT", "120"))) as response:
            data = json.load(response)
        message = data["choices"][0]["message"]
        # Some OpenRouter routes put the usable text in reasoning/refusal while
        # returning a null content field. Preserve a useful response instead of
        # making the router treat a valid HTTP 200 as an empty failure.
        return (message.get("content") or message.get("reasoning") or
                message.get("refusal") or "").strip()
    return call

def environment_providers():
    providers = {}
    groq = openai_compatible_provider(
        "https://api.groq.com/openai/v1/chat/completions", os.getenv("GROQ_API_KEY", ""),
        os.getenv("FRANCO_GROQ_MODEL", "llama-3.1-8b-instant"))
    openrouter = openai_compatible_provider(
        "https://openrouter.ai/api/v1/chat/completions", os.getenv("OPENROUTER_API_KEY", ""),
        os.getenv("FRANCO_OPENROUTER_MODEL", os.getenv("FRANCO_OPENROUTER_FAST_MODEL", "openrouter/auto")),
        {"HTTP-Referer": os.getenv("FRANCO_SITE_URL", "http://127.0.0.1"),
         "X-Title": os.getenv("FRANCO_APP_TITLE", "FRANCO / Jarvis")})
    if groq: providers["groq"] = groq
    if openrouter: providers["openrouter"] = openrouter
    return providers


class LatencyRouter:
    def __init__(self, providers, logger=None, cache_size=128, ttl=300):
        self.providers = {k: v for k, v in providers.items() if v}
        self.logger, self.cache_size, self.ttl = logger, cache_size, ttl
        self._cache, self._breakers, self._metrics = OrderedDict(), {}, []
        self._lock = threading.RLock()

    def is_available(self):
        return bool(self.providers)

    @staticmethod
    def classify(prompt):
        low = prompt.lower()
        if len(prompt) > 1200 or re.search(r"\b(architettura|analizza in profondità|debug complesso|progetto completo)\b", low):
            return "complex"
        if len(prompt) < 180 and not re.search(r"\b(codice|analizza|confronta|pianifica|spiega)\b", low):
            return "fast"
        return "standard"

    def _order(self, kind):
        requested = {"fast": ("groq", "openrouter", "local", "default"),
                     "standard": ("openrouter", "groq", "default", "local"),
                     "complex": ("openrouter", "default", "groq", "local")}[kind]
        ordered = [name for name in requested if name in self.providers]
        # Custom providers used by plugins and tests remain usable even when
        # they are not part of the built-in latency preference table.
        return ordered or list(self.providers)

    def _usable(self, name):
        state = self._breakers.get(name, {})
        return state.get("open_until", 0) <= time.monotonic()

    def _fail(self, name):
        state = self._breakers.setdefault(name, {"failures": 0, "open_until": 0})
        state["failures"] += 1
        if state["failures"] >= 3:
            state["open_until"] = time.monotonic() + 30

    def _ok(self, name):
        self._breakers[name] = {"failures": 0, "open_until": 0}

    def chat(self, prompt, system=None, max_tokens=450, temperature=.65,
             task_type=None, stream_callback=None, **kwargs):
        kind = self.classify(prompt)
        key = (kind, system or "", prompt, max_tokens, round(float(temperature), 2))
        now = time.monotonic()
        with self._lock:
            cached = self._cache.get(key)
            if cached and now - cached[0] < self.ttl:
                self._cache.move_to_end(key)
                return cached[1]
        last_error = None
        for name in self._order(kind):
            if not self._usable(name):
                continue
            started = time.perf_counter()
            try:
                result = self.providers[name](prompt=prompt, system=system,
                    max_tokens=max_tokens, temperature=temperature,
                    task_type=task_type, **kwargs)
                result = str(result or "").strip()
                if not result:
                    raise RuntimeError("risposta vuota")
                elapsed = time.perf_counter() - started
                if stream_callback:
                    for part in re.findall(r"\S+\s*", result):
                        stream_callback(part)
                metric = {"class": kind, "provider": name, "latency_s": round(elapsed, 3),
                          "tokens_per_s": round(len(result.split()) / max(.001, elapsed), 1),
                          "timestamp": time.time()}
                with self._lock:
                    self._metrics = (self._metrics + [metric])[-100:]
                    self._cache[key] = (now, result)
                    self._cache.move_to_end(key)
                    while len(self._cache) > self.cache_size:
                        self._cache.popitem(last=False)
                self._ok(name)
                return result
            except Exception as error:
                last_error = error
                self._fail(name)
        raise RuntimeError(f"Nessun modello disponibile: {last_error}")

    def metrics(self):
        with self._lock:
            return list(self._metrics)
