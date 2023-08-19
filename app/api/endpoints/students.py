from fastapi import APIRouter

from app.services.get_dropout_students import GetDroupoutStudents
from app.services.get_income_risk import GetIncomeRisk

router = APIRouter()
get_dropout_students = GetDroupoutStudents()
get_income_risk = GetIncomeRisk()

@router.get("/")
def get_students():
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

# return {
#     "data": [{
#          "name": "John",
#         "courseName": "Matemática",
#     }],
#     "meta": {
#         "monthlyIncome": 1000,
#         "yearlyIncome": 12000,
#         "evasionRiskPercentage": "87",
#         "evationRiskStudentsCount": 3769,
#     },
# }