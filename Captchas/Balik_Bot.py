import pyautogui
import time
import pydirectinput
from python_imagesearch import imagesearch
from attempt import *
from toBinary import *
from OCR import *
import numpy as np
import cv2
import os


os.chdir("C:/Me/PythonKayıt/Metin2_Balik_Botu/Captchas")
cwd = os.getcwd()

print("Current working directory: {0}".format(cwd))

clNum = int(input("Kaç client calıştıracaksınız ?: "))
clRef = [[0,0],[0,0],[0,0],[0,0]]
clOrta = [[0,0],[0,0],[0,0],[0,0]]
zirh = [[0,0],[0,0],[0,0],[0,0]]
sekme1 = [[0,0],[0,0],[0,0],[0,0]]
sekme2 = [[0,0],[0,0],[0,0],[0,0]]

for i in range(clNum):
    print("{}. Client'in 5 sn sonra kose noktası referans olarak isaretlenecek\nBunun için Mouse'u clientin tam kosesine gelecek sekilde bekletin".format(i+1))
    time.sleep(5)
    clRef[i][0],clRef[i][1] = pyautogui.position()
    print("{}. Client'in referans noktası kaydedildi: {},{}".format(i+1,clRef[i][0],clRef[i][1]))
    clOrta[i][0],clOrta[i][1] = clRef[i][0] + 400,clRef[i][1] + 300
    sekme1[i][0], sekme1[i][1] = clRef[i][0] + 660, clRef[i][1] + 230
    sekme2[i][0], sekme2[i][1] = clRef[i][0] + 695, clRef[i][1] + 230

    zirh[i][0],zirh[i][1] = clRef[i][0] + 773, clRef[i][1] + 497

envanter1 = []
envanter2 = []
envanter3 = []
envanter4 = []
sayac = 0
for i in range(260,516,32):
    for j in range(650,810,32):
        sayac +=1
        if sayac <= 20:
            envanter1.append([clRef[0][0] + j, clRef[0][1] + i,200])
        else:
            envanter1.append([clRef[0][0] + j, clRef[0][1] + i])
sayac = 0

for i in range(260,516,32):
    for j in range(650,810,32):
        sayac += 1
        if sayac <= 20:
            envanter2.append([clRef[1][0] + j, clRef[1][1] + i,200])
        else:
            envanter2.append([clRef[1][0] + j, clRef[1][1] + i])
sayac = 0

for i in range(260,516,32):
    for j in range(650,810,32):
        sayac += 1
        if sayac <= 20:
            envanter3.append([clRef[2][0] + j, clRef[2][1] + i,200])
        else:
            envanter3.append([clRef[2][0] + j, clRef[2][1] + i])
sayac = 0

for i in range(260,516,32):
    for j in range(650,810,32):
        sayac += 1
        if sayac <= 20:
            envanter4.append([clRef[3][0] + j, clRef[3][1] + i,200])
        else:
            envanter4.append([clRef[3][0] + j, clRef[3][1] + i])


pixel_deger1 = []
pixel_deger2 = []
pixel_deger3 = []
pixel_deger4 = []

def Balik_Yakala(zirh_Lokx,zirh_Loky,envanter_Lokx,envanter_Loky,clOrta_Lokx,clOrta_Loky):
    pyautogui.moveTo(clOrta_Lokx,clOrta_Loky)
    time.sleep(0.1)
    pyautogui.rightClick(clOrta_Lokx,clOrta_Loky)
    time.sleep(1)
    pydirectinput.keyDown("space")
    time.sleep(0.1)
    pydirectinput.keyUp("space")
    time.sleep(0.1)
    pyautogui.moveTo(zirh_Lokx, zirh_Loky)
    time.sleep(0.1)
    pyautogui.rightClick(zirh_Lokx, zirh_Loky)
    time.sleep(0.1)
    pyautogui.moveTo(envanter_Lokx, envanter_Loky)
    time.sleep(0.1)
    pyautogui.rightClick(envanter_Lokx, envanter_Loky)
    time.sleep(0.1)
    pydirectinput.keyDown("space")
    time.sleep(0.1)
    pydirectinput.keyUp("space")

