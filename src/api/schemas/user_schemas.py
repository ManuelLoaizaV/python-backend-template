from pydantic import Field

from .base import BaseRequest, BaseResponse


class UserCreate(BaseRequest):
    name: str = Field(min_length=1, max_length=100)


class UserGenerate(BaseRequest):
    purpose: str | None = Field(default=None, min_length=1, max_length=200)


class UserData(BaseResponse):
    id: int
    name: str
