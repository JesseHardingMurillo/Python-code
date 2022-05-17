month = int(input("Enter a month of year (1-12): "))
season = None

if month == 1 or month == 2 or month == 12:
    season = "Winter"
elif month == 3 or month == 4 or month == 5:
    season = "Spring"
elif month == 6 or month == 7 or month == 8:
    season = "Summer"
elif month == 9 or month == 10 or month == 11:
    season = "Fall"
else:
    season = "Incorrect month"
print(f"For the month {month} the season is {season}")