def Olta_At(clOrta_Lokx,clOrta_Loky,envanter_Lokx,envanter_Loky):
    pyautogui.moveTo(clOrta_Lokx,clOrta_Loky)
    time.sleep(0.1)
    pyautogui.rightClick(clOrta_Lokx,clOrta_Loky)
    time.sleep(0.1)
    pyautogui.moveTo(envanter_Lokx, envanter_Loky)
    time.sleep(0.1)
    pyautogui.rightClick(envanter_Lokx, envanter_Loky)
    time.sleep(0.1)
    pydirectinput.keyDown("space")
    time.sleep(0.1)
    pydirectinput.keyUp("space")



def istridye_ac(env,sek1x,sek1y,sek2x,sek2y):
    pyautogui.moveTo(sek2x, sek2y)
    time.sleep(0.1)
    pyautogui.leftClick(sek2x, sek2y)
    time.sleep(0.1)
    for kordinat in env:
        pyautogui.moveTo(kordinat[0], kordinat[1])
        time.sleep(0.1)
        pyautogui.rightClick(kordinat[0], kordinat[1])
        time.sleep(0.1)
    pyautogui.moveTo(sek1x,sek1y)
    time.sleep(0.1)
    pyautogui.leftClick(sek1x,sek1y)
    time.sleep(0.1)





time_tutma1 = 0
time_tutma2 = 0
time_tutma3 = 0
time_tutma4 = 0

envsay1 = 0
envsay2 = 0
envsay3 = 0
envsay4 = 0

tstart = time.time()
captchachanged = [-1, -1]




