months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
leapyear_months = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_of_week = 1 # the 1st of January 1901 is Tuesday
sundays_on_first = 0

for year in range(1901, 2001):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_of_month = leapyear_months
    else:
        days_of_month = months
    
    for month in days_of_month:
        if days[day_of_week] == "Sunday":
            sundays_on_first += 1
        day_of_week = (day_of_week + days_of_month[month]) % 7

print(sundays_on_first)