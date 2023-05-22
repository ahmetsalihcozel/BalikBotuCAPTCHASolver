import pyautogui
import pydirectinput
import time

clRefx,clRefy = 8,31
envanter = [[clRefx + 650, clRefy + 260],
            [clRefx + 680, clRefy + 260],
            [clRefx + 710, clRefy + 260],
            [clRefx + 745, clRefy + 260],
            [clRefx + 775, clRefy + 260],
            [clRefx + 650, clRefy + 295],
            [clRefx + 680, clRefy + 295],
            [clRefx + 710, clRefy + 295],
            [clRefx + 745, clRefy + 295],
            [clRefx + 775, clRefy + 295],
            ]

x,y = 8,31

while True:
    x1,y1 = pyautogui.position()
    #print(x1,y1)
    #pyautogui.rightClick(envanter[1][0], envanter[1][1])
    print(x1,y1)
    time.sleep(2)
