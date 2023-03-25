import os

APPLIST = "AppList.txt"


def getFullPath(path, fname):
    return path + "\\" + fname

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