from dataclasses import dataclass


@dataclass(slots=True)
class UserEntity:
    id: int
    name: str
