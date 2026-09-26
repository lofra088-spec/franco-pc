"""franco.security.scanner — Scanner.

Public surface re-exported from the FRANCO monolith (src/franco/_monolith.py).
"""

from .._monolith import (
    DNSAnalyzer,
    HTTPSecurityAnalyzer,
    IPIntel,
    MalwareScanner,
    NetworkScanner,
    SSLAnalyzer,
    SubdomainEnumerator,
    VulnerabilityScanner,
)

__all__ = [
    "DNSAnalyzer",
    "HTTPSecurityAnalyzer",
    "IPIntel",
    "MalwareScanner",
    "NetworkScanner",
    "SSLAnalyzer",
    "SubdomainEnumerator",
    "VulnerabilityScanner",
]
