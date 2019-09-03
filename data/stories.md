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
