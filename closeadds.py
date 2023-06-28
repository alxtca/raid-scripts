import pyautogui
import shared
import time

# how do I know if add is on screen?
# - Forge is not visible

def closeAdds():
    print("closeAdds starting.")
    print("waiting for add to appear")

    for i in range(4):
        time.sleep(1)
        forge = pyautogui.locateOnScreen('./bilder/forge.PNG', grayscale = False, confidence = 0.98)
        if(forge):
            print("No adds detected")
        else:
            print("add detected, closing add")
            shared.clickWrap('closeadd_clickaway')
            attention()

# some adds require extra confirmation.
def attention():
    time.sleep(2)
    if (pyautogui.locateOnScreen('./bilder/attention.PNG', grayscale = True, confidence = 0.9)):
        print("closing attention")
        shared.clickWrap('close')

if __name__ == "__main__":
    closeAdds()