import os
from tkinter import *
import tkinter.filedialog
from tkinter.filedialog import *

#TO-DO LIST
#1. CAN WRITE/EDIT TEXT
#2. CAN SAVE INTO .TXT FILE
#3. CAN SEARCH FOR WORDS

root = Tk()
root.title("Text Editor")
root.geometry("400x400")
currentFile = " "

#MENU BAR
def createFile():
    clearText()
    renameFileNameLabel("Untitled")
    filemenu.entryconfigure(2,state=DISABLED)

def saveNewFile():
    global currentFile
    savelocation = tkinter.filedialog.asksaveasfilename(title = "Select file",filetypes = (("text file","*.txt"),("all files","*.*")))
    if ".txt" not in savelocation:
        savelocation+=".txt"
    file1 = open(savelocation, "w+")
    file1.write(text.get("1.0", "end-1c"))
    file1.close()
    renameFileNameLabel(os.path.basename(os.path.basename(savelocation)))
    filemenu.entryconfigure(2,state=ACTIVE)
    currentFile = savelocation
    os.chdir(r'{}'.format(os.path.dirname(savelocation)))

def openFile():
    global currentFile
    selectedFile = tkinter.filedialog.askopenfilename(title = "Select file",filetypes = ((".txt files","*.txt"),("all files","*.*")))
    selectedFile = open(selectedFile,"r")
    renameFileNameLabel(os.path.basename(selectedFile.name))
    clearText()
    text.insert(END,selectedFile.read())
    filemenu.entryconfigure(2,state=ACTIVE)
    os.chdir(r'{}'.format(os.path.dirname(selectedFile.name)))
    currentFile = os.getcwd()+"\\"+os.path.basename(selectedFile.name)

def saveFile():
    file1 = open(currentFile, "w+")
    file1.write(text.get("1.0", "end-1c"))
    file1.close()

def clearText():
    text.delete(1.0,END)

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=createFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile, state=DISABLED)
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
editmenu.add_command(label="Clear", command=clearText)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

#INDIVIDUAL .TXT FILE NAME LABEL
fileNameLabel = Label(root,text="Untitled",background="white")
fileNameLabel.pack(side=TOP,fill=X)

def renameFileNameLabel(val):
    fileNameLabel.configure(text=val)

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