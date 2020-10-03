import calendar
mybirthyear= int(input("Mybirthyear="))
if calendar.isleap(mybirthyear) == True:
    print("Year {} was a leap year".format(mybirthyear))
else:
    print("Year {} was not a leap year".format(mybirthyear))
