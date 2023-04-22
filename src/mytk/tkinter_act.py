import tkinter as tk
from   file    import file_act as fa
from   msys    import path_glob as pg
from   tksheet import Sheet


def showLst():
    
    Lst = []
    
    
    def on_cell_click(e):
        
        cell  = sheet.get_currently_selected()
        
        if len(cell) == 0:
            return
        
        print(sheet.data[cell[0][1]])
        
        return
        
        
    
    # Tkオブジェクトを作成し、ウィンドウを表示する
    root  = tk.Tk()
    
    #tksheetを作成
    sheet = Sheet(root, width = 850, height = 600)
    sheet.grid()
    sheet.pack(fill="both", expand=True)
    
    sheet.headers(newheaders = ["title", "hWnd", "left", "top", "width", "height"] )

    
    vLst = fa.getLineLst_FromPath(fa.getFullPath(pg.TBL_PATH, fa.WININFO))
    
    for line in vLst:
        Lst.append(mkClmn(line))
    
    sheet.set_sheet_data(Lst)
    sheet.set_column_widths([300,100,100,100,100,100])
    sheet.set_all_row_heights(height = 30)
    
    sheet.enable_bindings()
    sheet.bind_all("<Button-1>", on_cell_click)
    


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

#有効範囲を作成する
#Lst⇒[[テーブルの幅リスト][テ幅ブルの高さリスト]]
def mkVadRng(Lst):
    
    tbl_w = 0
    tbl_h = 0

    
    for cmp in Lst[0]:
        tbl_w = tbl_w + cmp
        
    for cmp in Lst[1]:
        tbl_h = tbl_h + cmp
        
        
    print(F"x={tbl_w}, y={tbl_h}")
        
    return (0, 0, tbl_h, tbl_w)


def chkValRng(Rect, x, y):
    
    return    