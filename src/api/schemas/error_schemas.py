from pydantic import BaseModel, Field

from domain.exceptions.base import ErrorCode, ErrorType


class ErrorDetail(BaseModel):
    type: ErrorType = Field(description="The type of error returned.")
    code: ErrorCode = Field(description="A short string indicating the error code.")
    message: str = Field(description="A human-readable message providing more details.")
    param: str | None = Field(description="The parameter related to the error, if any.")


class ErrorResponse(BaseModel):
    error: ErrorDetail
