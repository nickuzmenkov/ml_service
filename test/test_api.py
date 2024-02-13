import pytest

from ml_service.api.app import app
from fastapi.testclient import TestClient


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


def test_predict(client: TestClient):
    response = client.get("/predict", params={"petal_width": 1, "petal_height": 1, "sepal_width": 1, "sepal_height": 1})
    response.raise_for_status()
    assert response.text
