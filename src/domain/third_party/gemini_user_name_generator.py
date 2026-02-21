from pydantic import BaseModel

from src.domain.exceptions.third_party import ThirdPartyIntegrationError
from src.domain.ports.user_name_generator import UserNameGenerator
from src.domain.third_party.gemini_service import GeminiService


class GeneratedNameResponse(BaseModel):
    name: str


class GeminiUserNameGenerator(UserNameGenerator):
    def __init__(
        self,
        *,
        api_key: str,
        model: str,
        timeout_seconds: int = 10,
    ) -> None:
        self._service = GeminiService(
            api_key=api_key,
            model=model,
            timeout_seconds=timeout_seconds,
        )

    def generate_name(self, *, purpose: str | None = None) -> str:
        prompt = "Generate a user"
        if purpose:
            prompt = f"Context: {purpose.strip()}"

        try:
            generated = self._service.generate_json(
                prompt=(
                    f"{prompt}: Return a JSON object with this exact shape: {GeneratedNameResponse.model_json_schema()}"
                ),
                response_schema=GeneratedNameResponse,
                temperature=0.8,
                max_output_tokens=32,
            )
        except ThirdPartyIntegrationError:
            raise

        raw_name = generated.name.strip()
        if not raw_name:
            raise ThirdPartyIntegrationError("Gemini response did not include a name")

        name = raw_name.splitlines()[0].strip().strip('"').strip("'")
        if not name:
            raise ThirdPartyIntegrationError("Gemini returned an empty name")

        return name
