# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 10:04:45 2021

@author: raneh
"""
import sys
import os
from tkinter import Tk, Label, Button
import tkinter as tk

def New_Window():
    
    Window = tk.Toplevel()
    Window.title("COWINMAN")
    Window.geometry("700x700")
    canvas = tk.Canvas(Window, height=300, width=200)
    canvas.pack()
   
    
    label0=tk.Label(Window,text=" COWINMAN!!  LET THE GAME BEGIN!",font=('Helvatica 10 bold '),fg="blue")
    canvas.create_window(150, 50, window=label0)
    Keypad=tk.Label(Window,bg="pink",width=100,height=500).place(x=390,y=250)
    man=tk.Label(Window,bg="grey",width=40,height=300).place(x=50,y=100)
    canvas.create_window(0, 10, window=man)
    def alphabet_enter(item):
        sr_al=item
        
    word_list= ['VIRUS','SANITIZER','MASK','PANDEMIC','OUTBREAK','REOPNEN','LOCKDOWN','PATIENT','DISEASE','RECOVER','MEDICINE','IMPACT','ANTIBODY',
            'ISOLATION','OUTBREAK','TEST','RECOVER','ANTIBODY','SYMPTOM','CRISIS','APPOINTMENT','HEALTH','REOPEN']
    
    

    def restart_program():
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        python = sys.executable
        os.execl(python, python, * sys.argv)




   # Button(Window, text="Restart", command=restart_program).pack()

  
    

    a=tk.Button(Window,text="A",font=('Helvatica 10 bold '),command=alphabet_enter("a"),bg="white",fg="black",height="3",width="4").place(x=400,y=300)

    b=tk.Button(Window,text="B",font=('Helvatica 10 bold '),command=alphabet_enter("b"),bg="white",fg="black",height="3",width="4").place(x=450,y=300)

    C=tk.Button(Window,text="C",font=('Helvatica 10 bold '),command=alphabet_enter("C"),bg="white",fg="black",height="3",width="4").place(x=500,y=300)


    D=tk.Button(Window,text="D",font=('Helvatica 10 bold '),command=alphabet_enter("d"),bg="white",fg="black",height="3",width="4").place(x=550,y=300)

    E=tk.Button(Window,text="E",font=('Helvatica 10 bold '),command=alphabet_enter("e"),bg="white",fg="black",height="3",width="4").place(x=600,y=300)
    F=tk.Button(Window,text="F",font=('Helvatica 10 bold '),command=alphabet_enter("f"),bg="white",fg="black",height="3",width="4").place(x=400,y=375)
    G=tk.Button(Window,text="G",font=('Helvatica 10 bold '),command=alphabet_enter("g"),bg="white",fg="black",height="3",width="4").place(x=450,y=375)
    H=tk.Button(Window,text="H",font=('Helvatica 10 bold '),command=alphabet_enter("h"),bg="white",fg="black",height="3",width="4").place(x=500,y=375)
    I=tk.Button(Window,text="E",font=('Helvatica 10 bold '),command=alphabet_enter("i"),bg="white",fg="black",height="3",width="4").place(x=550,y=375)



    J=tk.Button(Window,text="J",font=('Helvatica 10 bold '),command=alphabet_enter("j"),bg="white",fg="black",height="3",width="4").place(x=600,y=375)
    K=tk.Button(Window,text="K",font=('Helvatica 10 bold '),command=alphabet_enter("k"),bg="white",fg="black",height="3",width="4").place(x=400,y=450)
    L=tk.Button(Window,text="L",font=('Helvatica 10 bold '),command=alphabet_enter("l"),bg="white",fg="black",height="3",width="4").place(x=450,y=450)
    M=tk.Button(Window,text="M",font=('Helvatica 10 bold '),command=alphabet_enter("m"),bg="white",fg="black",height="3",width="4").place(x=500,y=450)
    N=tk.Button(Window,text="N",font=('Helvatica 10 bold '),command=alphabet_enter("n"),bg="white",fg="black",height="3",width="4").place(x=550,y=450)


    O=tk.Button(Window,text="O",font=('Helvatica 10 bold '),command=alphabet_enter("o"),bg="white",fg="black",height="3",width="4").place(x=600,y=450)
    P=tk.Button(Window,text="P",font=('Helvatica 10 bold '),command=alphabet_enter("p"),bg="white",fg="black",height="3",width="4").place(x=400,y=525)
    Q=tk.Button(Window,text="Q",font=('Helvatica 10 bold '),command=alphabet_enter("q"),bg="white",fg="black",height="3",width="4").place(x=450,y=525)
    R=tk.Button(Window,text="R",font=('Helvatica 10 bold '),command=alphabet_enter("r"),bg="white",fg="black",height="3",width="4").place(x=500,y=525)
    S=tk.Button(Window,text="S",font=('Helvatica 10 bold '),command=alphabet_enter("s"),bg="white",fg="black",height="3",width="4").place(x=550,y=525)

    T=tk.Button(Window,text="T",font=('Helvatica 10 bold '),command=alphabet_enter("t"),bg="white",fg="black",height="3",width="4").place(x=600,y=525)
    U=tk.Button(Window,text="U",font=('Helvatica 10 bold '),command=alphabet_enter("u"),bg="white",fg="black",height="3",width="4").place(x=400,y=600)
    V=tk.Button(Window,text="V",font=('Helvatica 10 bold '),command=alphabet_enter("v"),bg="white",fg="black",height="3",width="4").place(x=450,y=600)
    W=tk.Button(Window,text="W",font=('Helvatica 10 bold '),command=alphabet_enter("w"),bg="white",fg="black",height="3",width="4").place(x=500,y=600)
    X=tk.Button(Window,text="X",font=('Helvatica 10 bold '),command=alphabet_enter("x"),bg="white",fg="black",height="3",width="4").place(x=550,y=600)
    Y=tk.Button(Window,text="Y",font=('Helvatica 10 bold '),command=alphabet_enter("y"),bg="white",fg="black",height="3",width="4").place(x=600,y=600)
    Z=tk.Button(Window,text="Z",font=('Helvatica 10 bold '),command=alphabet_enter("z"),bg="white",fg="black",height="3",width="4").place(x=650,y=600)
    RESTART=tk.Button(Window,text="RESTART",font=('Helvatica 7 bold '),bg="white",fg="red",height="3",width="4",command=restart_program()).place(x=650,y=525)
