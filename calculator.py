from tkinter import *

mainWindow = Tk()
mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindow["padx"] = 8

topFrame = Frame(mainWindow)
topFrame.grid(row=0, column=0, sticky='nw')
entry = Entry(topFrame)
entry.grid(row=0, column=0, stick='nsew', pady=2)

buttonsFrame = Frame(mainWindow)
buttonsFrame.grid(row=1, column=0, sticky='nw')

keys = [
    [('C', 1), ('C1', 1)],
    [('7', 1), ('8', 1), ('9', 1), ('/', 1)],
    [('4', 1), ('5', 1), ('6', 1), ('x', 1)],
    [('1', 1), ('2', 1), ('3', 1), ('-', 1)],
    [('0', 1), ('=', 1), ('+', 1)],

]

row = 0
for key in keys:
    col = 0
    for value in key:
        button = Button(buttonsFrame, text=value[0], width=5, height=2)
        button.grid(row=row, column=col, columnspan=value[1], sticky=E + W)
        col += 1
    row += 1

mainWindow.update() #this method must be called inorder to customize the size of the main window
mainWindow.minsize(buttonsFrame.winfo_width() + 8, entry.winfo_height() + buttonsFrame.winfo_width())
mainWindow.maxsize(buttonsFrame.winfo_width() + 8, entry.winfo_height() + buttonsFrame.winfo_width())

mainWindow.minsize()

mainloop()