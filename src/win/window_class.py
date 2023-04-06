
class WindowInf:
    
    rect = (0, 0, 0, 0)
    
    def __init__(self, title, hWnd, rect):
        
        self.title = title
        self.hWnd  = hWnd
        self.rect  = rect 
        
        return
    
    def getInfLst(self):
        Lst = []
        
        Lst.append(self.title)
        Lst.append(self.hWnd)
        Lst.append(self.rect)    
        
        return Lst
    
    #カンマで繋がった情報の文字列を取得する
    def getInfStr(self):
        
        dat = "title=" + str(self.title) + ", hwnd=" + str(self.hWnd) + ", " + self.getRect_Str()
        return dat
        
    def getRect_Str(self):
        return "left={}, top={}, width={}, height={}".format(self.rect[0], self.rect[1], self.rect[2], self.rect[3])