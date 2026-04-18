# SysCardiologia

Sistema de Gestión Cardiológica Profesional para escritorio con Python.

## Características principales

- Autenticación segura con bcrypt
- RBAC con roles: Admin, Cardiólogo, Enfermero, Recepcionista
- Base de datos PostgreSQL con SQLAlchemy
- Auditoría completa (acceso exclusivo para Admin)
- Gestión completa de pacientes, consultas y citas
- Exportación de reportes en PDF y Excel
- Interfaz moderna PyQt5 con estructura modular

## Estructura

```text
SysCardiologia/
├── main.py
├── requirements.txt
├── config.py
├── .env.example
├── database/
├── ui/
├── logic/
├── assets/
└── docs/
```

## Instalación

1. Crear entorno virtual e instalar dependencias:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

2. Configurar variables de entorno:

```bash
cp .env.example .env
# ajustar DATABASE_URL y SECRET_KEY
```

3. Crear base de datos PostgreSQL y ejecutar:

```bash
python main.py
```

La aplicación crea tablas y roles iniciales automáticamente al iniciar.

## Credenciales iniciales

Tomadas desde entorno:
- Usuario: `DEFAULT_ADMIN_USERNAME`
- Contraseña: `DEFAULT_ADMIN_PASSWORD`

## Pruebas

```bash
python -m unittest discover -v
```
