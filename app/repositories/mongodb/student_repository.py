from typing import List

from fastapi import Depends
from app.domain.entities.course import Course
from app.domain.entities.student import Student

from pymongo.database import Database
from app.repositories.models.student import StudentModel

from app.repositories.mongodb.get_database import get_database


class MongoDBStudentRepository:
    def __init__(self, database: Database = Depends(get_database)):
        self.database = database

    def get_students_in_dropout(self) -> List[Student]:
        students_dict = list(self.database.students.find({"dropout": True}))
        students = list(map(lambda student: StudentModel(
            student).to_entity(), students_dict))

        return students

    def get_all_students(self) -> List[Student]:
        students_dict = list(self.database.students.find({}))
        students = list(map(lambda student: StudentModel(
            student).to_entity(), students_dict))

        return students

    def count_students(self) -> int:
        return self.database.students.count_documents({})

    def update_many(self, students: List[Student]):
        students_dict = list(map(lambda student: StudentModel.from_entity(
            student).to_dict(), students))

        for student in students_dict:
            self.database.students.update_one(
                {"_id": student["_id"]}, {"$set": {"dropout": student["dropout"]}})

    def count_students_by_category(self, category: str) -> int:
        if category not in ["income", "payment_status", "engagement", "attendance", "performance"]:
            raise ValueError(f"Invalid category: {category}")

        count = self.database.students.count_documents({category: {"$exists": True, "$ne": None}})

        return count
