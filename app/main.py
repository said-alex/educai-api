from fastapi import FastAPI
from dotenv import load_dotenv
from app.api.endpoints import (
    healthcheck,
    students,
    classify_students
)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

app.include_router(students.router, prefix="/students", tags=["students"])

app.include_router(classify_students.router,
                   prefix="/classify", tags=["classify"])

app.include_router(healthcheck.router,
                   prefix="/healthcheck", tags=["healthcheck"])
