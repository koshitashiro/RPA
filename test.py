import tkinter as tk
import tksheet

def test():

    dic = {}

    def pr(e):
        selected_cell = sheet.get_currently_selected()
        item = dic[selected_cell]
        print(item)

    rt = tk.Tk()
    rt.title('test')
    rt.geometry("1800x1000")

    frm_a = tk.Frame(rt)
    frm_a.pack()

    title_list = ['title' + str(x) for x in range(8)]
    content_list = [['cell_' + '行' + str(j) + '_列_' + str(i) for i in range(10)] for j in range(300)]

    sheet = tksheet.Sheet(frm_a,
                       width=1200,
                       height=900,
                       header_align='center',
                       headers=title_list,  # タイトル
                       data=content_list,  # テーブルのデータ
                       show_row_index=False)  # 行番号を非表示

    for row in range(len(content_list)):
        for column in range(len(title_list)):
            cell_key = (row, column)
            dic[cell_key] = ''

    sheet.bind("<1>", pr)
    sheet.pack()

    print(dic)

    rt.mainloop()
