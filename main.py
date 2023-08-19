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
