import pyautogui
import time

timesToRun = 25
currentRun = 0

campain = 'replay_campain'
dungeon = 'replay'
doomtower = 'replay2_doomtower'
bommal = 'doomtower_bommal_retry'

toRepeat = campain

while(currentRun < timesToRun):
    result = pyautogui.locateOnScreen(f'./bilder/{toRepeat}.PNG', grayscale = True, confidence = 0.96)
    print (result)
    if(result):
        currentRun += 1
        print(currentRun, " clicking", result)
        pyautogui.click(result)

        time.sleep(5)
        # if energy is empty
        refill = pyautogui.locateOnScreen('./bilder/confirm_refill.PNG', grayscale = True, confidence = 0.97)
        if(refill):
            pyautogui.click(refill)
            pyautogui.click(result)

    time.sleep(10)
print("COMLETE")

"""
leveling up chickens
spider 20 - exp per run - 5999
spider 25 - exp per run - 5999
minotaur 15-exp per run - 4152

                    runs
rank 1 - 22761      - 4
rank 2 - 81326      - 14
rank 3 - 200681     - 34
rank 4 - 449082     - 75 
rank 5 - 963806     - 160
rank 6 - 2010669    - 335

300k exp

"""