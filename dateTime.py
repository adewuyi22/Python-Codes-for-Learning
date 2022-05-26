#A date in Python is not a data type of its own, 
# but we can import a module named datetime to work with dates as date objects.

import datetime

#printing the current date
mydate=datetime.datetime.now()
print("\nMy current date is:", mydate) 

#Return the year and name of weekday:
x = datetime.datetime.now()

print(x.year)
print(x.strftime("Today is: %A"))

#To Create a date object:
x = datetime.datetime(2020, 5, 20)
print(x)

#Display the name of the current month:
x = datetime.datetime.now()
print("The current Month is:", x.strftime("%B"))

#Today's Date is:
x = datetime.datetime.now()
print("Today's Date is:", x.strftime("%d %B %Y"))
