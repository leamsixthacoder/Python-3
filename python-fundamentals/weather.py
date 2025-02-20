import requests

city = "Miami"
url = f"http://api.weatherapi.com/v1/current.json?key=4810ce797abb4670a4f24823252002&q={city}&aqi=no"
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get("current").get("temp_f")
description = weather_json.get("current").get("condition").get("text")

print(f"Today's weather in {city} is {description} with a temperature of {temp} degrees.")