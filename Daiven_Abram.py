
    

        
yup = True
done = True

import math

numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]


while(yup):
            
            print("Hello user, what would you like to do?")
            print("Add (1)")
            print("Subtract (2)")
            print("Multiply (3)")
            print("Divide (4)")
            print("Exponentiate or Decay (5)")
            print("Factorial (6)")
            print("Logarithm (7)")
            print("Modulo (8)")
            
            choice_bW = True
            
            while(choice_bW):
                
                print(" ")
                choice_b = input ("Input which option you would like to choose: ")
                print(" ")
                
                if (choice_b) in numbers:
                    choice_bW = False
                
                else:
                    print("Please input the digit corresponding to the operation you wish to use")
                    
            match choice_b :
     
                case "1":
                
                    try:
                    
                        a_T = True
                        
                        while(a_T):
                            
                            print(" ")
                            a = input("Please input your first number: ")
                            print(" ")
                            
                            try: a = eval(a)
                            
                            except:
                                print("Please input a number")
                                

                            if str != type(a):
                                a_T = False 
                            
                        b_T = True
                        
                        while(b_T):
                            
                            print(" ")
                            b = input("Please input your second number: ")
                            print(" ")
                            
                            try: b = eval(b)
                            
                            except:
                                print("Please input a number")
                                

                            if str != type(b):
                                b_T = False 
                    
                            
                        
                        print(" ")
                        print(a, "+", b, "=", a+b)
                        print(" ")
                        print(" ")
                        
                    except:
                        print(" ")
                        print("There was an error loading your result")
                        print("If the result was expected to be greater then 4300 digits, this calculator isn't for you")
                        print(" ")
                    
            
                case "2":
                    a_T = True
                    
                    try:
                    
                        while(a_T):
                            
                            print(" ")
                            a = input("Please input your first number: ")
                            print(" ")
                            
                            try: a = eval(a)
                            
                            except:
                                print("Please input a number")
                                

                            if str != type(a):
                                a_T = False 
                            
                        b_T = True
                        
                        while(b_T):
                            
                            print(" ")
                            b = input("Please input your second number: ")
                            print(" ")
                            
                            try: b = eval(b)
                            
                            except:
                                print("Please input a number")
                                

                            if str != type(b):
                                b_T = False 
                            
                        
                        print(" ")
                        print(a, "-", b, "=", a-b)
                        print(" ")
                        print(" ")
                    
                    except:
                        print(" ")
                        print("There was an error loading your result")
                        print("If the result was expected to be greater then 4300 digits, this calculator isn't for you")
                        print(" ")
                
                case "3":
                   
                    a_T = True
                    
                    try:
                    
                        while(a_T):
                            
                            print(" ")
                            a = input("Please input your first number: ")
                            print(" ")
                            
                            try: a = eval(a)
                            
                            except:
                                print("Please input a number")
                                

                            if str != type(a):
                                a_T = False 
                            
                        b_T = True
                        
                        while(b_T):
                            
                            print(" ")
                            b = input("Please input your second number: ")
                            print(" ")
                            
                            try: b = eval(b)
                            
                            except:
                                print("Please input a number")
                                

                            if str != type(b):
                                b_T = False 
                                
            
                        print(" ")
                        print(a, "*", b, "=", a*b)
                        print(" ")
                        print(" ")
                        
                    except:
                        print(" ")
                        print("There was an error loading your result")
                        print("If the result was expected to be greater then 4300 digits, this calculator isn't for you")
                        print(" ")
                
                case "4":
                    a_T = True
                    
                    try:
                    
                        while(a_T):
                            
                            print(" ")
                            a = input("Please input your first number: ")
                            print(" ")
                            
                            try: a = eval(a)
                            
                            except:
                                print("Please input a number")
                                

                            if str != type(a):
                                a_T = False 
                            
                        b_T = True
                        
                        while(b_T):
                            
                            print(" ")
                            b = input("Please input your second number: ")
                            print(" ")
                            
                            try: b = eval(b)
                            
                            except:
                                print("Please input a number")
                                
                            if b == 0:
                                print("Please divide by a number other then 0")
                                b = str(b)
                            
                            if str != type(b):
                                b_T = False
                        
                        print(" ")
                        print(a, "/", b, "=", a/b)
                        print(" ")
                        print(" ")
                    
                    except:
                        print(" ")
                        print("There was an error loading your result")
                        print("If the result was expected to be greater then 4300 digits, this calculator isn't for you")
                        print(" ")
                    
                
                case "5":
                    a_T = True
                    
                    try:
                    
                        while(a_T):
                            
                            print(" ")
                            a = input("Please input your first number: ")
                            print(" ")
                            
                            try: a = eval(a)
                            
                            except:
                                print("Please input a number")
                                
                            
                                

                            if str != type(a):
                                a_T = False 
                            
                        b_T = True
                        
                        while(b_T):
                            
                            print(" ")
                            b = input("Please input your second number, for \"roots\", input a decimal: ")
                            print(" ")
                            
                            try: b = eval(b)
                            
                            except:
                                print("Please input a number")
                                
                            if (a < 0 and float == type(b)):
                                print("Please input a non-fractional number for a negative base")
                                b = str(b)

                                
                            
                            
                            elif str != type(b):
                                b_T = False 
                                
                    
                    
                        print(" ")
                        print(str(a) + " ^ " + str(b), "=", a**b)
                        print(" ")
                        print(" ")
                        
                    except:
                        print(" ")
                        print("There was an error loading your result")
                        print("If the result was expected to be greater then 4300 digits, this calculator isn't for you")
                        print(" ")
                    
                
                case "6":
                    a_T = True
                    
                    try:
                    
                        while(a_T):
                            
                            print(" ")
                            a = input("Please input your first number: ")
                            print(" ")
                                    
                            try: a = eval(a)
                            
                            except:
                                
                                print("Please input a number")
                                
                            if str != type(a):
                                a_T = False 
                    
                            
                        if a == 0:
                            print(" ")
                            print (a, "!", "=",1)
                            print(" ")
                            print(" ")
                            
                        
                        elif int == type(a):
                            print(" ")
                            print (abs(a), "!", "=",math.gamma(abs(a)))
                            print(" ")
                            print(" ")
                            
                        elif float == type(a):
                            print(" ")
                            print("As defined by the gamma function")
                            print(" ")
                            print (abs(a), "!", "=",math.gamma(abs(a)))
                            print(" ")
                            print(" ")
                            
                    except:
                        print(" ")
                        print("There was an error loading your result")
                        print("If the result was expected to be greater then 4300 digits, this calculator isn't for you")
                        print(" ")
                                

            
                case "7":
                    a_T = True
                    
                    try:
                    
                        while(a_T):
                            
                            print(" ")
                            a = input("Please input your first number: ")
                            print(" ")
                            
                            try: a = eval(a)
                            
                            except:
                                print("Please input a number")
                                

                            if str != type(a):
                                a_T = False 
                            
                        b_T = True
                        
                        while(b_T):
                            
                            print(" ")
                            b = input("Please input your second number: ")
                            print(" ")
                            
                            try: b = eval(b)
                            
                            except:
                                print("Please input a number")
                        
                            if b == 0:
                                print("Please input a base other then 0")
                                print("log_0 of every number is undefined")
                                b = str(b)
                            
                                
                            if str != type(b):
                                b_T = False 
                                
                                
                        
                        print(" ")
                        print("("+str(abs(a))+")" + "log_"+ "("+str(abs(b))+")", "=", math.log(abs(a),abs(b)))
                        print(" ")
                        print(" ")
                        
                        
                    except:
                        print(" ")
                        print("There was an error loading your result")
                        print("If the result was expected to be greater then 4300 digits, this calculator isn't for you")
                        print(" ")
                        
            
                case "8":
                    a_T = True
                    
                    try:
                    
                        while(a_T):
                            
                            print(" ")
                            a = input("Please input your first number: ")
                            print(" ")
                            
                            try: a = eval(a)
                            
                            except:
                                print("Please input a number")
                                

                            if str != type(a):
                                a_T = False 
                            
                        b_T = True
                        
                        while(b_T):
                            
                            print(" ")
                            b = input("Please input your second number: ")
                            print(" ")
                            
                            try: b = eval(b)
                            
                            except:
                                print("Please input a number")
                                
                                
                            if b == 0:
                                print("Please input a base other then 0")
                                print("mod_0 of every number is undefined")
                            
                            elif str != type(b):
                                b = abs(b)
                                a = abs(a)
                                b_T = False
                        
                    
                        print(" ")
                        print("("+str(a)+")" + "mod"+ "("+str(b)+")", "=", a%b)
                        print(" ")
                        print(" ")
                    
                    except:
                        print(" ")
                        print("There was an error loading your result")
                        print("If the result was expected to be greater then 4300 digits, this calculator isn't for you")
                        print(" ")
                        
                    
           
           
            done = True
                    
    
            while(done):
                        
                    continu_e = input ("Would you like to make another calculation? Yes or No : ")
                        
                    if continu_e.lower() == "no":
                        yup = False
                        done = False
            
                        
                    elif continu_e.lower() == "yes":
                        print(" ")
                        yup = True
                        done = False
                        
                    else:
                        print(" ")
                        print("Please input Yes or No")
                        print(" ")
    



                    

