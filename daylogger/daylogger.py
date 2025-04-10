#!/usr/bin/env python3
'''Updates daylogger.txt file based on day and logger times.'''

import datetime
import time
import pytz

def write_goals(goals):
    with open("goals.txt",'w') as gl:
        for goal in goals.keys():
            gl.write(str(goal)+": "+str(goals[goal])+"\n")

# Open all greeting files
with open("birthdays.txt",'r') as bd:
    birthday_lines = bd.readlines()
    birthdays = []
    for line in birthday_lines:
        new_line = line.split(':')
        new_line[-1] = new_line[-1].strip("\n")
        birthdays.append(new_line)
with open("holidays.txt",'r') as hol:
    hol_lines = hol.readlines()
    holidays = []
    for holiday in hol_lines:
        new_line = holiday.split(":")
        new_line[-1] = new_line[-1].strip("\n")
        holidays.append(new_line)

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

# Holidays

if month == birthdays[0][1]:
    if date.day == birthdays[0][2]:
        celebrate = True
        age = str(date.year - birthdays[0][3])
        num_strings = {
            1: "st",
            2: "nd",
            3: "rd",
        }
        if age%10 < 4:
            num_string = num_strings[age%10]
        else:
            num_string = "th"
        holiday = age+num_string+" Birthday"


# CD functions
def hour_count(hours, days):
    if hours < 0:
        hours = 24 + hours
        days -= 1
    return hours, days
def minute_count(hours, minutes):
    if minutes < 0:
        minutes = 60 + minutes
        hours -= 1
    return hours, minutes

# Countdown
with open("countdown.txt",'r') as cd:
    cd_string = cd.readline().strip("\n")
    CT = pytz.timezone(cd.readline().strip("\n"))
    cd_time = datetime.datetime.now(CT)
    cd_date = cd.readline().split(":")
    for i in range(len(cd_date)):
        cd_date[i] = int(cd_date[i].strip("\n"))
    cd_hour = cd.readline().split(":")
    for i in range(len(cd_hour)):
        cd_hour[i] = int(cd_hour[i].strip("\n"))
    
    delta = datetime.date(cd_date[2],cd_date[0],cd_date[1])-datetime.date(date.year,date.month,date.day)
    days = delta.days
    hours = cd_hour[0]-cd_time.hour
    hours, days = hour_count(hours, days)

    minutes = cd_hour[1]-cd_time.minute-1
    hours, minutes = minute_count(hours, minutes)
    hours, days = hour_count(hours, days)
    
    seconds = 60 - cd_time.second
    if cd_time.second == 0:
        minutes += 1
        seconds = 0

# Daytime
now = time.localtime()
if now.tm_hour < 12:
    day_str = "morning"
elif now.tm_hour < 17:
    day_str = "afternoon"
else:
    day_str = "evening"


celebrate = False
goals = {}
if new_day:
    for hol in holidays:
        if hol[0] == "---" or hol[0] == "":
            continue
        if int(hol[1]) == date.month and int(hol[2]) == date.day:
            celebrate = True
            if len(hol)==4:
                print("\n"+hol[3]+" "+hol[0]+"!")
            else:
                print("\nHappy "+hol[0]+"!")
    if not celebrate:
        print("\nGood "+day_str+", "+birthdays[0][0]+"!")
    if days < 0:
        print(cd_string,"has already passed :)")
    else:
        conjunction = "are "
        day_string = "days"
        hour_string = "hours"
        minute_string = "minutes"
        second_string = "seconds"
        if days == 1:
            day_string = "day"
            conjunction = "is "
        if hours == 1:
            hour_string = "hour"
        if minutes == 1:
            minute_string = "minute"
        if seconds == 1:
            second_string = "second"

        print("There "+conjunction+str(days)+" "+day_string+", "+str(hours)+" "+hour_string+", "+str(minutes)+ \
            " "+minute_string+", and "+str(seconds)+" "+second_string+" until "+cd_string+".")
    for bd in birthdays:
        if int(bd[1]) == date.month and int(bd[2]) == date.day:
            print("\nIt's "+bd[0]+"'s birthday today!")

    with open("daylogger.txt",'w') as dl:
        dl.write(str(date.month)+"-"+str(date.day)+"-"+str(date.year)+"\n\n")
        string = "Today my reason is: "
        dl.write(string.rstrip("\n"))
        reason = input("\nWhat is your reason today?: ")
        dl.write(reason+"\n")

        # Goals
        print("\nWhat are your goals for today?")
        goal = "carpe diem"
        count = 1
        while True:
            goal = input("Goal "+str(count)+" (or ENTER to cancel): ")
            if len(goal) == 0:
                break
            goals[count] = goal
            count += 1
        dl.write("\nDaily Goals:\n")
        for goal in goals.keys():
            dl.write("\t"+str(goal)+": "+str(goals[goal])+"\n")
        dl.write("\n")

    write_goals(goals)


else:
    first_entry = False
    # Goals:
    with open("goals.txt",'r') as goal:
        goal_lines = goal.readlines()
        for line in goal_lines:
            g = line.split(":")
            if len(g) < 2:
                continue
            goals[int(g[0])] = g[1].strip(" ").strip("\n")
    if len(goals) == 0:
        print("\nGood job! You accomplished all your daily goals!")
    else:
        print("\nRemaining daily goals:")
        for goal in goals.keys():
            print("\t"+str(goal)+": "+str(goals[goal]))
        completed = input("\nDid you complete any of these goals? (ENTER to skip): ")
        if len(completed) > 0:
            complete_idx = completed.split(",")
            for idx in complete_idx:
                idx.strip(" ")
                del goals[int(idx)]
        write_goals(goals)
    with open("daylogger.txt",'r') as dl:
        lines = dl.readlines()
        num_lines = len(lines)
        if lines[-2][22:33] != "hour is to ":
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
        dl.write("\n"+current_time+"-")
        dl.write("\n\tI "+achieve+".")
        dl.write("\n\tI learned "+learn+".")
        dl.write("\n\tMy goal for the next hour is to "+goal+".\n\n")

