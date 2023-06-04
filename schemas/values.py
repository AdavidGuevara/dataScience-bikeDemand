from typing import List, Optional
from pydantic import BaseModel, Field
from enum import Enum


class Choise(str, Enum):
    no = "no"
    yes = "yes"


class Season(str, Enum):
    summer = "summer"
    winter = "winter"
    spring = "spring"
    autumn = "autumn"


class Day(str, Enum):
    night = "night"
    early_morning = "early morning"
    morning = "morning"
    afternoon = "afternoon"


class Values(BaseModel):
    seasons: List[Season]
    day_div: List[Day]
    holiday: List[Choise]
    c: float = Field(ge=-17.80, le=39.40, default=10.8)
    rain_snow: List[Choise]
    humidity: float = Field(ge=0, le=98, default=49)
    radiation: float = Field(ge=0, le=3.52, default=1.76)
    wind_speed: float = Field(ge=0, le=7.40, default=3.7)
    