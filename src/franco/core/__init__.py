"""franco.core sub-package (lazy re-exports)."""
import importlib

_EXPORTS = {
    "APIError": "exceptions",
    "BackupManager": "backup",
    "CacheManager": "cache",
    "CommandCategory": "types",
    "CommandResult": "models",
    "ConfigurationError": "exceptions",
    "ConfigurationManager": "config",
    "ConversationMessage": "models",
    "DatabaseManager": "database",
    "DependencyError": "exceptions",
    "EventBus": "events",
    "EventData": "models",
    "FileInfo": "models",
    "FrancoException": "exceptions",
    "LogLevel": "types",
    "MemoryManager": "memory",
    "MoodType": "types",
    "NetworkError": "exceptions",
    "NetworkScanResult": "models",
    "PasswordAnalysis": "models",
    "PermissionDeniedError": "exceptions",
    "Priority": "types",
    "ProcessInfo": "models",
    "ResourceNotFoundError": "exceptions",
    "ScheduledTask": "models",
    "SecurityError": "exceptions",
    "SecurityLevel": "types",
    "StateManager": "state",
    "StructuredLogger": "logging",
    "SystemMetrics": "models",
    "SystemState": "types",
    "TaskScheduler": "scheduler",
    "TimeoutError": "exceptions",
    "ValidationError": "exceptions",
    "VulnerabilityInfo": "models",
    "Workflow": "models",
    "WorkflowStep": "models",
    "async_to_sync": "utils",
    "cached": "utils",
    "chunk_list": "utils",
    "circuit_breaker": "utils",
    "cleanup_old_files": "utils",
    "decode_base64": "utils",
    "deprecated": "utils",
    "encode_base64": "utils",
    "extract_emails": "utils",
    "extract_ips": "utils",
    "extract_urls": "utils",
    "flatten_dict": "utils",
    "format_bytes": "utils",
    "format_duration": "utils",
    "fuzzy_match": "utils",
    "generate_id": "utils",
    "generate_password": "utils",
    "get_current_datetime_formatted": "utils",
    "get_file_hash": "utils",
    "get_file_info": "utils",
    "get_local_ip": "utils",
    "get_public_ip": "utils",
    "hash_text": "utils",
    "is_port_open": "utils",
    "is_valid_email": "utils",
    "is_valid_ip": "utils",
    "is_valid_url": "utils",
    "levenshtein_distance": "utils",
    "log_call": "utils",
    "merge_dicts": "utils",
    "parse_time_expression": "utils",
    "rate_limit": "utils",
    "require_dependency": "utils",
    "resolve_hostname": "utils",
    "retry": "utils",
    "reverse_dns": "utils",
    "run_command": "utils",
    "safe_json_dumps": "utils",
    "safe_json_loads": "utils",
    "sanitize_filename": "utils",
    "singleton": "utils",
    "slugify": "utils",
    "thread_safe": "utils",
    "timed": "utils",
    "truncate": "utils",
    "unflatten_dict": "utils",
    "unique_list": "utils",
    "validate_args": "utils",
    "verify_hash": "utils",
}

__all__ = sorted(_EXPORTS)


def __getattr__(name):
    leaf = _EXPORTS.get(name)
    if leaf is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    mod = importlib.import_module(f"{__name__}.{leaf}")
    value = getattr(mod, name)
    globals()[name] = value
    return value


def __dir__():
    return sorted(set(list(globals()) + __all__))
