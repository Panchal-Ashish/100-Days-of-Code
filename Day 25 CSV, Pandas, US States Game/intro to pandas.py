# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)



# # accessing csv files using pandas
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data)


# # accessing particular columns
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])


# # type converting to dictionary    (dataframe)
# import pandas
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# # type converting to list     only applicable to dataseries... (dataseries)
# import pandas
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(temp_list)


# # finding average of all temperatues using Pandas
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"].mean())


# # finding max temp of week
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"].max())

# # accessing data in rows
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data[data.day == "Monday"])       # get the row that has the day monday
# print(data[data.day == "Thursday"])       # get the row that has the day Thursday

# # accessing row with day where temperature is maximum
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data[data.temp == data["temp"].max()])

# # accessing a particular data from the row... condition of monday
# import pandas
# data = pandas.read_csv("weather_data.csv")
# monday = data[data.day == "Monday"]
# print(monday.condition)


# converting the mondays temperature into fahrenheit
# import pandas
# data = pandas.read_csv("weather_data.csv")
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# temp_f = monday_temp * 9/5 + 32
# print(temp_f)


# #  #iterating (looping) through pandas dataframe
# import pandas
# data = pandas.read_csv("weather_data.csv")
# for (index,row) in data.iterrows():
#     #print(row)
#     print(row.day)      # accessing particular info from the row i.e. day
#     if row.condition == "Sunny":    # filtering all elements depending on a particular condition... i.e. sunny
#         print(row)




# # creating data frame from scratch
# import pandas
# data_dict = {
#     "students":["priyank","harsh","ashish","pratham"],
#     "scores":[78,77,90,91]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
# for (index, row) in data.iterrows():    # only iterrow example, not saving
#     # print(row)
#     print(row.students)      # accessing particular info from the row
#     if row.scores == 90:  # filtering all elements depending on a particular condition
#         print(row)
#
# # saving the file
# data.to_csv("new_data.csv")       # requires only one parameter, the storage path
