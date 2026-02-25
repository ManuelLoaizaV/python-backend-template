from typing import TypeVar

from google import genai
from google.genai import types
from pydantic import BaseModel, ValidationError

from domain.exceptions.third_party import ThirdPartyIntegrationError

SchemaModel = TypeVar("SchemaModel", bound=BaseModel)


class GeminiService:
    def __init__(
        self,
        *,
        api_key: str,
        model: str,
        timeout_seconds: int = 10,
    ) -> None:
        self.model = model
        self.timeout_seconds = timeout_seconds
        self._client = genai.Client(api_key=api_key)

    def generate_json(
        self,
        *,
        prompt: str,
        response_schema: type[SchemaModel],
        temperature: float = 0.8,
        max_output_tokens: int = 256,
    ) -> SchemaModel:
        try:
            response = self._client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=temperature,
                    max_output_tokens=max_output_tokens,
                    response_mime_type="application/json",
                    response_schema=response_schema,
                ),
            )
        except Exception as exc:
            raise ThirdPartyIntegrationError("Gemini request failed") from exc

        parsed = response.parsed
        if parsed is None:
            raise ThirdPartyIntegrationError(
                "Gemini response did not include valid JSON"
            )

        if isinstance(parsed, response_schema):
            return parsed

        try:
            return response_schema.model_validate(parsed)
        except ValidationError as exc:
            raise ThirdPartyIntegrationError(
                "Gemini response did not match expected schema"
            ) from exc
