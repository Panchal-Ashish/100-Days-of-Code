import requests
from twilio.rest import Client
import os

account_sid = 'AC2859004428bce7afcad28175bb8e4d98'
auth_token = 'cbcb1221265a2c170eec585158537556'

api_key = "8277def61f0af14dec7054ddb3de60d4"    # from weather map
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
        #         from_='+17082942621',
        #         to='+917506058102'
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
#                 from_='+17082942621',
#                 to='+917506058102'
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
        from_='+17082942621',
        to='+917506058102'
    )
    print(message.status)
    # print(message.sid)

# print(data)