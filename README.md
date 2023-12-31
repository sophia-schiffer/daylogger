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
