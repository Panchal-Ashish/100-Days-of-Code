import smtplib
import random
import datetime as dt


today = dt.datetime.now()
weekday = today.weekday()
if weekday == 3:    # mon = 0, tues = 1, wed =2, .....
    with open("quotes.txt") as quotes:
        data = quotes.readlines()
        quote = random.choice(data)

    my_email = "job.ashish28@gmail.com"
    password = "Ashish_28"

    with smtplib.SMTP("smtp.gmail.com", port= 587) as connection:
        connection.starttls()
        connection.login(user= my_email,password= password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:weekly motivational quote\n\n {quote}")