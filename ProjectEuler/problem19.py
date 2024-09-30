from itertools import cycle
from time import sleep
days = ["wednesday", "thursday", "friday", "saturday", "sunday", "monday", "tuesday"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
year = 1901
monthcont = 0
day = 0
month = 0
suncont = 0

for i in cycle(range(7)):
    leap = not year%4
    if leap:
        febdays = 29
    else:
        febdays = 28
    monthdays = [31, febdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day == monthdays[month%len(months)]:
        day = 0
        if not (month+1)%len(months) and month != 0:
            year += 1
        month += 1
    if day == 1 and days[i-1] == "sunday":
        suncont += 1
    if year == 2001:
        break
    day += 1    
    

print(suncont)
