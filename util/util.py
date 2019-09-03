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



# find_city(get_city_list(),'pun')
