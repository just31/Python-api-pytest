import pytest

from api.client import RestfulDoorwayClient


@pytest.fixture(scope="session")
def client():
    client = RestfulDoorwayClient("https://testsite.com/")
    return client
