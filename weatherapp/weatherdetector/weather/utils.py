
def unit_conversion(meassure, unit):
    #temperature units
    if unit == "K":
        unit = "ºK"
    elif unit == "C":
        unit = "ºC"
        meassure -= 273.15
    elif unit == "F":
        unit = "ºF"
        meassure = (meassure - 273.15)*9/5 + 32
    #wind units
    elif unit == "ms":
        unit = "m/s"
    elif unit == "kmh":
        unit = "km/h"
        meassure *= 3.6
    elif unit == "mh":
        unit = "miles/h"
        meassure *= 2.237
    else:
        raise ValueError("Wrong unit")
    return format_measure(meassure, unit)


def format_measure(measure, unit):
    return f"{measure:.2f} {unit}"