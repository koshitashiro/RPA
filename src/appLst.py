import mngPath as mp
import opFile as opf
import pygetwindow as pgw

def getDispLst():
    uLst     = []   #使用するアプリ一覧
    winInfoLst = []   #一覧表示させるリスト
    
    uLst = getAppLst()
    
    for app in uLst:
        app_window = pgw.getWindowsWithTitle(app)
        if len(app_window) != 0:
            for i in range(len(app_window)):
                jprint(app_window[i])
        
    #print(dispLst)
    return          
        
def getAppLst():
    
    path   = opf.getFullPath(mp.TBL_PATH, opf.APPLIST)
    Lst = []
    
    f    = open(path)
    fdata = f.read()
    
    Lst = opf.getLineLst(fdata)
    
    f.close()
    
    #print(Lst)
    
    return Lst
            
        