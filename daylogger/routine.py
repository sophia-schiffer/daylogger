#!/usr/bin/env python3
'''Script that reads 'routine.txt' to inform user what the next
    step in the daily routine is. Conditions are separate based on
    AM, PM, and midday.
'''

import datetime

def read_routine():
    with open("routine.txt",'r') as rt:
        routine_lines = rt.readlines()
        routine = []
        for line in routine_lines:
            new_line = line.split(':')
            new_line[-1] = new_line[-1].strip("\n")
            routine.append(new_line)

    return routine

def get_time():
    time = datetime.datetime.now()
    hour = time.hour
    minute = time.minute

    return hour, minute

def get_day():
    time = datetime.datetime.now()
    day = time.weekday()

    return day

def split_routine(routine):
    am = []
    pm = []
    midday = []
    count = 0
    for step in routine:
        if step[0] == "---":
            count += 1
            continue
        if count == 0:
            midday.append(step)
        elif count == 1:
            am.append(step)
        else:
            pm.append(step)

    return am, pm, midday

if __name__ == "__main__":
    routine = read_routine()
    hour, minute = get_time()
    day = get_day()
    am, pm, midday = split_routine(routine)

    routine_list = []
    if hour < 12:
        if (hour < int(am[-1][0]) or (hour == int(am[-1][0]) and minute <= int(am[-1][0]))) or day == 5 or day == 6:
            routine_list = am.copy()
        else:
            routine_list = midday.copy()

    else:
        if hour > int(pm[0][0]) and minute >= int(pm[0][1]):
            routine_list = pm.copy()
            for item in routine_list:
                item[0] = str(int(item[0])+12)
        else:
            routine_list = midday.copy()
    
    print("Your routine (press enter to advance):")

    if routine_list == am or routine_list == pm:
        for step in routine_list:
            tried = False
            while not tried:
                if hour > int(step[0]) or (hour == int(step[0]) and minute >= int(step[1])):
                    input(step[2])
                    tried = True
                else:
                    print("Next task at "+step[0]+":"+step[1]+".")
                    input("Press enter when time is reached.")
                hour, minute = get_time()
    else:
        for step in routine_list:
            input(step[0])

    print("Routine complete!")
