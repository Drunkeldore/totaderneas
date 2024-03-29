from tkinter import *
from tkinter import ttk

import os
#Formatting the classlist to remove symbols and class numbers
with open("classList.txt", "r") as file:
    rawclasslist = file.readlines()
classlist = [each.replace(" ï¿½" , "")[:-5] for each in rawclasslist]


# USE THIS to prevent issues with original list
classlistCOPY = classlist

#Finding the right width for Listbox based on longest class name
word_width = 0
for each in classlist:
    if len(each) > word_width:
        word_width = len(each)

root = Tk()
root.title("This is my name")
root.maxsize(1800, 600)
root.configure(background="#1a5d7f")

# An absolute mess creating all the frames needed.
frma = LabelFrame(root, text="Not Started", labelanchor="n", borderwidth=0, bg="#003057", font=("FUTURA STANDARD", 16, "underline"), fg="white")
frmb = LabelFrame(root, text="Currently In", labelanchor="n", borderwidth=0, bg="#003057", font=("FUTURA STANDARD", 16, "underline"), fg="white")
frmc = LabelFrame(root, text="Finished", labelanchor="n", borderwidth=0, bg="#003057", font=("FUTURA STANDARD", 16, "underline"), fg="white")
# frmbtna = LabelFrame(root, borderwidth=0)
# frmbtnb = ttk.LabelFrame(root, borderwidth=0)
# frmbtnc = ttk.LabelFrame(root, borderwidth=0)

frma.grid(column=0, row=0)
frmb.grid(column=1, row=0)
frmc.grid(column=2, row=0)
# frmbtna.grid(column=0, row=1)
# frmbtnb.grid(column=1, row=1)
# frmbtnc.grid(column=2, row=1)
#frame_list = [frma, frmb, frmc, frmbtna, frmbtnb, frmbtnc]


nslist = Listbox(frma, width=word_width, height=25, selectmode=MULTIPLE, highlightthickness=0, borderwidth=0, font=("FUTURA STANDARD", 12), name="nslist")
nslist.pack()

cinlist = Listbox(frmb, width=word_width, height=25,  selectmode=MULTIPLE, highlightthickness=0, borderwidth=0, font=("FUTURA STANDARD", 12), name="cinlist")
cinlist.pack()

finlist = Listbox(frmc, width=word_width, height=25, selectmode=MULTIPLE, highlightthickness=0, borderwidth=0, font=("FUTURA STANDARD", 12), name="finlist")
finlist.pack()

#Not started list
path = "./nslist.txt"
if not os.path.exists(path):
    with open("nslist.txt", "w") as file:
        for each in classlistCOPY:
            file.write(each + "\n")

else:
    with open("nslist.txt", "r") as file:
        notstartlist = file.readlines()
    
    for each in notstartlist:
        nslist.insert(END, each)
    
#Currently in List
path = "./cinlist.txt"
if not os.path.exists(path):
    with open("cinlist.txt", "w") as file:
        file.close()
with open("cinlist.txt", "r") as file:
    currentinlist = file.readlines()

for each in currentinlist:
    cinlist.insert(END, each)

#Finished List
path = "./finlist.txt"
if not os.path.exists(path):
    with open("finlist.txt", "w") as file:
        file.close()
with open("finlist.txt", "r") as file:
    finishedlist = file.readlines()
for each in finishedlist:
    finlist.insert(END, each)


def moveclassover(source, destination):
    selected = source.curselection()

    stringsource = source.winfo_name() + ".txt"
    stringdestination = destination.winfo_name() + ".txt"
    
    for each in selected[::-1]:
        destination.insert(END, source.get(each))
        source.delete(each)
    #print(stringsource + "\n" + stringdestination)
    #print(nslist.get(0, 'end'))
    with open(stringsource, "w") as file:
        for each in source.get(0, "end"):
            file.write(each)
    
    with open(stringdestination, "w") as file:
        for each in destination.get(0, "end"):
            file.write(each)

#TODO refactor each list.txt to be all lowercase. Makes this function significantly easier to manage.




        



#Movement Buttons
rightarrow = PhotoImage(file="./images/rightArrow.png")
leftarrow = PhotoImage(file="./images/leftArrow.png")

notstartedbtn = Button(root, command=lambda: moveclassover(nslist, cinlist), image=rightarrow, width=20, height=10)
notstartedbtn.grid(column=0, row=1, pady=10, padx=5)

firstcinbtn = Button(root, command=lambda: moveclassover(cinlist, finlist), image=rightarrow, width=20, height=10)
firstcinbtn.grid(column=1, row=1, pady=10, padx=5)

firstcinbtntwo = Button(root, command=lambda: moveclassover(cinlist, nslist), image=leftarrow, width=20, height=10)
firstcinbtntwo.grid(column=1, row=2, pady=10, padx=5)

finbtn = Button(root, command=lambda: moveclassover(finlist, cinlist), image=leftarrow, width=20, height=20)
finbtn.grid(column=2, row=1)



root.mainloop()
