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
import errorhandling
import doomtower
from errorhandling import errorManager
import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from pprint import pprint
import json
import requests
from ztest2 import TESSERACT_CONFIG_CHIMERA_DAMAGE, _convert_to_millions

from PIL import Image
import re
from collections import Counter


def main():
    for i in range(50):
        dmg = _readDmg()
        if dmg == 0:
             print("0 dmg detected, retry reading")
        elif dmg > 0 and dmg < 8000:
                print("Correct damage reading detected. Damage is too low. Starting new run")
                shared.clickWrap('hydra_free_regroup')
                shared.clickWrap('hydra_start_run')
        elif dmg > 8000:
                print("Big damage detected. Pause script")
                break
        #else start another run


def _readDmg():
    hydra_run_ended = pyautogui.locateOnScreen('./bilder/hydra_result_screen.PNG', grayscale=True, confidence=0.8, minSearchTime=4000000)
    #time.sleep(5)
    if hydra_run_ended:
        x,y,w,h = hydra_run_ended

        left = x-190
        top = y+94
        width = 215
        height = 44

        # take multiple reading to know which number is most frequesnt in readings. That number should be the correct one.
        results = []
        for i in range(20):
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            final_img = _prepareNumberImageForTesseract(screenshot)
            hydra_dmg_text = pytesseract.image_to_string(final_img, config=TESSERACT_CONFIG_CHIMERA_DAMAGE)
            #print("text extracted ", hydra_dmg_text)
            converted = _convert_to_millions(hydra_dmg_text)
            #print("text extracted:", hydra_dmg_text, " converted:", converted)
            if converted is not None:
                 results.append(converted)
        most_common_value, count = Counter(results).most_common(1)[0]
        print("results ", results)
        print("most common value ", most_common_value)
        return most_common_value
     

def _prepareNumberImageForTesseract(screenshot):
        img_np = np.array(screenshot)
        gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        scale_percent = 200  # percent of original size (e.g., 200% = double size)
        width = int(gray.shape[1] * scale_percent / 100)
        height = int(gray.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(gray, dim, interpolation=cv2.INTER_LANCZOS4)
        _, thresh = cv2.threshold(resized, 200, 255, cv2.THRESH_BINARY)
        # 220, 255
        final_img = Image.fromarray(thresh)
        #final_img.show()
        #screenshot.show()
        return final_img


if __name__ == "__main__":
    #main()
    _readDmg()