import requests
import os
from dotenv import load_dotenv

load_dotenv()
pixela_endpoint = "https://pixe.la/v1/users"
pixela_params = {
    "token": os.getenv("TOKEN"),
    "username": "xaephare",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

