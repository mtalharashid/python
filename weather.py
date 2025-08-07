# ------------------------------------- Google Weather API -----------------------------------
# get a city name from user and show the weather report of that specific city 

import requests

city = input("Enter the city name: ")

API_KEY = 'd993c1b134e6b539aa1bad9e927d17e3'
# city = 'Dubai'
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

for key, value in data.items():
    print(f"{key.capitalize()}: {value}")
    
print("---------------------------------------------------------------------------------")
print("----------------------------- 2nd API -------------------------------------------")
print("---------------------------------------------------------------------------------")

# ------------------------------------- Open Meteo Weather API -----------------------------------

# add 'long' and 'lat' of Dubai

latitude = 25.276987
longitude = 55.296249

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

response = requests.get(url)
data = response.json()
data = data['current_weather']

for result in data:
    print(result.capitalize(), data[result])

for key, value in data.items():
    print(f"{key.capitalize()}: {value}")

