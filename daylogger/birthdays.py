#!/usr/bin/env python3
'''Script that informs user of birthdays coming up
    Uses terminal command to output sorted birthdays
    
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
        print('Usage: birthdays.py -s <timeline string> -n <name> -m <month> -d <day>')
        return
    for opt, arg in opts:
        if opt == '-h':
            print('Usage: birthdays.py -s <timeline string>')
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

def read_birthdays():
    with open("birthdays.txt",'r') as bd:
        birthday_lines = bd.readlines()
        birthdays = []
        for line in birthday_lines:
            new_line = line.split(':')
            new_line[-1] = new_line[-1].strip("\n")
            birthdays.append(new_line)

    return birthdays

def sort_birthdays(birthdays):
    sorted_birthdays = sorted(birthdays, key=lambda x: x[1])
    return sorted_birthdays

def print_birthdays(month, birthdays):
    for bday in birthdays:
        print(str(bday[0])+": "+str(month)+"/"+str(bday[1]))

def input_new(name, month, day):
    if month == '':
        print("Error: No month entered")
        return
    if day == '':
        print("Error: No day entered")
        return

    with open("birthdays.txt",'a') as bd:
        bd.write(name+":"+month+":"+day+"\n")

    print("Birthday added")

if __name__ == '__main__':
    today = datetime.date.today()
    timeline, name, month, day = get_args()
    birthdays = read_birthdays()
    relevant_birthdays = {}
    
    if name != '':
        input_new(name, month, day)

    if timeline == 'month':
        for bday in birthdays:
            if int(bday[1]) == today.month:
                relevant_birthdays[bday[0]] = int(bday[2])
        print_birthdays(today.month,sort_birthdays(relevant_birthdays.items()))

    elif timeline == 'year':
        month = 1
        while month <= 12:
            for hol in birthdays:
                if hol[0] == "---" or hol[0] == "":
                    continue
                elif int(hol[1]) == month:
                    relevant_birthdays[hol[0]] = int(hol[2])
            new_birthdays = sort_birthdays(relevant_birthdays.items())
            print_birthdays(month,new_birthdays)
            month += 1
            relevant_birthdays = {}
