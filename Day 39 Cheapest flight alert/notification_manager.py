import requests
from flight_data import *
from twilio.rest import Client

# TWILIO_ACC_ID = "TWILIO ACCOUNT ID"
# TWILIO_AUTH_TOKEN = "TWILIO ACCOUNT AUTH KEY"
# TWILIO_FROM_NUMBER = "TWILIO_FROM_NUMBER"
# TWILIO_TO_NUMBER = 'TWILIO_TO_NUMBER '


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_ACC_ID, TWILIO_AUTH_TOKEN)

    def send_sms(self,message):
        self.client.messages.create(body= message, from_= TWILIO_FROM_NUMBER, to= TWILIO_TO_NUMBER)
