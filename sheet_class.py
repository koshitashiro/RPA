from tkinter import Frame
from tksheet import Sheet

class MySht(Frame):
    def __init__(self, master, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.sheet = Sheet(self)
        self.sheet.pack(fill="both", expand=True)