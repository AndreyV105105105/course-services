"""Фабрика FastAPI-приложения."""

from collections.abc import Iterable
from typing import Any

from fastapi import APIRouter, FastAPI

from src.core.config import Settings


def create_app(settings: Settings, routers: Iterable[APIRouter], **params: Any) -> FastAPI:
    """Создаёт приложение из настроек и подключает к нему роутеры."""
    app_params = {**settings.app.model_dump(), **params}
    app = FastAPI(**app_params)
    for router in routers:
        app.include_router(router)
    return app
