"""franco.core.exceptions — FRANCO exception hierarchy.

Extracted for real out of the monolith (zero dependencies), so it imports
without dragging the whole app. Faithful copy of the historical classes.
"""
from __future__ import annotations

from datetime import datetime
from typing import Dict

__all__ = [
    "FrancoException", "ConfigurationError", "NetworkError", "SecurityError",
    "APIError", "ValidationError", "ResourceNotFoundError",
    "PermissionDeniedError", "TimeoutError", "DependencyError",
]


class FrancoException(Exception):
    """Base exception for FRANCO system."""

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
            "timestamp": self.timestamp.isoformat(),
        }


class ConfigurationError(FrancoException):
    """Configuration-related errors."""
    def __init__(self, message: str, details: Dict = None):
        super().__init__(message, "CONFIG_ERROR", details)


class NetworkError(FrancoException):
    """Network-related errors."""
    def __init__(self, message: str, details: Dict = None):
        super().__init__(message, "NETWORK_ERROR", details)


class SecurityError(FrancoException):
    """Security-related errors."""
    def __init__(self, message: str, details: Dict = None):
        super().__init__(message, "SECURITY_ERROR", details)


class APIError(FrancoException):
    """API-related errors."""
    def __init__(self, message: str, details: Dict = None):
        super().__init__(message, "API_ERROR", details)


class ValidationError(FrancoException):
    """Validation-related errors."""
    def __init__(self, message: str, details: Dict = None):
        super().__init__(message, "VALIDATION_ERROR", details)


class ResourceNotFoundError(FrancoException):
    """Resource not found errors."""
    def __init__(self, message: str, details: Dict = None):
        super().__init__(message, "NOT_FOUND", details)


class PermissionDeniedError(FrancoException):
    """Permission denied errors."""
    def __init__(self, message: str, details: Dict = None):
        super().__init__(message, "PERMISSION_DENIED", details)


class TimeoutError(FrancoException):  # noqa: A001 — intentional domain name
    """Timeout errors."""
    def __init__(self, message: str, details: Dict = None):
        super().__init__(message, "TIMEOUT", details)


class DependencyError(FrancoException):
    """Missing dependency errors."""
    def __init__(self, dependency: str, details: Dict = None):
        message = f"Dipendenza mancante: {dependency}"
        super().__init__(message, "DEPENDENCY_MISSING", details)
        self.dependency = dependency
