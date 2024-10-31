#!/usr/bin/env python3
'''Script that informs user of birthdays coming up
    Uses terminal command to output sorted birthdays
    
    -s month, year
'''

import datetime
import sys
import getopt

def get_args():
    entry = None
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hs:",["sort="])
    except getopt.GetoptError:
        print("Error: Invalid arguments")
        print('Usage: birthdays.py -s <timeline string>')
        return
    for opt, arg in opts:
        if opt == '-h':
            print('Usage: birthdays.py -s <timeline string>')
            sys.exit(2)
        elif opt in ("-s", "--sort"):
            entry = arg
    
    return entry

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

if __name__ == '__main__':
    today = datetime.date.today()
    timeline = get_args()
    birthdays = read_birthdays()
    relevant_birthdays = {}
    
    if timeline == 'month':
        for bday in birthdays:
            if int(bday[1]) == today.month:
                relevant_birthdays[bday[0]] = int(bday[2])
    elif timeline == 'year':
        for bday in birthdays:
            relevant_birthdays[bday[0]] = int(bday[1])
            #TODO add recursion for month then day sort

    print_birthdays(today.month,sort_birthdays(relevant_birthdays.items()))
