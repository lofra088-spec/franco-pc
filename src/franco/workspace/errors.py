"""Errors safe to display through the local HTTP API."""


class WorkspaceError(Exception):
    status = 400
    code = "invalid_request"

    def __init__(self, message, *, fields=None):
        super().__init__(message)
        self.fields = fields or {}

    def payload(self):
        return {
            "error": {
                "code": self.code,
                "message": str(self),
                "fields": self.fields,
            }
        }


class NotFound(WorkspaceError):
    status = 404
    code = "not_found"


class Conflict(WorkspaceError):
    status = 409
    code = "conflict"


class Unauthorized(WorkspaceError):
    status = 403
    code = "forbidden"


class PayloadTooLarge(WorkspaceError):
    status = 413
    code = "payload_too_large"
