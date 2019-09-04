from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
import requests
from util import bot_util
import logging

logger = logging.getLogger(__name__)


class WeatherSearch(object):
    def __init__(self):
        self.api_id = 'XXX'

    def searchByName(self, city_name):
        # do search here
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city_name, self.api_id)
        print(url)
        result = requests.get(url).json()
        print(result)

        return result

    def searchByCity_country(self, city, country):
        # do search here
        return {"dummy": "Sunny"}

    def searchById(self, city_id):
        # do search here
        return {"dummy": "Clear"}


class WeatherActions(Action):

    def name(self):
        return "action_search_weather"

    def run(self, dispatcher, tracker, domain):
        return None


class WeatherForm(FormAction):

    def name(self):  # type: () -> Text
        return "weather_form"

    # def get_city_list(self, name):
    #     #load json
    #     #search city
    #     return None

    # # @staticmethod
    # def validate_city(self, slot_dict, dispatcher, tracker, domain):  # type: (Dict[Text, Any], CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
    #     print(slot_dict)
    #     import pdb
    #     pdb.set_trace()
    #     city = slot_dict.lower()
    #     city_list = find_city(city)
    #     if len(city_list) == 1:
    #         print(city_list)
    #         city_name= city_list[0]['name']
    #         country_code = city_list[0]['country']
    #         SlotSet("country",country_code)
    #         return {"city": city_name}
    #     else:
    #         dispatcher.utter_template("utter_wrong_city", tracker)
    #         return [SlotSet("city", None), SlotSet("country", None)]

    @staticmethod
    def required_slots(tracker):  # type: (Tracker) -> List[Text]
        return ["city"]



    def submit(self, dispatcher, tracker,
               domain):  # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        weather_info = WeatherSearch()
        city = tracker.get_slot('city')
        result = weather_info.searchByName(city)
        logger.info(result)
        result_dict = bot_util.create_message(result)
        dispatcher.utter_message('Weather for {} is {}. Temperature is {} kelvin, humidity is {} and wind speed is {}'.format(city,
                                                                     result_dict['weather'],
                                                                     result_dict['temp'], result_dict['humidity'],
                                                                     result_dict['wind_speed']))
        return [SlotSet("city", None)]


class TemperatureAction(FormAction):
    def name(self):  # type: () -> Text
        return "temperature_form"

    @staticmethod
    def required_slots(tracker):  # type: (Tracker) -> List[Text]
        return ["city"]

    def submit(self, dispatcher, tracker,
               domain):  # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        weatherInfp = WeatherSearch()
        city = tracker.get_slot('city')
        result = weatherInfp.searchByName(city)
        logger.info(result)
        result_dict = bot_util.create_message(result)
        dispatcher.utter_message('Temperature for {} is {} kelvin'.format(city, result_dict['temp']))
        return [SlotSet("city", None)]
