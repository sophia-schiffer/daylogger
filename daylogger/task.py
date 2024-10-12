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
with open("task.txt",'r') as tsk:
    task_lines = tsk.readlines()
    for task in task_lines:
        new_line = task.split(":")
        new_line[-1] = new_line[-1].strip("\n")
        tasks[new_line[0]] = new_line[1]

task_list = list(tasks.keys())
assert len(task_list) > 0

max_task = -1
max_key = task_list[0]
second_task = -1
second_key = task_list[0]
for task in task_list:
    task_val = float(tasks[task])
    if task_val > max_task:
        max_task = task_val
        second_key = max_key
        second_val = tasks[max_key]
        max_key = task
    elif task_val > second_task:
        second_key = task
        second_val = task_val

print("Your top priority is:", max_key)
print("Your next priority is:", second_key)
