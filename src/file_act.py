import datetime
import window_class as wc
import mngPath as mp


USEAPP  = "UseApp.txt"
WININFO = "WinInfo.txt"

#FullPathを取得する
def getFullPath(path, fname):
    return path + "\\" + fname

#パスからファイルを開き行ごとのデータを取得する
def getLine_Path(path):
    
    f    = open(path, "r", encoding="UTF-8")
    fdata = f.read()
    
    Lst = getLine_data(fdata)
    
    f.close()
    
    return Lst

#データから行ごとのデータを取得する
def getLine_data(fdata):
    
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
def writeWinInfo(Lst):
    f = open(getFullPath(mp.TBL_PATH, WININFO), "w", encoding="UTF-8")
    
    now = str(datetime.datetime.now())
    f.write("#WININFO --- " + str(now) + "\n")
    f.write("#hWnd, left, top, wight, heigth, title\n")
    
    for inf in Lst:
        f.write(wc.WindowInf.getInfStr(inf) + "\n")
    
    f.close
    
    return

    