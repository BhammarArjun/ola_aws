import pytest #type: ignore
from app import app

@pytest.fixture()
def client():
    return app.test_client()

def test_welcome():
    resp = client.get("/")
    assert resp.text == """Welcome to the API Version of my Model: How to navigate? (use Postman) --- try "/guide", or "/predict"""