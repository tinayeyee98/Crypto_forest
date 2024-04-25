import pytest
from fastapi.testclient import TestClient

from app.models.crypto_model import CryptocurrencyPrices
from app.routes.v1.crypto_api import router


class MockDatabaseManager:
    async def connect(self):
        pass

    async def disconnect(self):
        pass

    async def execute_query(self, query):
        # Simulate database query result
        return [("Bitcoin", "BTC", 50000.0), ("Ethereum", "ETH", 3000.0)]


@pytest.fixture
def client():
    """
    Fixture to create a FastAPI test client with the provided router.

    Returns:
        TestClient: A FastAPI test client instance.
    """
    return TestClient(router)


def test_get_cryptocurrency_list(client, monkeypatch):
    """
    Test function to verify the behavior of the '/v1/cryptocurrencies' endpoint.

    Args:
        client (TestClient): A FastAPI test client instance.
        monkeypatch (MonkeyPatch): Pytest monkeypatch fixture for mocking objects.

    Returns:
        None
    """
    # Mock DatabaseManager
    monkeypatch.setattr("app.routes.v1.crypto_api.db_manager", MockDatabaseManager())

    # Make a request to the endpoint
    response = client.get("/v1/cryptocurrencies")

    # Check if the response is successful
    assert response.status_code == 200

    # Check if the response contains expected data
    assert b"Bitcoin" in response.content
    assert b"BTC" in response.content
    assert b"50000.0" in response.content
