#画面をコントロールする
#winctrl.py

import pyautogui   as pgui
import pygetwindow as pgw

pgui.PAUSE = 0.25

def testpgui(hwnd, title):
    
    print(F"{hwnd} {title}")
    
    win = pgw.Window(hwnd)
    
    #activateのみだと最小化された画面はアクティブにならない
    #ただし、この操作によって画面サイズが変更される可能性がある
    win.restore()
    win.activate()
    
    memoCtrl()
    
    return

def memoCtrl():
    pgui.write("memo")
    pgui.press("enter")
    
    pgui.hotkey("ctrl", "shift", "s")
    pgui.write("test.txt", interval=0.25)
    pgui.press("enter")
    
    return