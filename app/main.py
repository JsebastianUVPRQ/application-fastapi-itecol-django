"""
Punto de entrada principal para ejecución como paquete
Ejecutar con: python -m app
"""

import uvicorn
from fastapi import FastAPI
from core.config import settings
from core.logger import configure_logger
from core.redis import connect_redis, close_redis
from core.security_headers import add_security_headers
from core.middleware import logging_middleware
from api.v1.endpoints import auth, users, classrooms, grades
from dependencies.database import engine, Base

# Configurar logger principal
logger = configure_logger()

def create_app() -> FastAPI:
    # Crear aplicación FastAPI
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        docs_url="/docs" if settings.DEBUG else None,
        redoc_url="/redoc" if settings.DEBUG else None
    )

    # Eventos de ciclo de vida
    @app.on_event("startup")
    async def startup_event():
        await connect_redis()
        if settings.ENVIRONMENT == "dev":
            logger.info("Creating database tables...")
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
        logger.info("Application startup complete")

    @app.on_event("shutdown")
    async def shutdown_event():
        await close_redis()
        logger.info("Application shutdown complete")

    # Middlewares
    app.middleware("http")(logging_middleware)
    app.middleware("http")(add_security_headers)

    # Routers
    app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
    app.include_router(users.router, prefix="/users", tags=["Users"])
    app.include_router(classrooms.router, prefix="/classrooms", tags=["Classrooms"])
    app.include_router(grades.router, prefix="/grades", tags=["Grades"])

    # Health check endpoint
    @app.get("/health", include_in_schema=False)
    async def health_check():
        return {"status": "ok", "environment": settings.ENVIRONMENT}

    return app

if __name__ == "__main__":
    # Configurar servidor Uvicorn con opciones
    uvicorn.run(
        "app.__main__:create_app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_config=None,  # Usar logging configurado
        factory=True,      # Usar factory function
        ssl_keyfile=settings.SSL_KEY_PATH if settings.ENVIRONMENT == "prod" else None,
        ssl_certfile=settings.SSL_CERT_PATH if settings.ENVIRONMENT == "prod" else None
    )