while True:

    pixel_deger1 = pyautogui.pixel(clRef[0][0] + 420, clRef[0][1] + 242)
    #print("1.Client RGB değerleri: {}".format(pixel_deger1))
    kosul1 = pixel_deger1[0] > 200 and pixel_deger1[1] > 200 and pixel_deger1[2] > 200
    if clNum > 1:
        pixel_deger2 = pyautogui.pixel(clRef[1][0] + 420, clRef[1][1] + 242)
        # print("2.Client RGB değerleri: {}".format(pixel_deger2))
        kosul2 = pixel_deger2[0] > 200 and pixel_deger2[1] > 200 and pixel_deger2[2] > 200
    else:
        kosul2 = 0
    if clNum > 2:
        pixel_deger3 = pyautogui.pixel(clRef[2][0] + 420, clRef[2][1] + 242)
        # print("3.Client RGB değerleri: {}".format(pixel_deger3))
        kosul3 = pixel_deger3[0] > 200 and pixel_deger3[1] > 200 and pixel_deger3[2] > 200
    else:
        kosul3 = 0
    if clNum > 3:
        pixel_deger4 = pyautogui.pixel(clRef[3][0] + 420, clRef[3][1] + 242)
        # print("4.Client RGB değerleri: {}".format(pixel_deger4))
        kosul4 = pixel_deger4[0] > 200 and pixel_deger4[1] > 200 and pixel_deger4[2] > 200
    else:
        kosul4 = 0

    pos = imagesearch.imagesearch("Bot_Ver_Keys.PNG",0.7)

    time_tutma1 += 1
    if clNum > 1:
        time_tutma2 += 1
    if clNum > 2:
        time_tutma3 += 1
    if clNum > 3:      
        time_tutma4 += 1

    if time_tutma1 > 60:
        if envanter1[envsay1][2] == 0:
            envsay1 += 1
        envX = envanter1[envsay1][0]  
        envY = envanter1[envsay1][1]
        Olta_At(clOrta[0][0], clOrta[0][1], envX, envY)
        envanter1[envsay1][2] -= 1
        time_tutma1 = 0

    if time_tutma2 > 60:
        if envanter2[envsay2][2] == 0:
            envsay2 += 1
        envX = envanter2[envsay2][0]
        envY = envanter2[envsay2][1]
        Olta_At(clOrta[1][0], clOrta[1][1], envX, envY)
        envanter2[envsay2][2] -= 1
        time_tutma2 = 0
        time_tutma1 += 0.3

    if time_tutma3 > 60:
        if envanter3[envsay3][2] == 0:
            envsay3 += 1
        envX = envanter3[envsay3][0]
        envY = envanter3[envsay3][1]
        Olta_At(clOrta[2][0], clOrta[2][1], envX, envY)
        envanter3[envsay3][2] -= 1
        time_tutma3 = 0
        time_tutma1 += 0.3

    if time_tutma4 > 60:
        if envanter4[envsay4][2] == 0:
            envsay4 += 1
        envX = envanter4[envsay4][0]
        envY = envanter4[envsay4][1]
        Olta_At(clOrta[3][0], clOrta[3][1], envX, envY)
        envanter4[envsay4][2] -= 1
        time_tutma4 = 0
        time_tutma1 += 0.3

    if kosul1 == 1 or kosul2 == 1 or kosul3 == 1 or kosul4 == 1 or pos[0] != -1:


        #captcha solver section

        refX = pos[0] - 1920
        refY = pos[1]

        #print(pos)
        #print(pos[0] != -1)
        #print(captchachanged[0] == -1)

        if pos[0] != -1:
            while pos[0] != -1:
                img = pyautogui.screenshot(region=(refX + 7, refY - 32, 37, 28))
                img2 = np.array(img)
                img1 = cv2.imwrite("cpt1.png", img2)
                binaryimg = toBinary(img2)
                predict = captchaPredict(binaryimg)
                for i in range(len(predict)):
                    attempt(pos[0],pos[1],predict[i])
                    pos = imagesearch.imagesearch("Bot_Ver_Keys.PNG", 0.7)
                    poscptch = imagesearch.imagesearch("cpt1.png", 0.8)
                    if pos[0] == -1 or poscptch[0] == -1:
                        time.sleep(0.1)
                        pydirectinput.keyDown("space")
                        time.sleep(0.1)
                        pydirectinput.keyUp("space")
                        break








        if pixel_deger1 != []:
            if pixel_deger1[0] > 200 and pixel_deger1[1] > 200 and pixel_deger1[2] > 200:
                if envanter1[envsay1][2] == 0:
                    envsay1 += 1
                envX = envanter1[envsay1][0]
                envY = envanter1[envsay1][1]
                Balik_Yakala(zirh[0][0],zirh[0][1],envX,envY,clOrta[0][0],clOrta[0][1])
                envanter1[envsay1][2] -= 1
                time_tutma1 = 0
                if clNum > 1:
                    time_tutma2 += 1.8
                if clNum > 2:
                    time_tutma3 += 1.8
                if clNum > 3:
                    time_tutma4 += 1.8

        if pixel_deger2 != []:
            if pixel_deger2[0] > 200 and pixel_deger2[1] > 200 and pixel_deger2[2] > 200:
                if envanter2[envsay2][2] == 0:
                    envsay2 += 1
                envX = envanter2[envsay2][0]
                envY = envanter2[envsay2][1]
                Balik_Yakala(zirh[1][0],zirh[1][1],envX, envY,clOrta[1][0],clOrta[1][1])
                envanter2[envsay2][2] -= 1
                time_tutma2 = 0
                time_tutma1 += 1.8
                if clNum > 2:
                    time_tutma3 += 1.8
                if clNum > 3:
                    time_tutma4 += 1.8

        if pixel_deger3 != []:
            if pixel_deger3[0] > 200 and pixel_deger3[1] > 200 and pixel_deger3[2] > 200:
                if envanter3[envsay3][2] == 0:
                    envsay3 += 1
                envX = envanter3[envsay3][0]
                envY = envanter3[envsay3][1]
                Balik_Yakala(zirh[2][0],zirh[2][1],envX, envY,clOrta[2][0],clOrta[2][1])
                envanter3[envsay3][2] -= 1
                time_tutma3 = 0
                time_tutma1 += 1.8
                if clNum > 1:
                    time_tutma2 += 1.8
                if clNum > 3:
                    time_tutma4 += 1.8

        if pixel_deger4 != []:
            if pixel_deger4[0] > 200 and pixel_deger4[1] > 200 and pixel_deger4[2] > 200:
                if envanter4[envsay4][2] == 0:
                    envsay4 += 1
                envX = envanter4[envsay4][0]
                envY = envanter4[envsay4][1]
                Balik_Yakala(zirh[3][0],zirh[3][1],envX, envY,clOrta[3][0],clOrta[3][1])
                envanter4[envsay4][2] -= 1
                time_tutma4 = 0
                time_tutma1 += 1.8
                if clNum > 1:
                    time_tutma2 += 1.8
                if clNum > 2:
                    time_tutma3 += 1.8





        tnow = time.time()

        if tnow - tstart > 1800:
            tstart = time.time()

            for i in range(clNum):
                sek1x, sek1y, sek2x, sek2y = sekme1[i][0], sekme1[i][1], sekme2[i][0], sekme2[i][1]
                if i == 0:
                    en = envanter1
                elif i == 1:
                    en = envanter2
                elif i == 2:
                    en = envanter3
                elif i == 3:
                    en = envanter4

                istridye_ac(en, sek1x, sek1y, sek2x, sek2y)




