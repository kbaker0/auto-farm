# temperature_min = 23
# temperature_max = 27
# conductivity_min = 8
# conductivity_max = 15
# humidity_min = 35
# humidity_max = 65
# water_min = 10
# water_max = 15
# ph_min = 5.5
# ph_max = 7.0

alert_dict = {
    'temperature_min' : 23,
    'temperature_max' : 27,
    'conductivity_min' : 8,
    'conductivity_max' : 15,
    'humidity_min' : 35,
    'humidity_max' : 65,
    'water_min' : 10,
    'water_max' : 15,
    'ph_min' : 5.5,
    'ph_max' : 7.0
    }

def alert(sensor, value):

    if sensor == "temperature":
        if value <= alert_dict.temperature_min or value >= alert_dict.temperature_max:
            print(sensor, " is out of the normal range")
    elif sensor == "conductivity":
        if value <= alert_dict.conductivity_min or value >= alert_dict.conductivity_max:
            print(sensor, " is out of the normal range")
    elif sensor == "humidity":
        if value <= alert_dict.humidity_min or value >= alert_dict.humidity_max:
            print(sensor, " is out of the normal range")
    elif sensor == "water":
        if value <= alert_dict.water_min or value >= alert_dict.water_max:
            print(sensor, " is out of the normal range")
    elif sensor == "pH":
        if value <= alert_dict.ph_min or value >= alert_dict.ph_max:
            print(sensor, " is out of the normal range: ", value)
    

