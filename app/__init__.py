"""
Módulo principal de la aplicación School Management System
"""

__version__ = "1.0.0"
__author__ = "Tu Equipo <team@schoolsystem.com>"
__license__ = "Proprietary"

from .__main__ import create_app

__all__ = ["create_app", "core", "models", "schemas", "api", "services"]