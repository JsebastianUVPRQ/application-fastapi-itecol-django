# Sistema de Gestión Escolar - FastAPI

Sistema completo de gestión para escuela primaria desarrollado con FastAPI y Docker.

## Características

- **Gestión de Estudiantes**: Registro, listas, historial académico
- **Gestión de Clases**: Asignaturas, horarios, calificaciones
- **Sistema de Notas**: Evaluaciones, promedios, reportes
- **Logs de Actividad**: Seguimiento de acciones y eventos
- **API RESTful**: Endpoints completos para todas las funcionalidades
- **Base de Datos**: PostgreSQL con SQLAlchemy
- **Docker**: Contenedores para desarrollo y producción

## Estructura del Proyecto

```
application-fastapi-django/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   └── api.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── crud/
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   ├── schemas/
│   └── main.py
├── docker/
├── scripts/
├── tests/
├── .env.example
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## Instalación y Uso

### Con Docker (Recomendado)

1. Clonar el repositorio
2. Copiar `.env.example` a `.env` y configurar variables
3. Ejecutar: `docker-compose up --build`

### Desarrollo Local

1. Crear entorno virtual: `python -m venv .venv`
2. Activar entorno: `.venv/bin/activate` (Linux/Mac) o `.venv\Scripts\activate` (Windows)
3. Instalar dependencias: `pip install -r requirements.txt`
4. Configurar base de datos
5. Ejecutar: `uvicorn app.main:app --reload`

## Endpoints Principales

- `/api/v1/students` - Gestión de estudiantes
- `/api/v1/classes` - Gestión de clases
- `/api/v1/grades` - Sistema de calificaciones
- `/api/v1/teachers` - Gestión de profesores
- `/api/v1/logs` - Registro de actividades

## Tecnologías

- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **Contenedores**: Docker, Docker Compose
- **Autenticación**: JWT
- **Documentación**: Swagger UI automática 