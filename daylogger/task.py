#!/usr/bin/env python3
'''Makes a priority queue of tasks based on importance.

    Priorities are input on a 1-10 scale and increment by 1 each day they are not completed.
    
    Input values:
    High: 7
    Medium: 3
    Low: 0
    *default is 3*
'''

import sys
import getopt

def write_tasks(task, priority):
    with open("task.txt",'a') as tsk:
        task_string = task + ":" + str(priority) + "\n"
        tsk.write(task_string)

def read_tasks():
    tasks = {}
    with open("task.txt",'r') as tsk:
        task_lines = tsk.readlines()
        for task in task_lines:
            new_line = task.split(":")
            new_line[-1] = new_line[-1].strip("\n")
            tasks[new_line[0]] = new_line[1]
    return tasks

def remove_top():
    tasks = read_tasks()
    
    # Find the key with the maximum value, converting the values to integers
    max_key = max(tasks, key=lambda k: int(tasks[k]))

    # Remove the key and its corresponding value
    del tasks[max_key]

    # Clear the file
    with open('task.txt', 'w'):
        pass  # This clears the file

    # Write the remaining tasks back to the file
    for task, value in tasks.items():
        write_tasks(task, value)



def sort_tasks(task_list):
    max_task = -1
    max_key = task_list[-1]
    second_task = -1
    second_key = task_list[-1]
    for task in task_list:
        task_val = float(tasks[task])
        if task_val > max_task:
            max_task = task_val
            second_key = max_key
            second_task = float(tasks[max_key])
            max_key = task
        elif task_val > second_task:
            second_task = task_val
            second_key = task
    
    return max_key, second_key

def input_new():
    new_task = ''
    priority = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:],"ht:p:r:",["task=","priority=","remove="])
    except getopt.GetoptError:
        print("Error: Invalid arguments")
        print('Usage: task.py -t <task string> -p <priority (high/medium/low)> -r <true/false>')
        return
    for opt, arg in opts:
        if opt == '-h':
            print('Usage: task.py -t <task string> -p <priority (high/medium/low)> -r <true/false>')
            return
        elif opt in ("-t", "--task"):
            new_task = arg
        elif opt in ("-p", "--priority"):
            priority = arg
        elif opt in ("-r", "--remove"):
            if arg == 'true':
                remove_top()
    
    if new_task == '':
        return
    if priority == "high":
        val = 7
    elif priority == "medium" or priority == '':
        val = 3
    elif priority == "low":
        val = 0
    else:
        try:
            val = float(priority)
        except ValueError:
            print("Priority must be high/medium/low or valid number.")

    write_tasks(new_task, val)

input_new()

tasks = read_tasks()
print("new tasks:", tasks)

task_list = list(tasks.keys())
assert len(task_list) > 0

max_key, second_key = sort_tasks(task_list)
print("Your top priority is:", max_key)
print("Your next priority is:", second_key)