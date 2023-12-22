'''Updates daylogger.txt file based on day and logger times.'''

import datetime

with open("daylogger.txt",'r') as dl:
    first_line = dl.readline()

doc_date = first_line.split("-")
doc_date[2] = doc_date[2][:4]

date = datetime.date.today()

new_day = False
if date.year > int(doc_date[2]):
    new_day = True

print(new_day)