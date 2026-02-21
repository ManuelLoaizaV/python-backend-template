from pydantic import BaseModel

class BaseResponse(BaseModel):
    """All responses should inherit from this class."""
    pass

class BaseRequest(BaseModel):
    """All requests should inherit from this class."""
    pass