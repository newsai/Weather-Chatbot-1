# Weather-Chatbot

This is an implementation of Weather Chatbot using RASA framework.
To fetch the weather details, I am using [OpenWeathermap Api](https://openweathermap.org/api)

If you want to use it, you need to specify  your API key in the Action.py file

```python
class WeatherSearch(object):
    def __init__(self):
        self.api_id = '<Your_API_Key>'
 ```
 
 Also currently I am training it is using terminal. Later will add script for training.
 To train the model, run
 ```bash
 rasa train
 ```
 
 To run, first run the action using
 ```bash
 rasa run actions
 ```
 
 and after it
 ```bash
 rasa shell --endpoints endpoints.yml 
 ```
 
 To run it in interactive mode, run
 ```bash
 rasa shell --endpoints endpoints.yml 
 ```
 
 Feel free to add  improvements, as I am creating for learning purpose
