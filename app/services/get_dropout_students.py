from fastapi import Depends

from app.repositories.in_memory.students_repository import InMemoryStudentsRepository

class StudentsInDropout:
    def __init__(self, name: str, course_name: str):
        self.name = name
        self.curse_name = course_name

class GetDroupoutStudents:
    def __init__(self, student_repo = Depends(InMemoryStudentsRepository)):
        self.student_repo = student_repo

    def get_students(self):
        students = self.student_repo.get_students_in_dropout()
        
        total_students = self.student_repo.count_students()
        percente_in_dropout = round(len(students) / total_students * 100, 2)

        students_response = list(map(lambda student: StudentsInDropout(student.name, student.course.name), students))   

        return students_response, percente_in_dropout
