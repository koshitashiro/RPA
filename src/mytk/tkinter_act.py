#tkinterを操作する
#tkinter_act.py
#テーブルを作成し、WinInfo.txtに記載されている画面情報を表示する
#header["title", "hWnd", "left", "top", "width", "height"]
#任意の画面情報をクリックすると、クリックイベントが発生する

import tkinter as tk
from   win     import winctrl   as wc
from   file    import file_act  as fa
from   msys    import path_glob as pg
from   tksheet import Sheet


HeadLst = ["title", "hWnd", "left", "top", "width", "height"]

def showLst():
    
    Lst = []
    
    #テーブルクリック時のイベント
    #e:イベント
    def on_cell_click(e):
        
        cell  = sheet.get_currently_selected()
        
        if len(cell) == 0:
            return
        
        clmdat = sheet.data[cell[0]] 
        title  = clmdat[HeadLst.index("title")]
        hwnd   = int(clmdat[HeadLst.index("hWnd")])
        
        wc.testpgui(hwnd, title)
        return
        
        
    
    # Tkオブジェクトを作成する
    root  = tk.Tk()
    
    #tksheetを作成
    sheet = Sheet(root, width = 850, height = 600)
    sheet.grid()
    sheet.pack(fill="both", expand=True)
    
    sheet.headers(newheaders = HeadLst )
    vLst = fa.getLineLst_FromPath(fa.getFullPath(pg.TBL_PATH, fa.WININFO))
    
    for line in vLst:
        line = line.strip("\n")
        Lst.append(mkClmn(line))
    
    #シートを作成する
    sheet.set_sheet_data(Lst)
    sheet.set_column_widths([300,100,100,100,100,100])
    sheet.set_all_row_heights(height = 30)
    
    #バインドを有効化する
    sheet.enable_bindings()
    
    #バインドには何種類かある..これがベストだとは思わないが今回はこれで良しとする
    sheet.bind_all("<Button-1>", on_cell_click)
    


    root.mainloop()
        

#行データを作成する
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

#テーブルの情報を取得する
def getTblInfo(str):
    return

#クリックイベントからタイトルを取得する
def get_title(imp):
    
    dat = imp
    # Lst = ["\'", "[", "]"]
    
    # for elm in Lst:
    #     dat.strip(elm)
    
    # dLst   = dat.split(",")
    title = imp[0]
    
    return title

#クリックイベントからハンドル情報を取得する
def get_handle(imp):
    
    dat = imp
    # Lst = ["\'", "[", "]"]
    
    # for elm in Lst:
    #     dat.strip(elm)
    
    # dLst   = dat.split(",")
    hwnd  = imp[1]
    
    return hwnd

