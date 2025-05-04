from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Base
    ENVIRONMENT: str = "dev"
    DEBUG: bool = False
    PROJECT_NAME: str = "School Management System"
    VERSION: str = "1.0.0"
    
    # Database
    DATABASE_URL: str
    TEST_DATABASE_URL: str = "postgresql+asyncpg://test:test@localhost/test_db"
    
    # Security
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    CORS_ORIGINS: list[str] = ["*"]
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    CACHE_TTL: int = 300  # 5 minutos
    
    # Rate Limits
    RATE_LIMITS: dict = {
        "auth": "10/minute",
        "api": "100/minute"
    }
    
    # Email
    SMTP_SERVER: str = "smtp.example.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = "user"
    SMTP_PASSWORD: str = "password"

    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()