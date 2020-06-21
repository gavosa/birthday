import datetime

month = datetime.date.today().month
day = datetime.date.today().day

if month == 6:
    if day < 24:
        print("Ooops, you are not 23 yet!")
    elif day > 24:
        print("You are past your birthday!")
    else:
        print("Webster, it's your birthday! You're turning a year older today!")
elif month < 6:
    print("It's not your birth month!")
else:
    print("It's past your birth month!")
