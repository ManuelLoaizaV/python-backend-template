from uuid import UUID

from pydantic import BaseModel, Field

from api.schemas.examples import Examples


class UserResponse(BaseModel):
    id: UUID = Field(
        description="Unique identifier for the object.",
        example=Examples.UUID,
    )
    username: str = Field(
        description="A unique and human-readable handle used for identification.",
        min_length=1,
        max_length=32,
        example=Examples.USERNAME,
    )
    full_name: str = Field(
        description="The user preferred display name.",
        min_length=1,
        max_length=256,
        example=Examples.FULL_NAME,
    )
