from main import app
from fastapi.testclient import TestClient

BACKEND = 'http://localhost:8000'
def test_create_game():
    client = TestClient(app)
    response = client.post(BACKEND)
    print(response)

def test_websocket():
    client = TestClient(app)
