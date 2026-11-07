"""Жизненный цикл: код при запуске и остановке приложения."""

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan_service_router(_app: FastAPI) -> AsyncIterator[None]:
    """Запуск и остановка ресурсов роутера service."""
    logger.debug("Lifespan (service router) startup")
    yield
    logger.debug("Lifespan (service router) shutdown")


@asynccontextmanager
async def lifespan_app(_app: FastAPI) -> AsyncIterator[None]:
    """Запуск и остановка ресурсов всего приложения."""
    logger.debug("Lifespan (app) startup")
    yield
    logger.debug("Lifespan (app) shutdown")
