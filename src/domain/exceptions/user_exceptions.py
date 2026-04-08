from domain.exceptions.base import BaseDomainError, ErrorCode, ErrorType


class UserAlreadyExistsError(BaseDomainError):
    def __init__(self, username: str):
        super().__init__(
            message=f"The username '{username}' is already registered.",
            type=ErrorType.CONFLICT_ERROR,
            code=ErrorCode.USERNAME_EXISTS,
            param="username",
        )
