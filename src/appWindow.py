
class appWindow:
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
        