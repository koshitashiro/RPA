import datetime
import appWindow as aw
import mngPath as mp


USEAPP      = "useApp.txt"
INITWINDOW  = "initWindow.txt"

#FullPathを取得する
def getFullPath(path, fname):
    return path + "\\" + fname

#行ごとのデータを取得する
def getLineLst(fdata):
    
    Lst  = []
    line = ""
    
    for i  in range(len(fdata)):
        if fdata[i] != "\n" and i != len(fdata)-1:
            line += fdata[i]
        else:
            if i == len(fdata)-1:
                line += fdata[i] 
            Lst.append(line)
            line = ""
    
    return Lst

#データを書き込む
def writeInitWindow(Lst):
    f = open(getFullPath(mp.TBL_PATH, INITWINDOW), "w", encoding="UTF-8")
    
    now = str(datetime.datetime.now())
    f.write("#mkInitWindowData --- " + str(now) + "\n")
    f.write("#hWnd, left, top, wight, heigth, title\n")
    
    for inf in Lst:
        f.writelines(aw.WindowInf.getInfStr(inf))
    
    f.close
    
    return
        
    