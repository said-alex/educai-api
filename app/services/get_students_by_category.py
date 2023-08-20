from fastapi import Depends

from app.repositories.mongodb.student_repository import MongoDBStudentRepository


class GetStudantByCategory:
    def __init__(self, student_repo: MongoDBStudentRepository = Depends(MongoDBStudentRepository)):
        self.student_repo = student_repo

    def get_by_category(self, category: str):
        return self.student_repo.count_students_by_category(category)
