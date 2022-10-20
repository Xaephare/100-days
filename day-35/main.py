import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
OWM_KEY = os.getenv('OWM_KEY')
CITY = 'Dunedin, NZ'
TWILIO_SID = 'AC211aff4bdedf4fe4e089961597d463a9'
AUTH_TOKEN = os.getenv('TOKEN')
PHONE_NUM = os.getenv('PHONE')

location_response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={CITY}&appid={OWM_KEY}")
location_response.raise_for_status()
location_data = location_response.json()
lat = location_data[0]['lat']
lon = location_data[0]['lon']

weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={OWM_KEY}")
weather_response.raise_for_status()
weather_data = weather_response.json()

# from 'list' index 0 - 5 == 6am - 9pm, 3h increments
weather_ids = [weather_data['list'][num]['weather'][0]['id'] for num in range(6)]
weather_times = [weather_data['list'][num]['dt_txt'] for num in range(6)]

print(weather_ids)
print(weather_times)

will_rain = False
for id_num in weather_ids:
    if id_num < 700:
        will_rain = True

if will_rain:
    client = Client(TWILIO_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="It's gonna rain today.",
        from_='+16614664633',
        to=PHONE_NUM
    )
    print(message.status)
