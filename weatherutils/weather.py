import requests


class Weather:

    def __init__(self):
        self.json = self.weather_info()
        self.temp_kelvin = self.get_temperature()
        self.celsius = self.kelvin_to_Celsius()
        self.description = self.get_description()
        self.c = str(self.round())


    def weather_info(self):
        url = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=gothenburg'
        return requests.get(url).json()

    def get_description(self):
        return self.json['weather'] [0] ["description"]

    def get_temperature(self):
        return self.json['main'] ["temp"]

    def kelvin_to_Celsius(self):
        return self.temp_kelvin- 273.15

    def round(self):
        return round(self.celsius)

    def temp_float_to_string(self):
        return str(self.c)








