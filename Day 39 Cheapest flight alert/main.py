
## FLIGHT SPECS CONSIDERED

## FLIGHT TYPE - ROUND
## NO.OF PASSENGERS = 2
## CLASS = ECONOMY
## TRAVEL RANGE = 6 MONTHS

##      your link to google sheets whicj=h contains the customer details    ##

#
#
# #---------------------------------------------------------------------------------------------------------#
#
# import requests
# from flight_search import *
# from data_manager import *
# import datetime as dt
# from notification_manager import NotificationManager
# from pprint import pprint
#
# TEQUILA_API_KEY = "TEQUILA_API_KEY"
# SHEETY_ENDPOINT = "SHEETY_ENDPOINT
# ORIGIN_CITY_CODE = "BOM"
#
# response = requests.get(url= SHEETY_ENDPOINT)
# # print(response.json())
# # print("\n")
# # pprint(response.json())
# # print("\n")
# sheet_data = response.json()["prices"]
# # print(f"sheet data : \n{sheet_data}")
# # print("\n")
#
#
# data_manager = DataManager()
# data_manager.destination_data = sheet_data
#
# for x in range(len(sheet_data)):
#     if sheet_data[x]['iataCode'] == "":
#
#         cityname = sheet_data[x]['city']
#         # print(cityname)
#
#         # FS = FlightSearch()
#         # code = FS.get_destination_code(cityname)
#         code = FlightSearch().get_destination_code(cityname)
#         # print(code)
# #
#         row_number = sheet_data[x]["id"]
#         # print(f"{row_number},{code}")
#
#         sheet_data = data_manager.update_code(row_number, code)
#
# response = requests.get(url= SHEETY_ENDPOINT)
# sheet_data = response.json()["prices"]
#
# # print(sheet_data)
#
# today_date = dt.datetime.now().date()
# tomorrow_date = today_date + dt.timedelta(days= 1)
# six_month_after_date = today_date + dt.timedelta(days= 6*30)
#
# for city in sheet_data:
#     # print(city["iataCode"])
#     flight = FlightSearch().check_flights(ORIGIN_CITY_CODE,
#                                           city["iataCode"],
#                                           from_time = tomorrow_date,
#                                           to_time = six_month_after_date,
#                                           passengers = 2)
#
#     if flight is None:
#         continue
#
#     if flight is not None and flight.price <= (city["lowestPrice"] * flight.passengers):
#         # notification_manager = NotificationManager()
#         message = f"Low price alert:\nOnly Rs.{flight.price} to travel from " \
#                   f"{flight.origin_city}-{flight.origin_airport} to "\
#                   f"{flight.destination_city}-{flight.destination_airport}, " \
#                   f"for {flight.passengers} passengers " \
#                   f"from {flight.out_date} to {flight.return_date}"
#         print(message)
#         # notification_manager.send_sms(message)



#------------------------------------------------------------------------------------------------------------------
# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from data_manager import DataManager
import datetime as dt
from notification_manager import NotificationManager
import requests
from flight_search import *
from data_manager import *


ORIGIN_CITY_CODE = "BOM"

flight_search = FlightSearch()
data_manager = DataManager()

sheet_data = data_manager.get_destination_data()
print(f"sheet data{sheet_data}")
for x in range(len(sheet_data)):
    if sheet_data[x]["iataCode"] == "":
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])
        print(f"sheet data: {sheet_data}")

        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()

today_date = dt.datetime.now().date()
tomorrow_date = today_date + dt.timedelta(days= 1)
six_month_after_date = today_date + dt.timedelta(days= 6*30)
for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_CODE,
        destination["iataCode"],
        from_time=tomorrow_date,
        to_time=six_month_after_date,
        passengers=2
    )

    if flight is None:
        continue

    if flight is not None and flight.price <= (destination["lowestPrice"] * flight.passengers):
        # print(destination["lowestPrice"] * flight.passengers) #
        # notification_manager = NotificationManager()

        message = f"Low price alert:\nOnly Rs.{flight.price} to travel from " \
                  f"\n{flight.origin_city}-{flight.origin_airport} to " \
                  f"\n{flight.destination_city}-{flight.destination_airport}," \
                  f"\nfor {flight.passengers} passengers" \
                  f"\nfrom {flight.out_date} to {flight.return_date}"
        print(message)
        # notification_manager.send_sms(message)

##--------------------------------------------------
