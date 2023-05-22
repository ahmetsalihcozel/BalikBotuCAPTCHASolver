def attempt(refX,refY,intkey):
    import pyautogui
    import time
    import cv2
    import numpy as np
    from python_imagesearch import imagesearch

    refX = refX - 1920
    keyboard = {
        "1": [refX + 23, refY + 13],
        "2": [refX + 68, refY + 13],
        "3": [refX + 113, refY + 13],
        "4": [refX + 23, refY + 36],
        "5": [refX + 68, refY + 36],
        "6": [refX + 113, refY + 36],
        "7": [refX + 23, refY + 59],
        "8": [refX + 68, refY + 59],
        "9": [refX + 113, refY + 59],
        "0": [refX + 70, refY + 85],
        "OK": [refX + 70, refY + 113],
    }

    stringkey = str(intkey)
    firstNum = stringkey[0]
    secondNum = stringkey[-1]

    pyautogui.moveTo(keyboard[firstNum][0],keyboard[firstNum][1])
    time.sleep(0.2)
    pyautogui.leftClick(keyboard[firstNum][0],keyboard[firstNum][1])
    time.sleep(0.2)
    pyautogui.moveTo(keyboard[secondNum][0], keyboard[secondNum][1])
    time.sleep(0.2)
    pyautogui.leftClick(keyboard[secondNum][0], keyboard[secondNum][1])
    time.sleep(0.2)
    pyautogui.moveTo(refX + 70,refY + 113 ,duration = 0.5)
    pyautogui.leftClick(refX + 70,refY + 110)
    pyautogui.leftClick(refX + 70, refY + 110)