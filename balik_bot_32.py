import pyautogui
from time import sleep
import win32
import win32api, win32ui, win32con, win32gui

def click_pg(name,x,y):
    hWnd = win32gui.FindWindow(None, namepg)
    #hWnd = win32gui.FindWindowEx(hWnd,None,None,None)

    click = win32api.MAKELONG(x,y)
    win32gui.SendMessage(hWnd,win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,click)
    win32gui.SendMessage(hWnd, win32con.WM_LBUTTONUP,None,click)

click = win32api.MAKELONG(200,200)
namepg = "Elsmetin2 Doğuya Has Macera "
hWnd = win32gui.FindWindow(None, namepg)
print(hWnd)
print(click)

click_pg(namepg,200,200)