## this will send email only when the program is run...
## so we will have to run it daily to check if today is someone's birthday...
## if yes then send the mail

## this runnng of code everyday can be avoided by hosting the code on internet (www.pythonanywhere.com)
## also, in the csv , we will have to save the data of all persons...


import smtplib
import random
import datetime as dt
import pandas


today = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}
print(birthdays_dict)


if today in birthdays_dict:
    birthday_person = birthdays_dict[today]["name"]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person)
        # does not replace and save in original file... so we have to create a new variable to save it there... or assikgn it to same variable again
        # print(contents)

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        my_email = "job.ashish28@gmail.com"
        password = "Ashish_28"
        to_address = birthdays_dict[today]["email"]
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_address,
                            msg=f"Subject:Happy Birthday!!!\n\n {contents}")


