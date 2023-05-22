from toBinary import *
import pyautogui
import numpy as np
import cv2
from python_imagesearch import imagesearch

img = pyautogui.screenshot(region=(1448, 248, 37,28 ))
img2 = np.array(img)
img1 = cv2.imwrite("cpt2.png", img2)

pos = imagesearch.imagesearch("Bot_Ver_Keys.PNG",0.7)
print(pos)