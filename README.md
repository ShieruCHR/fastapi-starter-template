# FastAPI Starter Template

日本語版は[こちら](README-ja.md)

This repository is a starter template for building backends with FastAPI (mostly for personal use, though).  
It comes with some pre-implemented features related to database and API versioning.

This `README.md` is 99% translated by ChatGPT.  
Original README can be found [here (Japanese)](README-ja.md).

## Libraries

The main libraries used in this starter template are as follows.  
 For more details, please refer to `requirements.txt`.

- FastAPI: A fast and modern web framework. [Documentation](https://fastapi.tiangolo.com/) [Repository](https://github.com/tiangolo/fastapi)
- SQLModel: An SQLAlchemy-based ORM with high affinity for FastAPI. [Documentation](https://sqlmodel.tiangolo.com/) [Repository](https://github.com/tiangolo/sqlmodel)
- Pydantic: A robust data validation library used as the base for FastAPI and SQLModel. [Documentation](https://docs.pydantic.dev/latest/) [Repository](https://github.com/pydantic/pydantic)

## Files

- `alembic.ini`: Configuration file used for database migration.
- `crud.py`: Defines CRUD operations for the database.
- `database.py`: Contains the connection information for the database, and the connection URI is automatically referenced from `alembic.ini` by default.
- `main.py`: The main file. Running this file starts the application in Stat Reload mode.
- `models.py`: Defines the database models (tables).
- `pagination.py`: A small class that helps pagination support.
- `schemas.py`: Defines the request and response schemas for the API.

- `migrations/`: Contains Alembic-related migrations.

- `api/`: API versioning folder.
- `api/__init__.py`: Registers API routers for different versions.

- `api/v1/`: API Version 1.
- `api/v1/__init__.py`: Automatically includes the `router` within the respective version Python file.
- `api/v1/main.py`: The main file for API Version 1.

## Usage

1. Create a new repository on GitHub using this repository as a template.  
Alternatively, clone the repository locally with the following command:

```sh
git clone https://github.com/ShieruCHR/fastapi-starter-template.git
cd fastapi-starter-template
```

2. Create and activate a virtual environment.

For Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

For macOS / Linux:

```sh
python3 -m venv venv
source venv/bin/activate
```

3. Install libraries.

```bash
pip install -r requirements.txt
```

4. Configure the database.
   Edit the `sqlalchemy.url` of `[alembic]` section in `alembic.ini`.
   Alternatively, replace `alembic_ini.get("alembic", "sqlalchemy.url")` with database URI in `database.py`.

5. Edit `crud.py`, `models.py`, and `schemas.py` to tailor them to your needs.

6. Perform the migration.

```sh
alembic upgrade head
```

7. Start the application.

```sh
uvicorn main:app --reload
# or "python main.py"
```

## API Documentation

FastAPI provides Swagger UI by default. Access it at <http://localhost:8000/docs>.
Additionally, this template generates `openapi.json` during application startup.
You can use tools like [OpenAPI Generator CLI](https://github.com/OpenAPITools/openapi-generator-cli) to generate a simple API client.

## API Versioning

This template offers a simple way to handle API versioning.
Let's create a new version of the API (`v2`) as an example.

1. Copy `api/v1/` to `api/v2/`.
2. Change `API_VERSION = 1` to `API_VERSION = 2` in `api/v2/__init__.py`.
3. Include the `v2` router in `api/__init__.py`'s `api_router`.

```diff
from glob import glob
from fastapi import APIRouter

from .v1 import router as v1_router
+ from .v2 import router as v2_router

api_router = APIRouter(prefix=\"/api\")

# Register API Routers
api_router.include_router(v1_router)
+ api_router.include_router(v2_router)
