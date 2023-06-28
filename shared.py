import pyautogui
import time
import datetime
import json

##How should click wrap work
#it will wait until what I try to click appear on screen and click it
#or after trying to locate for x-seconds - end (but in this case rest of the script will fail)
#return coordinates of clicked button
def clickWrap(filename, wait=60, confidence=0.9):
    current = 0
    #wait until it appears or timedout
    print(f'waiting for {filename} to apepar...')
    while(current < wait):
        time.sleep(1)
        result = pyautogui.locateOnScreen(f'./bilder/{filename}.PNG', grayscale = True, confidence = confidence)
        if (result):
            pyautogui.click(result)
            print(f'clicked on {filename}. Next operation starts in 2s.')
            time.sleep(2)
            return result
        else:
            current += 1
    print(f"Could not find-{filename}")

def dragDungeon():
    print("dragDungeon. Waiting for Arcane keep to appear")
    while(True):
        result = pyautogui.locateOnScreen('./bilder/arcane_keep.PNG', grayscale = True, confidence = 0.9)
        if(result):
            pyautogui.mouseDown(result)
            x,y,w,h = result
            pyautogui.moveTo(x-500, y, 1)
            pyautogui.mouseUp()
            ice_golem = pyautogui.locateOnScreen('./bilder/ice_golem_drag.PNG', grayscale = True, confidence = 0.9)
            x,y,w,h = ice_golem
            pyautogui.mouseDown(ice_golem)
            pyautogui.moveTo(x-640, y, 1)
            pyautogui.mouseUp()
            return

def dragCampain():
    print("dragCampain. Waiting for Sewers of Arnoc to appear")
    while(True):
        result = pyautogui.locateOnScreen('./bilder/sewers_of_arnoc.PNG', grayscale = True, confidence = 0.9)
        if(result):
            pyautogui.mouseDown(result)
            x,y,w,h = result
            pyautogui.moveTo(x-500, y, 1)
            pyautogui.mouseUp()
            ice_golem = pyautogui.locateOnScreen('./bilder/ice_golem_drag.PNG', grayscale = True, confidence = 0.9)
            x,y,w,h = ice_golem
            pyautogui.mouseDown(ice_golem)
            pyautogui.moveTo(x-640, y, 1)
            pyautogui.mouseUp()
            return

def dragDoomtower():
    print("dragDoomtower. Waiting for Doom tower to appear")
    while(True):
        result = pyautogui.locateOnScreen('./bilder/drag_doomtower.PNG', grayscale = True, confidence = 0.9)
        if(result):
            pyautogui.mouseDown(result)
            x,y,w,h = result
            pyautogui.moveTo(x-300, y, 1)
            pyautogui.mouseUp()
            break

def clickBelow(filename):
        print(f'clickBelow. waiting for {filename} to apepar...')
        while(True):     
            result = pyautogui.locateOnScreen(f'./bilder/{filename}.PNG', grayscale = True, confidence = 0.9)
            if (result):
                x, y, w, h = result
                x2 = x+w/2
                y2 = y + 53
                pyautogui.moveTo(x2, y2)
                pyautogui.click(x2, y2)
                return

def clickToTheRight(filename, conf=0.98):
        print(f'clickToTheRight. Waiting for {filename} to appear...')
        while(True):
            result = pyautogui.locateOnScreen(f'./bilder/{filename}.PNG', grayscale = True, confidence = conf)
            if (result):
                x, y, w, h = result
                pyautogui.click(x+w+50, y+h/2)
                return

def clickAboveAndTotheright(filename):
        print(f'clickAboveAndTotheright. Waiting for {filename} to appear...')
        while(True):     
            result = pyautogui.locateOnScreen(f'./bilder/{filename}.PNG', grayscale = False, confidence = 0.9)
            if (result):
                x, y, w, h = result
                x2 = x+w/2 + 555
                y2 = y - 110
                pyautogui.moveTo(x2, y2)
                pyautogui.click(x2, y2)
                return

def checkExist(filename, wait=60):
    current = 0
    while(current < wait):
        time.sleep(1)
        result = pyautogui.locateOnScreen(f'./bilder/{filename}.PNG', grayscale = True, confidence = 0.9)
        if (result):
            print(filename, " exist")
            return result
        else:
            print("Can't see it, retry in 1s.")
            current += 1
    print(f"Could not find-{filename}")

def isEnergyFull():
    result = pyautogui.locateOnScreen('./bilder/fullenergy.PNG', grayscale = False, confidence = 0.9)
    if(result):
        print("Energy is full")
        return True
    print("Energy is not full")
    return False

def readyToRun(what_to_run, whe_to_start=4):
    time_now = datetime.datetime.now().replace(microsecond=0)
    time_to_run = time_now.replace(hour=whe_to_start, minute=0, second=0)

    dailyes_from_file = json.load(open(f'./textfiles/{what_to_run}.txt'))
    print(datetime.datetime.fromisoformat(dailyes_from_file["date"]).date())

    if(datetime.datetime.fromisoformat(dailyes_from_file["date"]).date() == time_now.date()):
        print(f'{what_to_run} - allready done today')
        return False
    
    # is not today                     - do dailyes - replace factionwars.txt content
    if(datetime.datetime.fromisoformat(dailyes_from_file["date"]).date() != time_now.date() 
       and time_now > time_to_run):
        print(f'Starting {what_to_run}')

        # Overwrite file with todays date
        with open(f'./textfiles/{what_to_run}.txt', 'w') as file:
            file.write(json.dumps({"date": time_now.isoformat()})) # use `json.loads` to do the reverse

        return True
    else:
        print("Too early to run")
        return False

def grabAndDrag(filename):
    result = pyautogui.locateOnScreen(f'./bilder/{filename}.PNG', grayscale = True, confidence = 0.9)
    pyautogui.mouseDown(result)
    x,y,w,h = result
    pyautogui.moveTo(x-600, y, 1)
    pyautogui.mouseUp()

if __name__ == "__main__":
    print("")
    