from enum import StrEnum


class ErrorType(StrEnum):
    API_ERROR = "api_error"
    INVALID_REQUEST_ERROR = "invalid_request_error"
    AUTHENTICATION_ERROR = "authentication_error"
    NOT_FOUND_ERROR = "not_found_error"
    CONFLICT_ERROR = "conflict_error"


class ErrorCode(StrEnum):
    # Auth / Registration
    USERNAME_EXISTS = "username_exists"
    PHONE_NUMBER_EXISTS = "phone_number_exists"

    # General
    PARAMETER_MISSING = "parameter_missing"
    RESOURCE_NOT_FOUND = "resource_not_found"
    INTERNAL_ERROR = "internal_server_error"


class BaseDomainError(Exception):
    def __init__(
        self,
        message: str,
        type: ErrorType = ErrorType.API_ERROR,
        code: ErrorCode = ErrorCode.INTERNAL_ERROR,
        param: str | None = None,
    ):
        self.message = message
        self.type = type
        self.code = code
        self.param = param
        super().__init__(self.message)
