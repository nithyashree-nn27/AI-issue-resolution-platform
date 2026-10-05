from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.

    Secrets and environment-specific values should never be
    hard-coded into application code.
    """

    app_name: str = "AI Issue Resolution Platform"
    app_version: str = "1.0.0"
    environment: str = "development"

    aws_region: str = "ap-south-1"

    retrieval_backend: str = "local"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()