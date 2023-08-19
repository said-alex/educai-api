from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return {"status": "ok"}

@app.get("/test_model_acuracy")
def get_test_model_acuracy():
    return {"msg": "test_model_acuracy"}

@app.get("/test_model_predict")
def get_test_model_predict():
    return {"msg": "get_test_model_predict"}

@app.get("/students")
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
