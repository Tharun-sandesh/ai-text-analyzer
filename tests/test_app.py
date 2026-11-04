
from fastapi.testclient import TestClient
from app import app

# Create a test client for our FastAPI application
client = TestClient(app)


# Test 1: Check whether the API is healthy
def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "health"}


# Test 2: Check positive sentiment
def test_positive_sentiment():
    response = client.post(
        "/analyze",
        json={"text": "I love Python"}
    )

    assert response.status_code == 200
    assert response.json()["sentiment"] == "positive"


# Test 3: Check negative sentiment
def test_negative_sentiment():
    response = client.post(
        "/analyze",
        json={"text": "I hate bugs"}
    )

    assert response.status_code == 200
    assert response.json()["sentiment"] == "negative"


# Test 4: Check neutral sentiment
def test_neutral_sentiment():
    response = client.post(
        "/analyze",
        json={"text": "Python is a language"}
    )

    assert response.status_code == 200
    assert response.json()["sentiment"] == "neutral"


# Test 5: Check empty input validation
def test_empty_text():
    response = client.post(
        "/analyze",
        json={"text": ""}
    )

    assert response.status_code == 422
