from fastapi import APIRouter, Depends, Response

from app.services.get_dropout_students import GetDroupoutStudents
from app.services.get_income_risk import GetIncomeRisk
from app.services.student_notifier import StudentNotifier

router = APIRouter()


@router.get("/")
async def get_students_stats(
        get_dropout_students: GetDroupoutStudents = Depends(
            GetDroupoutStudents),
        get_income_risk: GetIncomeRisk = Depends(GetIncomeRisk)):

    evationRiskStudentsCount, evasionRiskPercentage = get_dropout_students.get_stats()
    monthly_income, yearly_income = get_income_risk.get_risk()

    return {
        "monthlyIncome": monthly_income,
        "yearlyIncome": yearly_income,
        "evasionRiskPercentage": evasionRiskPercentage,
        "evationRiskStudentsCount": evationRiskStudentsCount,
    }


@router.post("/notify", status_code=204, response_class=Response)
async def notify(student_notifier: StudentNotifier = Depends(StudentNotifier)):
    student_notifier.notify()
