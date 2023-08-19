from app.repositories.in_memory.students_repository import InMemoryStudentsRepository

class GetDroupoutStudents:
    def __init__(self):
        self.student_repo = InMemoryStudentsRepository()

    def get_students(self):
        students = self.student_repo.get_students_in_dropout()
        
        total_students = self.student_repo.count_students()
        percente_in_dropout = round(len(students) / total_students * 100, 2)

        return students, percente_in_dropout
