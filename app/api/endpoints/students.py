from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_students():
    return {
        "data": [{
             "name": "John",
            "courseName": "Matemática",
        }],
        "meta": {
            "monthlyIncome": 1000,
            "yearlyIncome": 12000,
            "evasionRiskPercentage": "87",
            "evationRiskStudentsCount": 3769,
        },
    }
