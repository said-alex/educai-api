from fastapi import FastAPI
from dotenv import load_dotenv

from app.api.endpoints import healthcheck, students

load_dotenv()

app = FastAPI()

app.include_router(students.router, prefix="/students", tags=["students"])
app.include_router(healthcheck.router, prefix="/healthcheck", tags=["healthcheck"])
