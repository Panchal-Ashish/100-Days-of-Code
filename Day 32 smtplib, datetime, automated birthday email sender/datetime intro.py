import datetime as dt

now = dt.datetime.now()     ## datetime.now()... dt is module (renamed), datetime is class... now is method to get the current date and time of my pc
print(now)

year = now.year
weekday = now.weekday()        # does not return day, but the no. of day in week with starting from 0 i.e monday, ....eg wednesday = 2
print(year)     # datatype int      ## can also access month,day,weekday,date,time, hr, minute, second, microsecond..... similarly
print(weekday)


# (now) method gives access to the current date and time... what if we want to get a particular date and time from past / future
# for that we need to specify the parameters inside datetime class inside datetime module
DOB = dt.datetime(year= 2001, month= 3, day= 28)
## hr, month and day mandatory .... all others are optional (have default values... hr= 00, min = 00... etc)
print(f"DOB = {DOB}")
