from schemas.values import Values


def values_list(values: Values):
    values_to_predict = list()

    # Include holiday:
    if values.holiday == "no":
        values_to_predict.append(0)
    else:
        values_to_predict.append(1)

    # Include °C:
    values_to_predict.append(values.c)

    # Include solar_rad:
    values_to_predict.append(values.solar_rad)

    # Include wind_speed:
    values_to_predict.append(values.wind_speed)

    # Include humidity:
    values_to_predict.append(values.humidity)

    # Include rain_snow:
    if values.rain_snow == "no":
        values_to_predict.append(0)
    else:
        values_to_predict.append(1)

    # Include day_div:
    if values.day_div == "morning" :
        values_to_predict = values_to_predict + [1, 0, 0]
    elif values.day_div == "afternoon":
        values_to_predict = values_to_predict + [0, 1, 0]
    elif values.day_div == "night":
        values_to_predict = values_to_predict + [0, 0, 1]
    else:
        values_to_predict = values_to_predict + [0, 0, 0]

    # Include season:
    if values.season == "spring":
        values_to_predict = values_to_predict + [1, 0, 0]
    elif values.season == "summer":
        values_to_predict = values_to_predict + [0, 1, 0]
    elif values.season == "autumn":
        values_to_predict = values_to_predict + [0, 0, 1]
    else:
        values_to_predict = values_to_predict + [0, 0, 0]

    return [values_to_predict]
