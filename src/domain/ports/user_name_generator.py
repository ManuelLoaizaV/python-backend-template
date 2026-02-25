from typing import Protocol


class UserNameGenerator(Protocol):
    def generate_name(self, *, purpose: str | None = None) -> str: ...
