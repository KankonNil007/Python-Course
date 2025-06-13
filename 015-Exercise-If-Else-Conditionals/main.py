# Exercise: Good Morning App using Time Module and Conditionals

import time

currentTimeHour = int(time.strftime('%H'))

if (currentTimeHour >= 6 and currentTimeHour < 11):
    print("Good Morning, Kankon")
if (currentTimeHour >= 11 and currentTimeHour < 16):
    print("Good Noon, Kankon")
if (currentTimeHour >= 16 and currentTimeHour < 18):
    print("Good Afternoon, Kankon")
if (currentTimeHour >= 18 and currentTimeHour < 22):
    print("Good Evening, Kankon")
else:
    print("Good Night, Kankon")
