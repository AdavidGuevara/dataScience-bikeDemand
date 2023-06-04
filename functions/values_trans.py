from schemas.values import Values


def values_list(values: Values):
    values_to_predict = list()

    # Include holiday:
    if "no" in values.holiday:
        values_to_predict.append(0)
    else:
        values_to_predict.append(1)

    # Include °C:
    values_to_predict.append(values.c)

    # Include solar_rad:
    values_to_predict.append(values.radiation)

    # Include wind_speed:
    values_to_predict.append(values.wind_speed)

    # Include humidity:
    values_to_predict.append(values.humidity)

    # Include rain_snow:
    if "no" in values.rain_snow:
        values_to_predict.append(0)
    else:
        values_to_predict.append(1)

    # Include day_div:
    if "morning" in values.day_div:
        values_to_predict = values_to_predict + [1, 0, 0]
    elif "afternoon" in values.day_div:
        values_to_predict = values_to_predict + [0, 1, 0]
    elif "night" in values.day_div:
        values_to_predict = values_to_predict + [0, 0, 1]
    else:
        values_to_predict = values_to_predict + [0, 0, 0]

    # Include season:
    if "spring" in values.seasons:
        values_to_predict = values_to_predict + [1, 0, 0]
    elif "summer" in values.seasons:
        values_to_predict = values_to_predict + [0, 1, 0]
    elif "autumn" in values.seasons:
        values_to_predict = values_to_predict + [0, 0, 1]
    else:
        values_to_predict = values_to_predict + [0, 0, 0]

    return [values_to_predict]
