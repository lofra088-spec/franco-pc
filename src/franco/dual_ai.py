"""
╔══════════════════════════════════════════════════════════════════════════════╗
║         FRANCO 6.0 — PATCH DUAL AI (OpenRouter + Claude fallback)            ║
║                                                                              ║
║  Gerarchia provider:                                                         ║
║    1. OpenRouter  →  accesso a 200+ modelli (GPT-4o, Gemini, Mistral, ecc)  ║
║    2. Claude      →  fallback se OpenRouter non disponibile / errore         ║
║                                                                              ║
║  Variabili d'ambiente:                                                       ║
║    OPENROUTER_API_KEY   → chiave OpenRouter  (obbligatoria per OR)           ║
║    CLAUDE_API_KEY       → chiave Anthropic   (fallback)                      ║
║    FRANCO_AI            → "openrouter" | "claude" | "auto" (default: auto)  ║
║    OPENROUTER_MODEL     → modello OpenRouter (default: google/gemini-2.5-flash-preview-05-20)     ║
║                                                                              ║
║  Compatibilità: drop-in replacement di MistralAIClient                      ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

from __future__ import annotations

import os
import re
import time
import json
import threading
import traceback
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ──────────────────────────────────────────────────────────────────────────────
# COSTANTI
# ──────────────────────────────────────────────────────────────────────────────

OPENROUTER_BASE = "https://openrouter.ai/api/v1/chat/completions"

# Modello di default — cambia qui o con la variabile OPENROUTER_MODEL
DEFAULT_OR_MODEL = os.environ.get(
    "OPENROUTER_MODEL",
    "nvidia/nemotron-3-ultra-550b-a55b:free"   # ottimo rapporto qualità/costo
)

# Modelli consigliati per diversi use-case (usabili con set_model())
OPENROUTER_MODELS = {
    # ── Gratuiti / quasi gratuiti ────────────────────────────────────────
    "nvidia-nemotron": "nvidia/nemotron-3-ultra-550b-a55b:free",
    "gemini-flash":      "google/gemini-2.5-flash",
    "gemini-pro":        "google/gemini-2.5-pro",
    "mistral-small":     "mistralai/mistral-small-3.2-24b-instruct:free",
    "mistral-medium":    "mistralai/mistral-medium-3",
    "llama-70b":         "meta-llama/llama-3.3-70b-instruct",
    "llama-free":        "meta-llama/llama-3.3-70b-instruct:free",
    "deepseek-r1":       "deepseek/deepseek-r1-0528:free",
    "deepseek-v3":       "deepseek/deepseek-chat-v3.1:free",
    "qwen-235b":         "qwen/qwen3-235b-a22b:free",
    "qwen-30b":          "qwen/qwen3-30b-a3b:free",
    # ── A pagamento (alta qualità) ───────────────────────────────────────
    "gpt-4o":            "openai/gpt-4o",
    "gpt-4o-mini":       "openai/gpt-4o-mini",
    "gpt-4.1":           "openai/gpt-4.1",
    "o3-mini":           "openai/o3-mini",
    "claude-sonnet":     "anthropic/claude-sonnet-4-5",
    "claude-opus":       "anthropic/claude-opus-4",
    "gemini-ultra":      "google/gemini-2.5-pro",
    "mistral-large":     "mistralai/mistral-large-2411",
}

# Timeout e retry
_DEFAULT_TIMEOUT  = 60   # secondi
_DEFAULT_MAX_RETRY = 3
_RETRY_BACKOFF     = 1.5

# ──────────────────────────────────────────────────────────────────────────────
# LOGGER DUMMY (se StructuredLogger non è disponibile)
# ──────────────────────────────────────────────────────────────────────────────

class _DummyLogger:
    def _log(self, tag, msg, level=""):
        ts = datetime.now().strftime("%H:%M:%S")
        prefix = f"[{ts}] [{level}] [{tag}]" if level else f"[{ts}] [{tag}]"
        print(f"{prefix} {msg}")
    def info(self, tag, msg, **kw):    self._log(tag, msg, "INFO")
    def debug(self, tag, msg, **kw):   self._log(tag, msg, "DEBUG")
    def warning(self, tag, msg, **kw): self._log(tag, msg, "WARN")
    def error(self, tag, msg, **kw):   self._log(tag, msg, "ERROR")
    def success(self, tag, msg, **kw): self._log(tag, msg, "OK")
    def exception(self, tag, msg, exc=None, **kw):
        self._log(tag, msg, "ERROR")
        if exc:
            traceback.print_exc()


# ──────────────────────────────────────────────────────────────────────────────
# OPENROUTER CLIENT
# ──────────────────────────────────────────────────────────────────────────────

class OpenRouterClient:
    """
    Client OpenRouter — compatibile con l'API OpenAI.
    Supporta 200+ modelli con un'unica chiave API.

    Caratteristiche:
      - Retry automatico con backoff esponenziale
      - Tracking token e costo
      - Rate limiting automatico (rispetta gli header OR)
      - Timeout configurabile
      - Context window variabile per modello
    """

    def __init__(self,
                 api_key:   str  = "",
                 model:     str  = DEFAULT_OR_MODEL,
                 logger            = None,
                 timeout:   int  = _DEFAULT_TIMEOUT,
                 max_retry: int  = _DEFAULT_MAX_RETRY,
                 site_url:  str  = "https://github.com/franco-ai",
                 site_name: str  = "FRANCO 6.0 NEXUS"):

        self.api_key   = (api_key or os.environ.get("OPENROUTER_API_KEY", "")).strip()
        self.model     = model
        self.logger    = logger or _DummyLogger()
        self.timeout   = timeout
        self.max_retry = max_retry
        self.site_url  = site_url
        self.site_name = site_name

        self._total_tokens   = 0
        self._total_calls    = 0
        self._total_cost_usd = 0.0
        self._lock           = threading.Lock()
        self._last_call_ts   = 0.0
        self._rate_limit_wait = 0.0  # secondi da attendere dopo 429

        if self.api_key:
            masked = ("..." + self.api_key[-4:]) if len(self.api_key) > 4 else "????"
            self.logger.success("OR",
                f"OpenRouterClient pronto  →  modello: {self.model}  "
                f"(chiave termina con: {masked}, lunghezza: {len(self.api_key)})")
        else:
            self.logger.warning("OR", "OPENROUTER_API_KEY non impostata — client disabilitato")

    # ── Utilità ───────────────────────────────────────────────────────────

    def is_available(self) -> bool:
        return bool(self.api_key)

    def set_model(self, model_alias_or_id: str):
        """Cambia modello (alias o ID completo)."""
        resolved = OPENROUTER_MODELS.get(model_alias_or_id, model_alias_or_id)
        self.model = resolved
        self.logger.info("OR", f"Modello → {self.model}")

    def list_models(self) -> Dict[str, str]:
        """Ritorna dizionario alias → ID dei modelli predefiniti."""
        return dict(OPENROUTER_MODELS)

    def get_statistics(self) -> Dict[str, Any]:
        with self._lock:
            return {
                "provider":      "openrouter",
                "model":         self.model,
                "total_calls":   self._total_calls,
                "total_tokens":  self._total_tokens,
                "total_cost_usd": round(self._total_cost_usd, 6),
                "available":     self.is_available(),
            }

    # ── Chiamata HTTP ─────────────────────────────────────────────────────

    def _call_api(self,
                  messages:    List[Dict],
                  max_tokens:  int   = 2000,
                  temperature: float = 0.85,
                  model:       str   = None) -> Tuple[str, int, int]:
        """
        Chiama l'API OpenRouter.
        Ritorna (testo_risposta, input_tokens, output_tokens).
        Solleva eccezione in caso di errore non recuperabile.
        """
        if not self.is_available():
            raise RuntimeError("OpenRouter non configurato (API key mancante)")

        model = model or self.model
        payload = json.dumps({
            "model":       model,
            "messages":    messages,
            "max_tokens":  max_tokens,
            "temperature": temperature,
        }).encode("utf-8")

        headers = {
            "Content-Type":  "application/json",
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer":  self.site_url,
            "X-Title":       self.site_name,
        }

        req = urllib.request.Request(
            OPENROUTER_BASE,
            data=payload,
            headers=headers,
            method="POST"
        )

        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                body = resp.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            code = e.code

            # Rate limit → leggi Retry-After
            if code == 429:
                retry_after = float(e.headers.get("Retry-After", 5))
                self._rate_limit_wait = retry_after
                raise RuntimeError(f"Rate limit OpenRouter — riprova tra {retry_after:.0f}s")

            raise RuntimeError(f"HTTP {code} OpenRouter: {body[:200]}")

        data = json.loads(body)

        if "error" in data:
            raise RuntimeError(f"OpenRouter error: {data['error']}")

        choices = data.get("choices", [])
        if not choices:
            raise RuntimeError("OpenRouter: nessuna scelta nella risposta")

        text = (choices[0].get("message", {}).get("content")
                or choices[0].get("text", "")).strip()

        usage = data.get("usage", {})
        inp   = int(usage.get("prompt_tokens", 0))
        out   = int(usage.get("completion_tokens", 0))

        return text, inp, out

    # ── Chat pubblica con retry ────────────────────────────────────────────

    def chat(self,
             prompt:      str,
             system:      str   = None,
             max_tokens:  int   = 2000,
             temperature: float = 0.85,
             model:       str   = None) -> str:
        """
        Invia un messaggio e ritorna la risposta testuale.
        Gestisce retry automatici con backoff esponenziale.
        """
        if not self.is_available():
            self.logger.error("OR",
                "Tentativo di chiamata con OPENROUTER_API_KEY vuota/non impostata. "
                "Verifica che la variabile d'ambiente sia impostata PRIMA di avviare FRANCO "
                "(stesso terminale, senza spazi attorno a '=').")
            return "OpenRouter non disponibile (API key mancante)."

        messages: List[Dict] = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        last_exc: Optional[Exception] = None
        delay = 1.0

        for attempt in range(1, self.max_retry + 1):
            # Rispetta rate limit segnalato
            if self._rate_limit_wait > 0:
                time.sleep(self._rate_limit_wait)
                self._rate_limit_wait = 0.0

            try:
                start = time.perf_counter()
                text, inp, out = self._call_api(
                    messages, max_tokens, temperature, model
                )
                elapsed = time.perf_counter() - start

                with self._lock:
                    self._total_tokens += inp + out
                    self._total_calls  += 1

                self.logger.debug("OR",
                    f"OK  {inp+out} tok  {elapsed:.2f}s  [{self.model}]")
                return text

            except Exception as exc:
                last_exc = exc
                self.logger.warning("OR",
                    f"Tentativo {attempt}/{self.max_retry} fallito: {exc}")
                if attempt < self.max_retry:
                    time.sleep(delay)
                    delay *= _RETRY_BACKOFF

        self.logger.error("OR", f"Tutti i tentativi falliti: {last_exc}")
        return f"[OpenRouter errore] {str(last_exc)[:150]}"

    def chat_with_image(self,
                        prompt:     str,
                        image_b64:  str,
                        system:     str = None,
                        max_tokens: int = 1000) -> str:
        """Vision: invia immagine in base64 + testo."""
        if not self.is_available():
            return "OpenRouter non disponibile."

        messages: List[Dict] = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({
            "role": "user",
            "content": [
                {"type": "image_url",
                 "image_url": {"url": f"data:image/png;base64,{image_b64}"}},
                {"type": "text", "text": prompt},
            ]
        })

        try:
            text, _, _ = self._call_api(messages, max_tokens, 0.5)
            return text
        except Exception as e:
            return f"[Vision error] {e}"


# ──────────────────────────────────────────────────────────────────────────────
# ALIAS: MistralAIClient → OpenRouterClient
# (mantenuto per retrocompatibilità con i vecchi import)
# ──────────────────────────────────────────────────────────────────────────────

class MistralAIClient(OpenRouterClient):
    """
    Alias retrocompatibile con il vecchio MistralAIClient.
    Ora usa OpenRouter internamente.
    """
    def __init__(self, api_key: str = "", logger=None, **kwargs):
        # Accetta sia OPENROUTER_API_KEY che MISTRAL_API_KEY come fallback
        key = (api_key
               or os.environ.get("OPENROUTER_API_KEY", "")
               or os.environ.get("MISTRAL_API_KEY", "")).strip()
        super().__init__(api_key=key, logger=logger, **kwargs)


# ──────────────────────────────────────────────────────────────────────────────
# DUAL AI ROUTER
# ──────────────────────────────────────────────────────────────────────────────

_FAILURE_MARKERS = (
    "nessun modello ha risposto",       # OmniAI: tutti i modelli gratuiti esauriti/occupati
    "openrouter non disponibile",       # OmniAI: manca la chiave o requests non installato
    "connectionerror", "connection refused",
    "failed to establish a new connection",
    # errori dei client cloud restituiti come stringa (non sollevati):
    # senza questi il messaggio d'errore veniva "parlato" come se fosse
    # una risposta valida, e il locale non veniva mai raggiunto.
    "ai non disponibile", "verifica la configurazione",
    "api key mancante", "non disponibile (api key",
    "errore di autenticazione", "limite richieste raggiunto",
    "read timed out", "timed out", "risposta non disponibile",
)


def _looks_like_failure(result: str) -> bool:
    """Rileva risposte-non-risposte del cloud: quota/crediti esauriti,
    nessuna connessione, o un messaggio di errore mascherato da stringa
    (i client qui non sollevano sempre eccezioni, a volte restituiscono
    testo d'errore come se fosse una risposta valida)."""
    r = result.strip().lower()
    if not r:
        return True
    if r.startswith("[") and "errore" in r:
        return True
    return any(marker in r for marker in _FAILURE_MARKERS)

class DualAIRouter:
    """
    Router intelligente tra OpenRouter e Claude.

    Logica di selezione (variabile FRANCO_AI):
      "openrouter" → sempre OpenRouter
      "claude"     → sempre Claude (Anthropic)
      "auto"       → OpenRouter se disponibile, Claude come fallback
                     (oppure viceversa in base a `default_ai`)

    Il router può essere istruito per task-type:
      router.set_preference("code",     "openrouter")
      router.set_preference("security", "claude")

    Selezione automatica per token:
      se la risposta di OR è vuota / errore → fallback automatico a Claude.
    """

    def __init__(self,
                 claude_client,
                 openrouter_client: Optional[OpenRouterClient] = None,
                 mistral_client:    Optional[OpenRouterClient] = None,
                 local_client       = None,
                 logger             = None,
                 default_ai:  str  = "auto"):

        self.claude     = claude_client
        # Accetta sia il nuovo openrouter_client che il vecchio mistral_client
        self.openrouter: Optional[OpenRouterClient] = (
            openrouter_client or mistral_client
        )
        # LLM locale (FrancoLocalAI, es. Llama-3.1-8B): offline, nessuna
        # quota, ma piu' lento/meno capace dei modelli cloud. Provider
        # "local" nel routing sotto.
        self.local = local_client
        self.logger     = logger or _DummyLogger()
        self.default_ai = os.environ.get("FRANCO_AI", default_ai).lower()

        # Preferenze per categoria di task
        self._task_prefs: Dict[str, str] = {}

        # Statistiche
        self._stats = {
            "openrouter": 0,
            "claude":     0,
            "local":      0,
            "fallback":   0,
        }

        self._log_init()

    def _log_init(self):
        or_ok  = self.openrouter and self.openrouter.is_available()
        cl_ok  = self.claude and self.claude.is_available()
        self.logger.success("ROUTER",
            f"DualAIRouter  OpenRouter={'✓' if or_ok else '✗'}"
            f"  Claude={'✓' if cl_ok else '✗'}"
            f"  default={self.default_ai}")

    # ── Configurazione ────────────────────────────────────────────────────

    def set_preference(self, task_type: str, provider: str):
        """Imposta provider preferito per un tipo di task."""
        self._task_prefs[task_type.lower()] = provider.lower()

    def set_model(self, model_alias_or_id: str):
        """Cambia modello OpenRouter (alias o ID completo)."""
        if self.openrouter:
            self.openrouter.set_model(model_alias_or_id)

    def prefer_openrouter(self):
        """Imposta OpenRouter come provider principale."""
        self.default_ai = "openrouter"
        self.logger.info("ROUTER", "Provider principale → OpenRouter")

    def prefer_claude(self):
        """Imposta Claude come provider principale."""
        self.default_ai = "claude"
        self.logger.info("ROUTER", "Provider principale → Claude")

    def prefer_local(self):
        """Imposta il modello locale (es. Llama-3.1-8B) come provider
        principale: offline, nessuna quota, ma piu' lento/meno capace."""
        self.default_ai = "local"
        self.logger.info("ROUTER", "Provider principale → Locale (offline)")

    # ── Selezione provider ────────────────────────────────────────────────

    def _pick_provider(self, task_type: str = None) -> str:
        """Determina il provider da usare per questa richiesta."""
        # 1. Preferenza per task specifico
        if task_type and task_type.lower() in self._task_prefs:
            return self._task_prefs[task_type.lower()]

        # 2. Variabile FRANCO_AI o default_ai
        pref = self.default_ai

        or_ok  = bool(self.openrouter and self.openrouter.is_available())
        cl_ok  = bool(self.claude and self.claude.is_available())
        lo_ok  = bool(self.local is not None)

        if pref == "local":
            return "local" if lo_ok else ("openrouter" if or_ok else "claude")
        if pref == "openrouter":
            return "openrouter" if or_ok else "claude"
        if pref == "claude":
            return "claude" if cl_ok else "openrouter"

        # auto: OpenRouter prima (più economico/versatile), poi Claude
        if or_ok:
            return "openrouter"
        if cl_ok:
            return "claude"
        return "openrouter"   # uno dei due dovrà gestire l'errore

    # ── Chiamata principale ───────────────────────────────────────────────

    def chat(self,
             prompt:      str,
             system:      str   = None,
             max_tokens:  int   = 2000,
             temperature: float = 0.85,
             task_type:   str   = None,
             model:       str   = None) -> str:
        """
        Invia prompt al provider selezionato.
        Se il provider primario fallisce → fallback automatico all'altro.
        """
        primary = self._pick_provider(task_type)

        def _usable(p: str) -> bool:
            # Un provider è utilizzabile solo se può DAVVERO rispondere:
            # per il cloud serve is_available() (chiave presente), non basta
            # che l'oggetto client esista — altrimenti un Claude senza chiave
            # verrebbe scelto come fallback e restituirebbe solo un errore.
            if p == "openrouter":
                return bool(self.openrouter and self.openrouter.is_available())
            if p == "claude":
                return bool(self.claude and self.claude.is_available())
            if p == "local":
                return self.local is not None
            return False

        # Ordine di tentativo: il provider scelto, poi tutti gli altri
        # realmente utilizzabili, col LOCALE come ultima rete di sicurezza
        # (offline, nessuna quota). Si scende lungo la catena finché uno
        # risponde davvero — così se il cloud va in timeout/quota, la
        # domanda finisce sul Llama locale invece di un "AI non disponibile".
        order = [primary] + [p for p in ("openrouter", "claude", "local") if p != primary]
        order = [p for p in order if _usable(p)]
        if not order and self.local is not None:
            order = ["local"]   # ultimo appiglio assoluto

        result = ""
        for i, provider in enumerate(order):
            if i > 0:
                self.logger.warning("ROUTER",
                    f"Provider precedente ha risposto male → fallback a '{provider}'")
                self._stats["fallback"] += 1
            result = self._try_provider(
                provider, prompt, system, max_tokens, temperature,
                model=(model if i == 0 else None),
            )
            if result and not _looks_like_failure(result):
                return result

        return result or "Risposta non disponibile da nessun provider AI."

    def _try_provider(self, provider: str,
                      prompt:      str,
                      system:      str   = None,
                      max_tokens:  int   = 2000,
                      temperature: float = 0.85,
                      model:       str   = None) -> str:
        try:
            if provider == "openrouter" and self.openrouter:
                self._stats["openrouter"] += 1
                return self.openrouter.chat(
                    prompt, system, max_tokens, temperature, model=model
                )
            elif provider == "claude" and self.claude:
                self._stats["claude"] += 1
                return self.claude.chat(
                    prompt, system, max_tokens, temperature
                )
            elif provider == "local" and self.local:
                self._stats["local"] += 1
                if not self.local.has_real_llm:
                    self.local.ensure_real_llm_loaded(timeout=60)
                kwargs = {"max_tokens": max_tokens, "temperature": temperature}
                if system:
                    kwargs["system"] = system
                return self.local.generate(prompt, **kwargs)
            else:
                return ""
        except Exception as e:
            self.logger.error("ROUTER", f"Provider '{provider}' exception: {e}")
            return ""

    def chat_with_image(self,
                        prompt:     str,
                        image_b64:  str,
                        system:     str = None,
                        max_tokens: int = 1000,
                        task_type:  str = "vision") -> str:
        """Vision: usa OpenRouter se disponibile (GPT-4o/Gemini), altrimenti Claude."""
        provider = self._pick_provider(task_type)
        try:
            if provider == "openrouter" and self.openrouter:
                return self.openrouter.chat_with_image(
                    prompt, image_b64, system, max_tokens
                )
            elif self.claude:
                return self.claude.chat_with_image(
                    prompt, image_b64, system, max_tokens
                )
        except Exception as e:
            self.logger.error("ROUTER", f"Vision error: {e}")
        return "Analisi visiva non disponibile."

    def get_statistics(self) -> Dict[str, Any]:
        stats = dict(self._stats)
        if self.openrouter and hasattr(self.openrouter, "get_statistics"):
            try:
                stats["openrouter_detail"] = self.openrouter.get_statistics()
            except Exception:
                pass
        if self.claude and hasattr(self.claude, "get_statistics"):
            try:
                stats["claude_detail"] = self.claude.get_statistics()
            except Exception:
                pass
        stats["default_ai"] = self.default_ai
        return stats


# ──────────────────────────────────────────────────────────────────────────────
# REAL FILE SAVER
# ──────────────────────────────────────────────────────────────────────────────

class RealFileSaver:
    """
    Salva file generati dall'AI su disco in modo robusto.

    Strategie di salvataggio (in ordine):
      1. Desktop dell'utente
      2. Documenti dell'utente
      3. Cartella corrente
      4. /tmp (ultimo resort)

    Funzionalità extra:
      - Auto-detect tipo file dall'estensione / contenuto
      - Auto-apertura file con l'app predefinita
      - Registro salvataggi in memoria
    """

    EXT_MAP = {
        "python":     ".py",
        "javascript": ".js",
        "typescript": ".ts",
        "java":       ".java",
        "c":          ".c",
        "c++":        ".cpp",
        "cpp":        ".cpp",
        "csharp":     ".cs",
        "rust":       ".rs",
        "go":         ".go",
        "bash":       ".sh",
        "shell":      ".sh",
        "powershell": ".ps1",
        "sql":        ".sql",
        "html":       ".html",
        "css":        ".css",
        "json":       ".json",
        "xml":        ".xml",
        "yaml":       ".yaml",
        "markdown":   ".md",
        "text":       ".txt",
        "txt":        ".txt",
    }

    def __init__(self, logger=None, prefer_desktop: bool = True):
        self.logger          = logger or _DummyLogger()
        self.prefer_desktop  = prefer_desktop
        self._saved_files: List[Dict] = []

        self._base_dirs: List[Path] = self._build_base_dirs()

    def _build_base_dirs(self) -> List[Path]:
        dirs = []
        desktop = Path.home() / "Desktop"
        docs    = Path.home() / "Documents" / "FRANCO"
        cwd     = Path.cwd() / "franco_output"
        tmp     = Path("/tmp") if Path("/tmp").exists() else Path(".")

        if self.prefer_desktop:
            dirs = [desktop, docs, cwd, tmp]
        else:
            dirs = [docs, desktop, cwd, tmp]

        # Crea le dir che non esistono
        for d in dirs:
            try:
                d.mkdir(parents=True, exist_ok=True)
            except Exception:
                pass

        return dirs

    def _resolve_ext(self, language_or_filename: str) -> str:
        name = language_or_filename.lower().strip()
        if "." in name:
            return Path(name).suffix or ".txt"
        return self.EXT_MAP.get(name, ".txt")

    def _unique_path(self, base_dir: Path, stem: str, ext: str) -> Path:
        """Genera path unico aggiungendo numero se il file esiste già."""
        candidate = base_dir / f"{stem}{ext}"
        counter = 1
        while candidate.exists():
            candidate = base_dir / f"{stem}_{counter}{ext}"
            counter += 1
        return candidate

    def save(self,
             content:  str,
             filename: str    = None,
             language: str    = "text",
             auto_open: bool  = False) -> Optional[str]:
        """
        Salva `content` su disco.
        Ritorna il path assoluto del file salvato, o None in caso di errore.
        """
        ext  = self._resolve_ext(filename or language)
        ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
        stem = (Path(filename).stem if filename and "." in filename
                else (filename or f"franco_{ts}"))
        # Pulisci caratteri non validi
        stem = re.sub(r'[<>:"/\\|?*]', "_", stem)[:80]

        for base_dir in self._base_dirs:
            try:
                path = self._unique_path(base_dir, stem, ext)
                path.write_text(content, encoding="utf-8")
                self.logger.success("SAVER", f"File salvato → {path}")
                self._saved_files.append({
                    "path":     str(path),
                    "size":     path.stat().st_size,
                    "saved_at": datetime.now().isoformat(),
                })
                if auto_open:
                    try:
                        import subprocess, sys
                        if sys.platform == "win32":
                            os.startfile(str(path))
                        elif sys.platform == "darwin":
                            subprocess.Popen(["open", str(path)])
                        else:
                            subprocess.Popen(["xdg-open", str(path)])
                    except Exception:
                        pass
                return str(path)
            except Exception as e:
                self.logger.warning("SAVER", f"Scrittura in {base_dir} fallita: {e}")
                continue

        self.logger.error("SAVER", "Impossibile salvare il file in nessuna directory")
        return None

    def save_code(self, code: str, language: str, description: str = "") -> Optional[str]:
        """Salva codice generato dall'AI."""
        ts   = datetime.now().strftime("%H%M%S")
        name = re.sub(r"\W+", "_", description[:30]).strip("_") if description else f"code_{ts}"
        return self.save(code, filename=name, language=language)

    def list_saved(self) -> List[Dict]:
        return list(self._saved_files)


# ──────────────────────────────────────────────────────────────────────────────
# PATCH COMMAND ENGINE
# ──────────────────────────────────────────────────────────────────────────────

def patch_command_engine(engine, router: DualAIRouter, saver: RealFileSaver):
    """
    Patcha CommandEngine per:
      1. Usare DualAIRouter (OpenRouter + Claude) al posto di chiamate dirette
      2. Salvare i file generati con RealFileSaver
      3. Aggiungere comandi extra per gestire i provider AI
    """
    engine._router = router
    engine._saver  = saver
    logger = getattr(engine, "logger", _DummyLogger())

    # ── _cmd_ai_fallback → usa DualAIRouter ──────────────────────────────
    _orig_ai_fallback = engine._cmd_ai_fallback

    def _patched_ai_fallback(text: str) -> str:
        mood     = engine.state.get("mood", None)
        mood_str = mood.value if hasattr(mood, "value") else "neutro"

        user_name = engine.memory.get_user_name()
        ora   = __import__("datetime").datetime.now().strftime("%H:%M")
        data  = __import__("datetime").datetime.now().strftime("%d/%m/%Y")

        recent = engine.memory.get_recent_history(6)
        history_lines = []
        for entry in recent:
            history_lines.append(f"Utente: {entry.get('u', '')}")
            history_lines.append(f"FRANCO: {entry.get('a', '')}")
        history_str = "\n".join(history_lines)

        notes = engine.memory.get("note", [])
        notes_str = ""
        if notes:
            notes_str = "Note recenti: " + " | ".join(
                n.get("testo", n) if isinstance(n, dict) else str(n)
                for n in notes[-3:]
            )

        system = f"""Sei FRANCO 6.0 NEXUS, assistente AI di nuova generazione ispirato a JARVIS.
Sei preciso, elegante, professionale, sottilmente ironico.
Parli SEMPRE in italiano. Non usi emoticon né markdown nelle risposte vocali.
Chiami sempre l'utente "{user_name}".

CONTESTO: Data: {data} — Ora: {ora} — Mood: {mood_str}
{notes_str}

STORICO RECENTE:
{history_str}"""

        try:
            response = router.chat(
                prompt=text,
                system=system,
                max_tokens=1500,
                temperature=0.9,
                task_type="conversation",
            )
        except Exception as e:
            logger.error("PATCH", f"Router errore, fallback Claude: {e}")
            response = _orig_ai_fallback(text)

        if response:
            engine.memory.add_to_history(text, response, mood_str)
            engine.memory.increment_stat("ai_queries")
            try:
                conv_id = engine.memory.get("conversation_id", "default")
                engine.db.add_message(conv_id, "user", text, mood=mood_str)
                engine.db.add_message(conv_id, "assistant", response, mood=mood_str)
            except Exception:
                pass

        return response

    engine._cmd_ai_fallback = _patched_ai_fallback

    # ── _cmd_generate_code → usa router + saver ───────────────────────────
    _orig_gen_code = engine._cmd_generate_code

    def _patched_generate_code(description: str, language: str = "python") -> str:
        if not description:
            return "Cosa devo programmare?"

        system = (
            f"Sei un esperto di {language}. Genera codice completo, funzionante e "
            f"ben commentato in italiano. Restituisci SOLO il codice, senza spiegazioni."
        )
        prompt = (
            f"Scrivi codice {language} per: {description}\n\n"
            f"Requisiti: gestione errori, type hints, docstring, best practices."
        )

        try:
            code = router.chat(
                prompt=prompt,
                system=system,
                max_tokens=3500,
                temperature=0.25,
                task_type="code",
            )
        except Exception as e:
            logger.error("PATCH", f"Code gen fallback: {e}")
            return _orig_gen_code(description, language)

        # Estrai solo il codice se c'è un blocco markdown
        code_match = re.search(
            r"```(?:\w+)?\n(.*?)```", code, re.DOTALL
        )
        if code_match:
            code = code_match.group(1).strip()

        # Salva su disco
        saved_path = saver.save_code(code, language, description)
        suffix = f"\n\n→ Salvato in: {saved_path}" if saved_path else ""

        preview = code[:400] + ("…" if len(code) > 400 else "")
        return f"Codice {language} generato.{suffix}\n\nAnteprima:\n{preview}"

    engine._cmd_generate_code = _patched_generate_code

    # ── Comandi gestione provider AI (accessibili via voce/testo) ─────────

    _orig_process = engine.process

    def _patched_process(raw_input: str) -> str:
        t = raw_input.lower().strip()

        # ── Cambio provider ─────────────────────────────────────
        if any(k in t for k in ["usa openrouter", "attiva openrouter", "passa a openrouter"]):
            router.prefer_openrouter()
            return "Passato a OpenRouter come provider principale."

        if any(k in t for k in ["usa claude", "attiva claude", "passa a claude",
                                  "usa anthropic", "attiva anthropic"]):
            router.prefer_claude()
            return "Passato a Claude (Anthropic) come provider principale."

        # ── Cambio modello OpenRouter ────────────────────────────
        model_match = re.search(
            r"(?:cambia modello|usa modello|modello)\s+(.+)", t
        )
        if model_match:
            alias = model_match.group(1).strip()
            router.set_model(alias)
            model_name = router.openrouter.model if router.openrouter else alias
            return f"Modello OpenRouter impostato a: {model_name}"

        # ── Stato provider AI ────────────────────────────────────
        if any(k in t for k in ["stato ai", "provider ai", "quale ai", "quale modello"]):
            stats = router.get_statistics()
            or_available = bool(
                router.openrouter and getattr(router.openrouter, "is_available", lambda: False)()
            )
            claude_available = bool(
                router.claude and getattr(router.claude, "is_available", lambda: False)()
            )
            or_model = f" ({router.openrouter.model})" if or_available else ""
            return (
                f"Provider attivo: {stats['default_ai']}. "
                f"OpenRouter{'✓' if or_available else '✗'}{or_model}. "
                f"Claude {'✓' if claude_available else '✗'}. "
                f"Chiamate OR: {stats['openrouter']}, Claude: {stats['claude']}, "
                f"Fallback: {stats['fallback']}."
            )

        # ── Lista modelli disponibili ────────────────────────────
        if any(k in t for k in ["lista modelli", "modelli disponibili", "elenco modelli"]):
            models = list(OPENROUTER_MODELS.keys())
            mid = len(models) // 2
            return (
                f"Modelli OpenRouter disponibili ({len(models)}): "
                f"{', '.join(models[:mid])} | {', '.join(models[mid:])}. "
                f"Usa 'cambia modello [nome]' per selezionare."
            )

        # ── File salvati ─────────────────────────────────────────
        if any(k in t for k in ["file salvati", "lista file generati", "codici generati"]):
            saved = saver.list_saved()
            if not saved:
                return "Nessun file salvato in questa sessione."
            lines = [Path(f["path"]).name for f in saved[-5:]]
            return f"File salvati ({len(saved)}): {', '.join(lines)}."

        # ── Delega al process originale ──────────────────────────
        return _orig_process(raw_input)

    engine.process = _patched_process

    logger.success("PATCH",
        f"CommandEngine patchato  →  provider={router.default_ai}  "
        f"OR={'✓' if router.openrouter and router.openrouter.is_available() else '✗'}  "
        f"Claude={'✓' if router.claude and router.claude.is_available() else '✗'}")
