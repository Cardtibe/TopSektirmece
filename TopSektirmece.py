from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q') == False:
    pic = pyautogui.screenshot(region=(0,300,640,300))
    width, height = pic.size
    for x in range(0,width,10):
        for y in range(0,height,10):
            r,g,b = pic.getpixel((x,y))

            if b == 0:
                click(x+0,y+300)
