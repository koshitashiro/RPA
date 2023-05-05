#画面をコントロールする
#winctrl.py

import pyautogui   as pgui
import pygetwindow as pw

def testpgui(hwnd, title):
    
    win = pw.getActiveWindowTitle()
    print(win)
    if win is not None:
        win.activate()
    
    pgui.click(100, 100)
    return