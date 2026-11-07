"""Бизнес-логика сервиса."""

from src.web.schemas import ServiceInfo


def get_service_info() -> ServiceInfo:
    """Возвращает текущее состояние сервиса."""
    return ServiceInfo()
