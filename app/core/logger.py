import logging
from logging.handlers import RotatingFileHandler
import structlog
from pathlib import Path
from core.config import settings

def configure_logger():
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.JSONRenderer()
        ],
        logger_factory=structlog.WriteLoggerFactory(
            file=RotatingFileHandler(
                filename=logs_dir/"app.log",
                maxBytes=10*1024*1024,  # 10MB
                backupCount=5,
                encoding="utf-8"
            )
        )
    )
    
    logger = structlog.get_logger()
    logger.info("Logger configured", log_level=settings.LOG_LEVEL)
    return logger