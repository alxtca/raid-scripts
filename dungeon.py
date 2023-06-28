import shared
import closeadds
import pyautogui
import time

# Dungeons to run. Each takes input with
# 1.file name with picture of dungeon entrance - example 'spider'
# 2.file name with dungeon level to run - example 'spider_20'
# 3.how many time to repeat dungeon

def icegolem(times_to_run=1):
    __dungeonRun('ice_golem', 'ice_golem_20', times_to_run)

def spider(times_to_run=1):
    __dungeonRun('spider', 'spider_20', times_to_run)

def dragon(times_to_run=1):
    __dungeonRun('dragon', 'dragon_20', times_to_run)

def fireknight(times_to_run=1):
    __dungeonRun('fireknight', 'fireknight_20', times_to_run)

def minotaur(times_to_run=1):
    __dungeonRun('minotaur', 'minotaur_15', times_to_run)

def arcaneKeep(times_to_run=1):
    __potionRun('arcane_keep', 'potion_keep_arcane_20', times_to_run)

def forceKeep(times_to_run=1):
    __potionRun('force_keep', 'potion_keep_force_20', times_to_run)

def magicKeep(times_to_run=1):
    __potionRun('magic_keep', 'potion_keep_magic_20', times_to_run)

def voidKeep():
    print("not done yet")

def __dungeonRun(dungeon_name:str, dungeon_level:str, times_to_run:int, start_energy='start_dungeon'):
    __initDungeon()
    shared.clickWrap(dungeon_name)
    shared.clickToTheRight(dungeon_level)
    __refyllAndReclick(dungeon_level)
    __repeatDungeon(times_to_run, dungeon_name, start_energy)
    __finilizeDungeon()

def __potionRun(dungeon_name:str, dungeon_level:str, times_to_run:int, start_energy='start_dungeon'):
    shared.clickWrap('battle')
    shared.clickWrap('dungeons')
    shared.clickWrap(dungeon_name)
    shared.clickToTheRight(dungeon_level)
    __refyllAndReclick(dungeon_level)
    __repeatDungeon(times_to_run, dungeon_name, start_energy)
    __finilizeDungeon()

def __initDungeon():
    shared.clickWrap('battle')
    shared.clickWrap('dungeons')
    shared.dragDungeon()

def __repeatDungeon(times_to_run: int, dungeon_name: str, start_energy: str):
    shared.clickWrap(start_energy)
    __refyllAndReclick(start_energy)
    current_run = 1
    while (current_run < times_to_run):
        print(f'{dungeon_name} run #{current_run}')
        result = shared.clickWrap('replay', 9000)
        __refyllAndReclick('replay')
        if (result):
            current_run += 1

def __finilizeDungeon():
    shared.clickWrap('bastion', 1200)
    print("Dungeon run finished")
    closeadds.closeAdds()

def __refyllAndReclick(what_to_repeat: str):
    print("checking refyll")
    time.sleep(4)
    refill_detected = pyautogui.locateOnScreen('./bilder/confirm_refill.PNG', grayscale = True, confidence = 0.97)
    if(refill_detected):
        print("refyll detected")
        print(refill_detected)
        pyautogui.click(refill_detected) 
        #shared.clickWrap('confirm_refill')
        shared.clickToTheRight(what_to_repeat)
    else:
        print("refyll not detected")


if __name__ == "__main__":
    print("Dungeon run #")
    #minotaur()
    #shared.dragDungeon()
