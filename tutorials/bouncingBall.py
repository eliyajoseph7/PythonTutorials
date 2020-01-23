from tkinter import *
import time
import random

root = Tk()
root.title("Bouncing ball")
root.resizable(0, 0)
root.geometry("500x570")
root.wm_attributes("-topmost", 1)
canvas = Canvas(root, width=500, height=500, bd=0, bg="Black", highlightbackground="Red", highlightthickness=0)
canvas.pack(padx=10, pady=10)
score = Label(width=50, height=80, text="Score:   00", font="Consolas 14 bold")
score.pack(side="left")
root.update()



root.mainloop()
