import requests
from twilio.rest import Client
import os

account_sid = 'Your Acc SID'
auth_token = 'Your Auth token'

api_key = "Your API Key"    # from weather map
endpoint = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lon":72.8479,
    "lat":19.0144,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}
response = requests.get(url= endpoint, params= parameters)
response.raise_for_status()
data = response.json()
print(data)
will_rain = False

for x in range(0,12):
    a = int(data["hourly"][x]["weather"][0]["id"])
    # print(a)
    if a < 700:
        will_rain = True
        # client = Client(account_sid, auth_token)
        # message = client.messages.create \
        #         (
        #         body="It will rain today. take an umbrella along",
        #         from_='your from no.',
        #         to='your to no.'
        #     )
        # print(message.status)
        # print(f"{a}: bring an umbrella")


# weather_slice = data["hourly"][:12]
# print(weather_slice)
# for hr in weather_slice:
#     condition = int(hr["weather"][0]["id"])
#     if condition < 700:
#         client = Client(account_sid, auth_token)
#         message = client.messages.create \
#                 (
#                 body="It will rain today. take an umbrella along",
#                 from_='your from no.',
#                 to='your to no.'
#             )
#         print(message.status)
##         will_rain = True
#         print(f"{condition}: bring an umbrella")

if will_rain:
    # print("bring an umbrella'")
    client = Client(account_sid, auth_token)
    message = client.messages.create \
        (
        body="It will rain today. take an umbrella along",
        from_='your from no.',
        to='your to no.'
    )
    print(message.status)
    # print(message.sid)

# print(data)
