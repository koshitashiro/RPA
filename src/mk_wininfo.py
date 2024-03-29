import sys.path_glob as mp
import pygetwindow as pgw
import win32gui
import file.file_act as fa
from win.window_class import WindowInf


def mkInitWindow():
    useLst = []   #使用するアプリ一覧
    mkLst  = []   #InitWindowリスト
    
    useLst = getUseLst()
    
    for openLst in useLst:
        openLst = pgw.getWindowsWithTitle(openLst)
        mkWindowInf(mkLst, openLst)
    
    fa.writeWinInfo(mkLst)
    return
    
#ウィンドウ情報を作成する
def mkWindowInf(mkLst, openLst):
    
    if len(openLst) == 0:
        return
    else:
        for i in range(len(openLst)):
                
            hwnd  = openLst[i]._hWnd
            Rect  = win32gui.GetWindowRect(hwnd)
            left, top, width, height = mkPosSize(Rect)
            title = win32gui.GetWindowText(hwnd)
            wInf = WindowInf(title, hwnd, left, top, width, height)
            mkLst.append(wInf)
                
    return mkLst

def mkPosSize(Rect):
    
    left   = Rect[0]
    top    = Rect[1]
    wight  = Rect[2] - Rect[0]   #right - left
    height = Rect[3] - Rect[1]   #bottom - top
    
        
    return left, top, wight, height

#使用するアプリのリストを作成する 
def getUseLst():
    
    path   = fa.getFullPath(mp.TBL_PATH, fa.USEAPP)
    Lst = []
    
    Lst = fa.getLineLst_FromPath(path)
    
    return Lst
            
        