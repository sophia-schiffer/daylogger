#!/usr/bin/env python3
'''Updates daylogger.txt file based on day and logger times.'''

import datetime
import time

with open("daylogger.txt",'r') as dl:
    first_line = dl.readline()

doc_date = first_line.split("-")
doc_date[2] = doc_date[2][:4]

date = datetime.date.today()
month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
month = month_names[date.month]

new_day = False
if date.year > int(doc_date[2]):
    new_day = True
    print("\nHappy "+str(date.year)+"!\n\n")

elif date.month > int(doc_date[0]):
    new_day = True
    print("\nHappy "+month+"!\n\n")

elif date.day > int(doc_date[1]):
    new_day = True
else:
    new_day = False

# Permanent Holidays
celebrate = False
if month == "February":
    if date.day == 2:
        celebrate = True
        holiday = "Groundhog Day"
    elif date.day == 14:
        celebrate = True
        holiday = "Valentine's Day <3"
elif month == "March":
    if date.day == 17:
        celebrate = True
        holiday = "St. Patty's Day"
elif month == "November":
    if date.day == 11:
        celebrate = True
        holiday = "Veteran's Day"
elif month == "December":
    if date.day == 2:
        celebrate = True
        age = str(date.year - 2001)
        holiday = age+"nd Birthday"
    elif date.day == 25 and new_day:
        print("\nMerry Christmas!\n\n")

# Annual holidays
#TODO: Easter, Thanksgiving

if new_day and celebrate:       
    print("\nHappy "+holiday+"!\n\n")

birthdays = {
    "Andrea": [4,19],
    "Markus": [4,28],
    "Mama & Lauren": [12,14],
    "Sylvia": [5,1],
    "Papa": [9,7]
}
if new_day:
    for key in birthdays.keys():
        if birthdays[key][0] == date.month and birthdays[key][1] == date.day:
            print("\nIt's "+key+"'s birthday today!")

if new_day:
    with open("daylogger.txt",'w') as dl:
        dl.write(str(date.month)+"-"+str(date.day)+"-"+str(date.year)+"\n\n")
        string = "Today my reason is: "
        dl.write(string.rstrip("\n"))
        reason = input("What is your reason today, Sophia?: ")
        dl.write(reason+"\n")

else:
    first_entry = False
    with open("daylogger.txt",'r') as dl:
        lines = dl.readlines()
        num_lines = len(lines)
        if num_lines < 5:
            first_entry = True
        
        if not first_entry:
            prev_goal = lines[-2][33:]
            print("\nYour previous goal was:", prev_goal)

    achieve = input("Accomplished: ")
    learn = input("Learned: ")
    goal = input("Goal: ")

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    with open("daylogger.txt","a") as dl:
        dl.write("\n\n"+current_time+"-")
        dl.write("\n\tI "+achieve+".")
        dl.write("\n\tI learned "+learn+".")
        dl.write("\n\tMy goal for the next hour is to "+goal+".\n")

