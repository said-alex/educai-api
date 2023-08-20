from fastapi import APIRouter, Depends
from app.api.models.predict import Predict

from app.machine_learn.dropout_prediction import DropoutPrediction

router = APIRouter()


@router.post("/")
async def predict(
        predict: Predict,
        dropout_prediction: DropoutPrediction = Depends(DropoutPrediction)):

    data = {
        'Desempenho Academico': [predict.performance],
        'Frequencia': [predict.attendance],
        'Engajamento': [predict.engagement],
        'Adimplencia': [predict.paymentStatus],
        'Renda': [predict.income]
    }

    dropout = dropout_prediction.predict(data)

    return {"dropout": dropout, "description": map_dropout_prediction(dropout)}


def map_dropout_prediction(prediction):
    if prediction == 0:
        return "risk of dropout"
    else:
        return "no risk of dropout"
