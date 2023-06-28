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

# This will
# run dungeons, arena, update units, etc...
# runs until stopped
# works only on resolution - 1024x768

#normal_cycle = False # Else intensive(run dungeon more frequent)
normal_cycle = True
intensive_cylce_rounds_left = 50
do_tag_team_arena = True # This can be automatically turned off on CVC days
do_faction_run2 = False

def normalCycle():
    guardianring.upgradeChampions()
    arena.classic()
    if(do_tag_team_arena):
        arena.tagTeam()
    guardianring.upgradeChampions()
    arena.classic()
    if(do_tag_team_arena):
        arena.tagTeam()

while(True):
    #collectgems.collectgems() - need a rework
    guardianring.upgradeChampions()
    market.buyShards()
    clanboss.unm()
    clanboss.nm()
    clanboss.brutal()

    #TODO: dollecting daily advanced quests - will not open on correct tab tomorrow?!?!?
    do_faction_run2 = dailyquests.main() # includes advanced quest collection
    factionwars.main(do_faction_run2) # includes run2
    doomtower.mainBossRepeat(15) #- OBS: if last fight wasn't boss, boss picture is hidden somewhat

    #if dailyquests.collectPlaytimeRewards():
    #    normal_cycle = False
    #    print("Intensive cycle activated")
    
    # collect energy from daily quests

    # advanced quests not possible ... yet

    if(normal_cycle):
        s = 1
        d = 1
        f = 1
        m = 1
        g = 1
        arcane_keep = 1
        force_keep = 1
        magic_keep = 1
    else:
        s = 5
        d = 2
        f = 2
        m = 9
        g = 3
        arcane_keep = 2
        force_keep = 5
        magic_keep = 3
    #dungeon.icegolem(g) # TypeError: cannot unpack non-iterable NoneType object
    dungeon.spider(s)
    #dungeon.dragon(d) # exp 289/e  (12-3 1081/e)
    #ungeon.fireknight(f) # 354/e stage 20
    #dungeon.minotaur(m)

    #dungeon.arcaneKeep(arcane_keep)
    #dungeon.forceKeep(force_keep)
    #dungeon.magicKeep(magic_keep)
    #dungeon.voidKeep()

    #IRON TWINS () todo

    #######fix this - farmcampain.farm(2)

    if(intensive_cylce_rounds_left > 0 and normal_cycle == False):
        intensive_cylce_rounds_left -= 1
        print("Intensive rounds left ", intensive_cylce_rounds_left)
    
    if(intensive_cylce_rounds_left == 0 and normal_cycle == False):
        normal_cycle = True
        intensive_cylce_rounds_left = 6
        print("Back to normal cycle")

    arena.classic()
    if(do_tag_team_arena):
        arena.tagTeam()
    if(normal_cycle):
        normalCycle()
        print("time to sleep")
        time.sleep(290)
    
    print("intensive_cylce_rounds_left ", intensive_cylce_rounds_left)
    







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

# buy items in Bazaar
# collect gems properly

# monitor server_maintenance with thred#2
# restart app 30 min later

# 12:00 CB resets, look for 



# If needed some time in future:
#time.sleep(1)
#opengame.runopen()
#dailylogin.collect() #2. on first run collect daily rewards
#closeadds.closeAdds()
#...
# opengame.closeGame()
