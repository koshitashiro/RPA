import tkinter as tk
from   appWindow import WindowInf, WindowSet

def showLst():
    # Tkオブジェクトを作成し、ウィンドウを表示する
    root = tk.Tk()
    root.title('Listbox Demo')

    # Listboxオブジェクトを作成し、ウィンドウ上に表示する
    listbox = tk.Listbox(root)
    listbox.pack()
    
    print(WindowSet.Lst)
    for item in WindowSet.Lst:
        for txt in item:
            print(type(txt))
            listbox.insert(tk.END, txt)

    # イベントループを開始する
    root.mainloop()