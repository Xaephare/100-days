import requests
import os
from datetime import datetime
from dotenv import load_dotenv

GENDER = "male"
WEIGHT = "72"
HEIGHT = "180"
AGE = 26

load_dotenv()
APP_ID = os.getenv("NUT_ID")
API_KEY = os.getenv("NUT_KEY")
SHEETY_KEY = os.getenv("SHEETY_KEY")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}
sheety_header = {
    "Authorization": f"Bearer {SHEETY_KEY}"
}


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.getenv("SHEETY")

# No these are not my actual body parameters
exercises_done = input("What did you do today?: ")
params = {
    "query": exercises_done,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=params,  headers=headers)
data = response.json()['exercises']

today = datetime.now()

for exercise in data:
    sheet_inputs = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_header)
