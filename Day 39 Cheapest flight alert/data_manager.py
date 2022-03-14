# import requests
#
# SHEETY_ENDPOINT = "your sheety endpoint to the sheet with flight price details"
#
# class DataManager():
#
#     def __init__(self):
#         self.destination_data = {}
#
#     def update_code(self, row_number, city_code):
#         sheety_params = {
#             "price":{
#                 'iataCode': city_code
#             }
#         }
#         requests.put(url= f"{SHEETY_ENDPOINT}/{row_number}", json= sheety_params)
#         return self.destination_data
#
#






# -------------------------------------------------------------------------------------------------------------


import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "your sheety endpoint to the sheet with flight price details"


class DataManager():

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):

        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        pprint(f"data manager ka data:\n{data}")
        self.destination_data = data["prices"]
        return self.destination_data


    # 6. In the DataManager Class make a PUT request and use the row id  from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            # print(response.text)
