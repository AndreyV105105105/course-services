"""Pydantic-схемы ответов API."""

from pydantic import BaseModel, ConfigDict


class BaseSchemaModel(BaseModel):
    """Базовая схема с общими настройками для всех схем API."""

    model_config = ConfigDict(from_attributes=True, validate_assignment=True, populate_by_name=True)


class ServiceInfo(BaseSchemaModel):
    """Состояние сервиса (health-check)."""

    healthy: bool = True
