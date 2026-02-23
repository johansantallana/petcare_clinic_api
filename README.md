# PetCare Clinic API

API REST para la gestión de una clínica veterinaria, construida con Flask y PostgreSQL.
## Tecnologías...

- **Python 3**
- **Flask** - Framework web
- **Flask-SQLAlchemy** - ORM
- **PostgreSQL** - Base de datos
- **python-dotenv** - Variables de entorno

## Estructura del proyecto

```
pet_care_api/
├── .env                 # Variables de entorno
├── requirements.txt     # Dependencias
├── src/
│   ├── __init__.py
│   ├── app.py           # Aplicación principal y rutas
│   └── models.py        # Modelos de base de datos
└── venv/                # Entorno virtual
```

## Modelos

### Owner

Representa al dueño de una mascota.

| Campo        | Tipo        | Restricciones          |
|--------------|-------------|------------------------|
| `id`         | Integer     | Primary Key            |
| `first_name` | String(20)  | Requerido              |
| `last_name`  | String(30)  | Requerido              |
| `email`      | String(30)  | Requerido, Único       |
| `phone`      | String(20)  | Opcional               |

## Endpoints

| Método | Ruta      | Descripción              |
|--------|-----------|--------------------------|
| GET    | `/`       | Estado general de la API |
| GET    | `/health` | Health check             |

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd pet_care_api
   ```

2. Crear y activar el entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configurar variables de entorno creando un archivo `.env`:
   ```
   DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/petcare_db
   FLASK_APP=src/app.py
   FLASK_DEBUG=True
   ```

5. Crear la base de datos en PostgreSQL:
   ```sql
   CREATE DATABASE petcare_db;
   ```

6. Ejecutar la aplicación:
   ```bash
   python src/app.py
   ```

La API estará disponible en `http://localhost:5000`
