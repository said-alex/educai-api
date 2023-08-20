from fastapi import Depends

from app.repositories.mongodb.student_repository import MongoDBStudentRepository


class StudentsInDropout:
    def __init__(self, name: str):
        self.name = name

class GetDroupoutStudents:
    def __init__(self, student_repo=Depends(MongoDBStudentRepository)):
        self.student_repo = student_repo

    def get_stats(self):
        students = self.student_repo.get_students_in_dropout()

        total_students = self.student_repo.count_students()
        percente_in_dropout = round(len(students) / total_students * 100, 2)

        return len(students), percente_in_dropout
