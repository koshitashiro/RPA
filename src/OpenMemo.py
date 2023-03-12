import pyautogui as pgui
import os
global root_path
global root_src
global pic_path

def OpenMemo():
    root_path = os.environ.get("RPA-PJ")
    pic_path  = str(root_path) + "/pic"
    print(pgui.size())
    #pgui.moveTo(500,600)
    
    print(root_path)
    position = pgui.locateOnScreen(pic_path + "/memo.png", confidence=0.9)
    pgui.click(position)
    print("test")