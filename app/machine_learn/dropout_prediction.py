import pickle
from typing import List
import pandas as pd


class PredictParams:
    def __init__(self, performance: int, attendance: int, engagement: int, payment_status: int, income: int):
        self.performance = performance
        self.attendance = attendance
        self.engagement = engagement
        self.payment_status = payment_status
        self.income = income


class DropoutPrediction:
    def __init__(self):
        self.model = pickle.load(
            open('app/machine_learn/models/dropout_model.pkl', 'rb'))

        self.scaler = pickle.load(
            open('app/machine_learn/scalers/scaler.pkl', 'rb'))

    def predict(self, data: List[PredictParams]) -> list:
        to_predict = {
            'Desempenho Academico': [performance for performance in map(lambda x: x.performance, data)],
            'Frequencia': [attendance for attendance in map(lambda x: x.attendance, data)],
            'Engajamento': [engagement for engagement in map(lambda x: x.engagement, data)],
            'Adimplencia': [payment_status for payment_status in map(lambda x: x.payment_status, data)],
            'Renda': [income for income in map(lambda x: x.income, data)]
        }

        to_transform = pd.DataFrame(to_predict)
        scaled = self.scaler.transform(to_transform)
        result = self.model.predict(scaled)

        return result.tolist()
