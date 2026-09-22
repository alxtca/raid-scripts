import pyautogui
import json
import errorhandling
import time 
import datetime
from flags import flagInstance


##How should click wrap work
#it will wait until what I try to click appear on screen and click it
#or after trying to locate for x-seconds - end (but in this case rest of the script will fail) - goal: restart game and restart script.
#return coordinates of clicked button
def clickWrap(filename, wait=60, confidence=0.9):
    #print(f'entered clickWrap for {filename}')
    if (errorhandling.gameReset()  == 'skip'):
        print(f'skip clickWrap for {filename}')
        return
    
    current = 0
    #wait until it appears or timedout
    print(f'waiting for {filename} to apepar...')
    while(current < wait):
        #print(f'Waiting... total seconds {wait}. Seconds left {current}')
        time.sleep(1)
        errorhandling.connectionError()
        errorhandling.logedInOnAnotherDevice()
        #errorhandling.maintennanceHandler()            

        result = pyautogui.locateOnScreen(f'./bilder/{filename}.PNG', grayscale = True, confidence = confidence)
        if (result):
            pyautogui.click(result)
            print(f'clicked on {filename}. Next operation starts in 2s.')
            time.sleep(2)
            return result
        else:
            current += 1
        if (errorhandling.gameReset()  == 'skip'):
            print(f'skip clickWrap for {filename}')
            return
    print(f"Could not find-{filename}")
    errorhandling.errorManager.error_detected = True

def clickWrapWithSkip(filename, searchTime = 3, confidence = 0.9)-> bool:
    result = pyautogui.locateOnScreen(f'./bilder/{filename}.PNG', grayscale = True, confidence = confidence, minSearchTime=searchTime)
    if (result):
        x,y,w,h = result
        pyautogui.click(x, y)
        print(f'clicked on {filename}')
        return True
    return False

def clickToTheRightWrapWithSkip(filename, searchTime = 3, confidence = 0.98)-> bool:
    result = pyautogui.locateOnScreen(f'./bilder/{filename}.PNG', grayscale = True, confidence = confidence, minSearchTime=searchTime)
    if (result):
        x,y,w,h = result
        pyautogui.click(x+w+50, y+h/2)
        return True
    return False

def waitWrap(waitFile, clickFile, wait=60):
    result = pyautogui.locateOnScreen(f'./bilder/{waitFile}.PNG', grayscale = True, confidence = 0.95, minSearchTime=wait)
    if(result):
        clickWrap(clickFile)
    else:
        errorhandling.errorManager.error_detected = True

def dragDungeon():
    result = errorhandling.gameReset() 
    if (result == 'skip'):
        print(f'skip clickWrap for ...')
        return
    print("dragDungeon. Waiting for Arcane keep to appear")
    result = pyautogui.locateOnScreen('./bilder/arcane_keep.PNG', grayscale = True, confidence = 0.9, minSearchTime=200)
    if(result):
        pyautogui.mouseDown(result)
        x,y,w,h = result
        pyautogui.moveTo(x-500, y, 1)
        pyautogui.mouseUp()
        time.sleep(1)
        ice_golem = pyautogui.locateOnScreen('./bilder/ice_golem_drag.PNG', grayscale = True, confidence = 0.9)
        x,y,w,h = ice_golem
        pyautogui.mouseDown(ice_golem)
        pyautogui.moveTo(x-640, y, 1)
        pyautogui.mouseUp()
        return
    else:
        errorhandling.errorManager.error_detected = True

def dragDungeonMore():
    result = errorhandling.gameReset() 
    if (result == 'skip'):
        print(f'skip clickWrap for ...')
        return
    print("dragDungeonMore. Waiting for Dragon to appear")
    result = pyautogui.locateOnScreen('./bilder/drag_more_dragon.PNG', grayscale = True, confidence = 0.9, minSearchTime=200)
    if(result):
        pyautogui.mouseDown(result)
        x,y,w,h = result
        pyautogui.moveTo(x-500, y, 1)
        pyautogui.mouseUp()
        return
    else:
        errorhandling.errorManager.error_detected = True

