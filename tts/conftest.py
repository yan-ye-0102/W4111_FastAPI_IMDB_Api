import pytest
from unittest.mock import patch
from resources.mysql_data_service import MySQLDataService, MySQLDataServiceConfig


@pytest.fixture
def mock_svc():
	config = MySQLDataServiceConfig()
	svc = MySQLDataService(config)
	with patch("resources.mysql_data_service.MySQLDataService.get_connection"):
		yield svc


MOCK_DB = {}

