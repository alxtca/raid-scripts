import os
import time
import pyautogui
import shared

def runopen():
    print("Starting game")
    path = r'C:\Users\alxtc\OneDrive\Desktop\rsl.lnk'
    os.startfile(path, 'open')
    time.sleep(20)
    while (pyautogui.locateOnScreen('./bilder/opening.PNG', grayscale = True, confidence = 0.9)):
        time.sleep(3)
    print("Game is open")

def closeGame():
    time.sleep(1)
    print("Closing game")
    pyautogui.hotkey('alt', 'f4')
    shared.clickWrap('ok_close')
