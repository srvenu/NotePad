from tkinter import *
import tkinter.messagebox as tmsg

#functions
def new():
    pass
def newWin():
    pass
def save():
    pass
def saveas():
    pass
def pagesetup():
    pass
def print1():
    pass

def cut():
    textbox.event_generate(("<<Cut>>"))

def copy():
    textbox.event_generate(("<<Copy>>"))

def paste():
    textbox.event_generate(("<<Paste>>"))

def help():
    pass

def about():
    tmsg.showinfo("About HandBook","This HandBook was developed by Venu SR on 14th Nov 2023 using Tkinter")


root= Tk()
#icon and Title
root.title("New Alpha - HandBook ")
root.wm_iconbitmap('fileimg.ico')

# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
# print(f'{width}x{height}')
# Button(text="Close",command=root.destroy).pack()


#default open size 
root.geometry("655x755")

#statusbar
statusvar = StringVar()
statusvar.set('HandBook version-1.0')
sbar = Label(root, textvariable=statusvar,relief=SUNKEN,anchor=W)
sbar.pack(side=BOTTOM,fill=X)

#text area and scrollbar

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
textbox=Text(root,font='lucida 12',yscrollcommand=scrollbar.set)
file = None
textbox.pack(fill=BOTH,expand=True)
scrollbar.config(command=textbox.yview)


mainmenu= Menu(root)
#file
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label='New',command=new)
m1.add_command(label='New Window',command=newWin)
m1.add_command(label='Open..',command=open)
m1.add_command(label='Save',command=save)
m1.add_command(label='Save As..',command=saveas)
m1.add_separator()
m1.add_command(label='Page Setup',command=pagesetup)
m1.add_command(label='Print',command=print1)
m1.add_separator()
m1.add_command(label='Exit',command=quit)
mainmenu.add_cascade(label="File",menu=m1)

#edit
m2=Menu(mainmenu,tearoff=0)
m2.add_command(label='Undo',command=new)
m2.add_command(label='Redo',command=newWin)
m2.add_separator()
m2.add_command(label='Cut',command=cut)
m2.add_command(label='Copy',command=copy)
m2.add_command(label='Paste',command=paste)
m2.add_command(label='Delete',command=saveas)
m2.add_separator()
m2.add_command(label='Find',command=pagesetup)
m2.add_command(label='Replace',command=print1)
m2.add_separator()
m2.add_command(label='Select all',command=print1)
mainmenu.add_cascade(label="Edit",menu=m2)

#Format
m3=Menu(mainmenu,tearoff=0)
m3.add_command(label='Word wrap',command=newWin)
m3.add_command(label='Font..',command=print1)
mainmenu.add_cascade(label="Format",menu=m3)

#view
m4=Menu(mainmenu,tearoff=0)
sm4=Menu(m4,tearoff=0)
m4.add_cascade(label='Zoom',menu=sm4)
sm4.add_cascade(label='Zoom In',command=print1)
sm4.add_cascade(label='Zoom Out',command=print1)
sm4.add_cascade(label='Restore Default Zoom',command=print1)
m4.add_checkbutton(label='Status Bar')
mainmenu.add_cascade(label="View",menu=m4)

#help
m5=Menu(mainmenu,tearoff=0)
m5.add_command(label='View Help',command=help)
m5.add_command(label='Send Feedback',command=print1)
m5.add_separator()
m5.add_command(label='About Alpha HandBook',command=about)
mainmenu.add_cascade(label="Help",menu=m5)

root.config(menu=mainmenu)


root.mainloop()

