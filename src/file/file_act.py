import datetime
from win.window_class import WindowInf as winf
from msys import path_glob as pg


USEAPP  = "UseApp.txt"
WININFO = "WinInfo.txt"


#FullPathを取得する
def getFullPath(path, fname):
    return path + "\\" + fname

#パスからファイルを開き、行ごとのデータをリストとして取得する
def getLineLst_FromPath(path):
    
    f    = open(path, "r", encoding="UTF-8")
    fdata = f.read()
    
    Lst = getLineLst_FromData(fdata)
    
    f.close()
    
    return Lst

#データから行ごとのデータをリストとして取得する
def getLineLst_FromData(fdata):
    
    Lst  = []
    line = ""
    
    for i  in range(len(fdata)):
        if fdata[i] != "\n" and i != len(fdata)-1:
            line += fdata[i]
        else:
            if i == len(fdata)-1:
                line += fdata[i]
                
            if chkRemLine(line) == True:
                line = ""
                continue 
            
            remEmpty(line)
            Lst.append(line)
            line = ""
    
    return Lst

#削除する行である
def chkRemLine(line):
    
    Lst = ["\n", "#"]
    
    for cmp in Lst:
        if line[0] == cmp:
            return True
        
    return False

#文字列内のスペースを消す
def remEmpty(line):
    
    Lst = [" ", "　", "\t"]
    
    for emp in Lst:
        line.strip(emp)
        
    return line

#文字の右側を取得する
def getRightSide(line, cmp):

    pos1 = line.find(cmp)
    pos2 = len(line)
    
    return(line[(pos1+1):pos2])
    
    
#ファイルを開き、行ごとの文字列を取得する
def getLine_FromPath(path):
    
    f    = open(path, "r", encoding="UTF-8")
    fdata = f.read()
    
    for line in f:
        print(line)
    
    f.close()
    
    return

#データを書き込む
def writeWinInfo(Lst):
    f = open(getFullPath(pg.TBL_PATH, WININFO), "w", encoding="UTF-8")
    
    now = str(datetime.datetime.now())
    f.write("#WININFO --- " + str(now) + "\n")
    f.write("#title, hWnd, left, top, wight, heigth\n")
    
    for inf in Lst:
        f.write(winf.getInfStr(inf) + "\n")
    
    f.close
    
    return

    