# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 13:11:05 2021

@author: Lenovo
"""

import tkinter as tk
from tkinter import messagebox
from string import ascii_uppercase
import random
import sys
import os

def New_window():
    window = tk.Toplevel()
    window.title("CowinMan")
    window.geometry("700x700")
    word_list= ['VIRUS','MASK','REOPNEN','PATIENT','DISEASE','RECOVER','MEDICINE','IMPACT',
            'TEST','SYMPTOM','CRISIS','HEALTH','REOPEN']


    label0=tk.Label(window,text=" COWINMAN!!  LET THE GAME BEGIN!",font=('Helvatica 10 bold '),fg="blue")
    #canvas.create_window(150, 50, window=label0)
    Keypad=tk.Label(window,bg="pink",width=100,height=500).place(x=390,y=250)
    man=tk.Label(window,bg="grey",width=40,height=300).place(x=50,y=100)




    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        numberOfGuesses =0 

        the_word=random.choice(word_list)
        the_word_withSpaces = " ".join(the_word)
        lblWord.set(' '.join("_"*len(the_word)))

    def guess(letter):
    	global numberOfGuesses
    	if numberOfGuesses<11:	
    		txt = list(the_word_withSpaces)
    		guessed = list(lblWord.get())
    		if the_word_withSpaces.count(letter)>0:
    			for c in range(len(txt)):
    				if txt[c]==letter:
    					guessed[c]=letter
    				lblWord.set("".join(guessed))
    				if lblWord.get()==the_word_withSpaces:
    					messagebox.showinfo("Hangman","You guessed it!")
    		else:
    			numberOfGuesses += 1

    			if numberOfGuesses==6:
    					messagebox.showwarning("Hangman","Game Over")
                        
    def restart_program():
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        python = sys.executable
        os.execl(python, python, * sys.argv)                    






    lblWord = tk.StringVar()
    tk.Label(window, textvariable  =lblWord,fg="black",height=5,width=30).place(x=400,y=100)
    tk.Button(window,text="A",font=('Helvatica 10 bold '),command=lambda: guess("A"),bg="white",fg="black",height="3",width="4").place(x=400,y=300)

    tk.Button(window,text="B",font=('Helvatica 10 bold '),command=lambda: guess("B"),bg="white",fg="black",height="3",width="4").place(x=450,y=300)

    tk.Button(window,text="C",font=('Helvatica 10 bold '),command=lambda: guess("C"),bg="white",fg="black",height="3",width="4").place(x=500,y=300)


    tk.Button(window,text="D",font=('Helvatica 10 bold '),command=lambda: guess("D"),bg="white",fg="black",height="3",width="4").place(x=550,y=300)

    tk.Button(window,text="E",font=('Helvatica 10 bold '),command=lambda: guess("E"),bg="white",fg="black",height="3",width="4").place(x=600,y=300)
    tk.Button(window,text="F",font=('Helvatica 10 bold '),command=lambda: guess("F"),bg="white",fg="black",height="3",width="4").place(x=400,y=375)
    tk.Button(window,text="G",font=('Helvatica 10 bold '),command=lambda: guess("G"),bg="white",fg="black",height="3",width="4").place(x=450,y=375)
    tk.Button(window,text="H",font=('Helvatica 10 bold '),command=lambda: guess("H"),bg="white",fg="black",height="3",width="4").place(x=500,y=375)
    tk.Button(window,text="I",font=('Helvatica 10 bold '),command=lambda: guess("I"),bg="white",fg="black",height="3",width="4").place(x=550,y=375)



    tk.Button(window,text="J",font=('Helvatica 10 bold '),command=lambda: guess("J"),bg="white",fg="black",height="3",width="4").place(x=600,y=375)
    tk.Button(window,text="K",font=('Helvatica 10 bold '),command=lambda: guess("K"),bg="white",fg="black",height="3",width="4").place(x=400,y=450)
    tk.Button(window,text="L",font=('Helvatica 10 bold '),command=lambda: guess("L"),bg="white",fg="black",height="3",width="4").place(x=450,y=450)
    tk.Button(window,text="M",font=('Helvatica 10 bold '),command=lambda: guess("M"),bg="white",fg="black",height="3",width="4").place(x=500,y=450)
    tk.Button(window,text="N",font=('Helvatica 10 bold '),command=lambda: guess("N"),bg="white",fg="black",height="3",width="4").place(x=550,y=450)


    tk.Button(window,text="O",font=('Helvatica 10 bold '),command=lambda: guess("O"),bg="white",fg="black",height="3",width="4").place(x=600,y=450)
    tk.Button(window,text="P",font=('Helvatica 10 bold '),command=lambda: guess("P"),bg="white",fg="black",height="3",width="4").place(x=400,y=525)
    tk.Button(window,text="Q",font=('Helvatica 10 bold '),command=lambda: guess("Q"),bg="white",fg="black",height="3",width="4").place(x=450,y=525)
    tk.Button(window,text="R",font=('Helvatica 10 bold '),command=lambda: guess("R"),bg="white",fg="black",height="3",width="4").place(x=500,y=525)
    tk.Button(window,text="S",font=('Helvatica 10 bold '),command=lambda: guess("S"),bg="white",fg="black",height="3",width="4").place(x=550,y=525)

    tk.Button(window,text="T",font=('Helvatica 10 bold '),command=lambda: guess("T"),bg="white",fg="black",height="3",width="4").place(x=600,y=525)
    tk.Button(window,text="U",font=('Helvatica 10 bold '),command=lambda: guess("U"),bg="white",fg="black",height="3",width="4").place(x=400,y=600)
    tk.Button(window,text="V",font=('Helvatica 10 bold '),command=lambda: guess("V"),bg="white",fg="black",height="3",width="4").place(x=450,y=600)
    tk.Button(window,text="W",font=('Helvatica 10 bold '),command=lambda: guess("W"),bg="white",fg="black",height="3",width="4").place(x=500,y=600)
    tk.Button(window,text="X",font=('Helvatica 10 bold '),command=lambda: guess("X"),bg="white",fg="black",height="3",width="4").place(x=550,y=600)
    tk.Button(window,text="Y",font=('Helvatica 10 bold '),command=lambda: guess("Y"),bg="white",fg="black",height="3",width="4").place(x=600,y=600)
    tk.Button(window,text="Z",font=('Helvatica 10 bold '),command=lambda: guess("Z"),bg="white",fg="black",height="3",width="4").place(x=650,y=600)
    #n=0
    #for c in ascii_uppercase:
        #tk.Button(window, text=c, command=lambda c=c: guess(c), font=('Helvetica 18'),bg="white",fg="black",width=30,height=5).grid(row=1+n//9,column=n%9)
        #n+=1
    tk.Button(window,text="RESTART",font=('Helvatica 7 bold '),bg="white",fg="red",height="4",width="4", command=restart_program).place(x=650,y=525)    

    tk.Button(window, text="Change\nWord",height="4",width="6", command=lambda:newGame(), font=("Helvetica 10 bold")).place(x=650,y=300)
    
    

    newGame()