from main import app
from fastapi.testclient import TestClient

def test_websocket():
    client = TestClient(app)
