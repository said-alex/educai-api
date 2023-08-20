from pydantic import BaseModel


class Predict(BaseModel):
    performance: int
    attendance: int
    engagement: int
    paymentStatus: int
    income: int
