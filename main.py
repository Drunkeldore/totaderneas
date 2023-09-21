from tkinter import *
from tkinter import ttk


#Formatting the classlist to remove symbols and class numbers
with open("classList.txt", "r") as file:
    rawclasslist = file.readlines()
classlist = [each.replace(" ï¿½" , "")[:-5] for each in rawclasslist]


#TODO To avoid fucking it all up USE THIS
classlistCOPY = classlist

#Finding the right width for Listbox based on longest class name
word_width = 0
for each in classlist:
    if len(each) > word_width:
        word_width = len(each)

root = Tk()
root.title("This is my name")
root.maxsize(800, 600)

frma = ttk.LabelFrame(root, text="Not Started", labelanchor="n")
frmb = ttk.LabelFrame(root, text="Currently In", labelanchor="n")
frmc = ttk.LabelFrame(root, text="Finished", labelanchor="n")

frame_list = [frma, frmb, frmc]
frma.grid(column=0)
frmb.grid(column=1)
frmc.grid(column=2)


nsslist = Listbox(frma, width=word_width, height=25, selectmode=MULTIPLE)
nslist = Text(frma, width=30, height=10)
nsslist.pack()

#Not started list
for each in classlist:
    nsslist.insert(END, each)

#Currently in List
for each in classlist:
    nsslist.insert(END, each)

#Finished List
for each in classlist:
    nsslist.insert(END, each)

b = ttk.Button()


root.mainloop()