# Daylogger
Script for generating textfile log to track and motivate yourself throughout your day.

## Setup
### Linux
1. Download `daylogger.py` and `daylogger.txt`. Save both these files in the same directory.
2. From root directory, you may wish to add this alias to your `.bash_aliases` file (optional):
3. ```
   echo "alias daylogger='python3 daylogger.py;open daylogger.txt'" >> .bash_aliases
   ```
4. ```
   cd ~/path/to/directory
   ```
5. Run
   1. With alias, run command `daylogger`.
   2. Else:
      ```
      python3 daylogger.py
      open daylogger.txt
      ```

### Windows
