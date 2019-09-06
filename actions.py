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
        result = requests.get(url).json()
        return result


class ActionChitchat(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self):
        return "action_chitchat"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message["intent"].get("name")

        # retrieve the correct chitchat utterance dependent on the intent
        if intent in [
            "ask_builder",
            "ask_weather",
            "ask_howdoing",
            "ask_whatspossible",
            "ask_whatisrasa",
            "ask_isbot",
            "ask_howold",
            "ask_languagesbot",
            "ask_restaurant",
            "ask_time",
            "ask_wherefrom",
            "ask_whoami",
            "handleinsult",
            "nicetomeeyou",
            "telljoke",
            "ask_whatismyname",
            "ask_howbuilt",
            "ask_whoisit",
        ]:
            dispatcher.utter_template("utter_" + intent, tracker)
        return []


class WeatherActions(Action):

    def name(self):
        return "action_search_weather"

    def run(self, dispatcher, tracker, domain):
        return None


class WeatherForm(FormAction):

    def name(self):  # type: () -> Text
        return "weather_form"

    @staticmethod
    def required_slots(tracker):  # type: (Tracker) -> List[Text]
        return ["city"]

    def submit(self, dispatcher, tracker,
               domain):  # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        weather_info = WeatherSearch()
        city = tracker.get_slot('city')
        result = weather_info.searchByName(city)
        logger.info(result)
        if result['cod'] == 200:
            result_dict = bot_util.create_message(result)
            dispatcher.utter_message(
                'Weather for {} is {}. Temperature is {:4.2f} C, humidity is {} % and wind speed is {} mps'.format(city,
                                                                                                             result_dict[
                                                                                                                 'weather'],
                                                                                                             int(result_dict[
                                                                                                                 'temp']) -273.15,
                                                                                                             result_dict[
                                                                                                                 'humidity'],
                                                                                                             result_dict[
                                                                                                                 'wind_speed']))
        else:
            dispatcher.utter_message(result['message'])
        return [SlotSet("city", None)]


class TemperatureAction(FormAction):
    def name(self):  # type: () -> Text
        return "temperature_form"

    @staticmethod
    def required_slots(tracker):  # type: (Tracker) -> List[Text]
        return ["city"]

    def submit(self, dispatcher, tracker,
               domain):  # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        weather_info = WeatherSearch()
        city = tracker.get_slot('city')
        result = weather_info.searchByName(city)
        logger.info('Result from API:{}'.format(result))
        if result['cod'] == 200:
            result_dict = bot_util.create_message(result)
            dispatcher.utter_message('Temperature for {} is {:4.2f} C'.format(city, int(result_dict['temp']) -273.15))
        else:
            dispatcher.utter_message(result['message'])
        return [SlotSet("city", None)]


class RainAction(FormAction):
    def name(self):  # type: () -> Text
        return "rain_form"

    @staticmethod
    def required_slots(tracker):  # type: (Tracker) -> List[Text]
        return ["city"]

    def submit(self, dispatcher, tracker,
               domain):  # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        weather_info = WeatherSearch()
        city = tracker.get_slot('city')
        result = weather_info.searchByName(city)
        logger.info('Result from API:{}'.format(result))
        if result['cod'] == 200:
            result_dict = bot_util.create_message(result)
            dispatcher.utter_message('Weather for for {} is {}. Humidity level is {} %'.format(
                city, result_dict['weather'],result_dict['humidity']))
        else:
            dispatcher.utter_message(result['message'])
        return [SlotSet("city", None)]
