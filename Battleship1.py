import random

lose = True


board = []

num_row = 5
num_col = 5

col_name = []



for n in range(0,num_col):
    
    row = []
        
    for i in range (0,num_row): 
            
        row.append(0)
        
    board.append(row)
 

    
for n in range (0,num_row):    
    
    yup = ""
    
    for i in range (0,num_col):
        
        yup = yup + str(board[n][i]) + " "
        
    print(yup)    
    
row_ai = random.randint(0,num_row-1)
col_ai = random.randint(0,num_col-1)

print (row_ai)
print (col_ai)

print (board[num_col-1][num_row-1])

board[col_ai][row_ai] = 1

print (board)

print("Welcome to battleship")

print(" ")

while (lose):
    
    ver = True
    
    while (ver):
        
       
        chosen_col = input("- Input the number of the column you wish to select: ")
        
        try: chosen_col = eval(chosen_col)
        
        except:
            print(" ")
            print ("Please input the integer of the position you which to choose")
            print(" ")
        
        if int == type(chosen_col): 
            ver = False
        
        elif type(chosen_col) != str:
            print(" ")
            print ("Please input the integer of the position you which to choose")
            print(" ")
            
            
    ver = True
    
    while (ver):
        
        print(" ")
        chosen_row = input("- Input the number of the row you wish to select: ")
        
        try: chosen_row = eval(chosen_row)
        
        except:
            print(" ")
            print ("Please input the integer of the position you which to choose")
            print(" ")
        

        if int == type(chosen_row): 
            ver = False
        
        else:
            print(" ")
            print ("Please input the integer of the position you which to choose")
            print(" ")
    
    if (chosen_col == col_ai) and (chosen_row == row_ai):
        print(" ")
        print ("You sunk my battleship!")
        print(" ")
        break
    

    

    
    

