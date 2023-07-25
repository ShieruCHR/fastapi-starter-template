import json
from typing import Annotated
from fastapi import APIRouter, Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from crud import CRUD
from api import api_router

from database import create_db
from pagination import Pagination

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # use "*" for all origins (not recommended)
        "http://localhost:3000",
        "https://example.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.on_event("startup")
def on_startup():
    create_db()


@app.get("/")
async def root():
    return "Hello World!"


with open("openapi.json", mode="w", encoding="UTF-8") as f:
    json.dump(app.openapi(), f, ensure_ascii=False)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)  # Run development server
