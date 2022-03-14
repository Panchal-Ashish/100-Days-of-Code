import requests
from flight_data import *
from twilio.rest import Client

# TWILIO_ACC_ID = "AC2859004428bce7afcad28175bb8e4d98"
# TWILIO_AUTH_TOKEN = "cbcb1221265a2c170eec585158537556"
# TWILIO_FROM_NUMBER = "+18482891741"
# TWILIO_TO_NUMBER = '+917506058102'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_ACC_ID, TWILIO_AUTH_TOKEN)

    def send_sms(self,message):
        self.client.messages.create(body= message, from_= TWILIO_FROM_NUMBER, to= TWILIO_TO_NUMBER)