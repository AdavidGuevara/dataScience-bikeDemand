class Values:
    def __init__(
        self,
        season: str,
        day_div: str,
        holiday: str,
        c: float,
        rain_snow: str,
        humidity: float,
        solar_rad: float,
        wind_speed: float,
    ) -> None:
        self.season = season
        self.day_div = day_div
        self.holiday = holiday
        self.c = c
        self.rain_snow = rain_snow
        self.humidity = humidity
        self.solar_rad = solar_rad
        self.wind_speed = wind_speed
