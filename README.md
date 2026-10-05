# FRANCO 7 — clean desktop core

The new V7 lives in `src/franco/v7` and does not import the legacy monolith.
It keeps local commands fast and sends only open conversation to OpenRouter.
The desktop UI is an always-on-top orange orb: click it to open the panel and
switch between Chat, Map & public sources, and Settings.

```powershell
pip install -e ".[desktop,dev]"
python -m franco --v7 --desktop
```

On Windows you can also double-click
`src/franco/v7/avvia_franco_v7.bat`. The microphone and Franco's spoken voice
have separate mute controls. Partial speech is interpreted while the user is
speaking, but actions execute only after endpoint detection finalizes the turn.

Fast V7 commands include:

- `apri OBS`, `apri Discord`, or another installed Start Menu application;
- `Franco mappa`;
- `mostrami le telecamere di Catanzaro`;
- `mostrami tutti i voli sopra Boston`;
- `cerca una persona Mario Rossi` for a sourced public-profile lead and a
  manual Max Intel comparison; private contact and location data are excluded;
- `geolocalizza questa foto C:\foto\piazza.jpg` using GeoSpy when
  `GEOSPY_API_KEY` is configured;
- `migliorati su ...`, followed by `conferma miglioramento` only after Franco
  has shown what it understood and which files it proposes to change.

Confirmed self-improvements compile, import, and run the V7 test suite. A
failed verification restores every touched file. Code size is not a target:
features must have a real handler and tests rather than placeholder lines.

## Legacy Franco 6

F.R.A.N.C.O. 6.0 — NEXUS EDITION

## What this is

FRANCO was one 19,000-line module. This package is the same brain, cut along
clean seams:

```
franco/
├── pyproject.toml
├── src/franco/
│   ├── _monolith.py       # the original file, verbatim — runtime source of truth
│   ├── app.py             # FrancoCore coordinator + `main` entrypoint
│   ├── core/              # exceptions, types, models, config, events, cache,
│   │                      # state, logging, database, memory, backup, scheduler, utils
│   ├── ai/                # claude, nlp, base, mistral, router
│   ├── voice/             # stt, tts, vad
│   ├── commands/          # registry, system, apps, security, files, web
│   ├── security/          # scanner, passwords, crypto, offensive
│   ├── ui/                # renderer, themes, particles, vision
│   ├── integrations/      # earthquakes, notifications, mobile, remote,
│   │                      # home_assistant, proactive, email
│   └── data/              # ports.json, http_codes.json, apps.json, themes.json
└── tests/
```

## How the split works (strangler-fig)

Every sub-module re-exports its real symbols **from `_monolith`** through an
explicit `__all__`. So the import paths are real and enforced today:

```python
from franco.security.scanner import NetworkScanner
from franco.ai.claude import ClaudeAIClient
from franco import get_core
```

No logic was rewritten, so nothing regressed. The monolith is now an internal
detail with clean seams cut around every subsystem.

## Migrating a class out of the monolith

1. Cut the class body from `src/franco/_monolith.py`.
2. Paste it into its facade module (e.g. `security/scanner.py`), replacing the
   `from ..._monolith import ...` line for that symbol.
3. Add whatever imports that class needs at the top of the module.
4. `pytest` — the public import path never changed, so the suite still passes.

Do it one class at a time. The seams are already cut.

## Run

```bash
pip install -e .
python -m franco            # or:  franco
pytest
```

## Config

Copy `.env.example` to `.env` and fill in your keys.

## Jarvis / OpenRouter / XTTS

The `jarvis_client/` directory contains the merged Jarvis interface source. The
Python runtime uses the same capabilities through `franco.integrations.JarvisBridge`:

```python
from franco.integrations.jarvis_bridge import JarvisBridge

bridge = JarvisBridge()
answer = bridge.chat("Cosa devo fare oggi?")
audio_wav = bridge.speak(answer)
```

Set `OPENROUTER_API_KEY` and `FRANCO_OPENROUTER_MODEL` in `.env`. Chat traffic
goes to OpenRouter; speech is sent only to the supervised loopback XTTS server
on `FRANCO_XTTS_URL`. No OpenAI key is needed for this path. `FRANCO_XTTS_SPEAKER`
and `FRANCO_XTTS_LANGUAGE` select the local voice.
