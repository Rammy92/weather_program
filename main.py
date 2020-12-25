import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Kungsbacka'

url = api_address
json_data = requests.get(url).json()
format_add = json_data['weather'] [0] ["description"]
formatted_add = json_data['main'] ["temp"]
Kelvin = float(formatted_add)
print(Kelvin)
Celsius = Kelvin - 273.15
temp = round(Celsius, 2)

print(format_add)
print(formatted_add)
print(Celsius)
print (temp)

