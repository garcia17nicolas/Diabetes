import pickle 
from fastapi import FastAPI
import numpy as np

from insterfases import DiabetesData


app = FastAPI()

with open ("RFDiabetesv132.pkl","rb") as file:
    model=pickle.load(file)


@app.get ("/")
def index():
    return{"Mensaje":"API 2 running"}

@app.post("/predict")
def predict(data: DiabetesData):
    data = data.model_dump()
    print(data)

    Pregnancies=data["Pregnancies"]
    Glucose=data["Glucose"]
    Bloodpressure=data["Bloodpressure"]
    Skinthinkness=data["Skinthinkness"]
    Insuline=data["Insuline"]
    BMI=data["BMI"]
    DiabetesPedigreeFuntion=data["DiabetesPedigreeFuntion"]
    Age=data["Age"]

    xin = np.array([Pregnancies,Glucose,Bloodpressure,Skinthinkness,
                    Insuline,BMI,DiabetesPedigreeFuntion,Age]).reshape(1,8)
    prediction = model.predict(xin)
    
    print(prediction)


    label_map = {0:"Paciente sano", 1: "Paciente enfermo"}
    label = [label_map[p] for p in prediction]
    print ("prediction:  ",label)
    
    return {"prediction" : str (label)}

if __name__=="__main__":
    app.rum()