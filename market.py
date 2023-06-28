import pyautogui
import shared
import time
import closeadds

def buyShards():
    result = pyautogui.locateOnScreen(f'./bilder/market_new.PNG', grayscale = False, confidence = 0.98)
    if(result):
        print("market has new items")
        pyautogui.click(result)
        time.sleep(2)
        __buyGreenShards()
        __buyAncientShards()
        __buyChampions6000()
        __buyChampions8000()
        shared.clickWrap('close_arena')
        closeadds.closeAdds()
    else:
        print("market has't updated yet...")

def __buyGreenShards():
    __buyShardsGeneral('market_green_shard', 'get5000')

def __buyAncientShards():
    __buyShardsGeneral('market_ancient_shard','get200000')

def __buyShardsGeneral(type, get_price):
    result = pyautogui.locateAllOnScreen(f'./bilder/{type}.PNG', grayscale = True, confidence = 0.90)
    for i in result:
        x,y,w,h = i
        print(x, y, w,h)
        pyautogui.click(x+w+50,y+h/2) #this should hit the button
        shared.clickWrap(get_price)
        time.sleep(0.6)

def __buyChampions6000():
    print("")
    result = pyautogui.locateAllOnScreen('./bilder/6000.PNG', grayscale = True, confidence = 0.97)
    for i in result:        
        x,y,w,h = i
        pyautogui.click(x+5,y+5)
        shared.clickWrap('6000get')
        shared.clickWrap('close_arena')
        time.sleep(1)

def __buyChampions8000():
    print("")
    result = pyautogui.locateAllOnScreen('./bilder/8000.PNG', grayscale = True, confidence = 0.9)
    for i in result:        
        x,y,w,h = i
        pyautogui.click(x+5,y+5)
        shared.clickWrap('8000get')
        shared.clickWrap('close_arena')
        time.sleep(1)


if __name__ == "__main__":
    #buyShards()
    #__buyGreenShards()
    #__buyAncientShards()
    #__buyChampions6000()
    __buyChampions8000()
