import shared
import pyautogui
import time
import closeadds

# This refresh classic arena and search champions from list of easy champions
# When no more arena tokens, will use free refills.

#todo: will probably break on gem refyll. take screenshot, and update line 83-90

easy_champs = [
    'arena_classic_arbiter',
    'arena_classic_armiger',
    'arena_classic_coldheart',
    'arena_classic_dh',
    'arena_classic_diabolist',
    'arena_classic_duches',
    'arena_classic_elhain',
    'arena_classic_fenax',
    'arena_classic_frozen_banshee',
    'arena_classic_gravechill',
    'arena_classic_heiress',
    'arena_classic_hk',
    'arena_classic_hounds',
    'arena_classic_incubus',
    'arena_classic_kael',
    'arena_classic_kymar',
    'arena_classic_lydia',
    'arena_classic_lysandra',
    'arena_classic_marishka',
    'arena_classic_magekiller',
    'arena_classic_nekmo',
    'arena_classic_pythion',
    'arena_classic_spirithost',
    'arena_classic_siphi',
    'arena_classic_ultan',
    ]

refyll_w_gem = True


def classic():
    shared.clickWrap('battle')
    shared.clickWrap('arena')
    shared.clickWrap('arena_classic')
    shared.clickWrap('arena_classic_refresh', 1000)
    result = pyautogui.locateOnScreen(f'./bilder/battle_arena_classic.PNG', grayscale = True, confidence = 0.95)
    if (result):
        x,y,w,h = result
        pyautogui.moveTo(x,y,0.4)
    searchAndFight()
    print("arena run finish")

def tagTeam():
    shared.clickWrap('battle')
    shared.clickWrap('arena')
    shared.clickWrap('tag_arena')
    shared.clickWrap('tag_arena_refresh', 1000)
    result = pyautogui.locateOnScreen(f'./bilder/tag_arena_battle.PNG', grayscale = True, confidence = 0.95)
    if (result):
        x,y,w,h = result
        pyautogui.moveTo(x,y,0.4)
    searchAndFightTagTeam()
    print("Tag arena run finish")

def searchAndFightTagTeam():
    total_scrolls = 0
    while (True):
        print("scanning for easy team")        
        result = pyautogui.locateOnScreen(f'./bilder/tag_arena_easyteam.PNG', grayscale = True, confidence = 0.98)
        if(result):
            print (result)
            shared.clickToTheRight('tag_arena_easyteam', 0.9)
            return_result = refyllTagTeam(result)
            if(return_result == 100):
                return ## Way to exit when all free battle are used up
            engageAndWaitTagTeam()
            total_scrolls = 0
        else:
            # print("Arbiter was not detected")
            print("easy team was not detected")
            pyautogui.scroll(-5)
            pyautogui.scroll(-5)
            pyautogui.scroll(-5)
            pyautogui.scroll(-5)
            time.sleep(0.5)
            total_scrolls += 1
            print("total scrolls", total_scrolls)
            if(total_scrolls > 6):
                print("no team has been found.")
                exitArena()
                return 'nomore_opponents' # ONLY WAY TO EXIT
        time.sleep(1)
        # return 'battle_finish'

def refyllTagTeam(attempted_battle_result):
    refyll_w_gem = False
    x,y,w,h = attempted_battle_result
    time.sleep(2)
    result = pyautogui.locateOnScreen('./bilder/confirm_arena_tokens.PNG', grayscale = True, confidence = 0.97)
    if (result):
        shared.clickWrap('confirm_arena_tokens')
        pyautogui.click(x+w/2+100,y+h/2)
    
    result = pyautogui.locateOnScreen('./bilder/tag_arena_gem_refyll.PNG', grayscale = True, confidence = 0.97)
    if (result):
        if(refyll_w_gem):
            shared.clickWrap('confirm_arena_gem_refyll')
            pyautogui.click(x+w/2+100,y+h/2)
        else:
            print("cross out gem refyll")
            print("Tag arena done for today")
            shared.clickWrap('tag_arena_refill_close')
            shared.clickWrap('close_arena')
            shared.clickWrap('bastion')
            return 100

def searchAndFight():
    total_scrolls = 0
    while (True):
        print("scanning for easy hero")        
        for x in easy_champs:
            result = pyautogui.locateOnScreen(f'./bilder/{x}.PNG', grayscale = True, confidence = 0.95)
            if (result):
                print("breaking for loop, champ detected")
                break
        if (result):
            print("Easy champ detected")
            x,y,w,h = result
            pyautogui.click(x+w/2+100,y+h/2)
            refyll(result)
            engageAndWait()
            total_scrolls = 0
        else:
            print("easy champion was not detected")
            pyautogui.scroll(-5)
            pyautogui.scroll(-5)
            pyautogui.scroll(-5)
            pyautogui.scroll(-5)
            time.sleep(0.5)
            total_scrolls += 1
            print("total scrolls", total_scrolls)
            if(total_scrolls > 6):
                print("no opponents has been found.")
                exitArena()
                return 'nomore_opponents' # ONLY WAY TO EXIT
        time.sleep(1)
        # return 'battle_finish'

def exitArena():
    shared.clickWrap('close_arena')
    shared.clickWrap('bastion')
    closeadds.closeAdds()

def refyll(attempted_battle_result):
    x,y,w,h = attempted_battle_result
    time.sleep(2)
    result = pyautogui.locateOnScreen('./bilder/confirm_arena_tokens.PNG', grayscale = True, confidence = 0.97)
    if (result):
        shared.clickWrap('confirm_arena_tokens')
        pyautogui.click(x+w/2+100,y+h/2)
    
    result = pyautogui.locateOnScreen('./bilder/confirm_arena_gem_refyll.PNG', grayscale = True, confidence = 0.97)
    if (result):
        if(refyll_w_gem):
            shared.clickWrap('confirm_arena_gem_refyll')
            pyautogui.click(x+w/2+100,y+h/2)
        else:
            print("cross out gem refyll")

def engageAndWait():
    shared.clickWrap('arena_classic_start') # confirm to start battle
    shared.clickWrap('arena_classic_taptocontinue', 900)
    shared.clickWrap('arena_classic_returntoarena')

def engageAndWaitTagTeam():
    shared.clickWrap('tag_arena_start')
    shared.clickWrap('tag_arena_continue', 900)
    shared.clickWrap('tag_arena_returntoarena')

if __name__ == "__main__":
    searchAndFight()