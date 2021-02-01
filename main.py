from tkinter import *
import tkinter.filedialog
from tkinter.filedialog import askopenfilename
import os

#TO-DO LIST
#1. CAN WRITE/EDIT TEXT
#2. CAN SAVE INTO .TXT FILE
#3. CAN SEARCH FOR WORDS

root = Tk()
root.title("Text Editor")
root.geometry("400x400")

#MENU BAR
def saveNewFile():
    savelocation = tkinter.filedialog.asksaveasfilename(title = "Select file",filetypes = (("text file","*.txt"),("all files","*.*")))
    if ".txt" not in savelocation:
        savelocation+=".txt"
    file1=open(savelocation, "w+")
    file1.write(text.get("1.0", "end-1c"))
    file1.close()

def openFile():
    selectedFile = tkinter.filedialog.askopenfilename(title = "Select file",filetypes = ((".txt files","*.txt"),("all files","*.*")))
    selectedFile = open(selectedFile,"r")
    print(selectedFile.read())

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=saveNewFile)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)


#HORIZONTAL AND VERTICAL SCROLLBARS
vScrollbar = Scrollbar(root)
vScrollbar.pack(side=RIGHT,fill=Y)
hScrollbar = Scrollbar(root,orient=HORIZONTAL)
hScrollbar.pack(side=BOTTOM,fill=X)

#TEXT WIDGET TO ALLOW TEXT INPUTS AND EDITS
#NOTES
#yscrollcommand/xscrollcommand: allows horizontal/vertical scrolling

#wrap:  in DEFAULT, if written text exceeds the width of container then it will continue
#       the text in a new line 
#       (NONE continues the text in the same line)

#fill:  Determines whether widget fills any extra space 
#       allocated to it by the packer, or keeps its own minimal dimensions: 
#       NONE (default), X (fill only horizontally), 
#       Y (fill only vertically), or BOTH (fill both horizontally and vertically)

#expand:   When set to true, widget expands to fill any space not otherwise used in widget's parent 
text = Text(root,wrap=NONE,yscrollcommand=vScrollbar.set,xscrollcommand=hScrollbar.set)
text.pack(fill=BOTH,expand=True)

#yview/xview is specified so that the scrollbar can either scroll vertically/horizontally
vScrollbar.config(command=text.yview)
hScrollbar.config(command=text.xview)

root.mainloop()