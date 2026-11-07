"""Настройки сервиса из переменных окружения и файла .env."""

import functools
from typing import final

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Параметры приложения, передаются в конструктор FastAPI."""

    title: str = "Course service title"
    description: str = "Course service description"
    summary: str = "Course service summary"
    version: str = "0.1.0"
    debug: bool = False
    docs_url: str = "/docs"
    openapi_url: str = "/openapi.json"


@final
class Settings(BaseSettings):
    """Корневые настройки сервиса."""

    app: AppSettings

    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env",
        env_nested_delimiter="__",
        env_file_encoding="utf-8",
    )


@functools.lru_cache
def get_settings() -> Settings:
    """Создаёт настройки при первом вызове и дальше возвращает их из кэша."""
    return Settings()
