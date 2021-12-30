import json

with open('sample.json') as json_file:
    data = json.load(json_file)
    print(data)
    my_cicle = data['growth_cycle']
    # print("Time off: " + my_cicle['time_off'])
    # print("Time on: " + my_cicle['time_on'])
    # print("Light color: " + my_cicle['led_color'])
