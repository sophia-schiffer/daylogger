#!/usr/bin/env python3
'''Script that informs user of holidays coming up
    Uses terminal command to output sorted holidays
    
    -s month, year
    -n name
    -m month
    -d day
'''

import datetime
import sys
import getopt

def get_args():
    entry = None
    new_name = ''
    new_month = ''
    new_day = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hs:n:m:d:",["sort="])
    except getopt.GetoptError:
        print("Error: Invalid arguments")
        print('Usage: holidays.py -s <timeline string> -n <name> -m <month> -d <day>')
        return
    for opt, arg in opts:
        if opt == '-h':
            print('Usage: holidays.py -s <timeline string>')
            sys.exit(2)
        elif opt in ("-s", "--sort"):
            entry = arg
        elif opt in ("-n", "--name"):
            new_name = arg
        elif opt in ("-m", "--month"):
            new_month = arg
        elif opt in ("-d", "--day"):
            new_day = arg
    
    return entry, new_name, new_month, new_day

def read_holidays():
    with open("holidays.txt",'r') as bd:
        birthday_lines = bd.readlines()
        holidays = []
        for line in birthday_lines:
            new_line = line.split(':')
            new_line[-1] = new_line[-1].strip("\n")
            holidays.append(new_line)

    return holidays

def sort_holidays(holidays):
    sorted_holidays = sorted(holidays, key=lambda x: x[1])
    return sorted_holidays

def print_holidays(month, holidays):
    for bday in holidays:
        print(str(bday[0])+": "+str(month)+"/"+str(bday[1]))

def input_new(name, month, day):
    if month == '':
        print("Error: No month entered")
        return
    if day == '':
        print("Error: No day entered")
        return

    with open("holidays.txt",'a') as bd:
        bd.write(name+":"+month+":"+day+"\n")

    print("Birthday added")

if __name__ == '__main__':
    today = datetime.date.today()
    timeline, name, month, day = get_args()
    holidays = read_holidays()
    relevant_holidays = {}
    
    if name != '':
        input_new(name, month, day)

    if timeline == 'month':
        for bday in holidays:
            if int(bday[1]) == today.month:
                relevant_holidays[bday[0]] = int(bday[2])
    elif timeline == 'year':
        for bday in holidays:
            relevant_holidays[bday[0]] = int(bday[1])
            #TODO add recursion for month then day sort

    print_holidays(today.month,sort_holidays(relevant_holidays.items()))
