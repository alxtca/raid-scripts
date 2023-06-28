import pyautogui
import shared
import pyautogui
import time
import closeadds

# Will repeat selected boss.
# To select boss, make screenshot of him and save as 'doom_towerboss.png'
def mainBossRepeat(times_to_repeat:int):
    if(shared.readyToRun('doomtower')):
        _init()
        _findFightRepeat(times_to_repeat)
        _finilize()

def climbStages():
    if(shared.readyToRun('doomtower')):
        _init()
        _autoClimb_9battles()
        _finilize()

def _autoClimb_9battles():
    shared.clickWrap('doom_tower_step1') #select first battle point
    shared.clickWrap('doom_tower_step2') #click start
    
    #now wait for 9 battle to complete
    #how? - because 'bastion' is visible between each
    #There should be completion window...
    # wait for doom_tower_step3 #auto climb complete

    shared.clickWrap('doom_tower_step4') #close X

def mainStageClimb():
    print("This is not developed yet")


def _findFightRepeat(to_repeat=7):
    shared.clickWrap('doom_towerboss')
    shared.clickWrap('start_doomtower')
    did_repeat = 0
    while (did_repeat < to_repeat):
        result = shared.clickWrap('replay2_doomtower', 1000)
        if(result):
            did_repeat += 1


def _init():
    shared.clickWrap('battle')
    shared.dragDoomtower()
    shared.clickWrap('doom_tower')

def _finilize():
    shared.clickWrap('bastion', 3000)
    closeadds.closeAdds()

if __name__ == "__main__":
    #mainBossRepeat(1)
    #_init()
    _init()
    _findFightRepeat(1)
    _finilize()
