# import pandas
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
#
# data_dict = {
#     "Fur color":["Gray","red","Cinnamon"],
#     "Count":[grey_squirrel_count, red_squirrel_count, black_squirrel_count]
# }
# file = pandas.DataFrame(data_dict)
# print(file)
# file.to_csv("squirrel_count.csv")
#


import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(len(data[data["Primary Fur Color"] == "Gray"]))
grey_squirrel_count = 0
red_squirrel_count = 0
black_squirrel_count = 0

for color in data["Primary Fur Color"]:
    if color == "Gray":
        grey_squirrel_count += 1
    elif color == "Cinnamon":
        red_squirrel_count += 1
    elif color == "Black":
        black_squirrel_count += 1


data_dict = {
    "Fur color":["Gray","red","Cinnamon"],
    "Count":[grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

file = pandas.DataFrame(data_dict)
file.to_csv("squirrel_count.csv")

