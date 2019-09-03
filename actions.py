# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []
from rasa_sdk import Action
from rasa_sdk.forms import FormAction


class WeatherSearch(object):
    def searchByName(self, city_name):
        #do search here
        return {"dummy":"Cloudy"}

    def searchByCity_country(self,city, country):
        # do search here
        return {"dummy": "Sunny"}

    def searchById(self, city_id):
        # do search here
        return {"dummy":"Clear"}


class WeatherActions(Action):

    def name(self):
        return "action_search_weather"

    def run(self, dispatcher, tracker, domain):
        return None


class WeatherForm(FormAction):
    def name(self):  # type: () -> Text:
        return "weather_form"

    @staticmethod
    def required_slots(tracker):  # type: (Tracker) -> List[Text]:
         return ["city"]

    def submit(self, dispatcher, tracker, domain):  # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_template("utter_submit", tracker)
        return []




