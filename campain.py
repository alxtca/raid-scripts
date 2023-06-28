import pyautogui
import time


#heroStars 1-5*
heroLevel = 5


def calculateRuns(herolvl):
    #12.3 +8652
    match herolvl:
        case 1:
            print("runs to run: ", 3)  # 24 energy
            return 2
        case 2:
            print("runs to run: ", 10) # 88 energy
            return 8
        case 3:
            print("runs to run: ", 22) # 200 energy
            return 23
        case 4:
            print("runs to run: ", 52) # 424 energy
            return 51
        case 5:
            print("runs to run: ", 112) # 896 energy
            return 112
    return 0


def campainRepeat(_timesToRun):
    currentRun = 0
    while(currentRun < _timesToRun):
        time.sleep(2)
        result = pyautogui.locateOnScreen('./bilder/replay_campain.PNG', grayscale = True, confidence = 0.98)
        if(result):
            currentRun += 1
            print(currentRun, " clicking", result)
            pyautogui.click(result)
            _refill(result)
    print("COMLETE")

def _refill(result_repeat):
    time.sleep(3)
    refill = pyautogui.locateOnScreen('./bilder/confirm_refill.PNG', grayscale = True, confidence = 0.97)
    if(refill):
        pyautogui.click(refill)
        time.sleep(1)
        pyautogui.click(result_repeat)

if __name__ == "__main__":
    timesToRun = calculateRuns(heroLevel)
    campainRepeat(timesToRun)
