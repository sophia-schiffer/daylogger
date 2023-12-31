# Daylogger
Script for generating textfile log to track and motivate yourself throughout your day.

## Setup
### Ubuntu
1. Download `daylogger` directory.
2. From root directory, you may wish to add this alias to your `.bash_aliases` file (optional):
    ```
   echo "alias daylogger='python3 ~/path/to/daylogger/daylogger.py;open daylogger.txt'" >> .bash_aliases
   ```
    where `/path/to/daylogger` is the location where the daylogger directory is saved.
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
