from tksheet import Sheet
import tkinter as tk

class sht(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        #self.grid_columnconfigure(0, weight = 1)
        #self.grid_rowconfigure(1, weight = 1)
        
        self.sheet_ini = Sheet(self, height = 400, width  = 900 )
        self.sheet_ini.enable_bindings((
            "single_select",
            "drag_select",
            "column_drag_and_drop",
            "row_drag_and_drop",
            "column_width_resize",
            "rc_insert_column",
            "rc_delete_column",
            "rc_insert_row",
            "rc_delete_row",
            "cut",
            "paste",
            "undo",
            "edit_cell"
        ))
        
        self.sheet_ini.grid(row = 0, column = 0, sticky = "nswe")
        self.sheet_ini.highlight_cells(row = 5, column = 5, bg = "#ed4337", fg = "white")
        self.sheet_ini.highlight_cells(row = 5, column = 1, bg = "#ed4337", fg = "white")
        self.sheet_ini.highlight_cells(row = 5, bg = "#ed4337", fg = "white", canvas = "row_index")
        self.sheet_ini.highlight_cells(column = 0, bg = "#ed4337", fg = "white", canvas = "header")
    
    def set_sheet_data(self, Lst):
        return self.sheet_ini.set_sheet_data(Lst)
        
        
    def set_column_widths(self, Lst):
        self.sheet_ini.set_column_widths(Lst)
        return
        
    def set_all_row_heights(self, dat):
        return self.sheet_ini.set_all_row_heights(height = dat)
        
    
    def headers(self, Lst, row):
        return self.sheet_ini.headers(newheaders = Lst, index = row)
        
        
app = sht()
app.mainloop()