# This is a simple notifier program

from datetime import date
import datetime

# enter your age
age = input("Enter your age: ")

# today is...
today = date.today()
print("Today's date:", today)

# week_days list
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# split the info for year, month and date.
divide = list(map(int, input("Enter date \n eg: 05/05/2019 \n\n").split('/')))

# get the weekday
day = datetime.date(divide[2], divide[1], divide[0]).weekday()
print(week_days[day])
