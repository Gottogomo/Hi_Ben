
from tkinter import *
from tkinter import ttk

win = Tk()

list_g = []

# Sets dimensions
win.geometry("500x700")



# Creates label above insert item
label=Label(win, text="Insert item", font=("Aerial 20 bold"), pady= 20)
label.pack()

# Create entry function, figuring out how to store
# bd adds little bar around (cool)
# investigate focus.set
entry_add = Entry(win, text = "",width= 20, bd= 5, font=('Aerial 16'))
entry_add.focus_set()
entry_add.pack()



# defines adding to a list
# sets entry_add equal to the var text_add
# It is then added to the canvas 
def add_list():
    text_add = entry_add.get()
 
    canvas.create_text(100, 30, text= text_add, fill="black", font=('Aerial 14'))




# button with add on it
#  command runs the defined function by it's name
# .pack allows pady to be used, also I think necessary to end any button
button_add = ttk.Button(win, text= "add", command= add_list, width= 20).pack(pady=20)


# Creates small bow to show the list text in
# Currently static
canvas= Canvas(win, width= 200, height= 300, yscrollincrement= 1, bg="lightgrey")
canvas.pack()


# Starts the window
# Investigate if necesary 
win.mainloop()







#.addtag_above(newTag, tagOrId)


#def add_label():
#   global label
#   label=Label(win, text="1. A Newly created Label", font=('Aerial 18'))
#   label.pack()

#def remove_label():
#   global label
#   label.pack_forget()

#def update_label():
#   global label
#   label["text"]="2. Yay!! I am updated"

# Create buttons for add/remove/update the label widget
#add=ttk.Button(win, text="Add a new Label", command=add_label)
#add.pack(anchor=W, pady=10)

#remove=ttk.Button(win, text="Remove the Label", command=remove_label)
#remove.pack(anchor=W, pady=10)

#update=ttk.Button(win, text="Update the Label", command=update_label)
#update.pack(anchor=W, pady=10)









#def display_text():
#   global entry
#   string= entry.get()
#   label.configure(text=string)

#Initialize a Label to display the User Input
#label=Label(win, text="", font=("Courier 22 bold"))
#label.pack()

#Create an Entry widget to accept User Input
#entry= Entry(win, width= 40)
#entry.focus_set()
#entry.pack()

#Create a Button to validate Entry Widget
#ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

#win.mainloop()








# Defined on left is "var" you call

#class Doodad:
#    def __init__(self, name, age, dob, sex):
        
#        self.name = name
#        self.age = age
#        self.dob = dob
#        self.sex = sex
        
        
#person1 = Doodad ("Callie", 57, "May 28th", "Female")







class Hero:
    def __init__(self,name,age,sex,bday):
        self.name = name
        self.age = age
        self.sex = sex
        self.birthday = bday


super_hero_list = []

superhero = Hero("bruce Banner", "47", "male", "June 15")

super_hero_list.append(superhero)

superhero = Hero("spiderman", "19", "male", "Feb 19")

super_hero_list.append(superhero)


for hero in super_hero_list:
    print(hero.name)