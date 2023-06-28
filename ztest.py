import pyautogui
import time
from datetime import datetime, timedelta
import shared
import farmcampain
import closeadds
import clanboss
import opengame
import dungeon
import arena
import doomtower
from cb import ready_to_run_cb


#result = checkCounter()
#print(result)

# open the file using open() function
#file = open("sample.txt", 'r') #  file.read() - read content        file.write("") - not writable
#file = open("sample.txt", 'r+') #  file.read() - read content        file.write("") - append 
#file = open("sample.txt", 'w') #  file.read() - error not readable  file.write("") - replaces
#file = open("sample.txt", 'w+') # file.read() - read nothing        file.write("") - replaces
#file = open("sample.txt", 'a') #  file.read() - error not readable  filr.write("") - append;      
#file = open("sample.txt", 'a+') # file.read() - read nothing        file.write("") - appends 


#print(readyToRunPart2('factionwars2'))

# 1. when to collect
# 2. forgot about "collected": bool


# Imagine the cycle
# step 1 - collect adv rewards
#     if (shared.readyToRun('dailyadvrewards', 7)):
            #collectedAdvancedDaily()

# step 2 - if collected - (check date is today)
# run factionwars again ( normally will happen same day but several hours later)
    # update factionwars2.txt {"date": "2023-05-28T14:04:35"}

def brutal():
    __cbSelected('brutal')

def __cbSelected(cb_difficulty):
    file_path = f'./textfiles/{cb_difficulty}.txt'
    print("starting clan boss run for ", file_path)
    execution_status = __ready_to_run_cb(file_path) #was did_run_today
    print("execution status: ", execution_status)
    if execution_status:
        __write_execution_status(file_path)

def __write_execution_status(file_path):
    current_datetime = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    with open(file_path, 'w') as file:
        file.write(current_datetime)

def __ready_to_run_cb(file_path, current_time=None):
    try:
        with open(file_path, 'r') as file:
            execution_datetime_str = file.read().strip()
            executed_last_time = datetime.strptime(execution_datetime_str, "%d.%m.%Y %H:%M:%S")
            current_datetime = current_time or datetime.now()
            if current_datetime.hour >= 12:
                current_time_frame_start = datetime(
                    current_datetime.year, current_datetime.month, current_datetime.day, 12, 0, 0
                )
            else:
                previous_day = current_datetime - timedelta(days=1)
                current_time_frame_start = datetime(
                    previous_day.year, previous_day.month, previous_day.day, 12, 0, 0
                )
            time_frame_end = current_time_frame_start + timedelta(days=1) - timedelta(seconds=1)
            if current_time_frame_start <= executed_last_time <= time_frame_end:
                print("Allready did run today")
                return False
            else:
                print("Ready to run")
                return True
    except FileNotFoundError:
        return False


while(True):
    clanboss.unm()
    clanboss.nm()
    clanboss.brutal()
    time.sleep(15)
#clanboss.test_write_brutal()

