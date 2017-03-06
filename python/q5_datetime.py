#Q5. Datetime
#Use Python to compute days between start and stop date.
#good source on how to present dates:
# http://www.tutorialscollection.com/python-datetime-how-to-work-with-date-and-time-in-python/

#from datetime import date #ended up to not using datetime
from dateutil.parser import parse
#dateutil is a 3rd party utility that now is a part of Python3.
#Parser attempts to auto-convert common string formats.

def days_from_start_to_end(date_start, date_stop, date_start1, date_stop1):
    date1 = parse(date_start1)
    date2 = parse(date_stop1)
    delta = date2 - date1
    print("A number of days between %r and %r is %r " % (date_start, date_stop, delta.days))

#version a.
print('-'*10)
date_start = '01-02-2013'
date_stop = '07-28-2015'
days_from_start_to_end(date_start, date_stop, date_start, date_stop)

#version b.
print('-'*10)
date_start = '12312013'
date_stop = '05282015'
date_start1 = date_start[0:2] + '-' + date_start[2:4] + '-' + date_start[4:]
date_stop1 = date_stop[0:2] + '-' + date_stop[2:4] + '-' + date_stop[4:]
days_from_start_to_end(date_start, date_stop, date_start1, date_stop1)

#version c.
print('-'*10)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
days_from_start_to_end(date_start, date_stop, date_start, date_stop)
