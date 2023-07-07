
while(True):
    
    print(" ")
    print("Change calculator")
    print(" ")
    print("Please enter the count of each coin type")

    x1,x2,x3,x4 = True,True,True,True

    Yes = True
    No = True

    while(x1):
    
        quarters = input("Quarters: ")
        
        try: quarters = eval(quarters)
        
        except: 
            print ("Input the number of Quarters, without words")

        if int == type(quarters):
            x1 = False
    
        elif float == type(quarters):
            
            print ("Input a whole number")

    while(x2):
    
        Dimes = input("Dimes: ")
        
        try: Dimes = eval(Dimes)
        
        except: 
            print ("Input the number of Dimes, without words")

        if int == type(Dimes):
            x2 = False
    
        elif float == type(Dimes):
            
            print ("Input a whole number")

    while(x3):
    
        Nick = input("Nickels: ")
        
        try: Nick = eval(Nick)
        
        except: 
            print ("Input the number of Nickels, without words")

        if int == type(Nick):
            x3 = False
    
        elif float == type(Nick):
            
            print ("Input a whole number")

    while(x4):
    
        Penn = input("Pennies: ")
        
        try: Penn = eval(Penn)
        
        except: 
            print ("Input the number of Pennies, without words")

        if int == type(Penn):
            x4 = False
    
        elif float == type(Penn):
            
            print ("Input a whole number")


        
    
    print(" ")
        

    print("You have", round(quarters*0.25 + Dimes*0.1 + Nick*0.05 + Penn*0.01,2)," dollars")