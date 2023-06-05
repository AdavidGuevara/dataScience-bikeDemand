import os
import pickle
import typing
from dotenv import load_dotenv
from schemas.values import Values
from fastapi.responses import HTMLResponse
from starlette.middleware import Middleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from functions.values_trans import values_list
from fastapi import FastAPI, Request, Form, status
from starlette.middleware.sessions import SessionMiddleware

load_dotenv()

middleware = [Middleware(SessionMiddleware, secret_key=os.environ["SECRET_KEY"])]

app = FastAPI(
    title="Despliege",
    description="Despliege del modelo de machine learning",
    version="1.0",
    middleware=middleware,
)

app.mount("/static", StaticFiles(directory="static"), name="static")


def flash(request: Request, message: typing.Any, category: str = "") -> None:
    if "_messages" not in request.session:
        request.session["_messages"] = []
    request.session["_messages"].append({"message": message, "category": category})


def get_flashed_messages(request: Request):
    print(request.session)
    return request.session.pop("_messages") if "_messages" in request.session else []


templates = Jinja2Templates(directory="./templates")
templates.env.globals["get_flashed_messages"] = get_flashed_messages

pickle2 = open("data/modeloE.pkl", "rb")
modelE = pickle.load(pickle2)


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post(
    "/",
)
def model_assembly(
    request: Request,
    season: str = Form(),
    day_div: str = Form(),
    holiday: str = Form(),
    c: float = Form(),
    rain_snow: str = Form(),
    humidity: float = Form(),
    solar_rad: float = Form(),
    wind_speed: float = Form(),
):
    """
    Funcion que permite predecir el numero de bicicletas demandadas bajo la condiciones ingresadas,
    con modelo regresion por ensamble.
    """

    values = Values(
        season, day_div, holiday, c, rain_snow, humidity, solar_rad, wind_speed
    )
    values_to_predict = values_list(values)
    prediction = modelE.predict(values_to_predict)[0]

    flash(
        request,
        f"A total demand of {int(prediction)} bicycles is estimated.",
        "success",
    )
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
