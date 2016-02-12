"""
birthday.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
import calendar
import datetime

from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

name = input("What is your name? ")
month = input("Hi "+name+", what was the name of the month you were born in? ")
year = input("And what year were you born in," +name+"? ")

if month == "January":
    monthnumb = 1
elif month == "February":
    monthnumb = 2
elif month == "March":
    monthnumb = 3
elif month == "April":
    monthnumb = 4
elif month == "May":
    monthnumb = 5
elif month == "June":
    monthnumb = 6
elif month == "July":
    monthnumb = 7
elif month == "August":
    monthnumb = 8
elif month == "September":
    monthnumb = 9
elif month == "October":
    monthnumb = 10
elif month == "November":
    monthnumb = 11
elif month == "December":
    monthnumb = 12

day = float(input("And the day? "))
if day == 31:
    if month == "October":
        print("You were born on Halloween! ")
else:   # 55 or warmer
    if monthnumb == todaymonth and day == todaydate:
        print("You were born today! ")

    
if 1 <= monthnumb <= 2: 
    season = "winter"
elif 3 <= monthnumb <= 5:
    season = "spring"
elif 6 <= monthnumb <= 8:
    season = "summer"
elif 9 <= monthnumb <= 11:
    season = "fall"


    
if 1980 <= year <= 1989:
    decade = "eighties"
elif 1990 <= year <= 1999:
    decade = "nineties"
elif year <1980:
    decade = "stone age"
    
print(+name+", you are a "+season+"baby of the"+decade+". ")
