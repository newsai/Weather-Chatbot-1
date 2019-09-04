## happy path
* greet
  - utter_greet
* praise
  - utter_praise

## sad path 1
* greet
  - utter_greet
* insult
  - utter_handleinsult

## sad path 2
* greet
  - utter_greet
* insult
  - utter_handleinsult
* goodbye
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye
  
## bot_functions 
* greet
  - utter_greet
* ask_whatspossible
    - action_chitchat

##story_form
* greet
    - utter_greet
* ask_whatspossible
    - action_chitchat
* search_weather
    - weather_form
    - form{"name": "weather_form"}
    - form{"name": null}
* praise
  - utter_praise

##story_chitchat
* greet
    - utter_greet
* ask_whatspossible
    - action_chitchat
* ask_howold
    - action_chitchat
* ask_isbot
    - action_chitchat
* ask_languagesbot
    - action_chitchat
* ask_time
    - action_chitchat
* ask_whatismyname
    - action_chitchat
* ask_wherefrom
    - action_chitchat
* ask_whoami
    - action_chitchat
* ask_builder
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* ask_whoisit
    - action_chitchat


## Generated Story 3183310183320455154
* greet
    - utter_greet
* ask_whatspossible
    - action_chitchat
* ask_whoisit
    - action_chitchat
* search_weather{"city": "Pune"}
    - slot{"city": "Pune"}
    - weather_form
    - form{"name": "weather_form"}
    - slot{"city": "Pune"}
    - slot{"city": "Pune"}
    - form{"name": null}
    - slot{"requested_slot": null}
* insult
  - utter_handleinsult
* goodbye
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
 * insult
  - utter_handleinsult

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
* praise
  - utter_praise
* goodbye
    - utter_goodbye

## interactive_story_1
* search_temperature
    - temperature_form
    - form{"name": "temperature_form"}
    - slot{"requested_slot": "city"}
* form: inform{"city": "Pune"}
    - slot{"city": "Pune"}
    - form: temperature_form
    - slot{"city": "Pune"}
    - slot{"city": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* search_temperature{"city": "Nagpur"}
    - slot{"city": "Nagpur"}
    - temperature_form
    - form{"name": "temperature_form"}
    - slot{"city": "Nagpur"}
    - slot{"city": "Nagpur"}
    - slot{"city": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* praise
  - utter_praise

## interactive_story_1
* search_weather{"city": "Pune"}
    - slot{"city": "Pune"}
    - weather_form
    - form{"name": "weather_form"}
    - slot{"city": "Pune"}
    - slot{"city": "Pune"}
    - slot{"city": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* search_temperature{"city": "Pune"}
    - slot{"city": "Pune"}
    - temperature_form
    - form{"name": "temperature_form"}
    - slot{"city": "Pune"}
    - slot{"city": "Pune"}
    - slot{"city": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* search_temperature
    - temperature_form
    - form{"name": "temperature_form"}
    - slot{"requested_slot": "city"}
* form: inform{"city": "Mumbai"}
    - slot{"city": "Mumbai"}
    - form: temperature_form
    - slot{"city": "Mumbai"}
    - slot{"city": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* search_weather{"city": "London"}
    - slot{"city": "London"}
    - weather_form
    - form{"name": "weather_form"}
    - slot{"city": "London"}
    - slot{"city": "London"}
    - slot{"city": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* search_temperature
    - temperature_form
    - form{"name": "temperature_form"}
    - slot{"requested_slot": "city"}
* form: inform{"city": "Lichtenrade"}
    - slot{"city": "Lichtenrade"}
    - form: temperature_form
    - slot{"city": "Lichtenrade"}
    - slot{"city": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* praise
  - utter_praise
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* search_temperature
    - temperature_form
    - form{"name": "temperature_form"}
    - slot{"requested_slot": "city"}
* form: inform{"city": "Mumbai"}
    - slot{"city": "Mumbai"}
    - form: temperature_form
    - slot{"city": "Mumbai"}
    - slot{"city": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* inform{"city": "Pune"}
    - slot{"city": "Pune"}
    - weather_form
    - form{"name": "weather_form"}
    - slot{"city": "Pune"}
    - slot{"city": "Pune"}
    - slot{"city": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* search_temperature
    - temperature_form
    - form{"name": "temperature_form"}
    - slot{"requested_slot": "city"}
* form: inform{"city": "Nagpur"}
    - slot{"city": "Nagpur"}
    - form: temperature_form
    - slot{"city": "Nagpur"}
    - slot{"city": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* praise
    - utter_praise
* goodbye
    - utter_goodbye
    
    
## fallback story
* greet
  - utter_greet
* out_of_scope
  - action_default_fallback
* greet
  - utter_greet

## interactive_story_1
* ask_whoisit
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* ask_howold
    - action_chitchat
* ask_builder
    - action_chitchat
* ask_whoami
    - action_chitchat
* ask_time
    - action_chitchat
* ask_languagesbot
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_isbot
    - action_chitchat
* ask_wherefrom
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* out_of_scope
  - action_default_fallback
