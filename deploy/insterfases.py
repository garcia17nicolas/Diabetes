from pydantic import BaseModel

class dataTest(BaseModel):
    nombre: str
    estudiantes: float


class DiabetesData(BaseModel):
    Pregnancies: int
    Glucose: float
    Bloodpressure: float
    Skinthinkness: float
    Insuline: float
    BMI: float
    DiabetesPedigreeFuntion: float
    Age: int
