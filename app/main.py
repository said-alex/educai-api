from fastapi import FastAPI
from app.api.endpoints import healthcheck, students

app = FastAPI()

app.include_router(students.router, prefix="/students", tags=["students"])
app.include_router(healthcheck.router, prefix="/healthcheck", tags=["healthcheck"])
