import shared
import pyautogui
import closeadds
import time


my_champions = [
    'arena_live_ronda',
    'arena_live_foli',
    'arena_live_arbiter',
    'arena_live_psylar',
    'arena_live_nekmo',
]

def main():
    if(_arenaIsActive()):
        _initArenaLive()
        #check if have arena live tokeens
        _findOpponent()
        _conductBattle()
        _exitArena()

def _conductBattle(times_to_repeat=1):
    # wait to find opponent
    while(True):
        result = pyautogui.locateOnScreen('./bilder/arena_live_pick_champions.PNG', grayscale = True, confidence = 0.95)
        if (result):
            print("Phase 1 has started")
            _pickChampions()
            break
    
    # wait for your turn to select champions (when plus-card is visible, one or two)
    # pick your champions 
        # if arena_live_youpick
            # select same champions - make a list and iterate
    # your opponent is picking
    # ban champion of opponnent
        # make a list of champions to ban, if not in the list, select any
    # select leader
        # 1. HK, 2. Zelotah 3. Ronda
    # when batttle starts, click auto
    # wait for battle to finish
    # click finish battle

    # repeat or exit

def _pickChampions():
    time.sleep(1)
    result = pyautogui.locateAllOnScreen('./bilder/arena_live_plus.PNG', grayscale = True, confidence = 0.95)
    

def _initArenaLive():
    shared.clickWrap('battle')
    shared.clickWrap('arena')
    shared.clickWrap('arena_live')

def _findOpponent():
    shared.clickWrap('arena_live_find_opponent')
    # check if asked to refyll
        # Live arena refill?
        # Confirm

def _exitArena():
    shared.clickWrap('close_arena')
    shared.clickWrap('bastion')
    closeadds.closeAdds()

def _arenaIsActive():
    result = pyautogui.locateAllOnScreen('./bilder/battle_arenalive.PNG', grayscale = True, confidence = 0.95)
    if(result):
        print("arena live is open")
    else:
        print("arena live is not active")

if __name__ == "__main__":
    #main()
    #_initArenaLive()
    #_findOpponent()
    _conductBattle()