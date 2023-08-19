from typing import List

from fastapi import Depends
from app.domain.entities.course import Course
from app.domain.entities.student import Student

from pymongo.database import Database
from app.repositories.models.student import StudentModel

from app.repositories.mongodb.get_database import get_database

class MongoDBStudentRepository:
    def __init__(self, database: Database= Depends(get_database)):
       self.database = database

    def get_students_in_dropout(self) -> List[Student]:
        students_dict = list(self.database.students.find({"dropout": True}))
        students = list(map(lambda student: StudentModel(student).to_entity(), students_dict))

        return students

    
    def count_students(self) -> int:
        return self.database.students.count_documents({})
