#!/usr/bin/env python3
'''Makes a priority queue of tasks based on importance.

    Priorities are input on a 1-10 scale and increment by 1 each day they are not completed.
    
    Input values:
    High: 7
    Medium: 3
    Low: 0
'''

import sys

def write_tasks(tasks):
    with open("tasks.txt",'w') as tsk:
        tsk.write("Tasks")

tasks = {}
with open("holidays.txt",'r') as tsk:
    task_lines = tsk.readlines()
    for task in task_lines:
        new_line = task.split(":")
        new_line[-1] = new_line[-1].strip("\n")
