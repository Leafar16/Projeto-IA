from enum import Enum

class Weather(Enum):
    CLEAR = 1
    RAIN = 3
    STORM = 2
    BLOCKED=999

    
# Example usage
def get_weather_cost(weather):
    return weather.value