import pyautogui
import shared
import time
import closeadds


#           --- auto stages ---
# banner_lord_crypt     - stage 15 - Need reviver
# barbarian_crypt       - stage 21
# dark_elf_crypt        - stage 20 - kaiden/spider
# demon_spawn_crypt     - stage 13 - need champs (summon free lego)
# dwarf_crypt           - stage 17 - lvl, dress up. One more cc - stun/provoke.
# high_elf_crypt        - stage 21 - 
# knights_revenant_crypt- stage 12 - need champs, Whisper, Pharsalas, Renegade
# lizardmen_crypt       - stage 21 - 
# ogryn_crypt           - stage 13 - need champs, Towering titan
# orc_crypt             - stage 21 - 
# sacred_order_crypt    - stage 16 - need cc/heal/revive - debuffer+BivaldA3 can heal - Cardinal/Godseeker Aniri whould do
# shadowkin_crypt       - stage 13 - lvl up, stun set on Sachi (a1-aoe)
# skinwalker_crypt      - stage 20 - need reviver/healer for boss
# undead_horde_crypt    - stage 19 - need reviver to stay alive


# Example. Build string for filename with stage to farm in opened crypt
filename = "shadowkin_crypt" + "_stage_to_farm"

crypts_today = []

middle_section = [
    'factionwars_barbarian_crypt', 
    'factionwars_demon_spawn_crypt', 
    'factionwars_ogryn_crypt', 
    'factionwars_high_elf_crypt', 
    'factionwars_dark_elf_crypt',
    'factionwars_orc_crypt',
    'factionwars_sacred_order_crypt',
    'factionwars_banner_lord_crypt'
    ]

left_section = [
    'factionwars_knights_revenant_crypt',
    'factionwars_lizardmen_crypt',
    'factionwars_skinwalker_crypt',
    'factionwars_undead_horde_crypt'
    ]

right_section = [
    'factionwars_shadowkin_crypt', 
    'factionwars_dwarf_crypt'
    ]

sections = [middle_section, left_section, right_section]

def main(run2=False):
    if(shared.readyToRun('factionwars')):
        _initFaction()
        _findCryptAndFight()
        shared.clickWrap('bastion')
        closeadds.closeAdds()
    if(shared.readyToRun('factionwars2', 7) and run2 == True):
        print("do more faction crypt")
        _initFaction()
        _findCryptAndFight()
        shared.clickWrap('bastion')
        closeadds.closeAdds()


def _findCryptAndFight():
    global crypts_today
    for section in sections:
        _dragTo(section)
        _scanCryptsAndAppend(section)
        if len(crypts_today) > 0:
            _doAllFightsIn(section)
        else:
            shared.clickWrap('close_arena')
            shared.clickWrap('factionwars')
        crypts_today = []

# will fight all crypt in provided section
def _doAllFightsIn(current_section:list):
    navigate_back_to_section = False
    for crypt in crypts_today: 
        if navigate_back_to_section == True: #never True on first run
            print(f'Navigating back to {current_section} for second crypt')
            _dragTo(current_section)
        print(crypt)
        shared.clickWrap(crypt)
        stage = crypt + "_stage_to_farm"
        shared.clickToTheRight(stage)
        shared.clickWrap('start_factionwars')           
        shared.clickWrap('replay_factionwars', 600) 
        shared.clickWrap('replay_factionwars', 600) 
        shared.clickWrap('map', 600)

        if len(crypts_today) > 1:
            navigate_back_to_section = True

# append to crypts_today if found a crypt
def _scanCryptsAndAppend(section:list):
    time.sleep(1)
    print('scanning crypts')
    for crypt in section:
        crypt_found = pyautogui.locateOnScreen(f'./bilder/{crypt}.PNG', grayscale = True, confidence = 0.9)
        if(crypt_found):
            crypts_today.append(crypt)

def _dragTo(section:list):
    if section == left_section :
        _dragLeft()
    if section == right_section:
        _dragRight()
       
#drag to right from middle section
def _dragRight():
    print("dragRight")
    while(True):
        result = pyautogui.locateOnScreen('./bilder/doom_tower_drag_right.PNG', grayscale = True, confidence = 0.9)
        if(result):
            pyautogui.mouseDown(result)
            x,y,w,h = result
            pyautogui.moveTo(x-600, y, 1)
            pyautogui.mouseUp()
            print("done")
            return

#drag to left from middle section
def _dragLeft():
    print("dragLeft")
    while(True):
        result = pyautogui.locateOnScreen('./bilder/doom_tower_drag_left.PNG', grayscale = True, confidence = 0.9)
        if(result):
            pyautogui.mouseDown(result)
            x,y,w,h = result
            pyautogui.moveTo(x+800, y, 1)
            pyautogui.mouseUp()
            print("done")
            return
        
def _initFaction():
    shared.clickWrap('battle')
    shared.clickWrap('factionwars')

if __name__ == "__main__":
    #main()
    _initFaction()
    _findCryptAndFight()
    shared.clickWrap('bastion')
    closeadds.closeAdds()