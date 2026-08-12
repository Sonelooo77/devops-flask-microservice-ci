import pytest
from app import app


@pytest.fixture
def client():
    """Configure un client de test Flask virtuel."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    """Vérifie que la route racine renvoie HTTP 200 et un message validé."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['status'] == "running"


def test_health_endpoint(client):
    """Vérifie que l'endpoint /health renvoie le statut UP."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == "UP"
    assert response.json['service'] == "flask-app"