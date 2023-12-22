#!/usr/bin/env python3
'''Updates daylogger.txt file based on day and logger times.'''

import datetime

with open("daylogger.txt",'r') as dl:
    first_line = dl.readline()

doc_date = first_line.split("-")
doc_date[2] = doc_date[2][:4]

date = datetime.date.today()

new_day = False
if date.year > int(doc_date[2]):
    new_day = True
elif date.month > int(doc_date[0]):
    new_day = True
elif date.day > int(doc_date[1]):
    new_day = True
else:
    new_day = False

if new_day:
    with open("daylogger.txt",'w') as dl:
        dl.write(str(date.month)+"-"+str(date.day)+"-"+str(date.year)+"\n\n")
        string = "Today my reason is: "
        dl.write(string.rstrip("\n"))
        reason = input("What is your reason today, Sophia?: ")
        dl.write(reason+"\n\n")

else:
    first_entry = False
    with open("daylogger.txt",'r') as dl:
        lines = dl.readlines()
        num_lines = len(lines)
        if num_lines < 4:
            first_entry = True
        
        if not first_entry:
            prev_goal = lines[-1]
            print("Your previous goal was:", prev_goal)

