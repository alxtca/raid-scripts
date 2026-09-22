import shared
import pyautogui
import closeadds
import time
import errorhandling
from errorhandling import errorManager
from datetime import datetime, timedelta
from flags import flagInstance


my_champions = [
    #'arena_live_armanz',
    'arena_live_marius',
    'arena_live_mavara',
    # 'arena_live_galathir',
    'arena_live_talenna',
    'arena_live_pallas',
    'arena_live_cat',
    'arena_live_karnage',
    # 'live_arena_donnie',
    # 'arena_live_jack',
    'arena_live_polara',
    #'arena_live_fabian',
    'arena_live_freya', 
    'arena_live_noelle',
    'arena_live_wukong',
    'arena_live_embris',
    'arena_live_rotos',
    'arena_live_frolni',
    'arena_live_ankora',
    'arena_live_kaja', 
    #'arena_live_arbiter',
]

speed_champions = [ ]

lead_champions = [
    #'arena_live_lead_arbiter',
    'arena_live_lead_karnage', # ok
    'arena_live_lead_mavara', # ok
    'arena_live_lead_talenna', # ok
    'arena_live_lead_cat', # oke

    'arena_live_lead_noelle', # 
    'arena_live_lead_wukong', # 
    'arena_live_lead_fabian',
    # 'arena_live_lead_armanz',
    #'arena_live_lead_mortu',
    'arena_live_lead_ankora',
    #'arena_live_lead_kaja',
]

ban_champions = [
    'arena_live_ban_solonar'
]


def main():
    if(flagInstance.no_cvc):
        for i in range(16):
            if(__ready_to_run_livearena()):
                if (errorhandling.gameReset()  == 'skip'):
                    return    
                if(_arenaIsActive()):
                    _initArenaLive()
                    _collectRefylls()
                    _claimChest()
                    if(_haveBattlesLeft()): #if not refylls are visible within 3 seconds, assumes searching opponent
                        _conductBattle()
                        _exitArena()
                    else:
                        _exitArena()
            else:
                print("aborting livearena")

# this run right after button 'find opponent' was clicked
def _conductBattle():
    if (errorhandling.gameReset()  == 'skip'):
        return
    counter_to_exit = 0
    championOrder = 0
    did_apply_filter = False

    while(True):
        print("starting select champ loop")
        pick_champions_now = pyautogui.locateOnScreen('./bilder/arena_live_pick_your_champions.PNG', grayscale = True, confidence = 0.95, minSearchTime=2)
        if (pick_champions_now):
            if did_apply_filter == False:
                shared.clickWrap("arena_live_filter")
                did_apply_filter = True

            print("Will try to pick champ -", my_champions[championOrder])
            champ_available = pyautogui.locateOnScreen(f'./bilder/{my_champions[championOrder]}.PNG', grayscale = True, confidence = 0.9, minSearchTime=2)
            if(champ_available):
                shared.clickWrap(my_champions[championOrder], confidence=0.9)
                confirm = pyautogui.locateOnScreen('./bilder/arena_live_confirm_pick.PNG', grayscale = False, confidence = 0.97, minSearchTime=2)
                if(confirm):
                    shared.clickWrap('arena_live_confirm_pick')
                    championOrder += 1
                else:
                    print("pick one more champ")
                    championOrder += 1
            else:
                championOrder += 1
        ban = pyautogui.locateOnScreen('./bilder/live_arena_ban_champions.PNG', grayscale = True, confidence = 0.95, minSearchTime=1)
        if(ban):
            break

        opponent_left = pyautogui.locateOnScreen('./bilder/arena_live_opponent_left.PNG', grayscale = True, confidence = 0.95, minSearchTime=1)
        if(opponent_left):
            shared.clickWrap('arena_live_return_to_arena_when_opponent_left')
            return
        # next operation should read return message and act accordingly

        cant_find_opponent = pyautogui.locateOnScreen('./bilder/arena_live_cant_find_opponent.PNG', grayscale = True, confidence = 0.95, minSearchTime=1)
        if(cant_find_opponent):
            shared.clickWrap('arena_live_refind')
            #might require different sequence to leave live arena - make a note when possible
        time.sleep(1)
        counter_to_exit += 1
        print("repeating select champ loop") #TODO: this cause game to restart. Find out why does it not exit the loop.
        if(counter_to_exit > 120):
            #how about clicking bastion, if no bastion then set error detected
            errorManager.error_detected = True
            return
    
    print("CHAMPION SELECTION IS DONE. NEXT PHASE IS BANNING.")

    #BANNING
    result = pyautogui.locateOnScreen('./bilder/arena_live_ban_champion_ban_leader.PNG', grayscale = True, confidence = 0.95, minSearchTime=120)
    if (result):
        if(shared.clickWrapWithSkip('arena_live_ban_solonar')):
            print("banned Solonar")
        else:
            shared.clickToTheRight('arena_live_ban_champion_ban_leader')
            
        shared.clickWrap('arena_live_confirm_pick')
    else:
        errorManager.error_detected = True

    print("PICKING MY LEAD")
    select_lead = pyautogui.locateOnScreen('./bilder/live_arena_pick_leader.PNG', grayscale = True, confidence = 0.95, minSearchTime=50)
    if(select_lead):
        for lead in lead_champions:
            print("trying to pick lead ", lead)
            lead_found = pyautogui.locateOnScreen(f'./bilder/{lead}.PNG', grayscale = True, confidence = 0.9, minSearchTime=3)
            if (lead_found):
                pyautogui.click(lead_found)
                #shared.clickWrap(lead, confidence=0.95)
                shared.clickWrap('arena_live_confirm_pick') # this should not trigger error state
                break

        # if no lead was found, what to do?
        # just skip lead selection and wait for AUTO button to appear - this is allready done.

    shared.clickWrap('arena_live_auto', 300)
    shared.clickWrap('arena_live_return', 1200)

