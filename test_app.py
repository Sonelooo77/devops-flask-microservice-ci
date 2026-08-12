import pytest
from app import app


@pytest.fixture
def client():
"""
    """"Fixture to configure a virtual Flask test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    """Ensure root route returns HTTP 200 and expected status."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['status'] == "running"


def test_health_endpoint(client):
    """Ensure health check route returns HTTP 200 and UP status."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == "UP"
    assert response.json['service'] == "flask-app"