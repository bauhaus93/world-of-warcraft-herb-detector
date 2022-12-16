#!/bin/env python3

import time
import pyautogui
import numpy as np
import cv2
import winsound

THRESHOLD = .9

reference = cv2.imread("herbs.png")
w, h = reference.shape[:-1]

did_beep = False
while True:
    img = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)

    result = cv2.matchTemplate(img, reference, cv2.TM_CCOEFF_NORMED)
    found_herbs = np.any(np.where(result >= THRESHOLD))
    if found_herbs and not did_beep:
        winsound.Beep(2500, 500)
        did_beep = True
    elif not found_herbs and did_beep:
        did_beep = False
    time.sleep(.5)