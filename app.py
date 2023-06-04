import pickle
from fastapi import FastAPI
from schemas.values import Values
from functions.values_trans import values_list
from fastapi.responses import RedirectResponse


app = FastAPI(
    title="Despliege",
    description="Despliege del modelo de machine learning",
    version="1.0",
)

pickle2 = open("data/modeloE.pkl", "rb")
modelE = pickle.load(pickle2)


@app.get("/")
def index():
    return RedirectResponse(url="/docs")


@app.post(
    "/model/enssemble",
    tags=["Machine Learnig"],
    description="Funcion que permite predecir el numero de bicicletas demandadas bajo la condiciones ingresadas, con modelo regresion por ensamble.",
)
def model_assembly(values: Values):
    values_to_predict = values_list(values)
    prediction = modelE.predict(values_to_predict)[0]
    return f"A total demand of {prediction} bicycles is estimated."
