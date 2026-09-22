import pyautogui
import time
from datetime import datetime, timedelta
import shared
import farmcampain
import closeadds
import clanboss
import opengame
import dungeon
import arena
import doomtower
from cb import ready_to_run_cb
import pydirectinput

import cv2
import numpy as np

time.sleep(1)

# step 1
# insted of reading picture from file, work with the screen
# ALT
# take a screenshot, and work with that.

# step 2
# extract coordinates from this process and use coordinates to make the click

# read game image (image of the game)
# in my case I don't have image, I rather need coordinate of the screen

# but just to verify this thing is working Ill take a screeen shot
#img = cv2.imread('bilder/game_market.png')
pyautogui.screenshot('screenshot_test.png')
img = cv2.imread('screenshot_test.png')

# read bananas image template
template = cv2.imread('bilder/market_uncommon_39000_transparent.png', cv2.IMREAD_UNCHANGED)
hh, ww = template.shape[:2]

# extract bananas base image and alpha channel and make alpha 3 channels
base = template[:,:,0:3]
alpha = template[:,:,3]
alpha = cv2.merge([alpha,alpha,alpha])

# do masked template matching and save correlation image
correlation = cv2.matchTemplate(img, base, cv2.TM_CCORR_NORMED, mask=alpha)

# set threshold and get all matches
threshhold = 0.95
loc = np.where(correlation >= threshhold)

#print("loc ", loc) # these are coordinates on the picture

# draw matches 
result = img.copy()
for pt in zip(*loc[::-1]):
    cv2.rectangle(result, pt, (pt[0]+ww, pt[1]+hh), (0,0,255), 1)
    print(pt)

# save results
cv2.imwrite('bananas_base2.png', base)
cv2.imwrite('bananas_alpha2.png', alpha)
cv2.imwrite('game_bananas_matches2.jpg', result)

#cv2.imshow('base',base)
#cv2.imshow('alpha',alpha)
#cv2.imshow('result',result)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

