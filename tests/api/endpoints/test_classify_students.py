
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_classify_students():
    response = client.post("/classify")
    assert response.status_code == 204
