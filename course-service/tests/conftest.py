import pytest
from fastapi.testclient import TestClient

from src.core.config import get_settings
from src.web.app import create_app
from src.web.routers import service_router


@pytest.fixture
def settings():
    return get_settings()


@pytest.fixture
def routers():
    return (service_router,)


@pytest.fixture
def app(settings, routers):
    return create_app(settings, routers)


@pytest.fixture
def app_client(app):
    with TestClient(app) as client:
        yield client