# Daylogger
Script for generating textfile log to track and motivate yourself throughout your day.

## Dependencies
```
pip install pytz
```

## Setup
### Ubuntu
1. Download `daylogger` directory.
2. From root directory, you may wish to add this alias to your `.bash_aliases` file (optional):
    ```
   echo "alias daylogger='cd ~/path/to/daylogger;python3 daylogger.py;open daylogger.txt'" >> .bash_aliases
   ```
    where `/path/to/daylogger` is the path to the daylogger directory from home directory.
3. Run
   1. With alias, run command `daylogger`.
   2. Else:
      ```
      cd ~/path/to/directory/daylogger
      python3 daylogger.py
      open daylogger.txt
      ```

### Windows
1. Download `daylogger` directory.
2. Install python3 and dependencies.
   **if Python is not installed, enter `python3` into the Windows cmd prompt**
4. Navigate to the `daylogger` folder in File Explorer and double click `daylogger.py` to execute script.
5. In the same directory, open `daylogger.txt` to see the result.
#### Alternative
1. Open Windows cmd prompt.
2. ```
   cd ~/path/to/directory/daylogger
   python3 daylogger.py
   daylogger.txt
   ```

## Usage
### Birthdays
1. Update `birthdays.txt` to replace my birthday with yours. This is the only birthday that should have theyear as well as the day. Updating this text file also changes the daily greeting to your name.

### Countdown
1. Update `countdown.txt` so that the first line is an event your are excited for.
2. The second line specifies a timezone included in the `pytz` python library.
3. The third and fourth lines are the date and time of your desired event, respectively, where the time is on a 24-hour clock.

### Holidays
1. The `holidays.txt` file contains some sample holidays that your daylogger will celebrate with you. You can customize this file to include any holidays you celebrate
2. The `---` separator is useful for blocking or categorizing your holidays. These lines are skipped in the code.
3. The default is "Happy _!" If there is a different word used to celebrate the holiday, place it after a colon after the day. (see line 4, "Merry Christmas!")

### Daylogger and Goals files
1. `daylogger.txt` and `goals.txt` get filled automatically by running the `daylogger.py` script. These do not need to be edited manually.
