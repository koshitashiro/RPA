#tkinterを操作する
#tkinter_act.py
#テーブルを作成し、WinInfo.txtに記載されている画面情報を表示する
#header["title", "hWnd", "left", "top", "width", "height"]
#任意の画面情報をクリックすると、クリックイベントが発生する

import sys
import tkinter as tk
from   win      import winctrl   as wc
from   file     import file_act  as fa
from   mysys    import path_glob as pg
from   tksheet  import Sheet


HeadLst = ["App", "title", "hWnd", "left", "top", "width", "height"]

def show_WinInfo():
    
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
    
    sheet = Sheet(root, width = 1050, height = 400)
    sheet.grid()
    sheet.pack(fill="both", expand=True)
    sheet.headers(newheaders = HeadLst)
    
    #テーブルデータの作成
    Lst = mkTblData()
    
    #シートを作成する
    sheet.set_sheet_data(Lst)
    sheet.set_column_widths([200,300,100,100,100,100,100])
    sheet.set_all_row_heights(height = 30)
    
    #バインドを有効化する
    sheet.enable_bindings()
    
    #バインドには何種類かある..これがベストだとは思わないが今回はこれで良しとする
    sheet.bind_all("<Button-1>", on_cell_click)
    root.mainloop()
    
    return

#テーブルデータを作成する
def mkTblData():
    Lst = []

    vLst = fa.getLineLst_FromPath(fa.getFullPath(pg.TBL_PATH, fa.WININFO))
    fa.getRect_FromWinInfo()
    
    for line in vLst:
        #テーブルのデータ数が7つでなければ終了
        cmpLst = fa.mkClmn(line)
        if len(cmpLst) != 7:
            sys.exit()
            
        Lst.append(cmpLst)
    
    return Lst
