from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Python Backend Template"
    environment: str = "development"
    database_url: str = "sqlite:///./app.db"
    test_database_url: str = "sqlite://"
    gemini_api_key: str | None = None
    gemini_model: str = "gemini-2.5-flash-lite"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