def dragCampain():
    result = errorhandling.gameReset() 
    if (result == 'skip'):
        print(f'skip clickWrap for ...')
        return
    print("dragCampain. Waiting for Sewers of Arnoc to appear")
    result = pyautogui.locateOnScreen('./bilder/sewers_of_arnoc.PNG', grayscale = True, confidence = 0.9, minSearchTime=200)
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
    else:
        errorhandling.errorManager.error_detected = True

def dragDoomtower():
    result = errorhandling.gameReset() 
    if (result == 'skip'):
        print(f'skip clickWrap for ...')
        return
    print("dragDoomtower. Waiting for Doom tower to appear")
    result = pyautogui.locateOnScreen('./bilder/drag_doomtower.PNG', grayscale = True, confidence = 0.9, minSearchTime=200)
    if(result):
        pyautogui.mouseDown(result)
        x,y,w,h = result
        pyautogui.moveTo(x-300, y, 1)
        pyautogui.mouseUp()
    else:
        errorhandling.errorManager.error_detected = True

def clickBelow(filename, extra_distance=0):
    result = errorhandling.gameReset() 
    if (result == 'skip'):
        print(f'skip clickWrap for {filename}')
        return
    print(f'clickBelow. waiting for {filename} to apepar...')    
    result = pyautogui.locateOnScreen(f'./bilder/{filename}.PNG', grayscale = True, confidence = 0.9, minSearchTime=1)
    if (result):
        x, y, w, h = result
        x2 = x+w/2
        y2 = y + 53 + extra_distance
        pyautogui.moveTo(x2, y2)
        pyautogui.click(x2, y2)
        return
    else:
        errorhandling.errorManager.error_detected = True

def clickToTheRight(filename, conf=0.98):
    if (errorhandling.gameReset()  == 'skip'):
        print(f'skip clickWrap for {filename}')
        return
    print(f'clickToTheRight. Waiting for {filename} to appear...')
    result = pyautogui.locateOnScreen(f'./bilder/{filename}.PNG', grayscale = True, confidence = conf, minSearchTime=200)
    if (result):
        x, y, w, h = result
        pyautogui.click(x+w+50, y+h/2)
    else:
        errorhandling.errorManager.error_detected = True
        
def clickToTheLeft(filename, conf=0.98):
    result = errorhandling.gameReset() 
    if (result == 'skip'):
        print(f'skip clickWrap for {filename}')
        return
    print(f'clickToTheLeft. Waiting for {filename} to appear...')
    result = pyautogui.locateOnScreen(f'./bilder/{filename}.PNG', grayscale = True, confidence = conf, minSearchTime=200)
    if (result):
        x, y, w, h = result
        pyautogui.click(x-20, y+h/2)
    else:
        errorhandling.errorManager.error_detected = True

def clickAboveAndTotheright(filename, x_correction=555, y_correction=110):
    result = errorhandling.gameReset() 
    if (result == 'skip'):
        print(f'skip clickWrap for {filename}')
        return
    print(f'clickAboveAndTotheright. Waiting for {filename} to appear...')   
    result = pyautogui.locateOnScreen(f'./bilder/{filename}.PNG', grayscale = False, confidence = 0.9, minSearchTime=200)
    if (result):
        x, y, w, h = result
        x2 = x+w/2 + x_correction
        y2 = y - y_correction
        pyautogui.moveTo(x2, y2)
        pyautogui.click(x2, y2)
    else:
        errorhandling.errorManager.error_detected = True

def checkExist(filename, wait=60):
    result = errorhandling.gameReset() 
    if (result == 'skip'):
        print(f'skip clickWrap for {filename}')
        return
    current = 0
    while(current < wait):
        time.sleep(1)
        result = pyautogui.locateOnScreen(f'./bilder/{filename}.PNG', grayscale = True, confidence = 0.9)
        if (result):
            print(filename, " exist")
            return result
        else:
            print(f'can not see {filename}, re-check in 1 second.')
            current += 1
    print(f"Could not find-{filename}")

def isEnergyFull():
    result = errorhandling.gameReset() 
    if (result == 'skip'):
        return
    result = pyautogui.locateOnScreen('./bilder/fullenergy.PNG', grayscale = False, confidence = 0.9)
    if(result):
        print("Energy is full")
        return True
    print("Energy is not full")
    return False

