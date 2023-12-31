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
2. Open Windows cmd prompt.
3. ```
   cd ~/path/to/directory/daylogger
   python3 daylogger.py
   open daylogger.txt
   ```
   **if python is not installed, enter `python3` into the terminal**
