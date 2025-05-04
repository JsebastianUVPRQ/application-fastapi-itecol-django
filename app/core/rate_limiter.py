from fastapi import HTTPException, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from core.redis import redis_client

limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="redis://localhost:6379",
    headers_enabled=True
)

def rate_limit_exception_handler(request: Request, exc: RateLimitExceeded):
    raise HTTPException(
        status_code=429,
        detail=f"Rate limit exceeded: {exc.detail}",
        headers={"Retry-After": str(exc.retry_after)}
    )

def get_rate_limiter():
    return limiter