
class WindowInf:
    
    
    def __init__(self, hWnd, left, top, width, height, title):
        self.hWnd   = hWnd
        self.left   = left
        self.top    = top
        self.width  = width
        self.height = height
        self.title  = title
        
        return
    
    def getInfLst(self):
        Lst = []
        
        Lst.append(self.hWnd)
        Lst.append(self.left)
        Lst.append(self.top)
        Lst.append(self.width)
        Lst.append(self.height)
        Lst.append(self.title)
        
        return Lst
    
    #カンマで繋がった情報の文字列を取得する
    def getInfStr(self):
        
        Str = "hwnd=" + str(self.hWnd) + ", left=" + str(self.left) + ", top=" + str(self.top) + ", width=" + str(self.width) + ", height=" + str(self.height) + ", title=" + self.title
        return Str
        
    
    def showEnt(self):
        print("hwnd=" + str(self.hWnd) + ", left=" + str(self.left) + ", top=" + str(self.top) + 
              ", width=" + str(self.width) + ", height=" + str(self.height) + 
              ", title=" + self.title)
        
        return
    
    
    
class WindowSet:
    #Lstは一つしか存在しない　シングルトンクラスの方が良いか？
    Lst = []
    
    def __init__(self, Lst):
        self.Lst = Lst
        return
    
    def appendLst(self, WindowInf):
        self.Lst.append(WindowInf)
        return
    
    def shoEnt(self):
        print(self.Lst)
        return
    