import requests
import datetime as dt
import os

AGE = 21
GENDER = "male"
WEIGHT_KG = 58
HEIGHT_CM = 168

TODAY = dt.datetime.now()
DATE = TODAY.strftime("%d/%m/%Y")
TIME = TODAY.strftime("%X")
print(DATE)
print(TIME)

APP_ID = os.environ["ENV_APP_ID"]     # nutritionix   
APP_KEY = os.environ["ENV_APP_KEY"]        # nutritionionix  

exercise_endpoint =  "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/45b16c9a9784d95e5305b68f0f4e7ec5/day38WorkoutTracker/workouts"

HEADER = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}


exercise_parameters = {
    "query": input("Tell me which exercises you did: "),
    "age": AGE,
    "gender": GENDER,
    "height_cm": HEIGHT_CM,
    "weight_kg": WEIGHT_KG
}

response = requests.post(url= exercise_endpoint, json= exercise_parameters, headers= HEADER)
data = response.json()
print(data)
print(type(data['exercises'][0]['nf_calories']))

bearer_headers = {
"Authorization": "Bearer Ashish"
}
for exercise in data['exercises']:
    sheety_parameters = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    ## BASIC AUTHENTICATIONS-------------------------
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_parameters, auth= ("xxyz","xxyz"))
    print(sheety_response.text)

    ## BEARER AUTHENTICATIONS------------------------------------------- first change auth settings in site
    # sheety_response = requests.post(url= sheety_endpoint, json=sheety_parameters, headers= bearer_headers)
    # print(sheety_response.text)




