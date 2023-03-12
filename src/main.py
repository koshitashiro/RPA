import os
import AppList


global root_path
global pic_path

def main():
    getPath()
    AppList.OpenWindow()
    

def getPath():
    root_path = os.environ.get("RPA-PJ")
    pic_path  = str(root_path) + "/pic"

if __name__ == '__main__':
    main()