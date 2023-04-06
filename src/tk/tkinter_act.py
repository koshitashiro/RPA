import tkinter as tk
from   file    import file_act as fa
from   msys    import path_glob as pg
from   tkinter import ttk
from   tksheet import Sheet
def showLst():
    
    Lst = []
    
    # Tkオブジェクトを作成し、ウィンドウを表示する
    root = tk.Tk()
    root.title('AppList')
    root.geometry("1000x400")
    
    #tksheetを作成
    sheet = Sheet(root)
    sheet.grid(row=0, column=0)
            
    sheet.headers(newheaders=["title", "hWnd", "left", "top", "width", "height"], index='row')
    sheet.set_column_widths("title", "height", 300)
    
    vLst = fa.getLineLst_FromPath(fa.getFullPath(pg.TBL_PATH, fa.WININFO))
    
    for line in vLst:
        Lst.append(mkClmn(line))
    
    sheet.set_sheet_data(Lst)
    sheet.set_
    sheet.pack()

    # イベントループを開始する
    root.mainloop()

#行を作成する
def mkClmn(line):
        
    csvLst = line.split(",")
        
    #valの数は
    if len(csvLst) != 6:
        return
        
    valLst = getValLst(csvLst)
        
    return valLst


#イコール(=)の右側のみを切り出す
def getValLst(srcLst):
    
    Lst = []
    
    for line in srcLst:
        line = fa.getRightSide(line, "=")
        Lst.append(line)
    
    return Lst