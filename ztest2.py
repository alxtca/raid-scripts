import pyautogui
import time
import datetime
import shared
import farmcampain
import closeadds
import clanboss
import opengame
import dungeon
import arena

# Goal is to repeat faction war fight if Defeated.

done = False
while(True):
    result = pyautogui.locateOnScreen(f'./bilder/factionwars_defeat.PNG', grayscale = False, confidence = 0.95)
    if (result):
        print(result)

    result = pyautogui.locateOnScreen(f'./bilder/factionwars_victory.PNG', grayscale = False, confidence = 0.95)
    if (result):
        print(result)
        done = True
    
    if(done):
        break
    
shared.clickWrap('bastion')
