from fastapi import FastAPI
from dotenv import load_dotenv

from app.api.endpoints import healthcheck, students, machine_learning, classify_students

load_dotenv()

app = FastAPI()

app.include_router(students.router, prefix="/students", tags=["students"])
app.include_router(machine_learning.router,
                   prefix="/predict", tags=["predict"])

app.include_router(classify_students.router,
                   prefix="/classify", tags=["classify"])

app.include_router(healthcheck.router,
                   prefix="/healthcheck", tags=["healthcheck"])
