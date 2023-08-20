import pickle
import pandas as pd


class PredictParams:
    perfomance: int
    attendance: int
    engagement: int
    payment_status: int
    income: int


class DropoutPrediction:
    def __init__(self):
        self.model = pickle.load(
            open('app/machine_learn/models/dropout_model.pkl', 'rb'))

        self.scaler = pickle.load(
            open('app/machine_learn/scalers/scaler.pkl', 'rb'))

    def predict(self, performance: int, attendance: int, engagement: int, payment_status: int, income: int) -> int:
        data = {
            'Desempenho Academico': [performance],
            'Frequencia': [attendance],
            'Engajamento': [engagement],
            'Adimplencia': [payment_status],
            'Renda': [income]
        }

        print(data)

        to_transform = pd.DataFrame(data)
        scaled = self.scaler.transform(to_transform)
        result = self.model.predict(scaled)

        return result[0].item()
