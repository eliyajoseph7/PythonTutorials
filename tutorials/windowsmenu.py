from tkinter import *
import os

root = Tk()
root.geometry('640x480-8-200')
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu) # creating a File menu
menu.add_cascade(label="File", menu=filemenu)

# creating sub-menus in the filemenu
filemenu.add_command(label="New File")
filemenu.add_command(label="Open Recent")
filemenu.add_command(label="save as")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)


helpmenu = Menu(menu) # creating a help menu
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Troubleshoot")
helpmenu.add_command(label="About")

filelist = Listbox(root)
filelist.grid(row=0, column=0)
filelist.config(border=2, relief='sunken')


scrollbar = Scrollbar(root, orient=VERTICAL, command=filelist.yview)
scrollbar.grid(row=0, column=2, sticky="nsw", columnspan=2)
filelist['yscrollcommand'] = scrollbar.set

for zone in os.listdir('D:/postgresql/bin'):
    filelist.insert(END, zone)




mainloop()

