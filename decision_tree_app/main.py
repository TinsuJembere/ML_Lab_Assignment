from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
templates = Jinja2Templates(directory="templates")

model = joblib.load("model.joblib")

# JSON input model
class InputData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(data: InputData):
    arr = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    pred_class = int(model.predict(arr)[0])

    flower_map = {
        0: "Setosa",
        1: "Versicolor",
        2: "Virginica"
    }

    return {
        "class": pred_class,
        "flower": flower_map[pred_class]
    }

