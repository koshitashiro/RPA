#画面情報クラス
#title : タイトル  (str) 
#hWnd  : ハンドル  (int) 
#rest  : 画面位置  (int x,int y, int width, int height)

class WindowInf:
    
    rect = (0, 0, 0, 0)
    
    def __init__(self, app, title, hWnd, rect):
        
        self.app   = app
        self.title = title
        self.hWnd  = hWnd
        self.rect  = rect 
        
        return
    
    
    #画面情報をリストとして取得する
    def getInfLst(self):
        Lst = []
        
        Lst.append(self.app)
        Lst.append(self.title)
        Lst.append(self.hWnd)
        Lst.append(self.rect)    
        
        return Lst
    
    #カンマで繋がった情報の文字列を取得する
    def getInfStr(self):
        
        dat = "app= " + str(self.app) + ", title=" + str(self.title) + ", hwnd=" + str(self.hWnd) + ", " + self.getRect_Str()
        return dat
    
    #画面位置情報のみを取得する
    #(int x,int y, int width, int height)
    def getRect_Str(self):
        return "left={}, top={}, width={}, height={}".format(self.rect[0], self.rect[1], self.rect[2], self.rect[3])
    
    #ハンドルを取得する
    def gethWnd(self):
        return self.hWnd