import tkinter as tk
from tkinter.ttk import *

TK = tk.Tk()
TK.title("Bamboo启动器")
TK.geometry("700x200")
TK.resizable(0, 0)

value = tk.StringVar()
value.set("请选择要游玩的版本")
values = ['FreeCreate Pre-Release Version 0.072.0-Alpha', 'FreeCreate Indev Version 0.536_03']
combobox = Combobox(
        master=TK,# 父容器
        height=20,  # 高度,下拉显示的条目数量
        width=70,  # 宽度
        state='readonly',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
        cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
        font=('Arial', 20),  # 字体
        textvariable=value,  # 通过StringVar设置可改变的值
        values=values,  # 设置下拉框的选项
        )
combobox.pack(padx=10,pady=20)

'''def get():
    print(combobox.get())

b = tk.Button(TK, text="确定", command=get())
b.place(x=10,y=20,height=70,width=100)'''

tk.mainloop()
