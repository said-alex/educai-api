from fastapi import APIRouter, Depends

from app.services.get_dropout_students import GetDroupoutStudents
from app.services.get_income_risk import GetIncomeRisk

router = APIRouter()


@router.get("/")
async def get_students(
        get_dropout_students=Depends(GetDroupoutStudents),
        get_income_risk=Depends(GetIncomeRisk)):

    students, evasionRiskPercentage = get_dropout_students.get_students()
    monthly_income, yearly_income = get_income_risk.get_risk()

    return {
        "data": students,
        "meta": {
            "monthlyIncome": monthly_income,
            "yearlyIncome": yearly_income,
            "evasionRiskPercentage": evasionRiskPercentage,
            "evationRiskStudentsCount": len(students),
        },
    }
