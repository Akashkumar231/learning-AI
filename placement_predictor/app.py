from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# load trained model
model = joblib.load("model.pkl")


class Student(BaseModel):
    iq: float
    cgpa: float


@app.post("/predict")
def predict(data: Student):
    input_data = np.array([[data.iq, data.cgpa]])
    prediction = model.predict(input_data)

    return {"placement": int(prediction[0])}