import pyautogui

def collectgems():
    result = pyautogui.locateOnScreen('./bilder/gems.PNG', grayscale = True, confidence = 0.9)
    if(result):
        pyautogui.click(result)
        print("Collected gems")
        return
    print("No gems")