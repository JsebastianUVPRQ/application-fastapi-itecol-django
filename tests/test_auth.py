import pytest
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession
from core.security import create_access_token
from models.user import User

@pytest.mark.asyncio
async def test_successful_login(client, test_user):
    response = await client.post("/auth/token", data={
        "username": test_user.email,
        "password": "testpassword"
    })
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()

@pytest.mark.asyncio
async def test_rate_limiting(client):
    for _ in range(10):
        response = await client.post("/auth/token", data={
            "username": "wrong@user.com",
            "password": "wrongpassword"
        })
    assert response.status_code == status.HTTP_429_TOO_MANY_REQUESTS

@pytest.mark.asyncio
async def test_protected_endpoint(client, test_user):
    token = create_access_token({"sub": test_user.email})
    response = await client.get("/users/me", 
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["email"] == test_user.email