from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FitBuddy"
    database_url: str = "sqlite:///./fitbuddy.db"

    gemini_api_key: str = ""
    gemini_workout_model: str = "gemini-3.8-flash"
    gemini_tip_model: str = "gemini-3.8-flash"
    demo_mode: bool = True

    admin_name: str = "FitBuddy Admin"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
