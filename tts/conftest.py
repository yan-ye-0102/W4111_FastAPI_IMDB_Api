from unittest.mock import patch

import pytest

from resources.mysql_data_service import MySQLDataService, MySQLDataServiceConfig
from resources.imdb_resources.artist_resource import ArtistResource
from service_factory import ServiceFactory

@pytest.fixture
def mock_svc():
    config = MySQLDataServiceConfig()
    svc = MySQLDataService(config)
    with patch("resources.mysql_data_service.MySQLDataService.get_connection"):
        yield svc


@pytest.fixture
def svc() -> MySQLDataService:
    config = MySQLDataServiceConfig()
    svc = MySQLDataService(config)
    yield svc

@pytest.fixture
def artist_resource():
        service_factory = ServiceFactory()
        yield service_factory.get_resource("ArtistResource")
