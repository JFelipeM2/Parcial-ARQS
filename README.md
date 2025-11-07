# Parcial-ARQS

# Task API – FastAPI + Docker

API REST sencilla de gestión de tareas, siguiendo separación por capas
(dominio, aplicación, adaptadores) y principios SOLID básicos.

## Requisitos

- Python 3.10+
- Docker (para ejecución en contenedor)

## Estructura del proyecto

```text
├── Dockerfile
├── README.md
├── app
│   ├── __init__.py
│   ├── adapters
│   │   ├── __init__.py
│   │   ├── http
│   │   │   ├── __init__.py
│   │   │   └── fastapi_app.py
│   │   └── persistence
│   │       ├── __init__.py
│   │       └── memory_task_repository.py
│   ├── application
│   │   ├── __init__.py
│   │   ├── ports
│   │   │   ├── __init__.py
│   │   │   └── task_repository.py
│   │   └── services
│   │       ├── __init__.py
│   │       └── task_service.py
│   └── domain
│       ├── __init__.py
│       └── task.py
(lo saqué con tree en ubuntu)

PD:el dockerignore fue necesario debido a que trabaje en una carpeta de onedrive y daba errores con ciertos archivos al momento de hacer build.
