from weatherutils.get_date import get_date
from weatherutils.weather import Weather
weather = Weather()

class File():

    def __init__(self):
        self.date = get_date()
        self.weather = weather.get_description()
        self.temp = weather.temp_float_to_string()

    def write_to_file(self):
        my_file = open("/home/rammy/weather_program/weather.txt", "a+")
        my_file.write("\n" + self.date + "It's " + self.weather + " outside." "\n" + "Outside temperature " + self.temp + " celsius." + "\n" )
        

