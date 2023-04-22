#画面情報を作成する
#mkwininfo_act.py
#1.UseApp.txtから使用するアプリリストを受け取る
#2.現在開いている画面のうち、名前の一部がアプリリストと一致する画面の情報を取得する

import pygetwindow as pgw
import win32gui
from win.window_class import WindowInf
from file import file_act as fa
from msys import path_glob as pg


#画面情報を作成する
def mkWindowInfo():
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
            pos   = win32gui.GetWindowRect(hwnd)    #画面ハンドラ
            rect  = mkPosSize(pos)                  #画面ポジション4点
            title = win32gui.GetWindowText(hwnd)    #タイトル
            wInf = WindowInf(title, hwnd, rect)     #画面情報インスタンスの作成
            mkLst.append(wInf)
                
    return mkLst

def mkPosSize(pos):
    
    return (pos[0], pos[1], pos[2] - pos[0], pos[3] - pos[1])


#使用するアプリのリストを作成する 
def getUseLst():
    
    path   = fa.getFullPath(pg.TBL_PATH, fa.USEAPP)
    Lst = []
    
    Lst = fa.getLineLst_FromPath(path)
    
    
    return Lst
            
        