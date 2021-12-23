# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 09:59:54 2021

@author: raneh
"""

import tkinter as tk

import main


root = tk.Tk()


root.geometry("700x700")




button = tk.Button(root, text="Click ME", bg='White', fg='Black',
                              command=lambda:main.New_Window() )

button.pack(side='top')
root.mainloop()