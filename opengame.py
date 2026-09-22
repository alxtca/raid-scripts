import os
import time
import pyautogui
import shared
import closeadds

def openGame():
    print("Starting game")
    path = r'C:\Users\alxtc\OneDrive\Desktop\rsl.lnk'
    os.startfile(path, 'open')
    time.sleep(2)
    result = pyautogui.locateOnScreen('./bilder/client_game_is_open.PNG', grayscale = True, confidence = 0.95, minSearchTime=600)
    #pyautogui.click(result)
    #shared.checkExist('client_game_is_open', 600)
    print("Game is open")
    #closeadds.closeAdds()
    #TODO: What if maintenance is still ongoing? need a handler for that

def closeGame():
    #NOTE- it works only if game client window is active
    time.sleep(1)
    print("Closing game in 5 seconds")
    time.sleep(5)
    #alternative -> click upper left icon -> Lukk
    pyautogui.hotkey('alt', 'f4')
    result = pyautogui.locateOnScreen('./bilder/ok_close.PNG', grayscale = True, confidence = 0.95, minSearchTime=10)
    pyautogui.click(result)
    #shared.clickWrap('ok_close')
