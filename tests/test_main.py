import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    """Prueba el endpoint raíz."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "Sistema de Gestión Escolar" in response.json()["message"]

def test_health_check():
    """Prueba el endpoint de verificación de salud."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_api_docs():
    """Prueba que la documentación esté disponible."""
    response = client.get("/docs")
    assert response.status_code == 200

def test_redoc():
    """Prueba que ReDoc esté disponible."""
    response = client.get("/redoc")
    assert response.status_code == 200

def test_openapi_json():
    """Prueba que el esquema OpenAPI esté disponible."""
    response = client.get("/api/v1/openapi.json")
    assert response.status_code == 200
    assert "openapi" in response.json() 