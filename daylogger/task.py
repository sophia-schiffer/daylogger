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
import datetime

TASKFILE = "task.txt"

def write_tasks(task, priority):
    with open(TASKFILE,'a') as tsk:
        task_string = task + ":" + str(priority) + "\n"
        tsk.write(task_string)

def read_tasks():
    tasks = {}
    with open(TASKFILE,'r') as tsk:
        task_lines = tsk.readlines()
        for task in task_lines[2:]:
            new_line = task.split(":")
            new_line[-1] = new_line[-1].strip("\n")
            tasks[new_line[0]] = new_line[1]

    return tasks

def reset_file(today):
    '''Clears text file'''
    with open(TASKFILE, 'w') as tsk:
        tsk.write(str(today.month)+"-"+str(today.day)+"-"+str(today.year)+"\n\n")

def write_all(tasks):
    '''Writes all tasks in task dictionary'''
    for task, value in tasks.items():
        write_tasks(task, value)

def remove_top(today):
    tasks = read_tasks()
    
    # Find the key with the maximum value, converting the values to integers
    max_key = max(tasks, key=lambda k: float(tasks[k]))

    # Remove the key and its corresponding value
    del tasks[max_key]

    # Clear the file
    reset_file(today)

    # Write the remaining tasks back to the file
    write_all(tasks)

def new_date(today):
    '''Determines whether task script has been run before
    '''
    with open(TASKFILE,'r') as tsk:
        first_line = tsk.readline()

    doc_date = first_line.split("-")
    doc_date[2] = doc_date[2][:4]

    if days_elapsed(today, doc_date) == 0:
        new = False
    else:
        new = True

    return new, doc_date

def days_elapsed(today, doc_date):
    '''Counts the number of days since numbers were updated
    '''
    
    prev = datetime.date(int(doc_date[2]),int(doc_date[0]),int(doc_date[1]))

    elapsed = today - prev
    return elapsed.days

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

def increment_values(date, prev, factor, tasks):
    '''Increments all task values by specified factor
    '''
    reset_file(date)
    elapsed = days_elapsed(date, prev)

    for task in tasks.keys():
        tasks[task] = min(float(tasks[task]) + factor*elapsed, 10)

    write_all(tasks)
    return tasks


def input_new(today):
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
                remove_top(today)
    
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

if __name__ == '__main__':
    today = datetime.date.today()

    tasks = read_tasks()

    # Increment tasks
    new_day, doc_date = new_date(today)
    increment_factor = 0.8

    if new_day:
        tasks = increment_values(today, doc_date, increment_factor, tasks)

    # Create new task
    input_new(today)
    tasks = read_tasks()

    task_list = list(tasks.keys())
    if len(task_list) == 0:
        print("No tasks to complete!")
        sys.exit()

    max_key, second_key = sort_tasks(task_list)
    print("Your top priority is:", max_key)
    print("Your next priority is:", second_key)
