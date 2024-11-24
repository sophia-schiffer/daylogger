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
    am, pm, midday = split_routine(routine)

    routine_list = []
    if hour < 12:
        if hour < am[-1][0] and minute < am[-1][1]:
            routine_list = am.copy()
        else:
            routine_list = midday.copy()

    else:
        if hour >= pm[-1][0] and minute >= pm[-1][1]:
            routine_list = pm.copy()
        else:
            routine_list = am.copy()
