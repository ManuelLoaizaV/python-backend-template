from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Python Backend Template"
    environment: str = "development"
    database_url: str = "sqlite:///./app.db"
    test_database_url: str = "sqlite://"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
