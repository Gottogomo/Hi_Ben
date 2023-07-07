
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import *


root = Tk()

root.geometry("700x500")


Grocery_List = []
Name_List = []





frame2 = ttk.Frame (root, relief= 'solid', width= 300, height= 500)




frame2.pack_propagate(False)
frame2.pack(pady= 50,padx= 40, side=tk.LEFT)


frame1 = ttk.Frame (root)
frame1.pack(pady= 40,padx= 70, side=tk.RIGHT)


label_add = ttk.Label(frame1, text= "Add items here", font= "Aeriel 14 bold")
label_add.pack()


entry_add = Entry(frame1, text= "")
entry_add.focus_set()
entry_add.pack(pady= 10)


label_Price = ttk.Label(frame1, text= "Add price here", font= "Aeriel 14 bold")
label_Price.pack()


entry_price = Entry(frame1, text= "")
entry_price.pack(pady= 10)


class Item:
        def __init__(self,item,quan,price):
            self.item = item
            self.quan = quan
            self.price = price





def ADD ():

    if (entry_add.get() not in Name_List) :

            Grocery_List.append(Item(entry_add.get(), "1", str(entry_price.get())))
            Name_List.append(entry_add.get())
            
            x = ""
           
            for i in range(len(Grocery_List)):
            
                x = x + (Grocery_List[i]).item +  ", " + str((Grocery_List[i]).quan) + ", " + str((Grocery_List[i]).price) + "\n"
                
                
            print(Name_List)
            
            List.set(x)
            
            print(x)
            
        

        
    else:
        
        x = ""
        
        count_index = Name_List.index(entry_add.get())
        
        Grocery_List[count_index].quan = int(Grocery_List[count_index].quan) + 1
        
        #print(Grocery_List[count_index].quan)
        
        for i in range(len(Grocery_List)):
            
                x = x + (Grocery_List[i]).item + ", " + str((Grocery_List[i]).quan) + ", " + str((Grocery_List[i]).price) + "\n"
                
        List.set(x)
        


button_add = ttk.Button(frame1, text= "Add item", command= ADD)
button_add.pack(pady= 10)


def REMOVE ():

    try:    

        count_index = Name_List.index(entry_add.get())
        
      
        
        Grocery_List[count_index].quan = int(Grocery_List[count_index].quan) - 1
        
  
        
        #print(Grocery_List[count_index].quan)
        
        if (int(Grocery_List[count_index].quan) == 0) :
        
            
            Grocery_List.remove(Grocery_List[count_index])
            Name_List.remove(Name_List[count_index])
    
        
        y = ""        
       
        
        for i in range(len(Grocery_List)):
            
                y = y + (Grocery_List[i]).item + ", " + str((Grocery_List[i]).quan) +  ", " + str((Grocery_List[i]).price) + "\n"
                
    
        print(Name_List)
        
        List.set(y)
        
        print(y)
        
    except:
        count = 1
        
button_remove = ttk.Button(frame1, text= "Remove item", command= REMOVE)
button_remove.pack(pady= 10)

            
            



List = tk.StringVar()
List_List = Label(frame2, textvariable = List, font= "Aeriel 14 bold", wraplength= 280)
List_List.pack(pady= 3, padx= 3, anchor= W)


    
    
    










root.mainloop()



#Idk = Text(frame1, width= 40, height= 30)
#    Idk.tag_add=(str(add_text)) 
#    Idk.pack()


#class Item:
#        def __init__(self,item,price):
#            self.item = item
#            self.price = price

#x = tk.StringVar(frame2)
#label_add3 = ttk.Label(frame2, textvariable= x.get(), font= "Aeriel 14 bold")
#label_add3.pack(pady= 3, padx= 3, anchor= W)
    


#def ADD ():
    
   
#    add_text = entry_add.get()
    
#    class Item:
#        def __init__(self,item,price):
#            self.item = item
#            self.price = price
        
#    Item_Item = Item(add_text,"0")
    
#    Grocery_List.append(Item_Item)
    
    
#    x = ""

#    for i in range(len(Grocery_List)):
    
#        x = x + (Grocery_List[i]).item + "\n"
    
#    x = tk.StringVar(frame2)
#    x.set(str(x))
    