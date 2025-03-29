
from fastapi import FastAPI, HTTPException

from insterfases import dataTest

app = FastAPI()
cursos ={
    "programacion":{"Fundamentos":15,"POO":20},
    "matematicas":{"matEspeciales":20,"calculoVect":25} 
}
@app.get("/")
def index():
    return {"Mensaje" : "Nicolas garcia"}

@app.get("/cursos")
def index():
    return cursos

@app.get("/cursos/{tipo}")
def tipoCursos(tipo: str):
    if tipo not in cursos:
        raise HTTPException(status_code=404,datail="Tipo de curso no encontrado")
    return {"curso":cursos[tipo]}

@app.post("/asignatura")
def asignatura(data: dataTest):
    data = data.model_dump()

    return {"asiganatura":data}


    
if __name__=="__main__":
    app.rum()