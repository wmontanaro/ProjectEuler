'''
Project Euler Problem 19:

You are given the following information, but you may prefer to do some
research for yourself.

1 Jan 1900 was a Monday.

Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
'''

import datetime

def day_counter(day, start_date, end_date):
    #day is 0-6 (0 == Monday), start_date and end_date in (Year, Month, Date)
    #format
    counter = 0
    cur_date = datetime.date(start_date[0], start_date[1], start_date[2])
    end_date = datetime.date(end_date[0], end_date[1], end_date[2])
    cur_day = cur_date.day
    cur_month = cur_date.month
    cur_year = cur_date.year
    while cur_date < end_date:
        if cur_date.weekday() == day:
            if cur_date.day == 1:
                counter += 1
        try:
            cur_date = cur_date.replace(day = cur_date.day+1)
        except ValueError:
            cur_date = cur_date.replace(day = 1)
            try:
                cur_date = cur_date.replace(month = cur_date.month+1)
            except ValueError:
                cur_date = cur_date.replace(month = 1)
                cur_date = cur_date.replace(year = cur_date.year+1)
    return counter

print("Problem 19 solution: " + str(day_counter(6, (1901, 1, 1), (2000, 12, 31))))
