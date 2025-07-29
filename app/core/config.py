from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # Configuración de la aplicación
    app_name: str = "Sistema de Gestión Escolar"
    debug: bool = True
    environment: str = "development"
    
    # Configuración de la base de datos
    database_url: str = "postgresql://school_user:school_password@localhost:5432/school_db"
    
    # Configuración de seguridad
    secret_key: str = "your-secret-key-here-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Configuración de logs
    log_level: str = "INFO"
    log_file: str = "logs/app.log"
    
    # Configuración de email (opcional)
    smtp_tls: bool = True
    smtp_port: int = 587
    smtp_host: Optional[str] = None
    smtp_user: Optional[str] = None
    smtp_password: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings() 