#画面をコントロールする
#winctrl.py

import pyautogui as pgui
import pywinauto as pwa

def testpwa():
    pwa.Application.top_window()
    


def testpgui():
    pgui.click(100, 100)
