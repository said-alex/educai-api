from fastapi import Depends
from app.notifier.email_notifier import EmailNotifier


from app.repositories.mongodb.student_repository import MongoDBStudentRepository


class StudentNotifier:
    def __init__(
            self,
            student_repo: MongoDBStudentRepository = Depends(
                MongoDBStudentRepository),
            email_notifier: EmailNotifier = Depends(EmailNotifier)):
        self.student_repo = student_repo
        self.email_notifier = email_notifier

    def notify(self):
        students_in_dropout = self.student_repo.get_students_in_dropout()

        for student in students_in_dropout:
            self.email_notifier.notify(
                "andre.glatz94@gmail.com",
                'Educaí - Atenção',
                f'Olá {student.name}, estamos entrando em contato para informar que você está com risco de evasão escolar. Por favor, entre em contato com a escola para mais informações.')
