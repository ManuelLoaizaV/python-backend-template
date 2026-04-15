from fastapi import Request, status
from fastapi.responses import JSONResponse

from domain.exceptions.base import BaseDomainError, ErrorType

ERROR_TYPE_TO_STATUS_CODE = {
    ErrorType.INVALID_REQUEST_ERROR: status.HTTP_400_BAD_REQUEST,
    ErrorType.AUTHENTICATION_ERROR: status.HTTP_401_UNAUTHORIZED,
    ErrorType.NOT_FOUND_ERROR: status.HTTP_404_NOT_FOUND,
    ErrorType.CONFLICT_ERROR: status.HTTP_409_CONFLICT,
    ErrorType.API_ERROR: status.HTTP_500_INTERNAL_SERVER_ERROR,
}


async def domain_exception_handler(request: Request, exc: BaseDomainError) -> JSONResponse:
    status_code = ERROR_TYPE_TO_STATUS_CODE.get(exc.type, status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JSONResponse(
        status_code=status_code,
        content={
            "error": {
                "type": exc.type.value,
                "code": exc.code.value,
                "message": exc.message,
                "param": exc.param,
            }
        },
    )
