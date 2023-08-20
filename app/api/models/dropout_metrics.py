from pydantic import BaseModel

class DropoutMetrics(BaseModel):
    dropoutRiskPercentage: float
    monthlyRevenueInRisk: float
    yearlyRevenueInRisk: float
