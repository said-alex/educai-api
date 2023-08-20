from fastapi import Depends
from app.machine_learn.dropout_prediction import DropoutPrediction, PredictParams

from app.repositories.mongodb.student_repository import MongoDBStudentRepository


class ClassifyStudents:
    def __init__(
            self,
            student_repo: MongoDBStudentRepository = Depends(
                MongoDBStudentRepository),
            dropout_prediction: DropoutPrediction = Depends(DropoutPrediction)):

        self.student_repo = student_repo
        self.dropout_prediction = dropout_prediction

    def classify(self):
        students = self.student_repo.get_all_students()

        for student in students:
            predict = self.dropout_prediction.predict(
                attendance=student.attendance,
                engagement=student.engagement,
                payment_status=student.payment_status,
                income=student.income,
                performance=student.performance
            )

            student.dropout = predict

            self.student_repo.update(student)

        return students
