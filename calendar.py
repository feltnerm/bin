#!/usr/bin/env python
#
# calendar.py
#
# Output a calendar

import calendar
from datetime import datetime

myCal = calendar.TextCalendar()
year = datetime.now().year
month = datetime.now().month
weekday_and_time_header = datetime.now().strftime("%A      %I:%m %p")
date_header = datetime.now().strftime("%B %d, %Y")
cal = myCal.formatmonth(year, month).split('\n')

print("%s" % weekday_and_time_header)

for row in cal:
    print(row)            

# vim: set syntax=python:
