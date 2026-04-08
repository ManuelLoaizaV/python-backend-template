import re

from pydantic import BaseModel, Field, field_validator

from api.schemas.examples import Examples


class RegisterRequest(BaseModel):
    username: str = Field(
        description="A unique and human-readable handle used for identification.",
        min_length=1,
        max_length=32,
        example=Examples.USERNAME,
    )
    password: str = Field(
        description="The secret string to authenticate the user. Must contain at least one number and one special character.",
        min_length=8,
        max_length=128,
        example=Examples.PASSWORD,
    )
    full_name: str = Field(
        description="The user preferred display name.",
        min_length=1,
        max_length=256,
        example=Examples.FULL_NAME,
    )

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, password: str) -> str:
        """Validate password strength."""
        if not re.search(pattern=r"\d", string=password):
            raise ValueError("Password must contain at least one number.")
        if not re.search(pattern=r"[\W_]", string=password):  # Non-alphanumeric or underscore
            raise ValueError("Password must contain at least one special character.")
        return password
