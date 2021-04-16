# This is a simple notifier program

from datetime import date
import datetime


# today is ...
today = date.today()
print("Today's date:", today)

# week_days list
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# split the info for year, month and date.
divide = list(map(int, input("Enter date \n eg: 2019-05-05 \n\n").split('-')))

# get the weekday
day = datetime.date(divide[0], divide[1], divide[2]).weekday()
print(week_days[day])
current_date = week_days[day]


# this is the notifier function, it prints you a notification for the day.
def notify(week_of_the_day):
    if week_of_the_day == "Friday":
        print("This is the last day of the weekdays. Have a beer mate! :D")
    elif week_of_the_day == "Saturday" or week_of_the_day == "Sunday":
        print("You still have time for a beer!")
    else:
        print("Have Fun! Work Hard! Make History!")


# call the function
notify(current_date)
