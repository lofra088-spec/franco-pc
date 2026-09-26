"""Cyber intent patterns — voice/text -> operation routing.

Wire into the main NLP intent table (e.g. franco brain/intent) with:
    from franco.cyber.intents import CYBER_INTENTS
    INTENTS.update(CYBER_INTENTS)

Each key is a regex (matched case-insensitively is recommended); each value is
the operation id handled by the cyber router / CyberJarvis.
"""
from __future__ import annotations

CYBER_INTENTS: dict[str, str] = {
    # Ricognizione
    r"scan(na|lare)?\s+(la\s+)?rete": "network_scan",
    r"scan(na|lare)?\s+(le\s+)?porte?\s+(di|su)\s+(.+)": "port_scan",
    r"trova\s+(sub)?domini\s+(di|per)\s+(.+)": "subdomain_enum",
    r"chi\s+è\s+(.+)": "whois_lookup",
    r"informazioni\s+(su|di)\s+(.+)": "osint_target",

    # Offensivo
    r"genera\s+(una\s+)?(reverse\s+)?shell": "gen_shell",
    r"genera\s+payload": "gen_payload",
    r"exploit(a|ta)?\s+(.+)": "run_exploit",
    r"crac(k|ca)\s+(il\s+)?hash\s+(.+)": "crack_hash",

    # Difensivo
    r"avvia\s+monitor(aggio)?": "start_monitor",
    r"ferma\s+monitor(aggio)?": "stop_monitor",
    r"hardenn(a|are)?\s+(il\s+)?sistema": "harden_system",
    r"analizza\s+(questo\s+)?(file|malware)\s+(.+)": "analyze_malware",

    # Web
    r"scanna\s+(il\s+)?sito\s+(.+)": "web_scan",
    r"testa\s+(per\s+)?sql\s+injection\s+(su|su)\s+(.+)": "test_sqli",
    r"testa\s+(per\s+)?xss\s+(su)\s+(.+)": "test_xss",

    # Reporting
    r"genera\s+report": "gen_report",
    r"riassunto\s+(cyber|sicurezza)": "cyber_summary",
}

# operation id -> CyberJarvis coroutine name (for the router to dispatch)
INTENT_TO_METHOD: dict[str, str] = {
    "network_scan": "full_recon",
    "port_scan": "attack_surface",
    "subdomain_enum": "full_recon",
    "osint_target": "full_recon",
    "gen_shell": "generate_shell",
    "run_exploit": "exploit_target",
    "crack_hash": "crack_hash",
    "start_monitor": "start_monitoring",
    "harden_system": "harden_system",
    "web_scan": "web_assessment",
    "cyber_summary": "get_summary",
}

__all__ = ["CYBER_INTENTS", "INTENT_TO_METHOD"]
