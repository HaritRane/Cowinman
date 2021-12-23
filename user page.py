# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 09:59:54 2021

@author: raneh
"""

import tkinter as tk

from main import New_Window


root = tk.Tk()

root.configure(bg='yellow')
root.geometry("600x300")
img = tk.PhotoImage(file=r'C:\Users\raneh\Downloads\backhang.png')
label = tk.Label( root, image=img)
label.place(x=0, y=0)
L1=tk.Label(root,text="Enter Name",font=('Helvatica 10 bold ')).pack(anchor=tk.CENTER)
E1=tk.Entry(root,bd=5,width=20)
E1.pack(anchor=tk.CENTER)


button = tk.Button(root, text="START", bg='White', fg='Black',
                              command=lambda:New_Window() )

button.pack(side='top')
root.mainloop()
