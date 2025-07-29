# Guía de Uso de la API - Sistema de Gestión Escolar

## Descripción General

Esta API proporciona endpoints completos para la gestión de una escuela primaria, incluyendo estudiantes, profesores, clases, calificaciones y logs de actividad.

## Endpoints Principales

### Estudiantes (`/api/v1/students`)

#### Crear Estudiante
```http
POST /api/v1/students/
Content-Type: application/json

{
  "student_id": "EST001",
  "first_name": "Juan",
  "last_name": "Pérez",
  "email": "juan.perez@email.com",
  "phone": "123456789",
  "date_of_birth": "2015-03-15",
  "address": "Calle Principal 123",
  "grade_level": 3,
  "is_active": true
}
```

#### Obtener Estudiantes
```http
GET /api/v1/students/
GET /api/v1/students/?grade_level=3
GET /api/v1/students/?skip=0&limit=10
```

#### Obtener Estudiante por ID
```http
GET /api/v1/students/{student_id}
```

#### Actualizar Estudiante
```http
PUT /api/v1/students/{student_id}
Content-Type: application/json

{
  "first_name": "Juan Carlos",
  "phone": "987654321"
}
```

#### Eliminar Estudiante
```http
DELETE /api/v1/students/{student_id}
```

### Profesores (`/api/v1/teachers`)

#### Crear Profesor
```http
POST /api/v1/teachers/
Content-Type: application/json

{
  "teacher_id": "PROF001",
  "first_name": "Ana",
  "last_name": "Rodríguez",
  "email": "ana.rodriguez@escuela.com",
  "phone": "111222333",
  "date_of_birth": "1985-05-12",
  "address": "Calle de los Maestros 1",
  "specialization": "Matemáticas",
  "is_active": true
}
```

#### Obtener Profesores
```http
GET /api/v1/teachers/
GET /api/v1/teachers/?specialization=Matemáticas
```

### Asignaturas (`/api/v1/subjects`)

#### Crear Asignatura
```http
POST /api/v1/subjects/
Content-Type: application/json

{
  "name": "Matemáticas",
  "code": "MAT001",
  "description": "Matemáticas básicas para primaria",
  "grade_level": 3,
  "is_active": true
}
```

#### Obtener Asignaturas
```http
GET /api/v1/subjects/
GET /api/v1/subjects/?grade_level=3
```

### Clases (`/api/v1/classes`)

#### Crear Clase
```http
POST /api/v1/classes/
Content-Type: application/json

{
  "name": "Matemáticas 3° A",
  "subject_id": 1,
  "teacher_id": 1,
  "grade_level": 3,
  "schedule": "Lunes y Miércoles 8:00-9:30",
  "room": "Aula 101",
  "max_students": 25,
  "is_active": true
}
```

#### Obtener Clases
```http
GET /api/v1/classes/
GET /api/v1/classes/?teacher_id=1
GET /api/v1/classes/?subject_id=1
GET /api/v1/classes/?grade_level=3
```

#### Matricular Estudiante
```http
POST /api/v1/classes/enrollments/
Content-Type: application/json

{
  "student_id": 1,
  "class_id": 1,
  "enrollment_date": "2024-01-15T08:00:00",
  "is_active": true
}
```

### Calificaciones (`/api/v1/grades`)

#### Crear Calificación
```http
POST /api/v1/grades/
Content-Type: application/json

{
  "student_id": 1,
  "class_id": 1,
  "grade_type": "examen",
  "grade_value": 8.5,
  "max_grade": 10.0,
  "comments": "Excelente trabajo",
  "graded_date": "2024-01-20T10:00:00"
}
```

#### Obtener Calificaciones
```http
GET /api/v1/grades/
GET /api/v1/grades/?student_id=1
GET /api/v1/grades/?class_id=1
GET /api/v1/grades/?student_id=1&class_id=1
```

#### Obtener Promedio de Estudiante
```http
GET /api/v1/grades/student/{student_id}/class/{class_id}/average
```

### Logs de Actividad (`/api/v1/logs`)

#### Crear Log
```http
POST /api/v1/logs/
Content-Type: application/json

{
  "user_id": 1,
  "user_type": "teacher",
  "action": "create",
  "resource_type": "grade",
  "resource_id": 1,
  "description": "Profesor Ana Rodríguez creó una nueva calificación"
}
```

#### Obtener Logs
```http
GET /api/v1/logs/
GET /api/v1/logs/?user_id=1
GET /api/v1/logs/?user_type=teacher
GET /api/v1/logs/?resource_type=student&resource_id=1
GET /api/v1/logs/recent/?limit=50
```

## Códigos de Estado HTTP

- `200 OK`: Operación exitosa
- `201 Created`: Recurso creado exitosamente
- `400 Bad Request`: Datos de entrada inválidos
- `404 Not Found`: Recurso no encontrado
- `500 Internal Server Error`: Error interno del servidor

## Autenticación

Actualmente la API no requiere autenticación, pero está preparada para implementar JWT en el futuro.

## Documentación Interactiva

- **Swagger UI**: `/docs`
- **ReDoc**: `/redoc`
- **OpenAPI JSON**: `/api/v1/openapi.json`

## Ejemplos de Uso

### Flujo Completo: Crear Estudiante y Matricularlo

1. **Crear Estudiante**
```bash
curl -X POST "http://localhost:8000/api/v1/students/" \
  -H "Content-Type: application/json" \
  -d '{
    "student_id": "EST004",
    "first_name": "Laura",
    "last_name": "González",
    "email": "laura.gonzalez@email.com",
    "grade_level": 3
  }'
```

2. **Matricular en Clase**
```bash
curl -X POST "http://localhost:8000/api/v1/classes/enrollments/" \
  -H "Content-Type: application/json" \
  -d '{
    "student_id": 4,
    "class_id": 1,
    "enrollment_date": "2024-01-15T08:00:00"
  }'
```

3. **Agregar Calificación**
```bash
curl -X POST "http://localhost:8000/api/v1/grades/" \
  -H "Content-Type: application/json" \
  -d '{
    "student_id": 4,
    "class_id": 1,
    "grade_type": "examen",
    "grade_value": 9.0,
    "graded_date": "2024-01-20T10:00:00"
  }'
```

## Notas Importantes

- Todos los endpoints devuelven JSON
- Las fechas deben estar en formato ISO 8601
- Los IDs son enteros autoincrementales
- Los recursos no se eliminan físicamente, se marcan como inactivos
- La API incluye validación de datos y manejo de errores 