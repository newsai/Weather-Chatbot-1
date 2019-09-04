import json

def get_city_list():
    with open('data/city.list.json') as f:
        j = json.load(f)
    return j

def find_city(city_name):
    city_list = get_city_list()
    cities = []
    for city in city_list:
        if city_name in city['name'].lower():
            cities.append(city)
    return cities


def create_message(json_response):
    weather = json_response['weather'][0]['main']
    temp = json_response['main']['temp']
    humidity = json_response['main']['humidity']
    wind_speed = json_response['wind']['speed']

    return {'weather': weather, 'temp': temp, 'humidity': humidity, 'wind_speed': wind_speed}
