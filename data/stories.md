## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye
  
## bot_functions 
* greet
  - utter_greet
* bot_functions
  - utter_bot_functions

##story_form
* greet
    - utter_greet
* bot_functions
    - utter_bot_functions
* search_weather
    - weather_form
    - form{"name": "weather_form"}
    - form{"name": null}

## Generated Story 3183310183320455154
* greet
    - utter_greet
* bot_functions
    - utter_bot_functions
* search_weather{"city": "Pune"}
    - slot{"city": "Pune"}
    - weather_form
    - form{"name": "weather_form"}
    - slot{"city": "Pune"}
    - slot{"city": "Pune"}
    - form{"name": null}
    - slot{"requested_slot": null}
* goodbye
    - utter_goodbye
* stop
    - utter_goodbye

## interactive_story_1
* search_weather{"city": "Pune"}
    - slot{"city": "Pune"}
    - weather_form
    - form{"name": "weather_form"}
    - slot{"city": "Pune"}
    - slot{"city": "Pune"}
    - form{"name": null}
    - slot{"requested_slot": null}

## interactive_story_1
* search_weather{"city": "London"}
    - slot{"city": "London"}
    - weather_form
    - form{"name": "weather_form"}
    - slot{"city": "London"}
    - slot{"city": "London"}
    - form{"name": null}
    - slot{"requested_slot": null}
* goodbye
    - utter_goodbye

## interactive_story_1
* search_weather
    - weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "city"}
* form: inform{"city": "Pune"}
    - slot{"city": "Pune"}
    - form: weather_form
    - slot{"city": "Pune"}
    - form{"name": null}
    - slot{"requested_slot": null}
* inform{"city": "Mumbai"}
    - slot{"city": "Mumbai"}
    - weather_form
    - form{"name": "weather_form"}
    - slot{"city": "Mumbai"}
    - slot{"city": "Mumbai"}
    - form{"name": null}
    - slot{"requested_slot": null}
* search_weather{"city": "Nagpur"}
    - slot{"city": "Nagpur"}
    - weather_form
    - form{"name": "weather_form"}
    - slot{"city": "Nagpur"}
    - slot{"city": "Nagpur"}
    - form{"name": null}
    - slot{"requested_slot": null}
* goodbye
    - utter_goodbye
