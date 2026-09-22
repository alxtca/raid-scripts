import time
import farmcampain
import clanboss
import opengame
import collectgems
import closeadds
import dailylogin
import dailyquests
import dungeon
import doomtower
import arena
import guardianring
import market
import factionwars
import arenalive
from flags import flagInstance
import errorhandling
from errorhandling import errorManager, unfinishedBattleCheck
import datetime
import chimeraclash
import hydraclash
import chimera
from chimera import Mode
import shared


# This will
# run dungeons, arena, update units, etc...
# runs until stopped
# works only on resolution - 1024x768

# restart is managed inside errorhandling

while(True):
    # TODO: make a global swither for main theme in stronghold: x-mas, halloween, etc...
    # 'is_halloween' png
    # it can automatically check what theam is it and apply it
    # buy items in bazaar

    print("cvcIncoming ", shared.cvcIncoming(True))
    #flagInstance.no_cvc = True # manual override

    print("Fresh start")
    errorManager.did_reset = False
    errorManager.error_detected = False
    closeadds.closeAdds()
    if(unfinishedBattleCheck() == 'detected'):
        closeadds.closeAdds()
    
    market.buyShards(False)
    guardianring.upgradeChampions()
    collectgems.main()
    dailyquests.main()

    dungeon.ironTwins()
    dungeon.icegolem() # TODO: make dungeon.main() that accept ENUM SPIDER | DRAGON | FK | MINO | EVENT | SD | SHOGUN | IRONTWINS | POTIONKEEP
    #dungeon.spider()
    #dungeon.dragon()
    #dungeon.fireknight()
    #dungeon.minotaur()
    #dungeon.eventDungeon()
    #dungeon.sanddevil()
    #dungeon.shogun()

    factionwars.main() 
    clanboss.main()
    doomtower.main()

    #chimeraclash.main()
    #hydraclash.main()
    #chimera.main(Mode.PUSH)

    arenalive.main()
    arena.tagTeam("2026-09-16")
    arena.classic() 

    #dungeon.arcaneKeep()
    #dungeon.forceKeep()
    #dungeon.magicKeep()
    #dungeon.spiritKeep()
    #dungeon.voidKeep()
    print("sleep 15 min ")
    time.sleep(900)






# todo list
# - collect advanced rewards and do more factionwars, doomtower boss, team arena.
# - how to avoid passing variables down several level of functions? -global variables?
# global variables to track clan boss, daily quests, ...
# multithreads for:
#   -watch out for maintenance events
#   -pause script execution
# log to include:
#   -dungeon wins
#   -arena wins/losses
#   -market shards aquired
#   -
# log can store to files(db) and read from files based on dates

# monitor server_maintenance with thred#2
# restart app 30 min later

# 12:00 CB resets, look for 
