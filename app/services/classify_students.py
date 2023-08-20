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

        params = [PredictParams(
            student.performance,
            student.attendance,
            student.engagement,
            student.payment_status,
            student.income
        ) for student in students]

        predictions = self.dropout_prediction.predict(params)

        for i in range(len(students)):
            if predictions[i] == 3:
                students[i].dropout = True
            else:
                students[i].dropout = False

        students_to_clustering = [
            student for student in students if student.dropout == True]

        params = [PredictParams(
            student.performance,
            student.attendance,
            student.engagement,
            student.payment_status,
            student.income
        ) for student in students_to_clustering]

        clustering = self.dropout_prediction.clustering(params)

        for i in range(len(students_to_clustering)):
            students[i].cluster = clustering[i]

        self.student_repo.update_many(students)

        return students