def readyToRun(what_to_run, whe_to_start=4):
    result = errorhandling.gameReset() 
    if (result == 'skip'):
        print(f'skip clickWrap for {what_to_run}')
        return False
    
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
        saveRun(what_to_run)
        return True
    else:
        print("Too early to run")
        return False
    
def didRunToday(filename):
    time_now = datetime.datetime.now().replace(microsecond=0)
    dailyes_from_file = json.load(open(f'./textfiles/{filename}.txt'))
    # check if saved today
    if(datetime.datetime.fromisoformat(dailyes_from_file["date"]).date() == time_now.date()):
        print(f'{filename} - allready done today')
        return True

def readyToRun_NoSave(filename, whe_to_start=4):
    time_now = datetime.datetime.now().replace(microsecond=0)
    time_to_run = time_now.replace(hour=whe_to_start, minute=0, second=0)

    dailyes_from_file = json.load(open(f'./textfiles/{filename}.txt'))

    # check if saved today
    if(datetime.datetime.fromisoformat(dailyes_from_file["date"]).date() == time_now.date()):
        print(f'{filename} - allready done today')
        return False
    # if not done today, check if its time to run it
    elif(time_now > time_to_run):
        print("time to run")
        return True
    else:
        print("not ready to run yet, try later")
        return False

def saveRun(filename):
    time_now = datetime.datetime.now().replace(microsecond=0)
    with open(f'./textfiles/{filename}.txt', 'w') as file:
        file.write(json.dumps({"date": time_now.isoformat()})) # use `json.loads` to do the reverse

def grabAndDrag(filename):
    result = errorhandling.gameReset() 
    if (result == 'skip'):
        print(f'skip clickWrap for {filename}')
        return
    result = pyautogui.locateOnScreen(f'./bilder/{filename}.PNG', grayscale = True, confidence = 0.9, minSearchTime=200)
    pyautogui.mouseDown(result)
    x,y,w,h = result
    pyautogui.moveTo(x-600, y, 1)
    pyautogui.mouseUp()

def pauseScriptUntilPressP():
    while True:
        key = input("Press 'p' to continue: ").strip().lower()
        if key == "p":
            break


def cvcIncoming(skipUntilEnd: bool) -> bool:
    cvc_ref_date: str = "2026-02-10" # a reference to an existed cvc in the past

    # for non pr cvc to keek score low
    #cvc_ref_date: str = "2026-02-15" # a reference to an existed cvc in the past

    ref_date = datetime.datetime.fromisoformat(cvc_ref_date).date()
    today = datetime.date.today()
    delta_days = (today - ref_date).days

    # To wait until non pr cvc is over on the last day - Thorsday until 11:00
    if (skipUntilEnd and (delta_days - 2) % 28 == 14 and datetime.datetime.now().time() < datetime.time(11, 0)):
        print("Skip everything until cvc is over")
        flagInstance.no_cvc = False
        return True

    # cvc starting today at 11:00
    if delta_days >= 0 and delta_days % 14 == 0 and datetime.datetime.now().time() < datetime.time(11, 0):
        print("cvc is today")
        flagInstance.no_cvc = False
        return True
    
    # cvc starting tomorrow (enter cvc preparation after 18:00 day before)
    tomorrow = today + datetime.timedelta(days=1)
    delta_day_tomorrow = (tomorrow - ref_date).days
    if delta_day_tomorrow >= 0 and delta_day_tomorrow % 14 == 0 and datetime.datetime.now().time() > datetime.time(16, 0):
        print("cvc is tomorrow")
        flagInstance.no_cvc = False
        return True

    flagInstance.no_cvc = True # no_cvc = True means sript will run everything
    return False


    """
    legacy

        print("cvc mode on: ", flagInstance.no_cvc)
    # Turn on cvc stuff
    target_datetime = datetime.datetime(2026, 2, 10, 11, 0, 0) # TODO: make this automatic turn on 12H before cvc start
    current_datetime = datetime.datetime.now()
    print("target_datetime ", target_datetime)
    print("current_datetime ", current_datetime)
    if current_datetime > target_datetime:
        print("turning on CVC mode")
        flagInstance.no_cvc = True # no_cvc = True means sript will run everything, tag arena, 
    print("cvc mode on: ", flagInstance.no_cvc)
    """


if __name__ == "__main__":
    print("cvcIncming ", cvcIncoming())

    