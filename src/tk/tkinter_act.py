import tkinter as tk
from file import file_act as fa
from msys import path_glob as pg
from   tkinter import ttk

def showLst():
    
    Lst = []
    
    column = ("hwnd", "left", "top", "width", "height", "title")
    
    # Tkオブジェクトを作成し、ウィンドウを表示する
    root = tk.Tk()
    root.title('AppList')
    root.geometry("1000x800")
    
    tree = ttk.Treeview(root, columns=column)
    
    tree.column("hwnd",   anchor="center", width=100)
    tree.column("left",   anchor="center", width=100)
    tree.column("top",    anchor="center", width=100)
    tree.column("width",  anchor="center", width=100)
    tree.column("height", anchor="center", width=100)
    tree.column("title",  anchor="center", width=300)
    
    tree.heading("hwnd",   text="hwnd",   anchor="center")
    tree.heading("left",   text="left",   anchor="center")
    tree.heading("top",    text="top",    anchor="center")
    tree.heading("width",  text="width",  anchor="center")
    tree.heading("height", text="height", anchor="center")
    tree.heading("title",  text="title",  anchor="center")
        
    Lst = fa.getLine_Path(fa.getFullPath(pg.TBL_PATH, fa.WININFO))
    print(Lst)
    for line in Lst:
        valLst = line.split(",")
        val = (valLst[0], valLst[1], valLst[2], valLst[3], valLst[4], valLst[5])
        tree.insert(parent="", index="end", values=val)
        
    tree.pack(pady=10)
            
        

    # イベントループを開始する
    root.mainloop()