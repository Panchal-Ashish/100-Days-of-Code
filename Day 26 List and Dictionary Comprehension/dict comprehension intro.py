# new_dict = {new_key: new_value for item in list}    #dict comprehension from list
# new_dict = {new_key: new_value for (key,value) in dict.items()}     #dict comprehension from dict

## conditional dict comprehension
# new_dict = {new_key: new_value for item in list if test}
# new_dict = {new_key: new_value for (key,value) in dict.items() if test}


# ## exercise 1... count no. of letters in word and write its corresponding count in the form of dict
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
# ## split method splits the sentence by 'space'( default space, id=f no parameter specified in ())and stores it in a list
# print(result)



## exercise 2... take a dict with week days and temperatures in C,return a dict with weekdays and temp in F
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp_c * 9/5 + 32) for (day, temp_c) in weather_c.items()}
print(weather_f)