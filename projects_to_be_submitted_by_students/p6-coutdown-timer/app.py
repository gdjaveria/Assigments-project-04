import time
import os

# This is a simple countdown timer program that takes input in minutes or seconds and counts down to zero.
def countdown_timer():
    print('welcome to countdown timer!')
    choice = input('Enter time in minutes (m) or seconds (s) (eg. 5m or 30s): ')

# Check if the input is valid.......
    if choice[-1] == 'm':
        total_seconds = int(choice[:-1]) * 60
    elif choice[-1] == 's':
        total_seconds = int(choice[:-1])
    else:
        print("Invalid input! use 'm' for minuites or 's' for seconds")
        return
    

    while total_seconds > 0:
        mins = total_seconds // 60
        secs = total_seconds % 60
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Time Left :{mins:02}:{secs:02}')
        time.sleep(1)
        total_seconds -= 1

# print the message when the time is up
    os.system('cls' if os.name == 'nt' else 'claesr')
    print('your Time is up!')

if __name__ == "__main__":
    countdown_timer()

    