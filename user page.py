import tkinter as tk

from main import New_Window


root = tk.Tk()

root.configure(bg='yellow')
root.geometry("600x300")

label = tk.Label( root)
label.place(x=0, y=0)
L1=tk.Label(root,text="Enter Name",font=('Helvatica 10 bold ')).pack(anchor=tk.CENTER)
E1=tk.Entry(root,bd=5,width=20)
E1.pack(anchor=tk.CENTER)


button = tk.Button(root, text="START", bg='White', fg='Black',
                              command=lambda:New_Window() )

button.pack(side='top')
root.mainloop()