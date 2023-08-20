from fastapi import APIRouter, Depends, Response

from app.services.get_dropout_students import GetDroupoutStudents
from app.services.get_income_risk import GetIncomeRisk
from app.services.get_students_by_category import GetStudantByCategory
from app.services.student_notifier import StudentNotifier
from app.api.models.dropout_metrics import DropoutMetrics
from app.api.models.dropout_metrics_by_category import DropoutMetricsByCategory

router = APIRouter()


@router.get("/dropout_metrics", response_model=DropoutMetrics, tags=["students"])
def get_dropout_metrics(
    get_dropout_students: GetDroupoutStudents = Depends(),
    get_income_risk: GetIncomeRisk = Depends()
):
    dropoutRiskStudentsCount, dropoutRiskPercentage = get_dropout_students.get_stats()
    monthlyRevenueInRisk, yearlyRevenueInRisk = get_income_risk.get_risk()
    return {
        "dropoutRiskPercentage": dropoutRiskPercentage,
        "monthlyRevenueInRisk": monthlyRevenueInRisk,
        "yearlyRevenueInRisk": yearlyRevenueInRisk
    }


@router.post("/notify", status_code=204, response_class=Response)
async def notify(student_notifier: StudentNotifier = Depends(StudentNotifier)):
    student_notifier.notify()


@router.get("/{category}")
def get_dropout_metrics_by_category(
    category: str = "",
    get_dropout_students: GetStudantByCategory = Depends(GetStudantByCategory),
):
    count = get_dropout_students.get_by_category(category)

    return {
        "category": category,
        "count": count,
    }