def _initArenaLive():
    if (errorhandling.gameReset()  == 'skip'):
        return
    shared.clickWrap('battle')
    shared.clickWrap('arena')
    shared.clickWrap('arena_live')

def _haveBattlesLeft():
    # This will check if there are more battles available. Refyll if available. Else communicate false
    if (errorhandling.gameReset()  == 'skip'):
        return
    
    shared.clickWrap('arena_live_find_opponent')
    refyll_modal = pyautogui.locateOnScreen('./bilder/live_arena_refyll_modal.PNG', grayscale = True, confidence = 0.95, minSearchTime=3)
    if(refyll_modal):
        print("refyll detected, handle refyll")        
        free_refyll = pyautogui.locateOnScreen('./bilder/arena_live_confirm_refyll.PNG', grayscale = True, confidence = 0.95, minSearchTime=1)
        gem_refyll_10 = pyautogui.locateOnScreen('./bilder/arena_live_10gem_refyll.PNG', grayscale = True, confidence = 0.95, minSearchTime=1)
        #gem_refyll_20 = pyautogui.locateOnScreen('./bilder/arena_live_20gem_refyll.PNG', grayscale = True, confidence = 0.95, minSearchTime=1)
        gem_refyll_20 = False
        
        if(free_refyll):
            shared.clickWrap('arena_live_confirm_refyll')
            shared.clickWrap('arena_live_find_opponent')
            return True
        elif(gem_refyll_10):
            shared.clickWrap('arena_live_10gem_refyll')
            shared.clickWrap('arena_live_find_opponent')
            return True
        elif(gem_refyll_20):
            shared.clickWrap('arena_live_10gem_refyll')
            shared.clickWrap('arena_live_find_opponent')
            return True
        else:
            print("no more cheap refylls today")
            shared.clickWrap('close_arena')
            # write timestamp - check timestamp in the beginning of the main()
            current_datetime = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            with open('./textfiles/arenalive.txt', 'w') as file:
                file.write(current_datetime)
            return False

    else:
        print("no refyll needed, proceed to battle")
        return True

def _claimChest():
    if (errorhandling.gameReset()  == 'skip'):
        return
    print("_claimChest")
    claim_chest = pyautogui.locateOnScreen('./bilder/arena_live_claim_chest.PNG', grayscale = True, confidence = 0.97, minSearchTime=3)
    if(claim_chest):
        shared.clickWrap('arena_live_claim_chest')
        shared.clickWrap('arena_live_claim_chest2')
    else:
        print("no chest to collect")

def _exitArena():
    if (errorhandling.gameReset()  == 'skip'):
        return
    print("_exitArena")
    shared.clickWrap('close_arena')
    shared.clickWrap('bastion')
    closeadds.closeAdds()

def _arenaIsActive():
    if (errorhandling.gameReset()  == 'skip'):
        return
    result = pyautogui.locateOnScreen('./bilder/battle_arenalive.PNG', grayscale = True, confidence = 0.95, minSearchTime=1)
    if(result):
        print("arena live is open")
        return True
    else:
        print("arena live is not active")
        return False

def _collectRefylls():
    if (errorhandling.gameReset()  == 'skip'):
        return
    print("_collectRefylls")
    result = pyautogui.locateOnScreen('./bilder/live_arena_battles55.PNG', grayscale = False, confidence = 0.99, minSearchTime=4)
    if(result):
        print("collecting refylls")
        shared.clickWrap('arena_live_collect_refyll')
    else:
        print("no refylls to collect")



def __ready_to_run_livearena():
    try:
        with open('./textfiles/arenalive.txt', 'r') as file:
            execution_datetime_str = file.read().strip()
            executed_last_time = datetime.strptime(execution_datetime_str, "%d.%m.%Y %H:%M:%S")
            current_datetime = datetime.now()

            if executed_last_time.date() == current_datetime.date():
                print("Allready did run today")
                return False
            else:
                print("Ready to run")
                return True
    except FileNotFoundError:
        return False
    



if __name__ == "__main__":
    flagInstance.no_cvc = True
    main()
