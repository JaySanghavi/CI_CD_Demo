from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_health_intentional_failure():
    response = client.get("/health")

    assert response.status_code == 500  # Intentional failure

# To make CI/CD successful, use the below test instead of the above one. Uncomment it and comment the above test_health_intentional_failure function.

'''
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Hello from CI/CD!"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
    
'''