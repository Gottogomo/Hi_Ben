


x = True
count = 0
duck = False
Mace = False
Tre = False
Dagg = False
Guts = False
Wallet = False
bridge = True
live_g = False
Wallet = False
Guts = False
none = False
dragon = True
Help = False
Notice = False
Vorpal = False
Padding = False
count_p = 0
Side = False
arm_c = False

import random

from graphics import *

def color_word(word,color,style):
    word = ("\033[" + style + ";" + color + ";40m" + word + "\033[0;0m")
    return word

def color(word,color):
    word = ("\033[1;" + color + ";40m " + word + "\033[0;0m")
    return word


while(x):

   

       

       

        
        print(" ")
        print(" ")
        print(" ")
        
        

        if count == 0:
            #dev = eval(input ("Skip or no: "))
            #count = dev
            print ("There are two doors ahead of you")
            print ("One is on the left (L), and one is on the right (R)")
            print (" ")

        if ((count == 4) and (way == "M")):
            count = "4M"



       
   
        if count == 3:
            print (" ")
            print ("A third door appears in the middle, accesible by M")
            print (" ")
   
        elif ((count == 4) or (count == "M4")) :
            print (" ")
            print("You feel a compulsion to enter the middle door")
            print (" ")

       
        
      
            
        
        way = input(color_word("Choose a door to enter, and remember, choose wisely: ","37","1"))
            
         

        print (" ")
        print (" ")

        
        
        if ((way == "Duck") and (duck == True)):
            print ("-"+color("*Quack*","33"))
    
            count = count - 1
            
        


      



        elif ((count == 0) or (count == 1) or (count == 2) or (count == 3) or (count == 4) or (count == "4M") or (count == 5) or (count == 9) or (count == 10) or (count == 12)):


            if (way == "M") :
                        print (" ")
                        print ("- You walk through the Middle door")
                        print (" ")

                        if count == "4M":
                            count = 4

                        if count == 3:
                            print(color_word("- Adventurous aren't we?","37","3"))
        
        
            elif ((way == "L" or "R") and (count == 4)):
                print (" ")
                print ("- You just can't bring yourself to go through the same doors again")
                print (" ")
                count = count - 1



            elif ((way == "L" or "R") and (count == "4M")):
                print (" ")
                print ("- It was so fun the first time, you can't bring yourself to not go through the middle again")
                print (" ")
                count = 4
                count = count - 1    
            
            elif  (((way == "L")) and ((count != "4M") or (count != 4))):
                print (" ")
                print ("- You walk through the Left door") 
        
            
            elif ((way == "R") and ((count != "4M") or (count != 4))):
                print (" ")
                print ("- You walk through the Right door") 
            
            else:
                print (" ")
                print("- You hit your head on the wall")
                count = count - 1

            
            if count == -1:
                print (" ")
                print (color("-If you don't like reading, this game might not be for you","31"))

        
        
        elif (count == 6):
            print ("There appears to be a box in the middle of the room")
            print (" ")
            
            box_1 = True
            
            while (box_1):

                box = input (color_word("Do you open the box?: ","37","1"))

                if (box == "Yes") or (box == "No"):
                     box_1 = False

                else:
                    print("This is a Yes or No question")

            if box == "Yes" :
                print (" ")
                print (" ")
                print (" ")
                print ("- You have now obtained a rubber ducky. Type in Duck to use")
                duck = True

            elif box == "No" :
                print (" ")
                print (" ")
                print (" ")
                print ("- You walk past the box, imumune to it's temptations, which also disapoints the coder")

        elif (count == 7):
            print("You now enter into an expansive armory")
            print ("You are surrounded by various weapons, so why not pick one up?")
            print (" ")
            print ("A Massive Mace (Mace)")
            print ("A Dull Dagger (Dagger)")
            print ("A Portable Trebuchet (Trebuchet)")
            print (" ")
            
            arm = True

            while (arm):
             
                arm_c = input (color_word("What weapon do you choose?: ","37","1"))

                if (arm_c == "Mace"):
                    print (" ")
                    print (" ")
                    print("- While difficult to carry, you grab the Massive Mace")
                    Mace = True
                    arm = False
                    
                elif (arm_c == "Dagger"):
                    print (" ")
                    print (" ")
                    print("- Though it may not be the most effective, you easily grab the Dull Dagger")
                    Dagg = True
                    arm = False

                elif (arm_c == "Trebuchet"):
                    print (" ")
                    print (" ")
                    print("- Realizing what is clearly the coolest option, you grab the Portable Trebuchet")
                    Tre = True
                    arm = False

                elif (arm_c == "Duck"):
                          print ("-"+color("*Quack*","33"))

                else:
                    print (" ")
                    print ("- You hit your head on the wall")
                    print (" ")


        elif (count == 8):
            print (" ")
            print("Infront of you is a massive goblin")
            print ("And they command you to answer his riddle to pass")
            print ("Do you answer his riddle (Riddle)? Or attack with your new found weapon (Attack)?")
            print (" ")
            

            Riddle = "yeah"
            choice_1 = True

            goblin_1 = True

            while (goblin_1):

                while (choice_1):
             
                
                    goblin_c = input (color_word("What do you choose?: ","37","1"))

                    if (goblin_c == "Riddle"):
                        choice_1 = False
                        pass
                        
                    elif (goblin_c == "Attack"):
                        choice_1 = False
                        pass

                    elif (goblin_c == "Duck"):
                          print ("-"+color("*Quack*","33"))

                    else:
                        print (" ")
                        print ("- You hit your head on the wall")
                        print (" ")

                if (goblin_c == "Attack") or (Riddle == "Lol"):
                    
                    if (Mace == True):

                            print (" ")
                            print (" ")
                            print("- You swing at the Goblin with your Massive Mace")
                            goblin_1 = False
                        
                    elif (Tre == True):

                            print (" ")
                            print (" ")
                            print ("- You pull your portable Trebuchet from your pocket, much to the Goblins surprise, and you shoot at the Goblin")
                            goblin_1 = False
                        
                    elif (Dagg == True):

                            print (" ")
                            print (" ")
                            print ("- You pull your Dull Dagger out, causing the Goblin to laugh and stumble back")
                            goblin_1 = False
                    

                elif goblin_c == "Riddle":
                        
                        print (" ")
                        print (" ")
                        print ("- Good choice adventurer")
                        print (" ")
                        print (" ")
                        print ("I am black and white, and red all over. What am I?")
                        print (" ")

                        Ans = input(color_word("I am: ","37","1"))

                        print (" ")
                        print (" ")
                        print ("- The goblin realizes he doesn't understand english. and goes to attack")
                        
                        Riddle = "Lol"
            print (" ")
            print (" ")
            print ("The goblin stumbles through the wall behind him, breaking it down, and knocking him out.")
            print ("This gives you an option to escape (Escape) through, or to finish the Goblin (Attack)")
            print (" ")

            choice_2 = True


            while (choice_2):
             
                
                    goblin_2c = input (color_word("What do you choose?: ","37","1"))

                    if (goblin_2c == "Escape"):
                        print (" ")
                        print ("- You run past the goblin into the next room")
                        live_g = True
                        choice_2 = False
                        pass
                        
                    elif (goblin_2c == "Attack"):
                         
                            if (arm_c == "Mace"):
                                    print (" ")
                                    print (" ")
                                    print ("- You smash through the goblin with your Massive Mace, easily taking the beast out")
                                    print (" ")
                                    print ("- You then, in a very dignified manner, use the goblins cloth to grab some of it's guts")
                                    print (" ")
                                    live_g = False
                                    Guts = True
                                    choice_2 = False
                                
                            elif (arm_c == "Dagger"):
                                    print (" ")
                                    print (" ")
                                    print ("- You stab through the goblins skin with your Dull Dagger, and the rust of the dagger kills the goblin")
                                    print (" ")
                                    print ("- You then, in a very dignified manner, steal his wallet full of gold coins")
                                    print (" ")
                                    live_g = False
                                    Wallet = True
                                    choice_2 = False

                            elif (arm_c == "Trebuchet"):
                                    print (" ")
                                    print (" ")
                                    print ("- You launch your Portable Trebuchet shots at the goblin, but their small size causes them to bounce off the Goblin")
                                    print (" ")
                                    print ("- You then, in a very dignified manner, run through the hole")
                                    print (" ")
                                    none = True
                                    live_g = False
                                    choice_2 = False
                        





                    elif (goblin_2c == "Duck"):
                          print ("-"+color("*Quack*","33"))

                    else:
                        print (" ")
                        print ("- You hit your head on the wall")
                        print (" ")

        
        elif (count == 11):

            Game_2 = True
             
            print ("A hooded figure is in the center of the room")
            print ("They raise their right hand, and in their raspy voice, they say")
            print (" ")

            paper = False
            scissors = False
            rock = False
           

            while (Game_2):
                 
                print (" ")
                
                move_1 = input(color_word("Rock, Paper, Scissors: ","37","1"))

                npc = int(random.randint(1,9))

                if ((npc == 1) or (npc == 2) or (npc == 3)):
                    npc_throw = "Paper"

                elif ((npc == 4) or (npc == 5) or (npc == 6)):
                    npc_throw = "Rock"

                elif ((npc == 7) or (npc == 8) or (npc == 9)):
                    npc_throw = "Scissors"

                str(npc_throw)

                if (move_1 == "Duck"):
                    print (" ")
                    print (" ")
                    print ("-"+color("*Quack*","33"))
                    print (" ")
                    print ("- The figure is confused, and chants again")
                    print (" ")

                elif (move_1 == npc_throw):
                     print (" ")
                     print ("You throw",move_1,"and the figure throws",npc_throw)
                     

                elif (move_1 == "Paper"):
                     
                    if (npc_throw == "Scissors"):
                        print (" ")
                        print ("You throw",move_1,"and the figure throws",npc_throw)

                    if (npc_throw == "Rock"):
                        print (" ")
                        print ("You throw",move_1,"and the figure throws",npc_throw)
                        Game_2 = False


                elif (move_1 == "Scissors"):
                     
                    if (npc_throw == "Rock"):
                        print (" ")
                        print ("You throw",move_1,"and the figure throws",npc_throw)

                    if (npc_throw == "Paper"):
                        print (" ")
                        print ("You throw",move_1,"and the figure throws",npc_throw)
                        Game_2 = False


                elif (move_1 == "Rock"):
                     
                    if (npc_throw == "Paper"):
                        print (" ")
                        print ("You throw",move_1,"and the figure throws",npc_throw)

                    if (npc_throw == "Scissors"):
                        print (" ")
                        print ("You throw",move_1,"and the figure throws",npc_throw)
                        Game_2 = False
                        
                elif (move_1 == "Callie"):
                    print("You're mean")
                    Game_2 = False

                else: 
                    print (" ")
                    print("The figure seems disapointed you didn't understand")


            print (" ")
            print (" ")
            print("You walk past the disappointed figure into the next room")
            
            
        elif (count == 13):
            print("Before you is a pit full of wolves")
            print ("The only way to get across is one rickity bridge in the center")
            print (" ")
            print ("You first think to head back, but on the other side is three open doorways leading to the outside world")
            print ("You realize your only option is to take the bridge (Bridge), or (Wait)")
            print (" ")
            
            
            
            while(bridge):
                
                choice_3 = input (color_word("Which do you choose?: ","37","1"))
                
                if choice_3 == "Wait":
                    print (" ")
                    print ("- You wait")
                    print (" ")
                    
                elif choice_3 == "Bridge":
                    bridge = False
                    
                elif choice_3 == "Duck":
                    print (" ")
                    print ("-"+color("*Quack*","33"))
                    print (" ")
                    
                else:
                    print (" ")
                    print ("- You hit your head on the wall")
                    print (" ")

            print (" ")
            print ("You attempt to pass over the bridge, but halfway through the bridge breaks from under you")
            print (" ")
            
            if live_g == True:
                print (" ")
                print("- You begin to harrowinglyy fall into the pit, but mid way through, the Goblin breaks through the wall")
                print (" ")
                print (" ")
                print ("The goblin catches you before you meet your fate, and thanks you for sparing his life")
                print ("He raises you safely to the other side, and as he leaves back through the wall")
                print (" ")
                print ("It seems you may finally be able to escape")
                
            elif Guts == True:
                print (" ")
                print("- As you harrowingly fall through the air, the guts held in your sack fall out onto the wolves below")
                print (" ")
                print (" ")
                print ("The wolves eat away at the meat, and seem to be completly oblivous to you")
                print ("This gives you time to climb the broken bridge as it hangs over the edge")
                print (" ")
                print ("It seems you may finally be able to escape")
                
            elif Wallet == True:
                print (" ")
                print("- As you harrowingly fall through the air, the gold coins in your wallet fall onto the wolves below")
                print (" ")
                print (" ")
                print ("Some wolves are blinded by the shimmering coins, and the others go to fight over the loot")
                print ("After recovering some of the dropped coins, the distraction gives you time to climb the broken bridge as it hangs over the edge")
                print (" ")
                print ("It seems you may finally be able to escape")
                
                
                
            elif none == True:
                print (" ")
                print("- As you harrowingly fall through the air, the Portable Trebuchet falls out of your pocket")
                print (" ")
                print (" ")
                print ("The wolves get a glimpse at the awe and beauty of the Portable Trebuchet as it falls")
                print ("They create an open path for you to land and walk through, which allows you to climb the broken bridge as it hangs over the edge")
                print (" ")
                print ("It seems you may finally be able to escape")
                
            else: 
                print (" ")
                print ("You skipped didn't you? You get a pass this time")
            
            
        
        elif count == 14:
           print ("You walk through the door, and it seems you have finally escaped")
           print ("You walk into a merry grass field")
           print (" ")
           print ("It's a beautiful day outside") 
           print ("Birds are singing") 
           print ("flowers are blooming") 
           print ("and on days like these") 
           print ("It's odd that the air smells like "+color_word("ash","31","4"))
           print (" ")
           print (" ")
           print ("The fields before you fall at once into an inferno")
           print ("The sky melts away as blue wallpaper falls off the brick walls")
           print ("A hill infront of you begins to grow and stretch until a giant dragon rips through the soil")
           print (" ")
           
           
           while (dragon):
               
                choice_f = input (color_word("What do you do?: ","37","1"))
               
                if ((choice_f == "Rock") or (choice_f == "Paper") or (choice_f == "Scissors")):
                
                    npc = int(random.randint(1,9))

                    if ((npc == 1) or (npc == 2) or (npc == 3)):
                        npc_throw = "Paper"

                    elif ((npc == 4) or (npc == 5) or (npc == 6)):
                        npc_throw = "Rock"

                    elif ((npc == 7) or (npc == 8) or (npc == 9)):
                        npc_throw = "Scissors"
                        
                    print (" ")
                    print ("- You throw",choice_f,"and the dragon throws",npc_throw)
                    print (" ")
                    
                    
                elif (choice_f == "Duck"):

                    print (" ")
                    print ("-"+color("*Quack*","33"))
                    print (" ")
                    
                elif ((choice_f == "Attack") or (choice_f == "Mace") or (choice_f == "Trebuchet") or (choice_f == "Dagger")):
                    
                    if (Vorpal == True):
                        print(" ")
                        print("- You attack the dragon with the blade, defeating the foe")
                        dragon = False
                        x = False
                        pass
                    
                    elif ((arm_c == Mace) or (choice_f == "Mace")):
                        if (arm_c == Mace):
                            print(" ")
                            print("- You try to takeout the dragon with your Massive Mace, but the attack deflects off the dragons armor")
                            print(" ")
                        else:
                            print (" ")
                            print ("- You do not have that item")
                            print (" ")
                            
                    elif ((arm_c == Tre) or (choice_f == "Trebuchet")):
                        
                        if (arm_c == Tre):
                            print(" ")
                            print("- You try to takeout the dragon with shots from your Portable Trebuchet, but the attack deflects off the dragons armor")
                            print(" ")
                        else:
                            print (" ")
                            print ("- You do not have that item")
                            print (" ")
                            
                    elif ((arm_c == Dagg) or (choice_f == "Dagger")):
                        
                        if (arm_c == Dagg):
                            print(" ")
                            print("- You try to takeout the dragon with your Dull Dagger, but the attack deflects off the dragons armor")
                            print(" ")
                        else:
                            print (" ")
                            print ("- You do not have that item")
                            print (" ")
                            
                
                elif ((choice_f == "L") or (choice_f == "R") or (choice_f == "M")):
                    
                    if (Padding == False):
                        print(" ")
                        print("- You need to grow confidence before approaching the dragon, try something else first")
                        print(" ")
                        
                    elif (Side == True):
                        print(" ")
                        print("- You think to run past the dragon again, but the temptation of the chest is too much")
                        print(" ")
                    
                    else:
                        
                        if choice_f == "M":
                            print(" ")
                            print("- You think to run past the dragon, but then remember you cannot run through the dragon")
                            print(" ")
                            Side = True
                            
                        elif choice_f == "L":
                            print(" ")
                            print("- You run past the left side of the dragon, and you notice on the other side a bridge that leads to a chest ")
                            print(" ")
                            Side = True
                        
                        elif choice_f =="R":
                            print(" ")
                            print("- You run past the right side of the dragon, and you notice on the other side a bridge that leads to a chest")
                            print(" ")
                            Side = True
                            
                      
                elif (choice_f == "Escape"):
                    print(" ")
                    print(color_word("- There is no escape","31","4"))
                    print(" ")
               
                    
                elif (choice_f == "Bridge"):
                    if (Side == True):
                        print(" ")
                        print ("- You cross the bridge to open the chest, and find inside a Vorpal Blade")
                        print(" ")
                        print("You now have a blade that can cut the dragons scale")
                        print(" ")
                        Vorpal = True
                    
                    else:
                        print(" ")
                        print("- You look around for a bridge, but see none on this side of the dragon")
                        print(" ")
                        Padding = True
                     
                    
                elif (choice_f == "Riddle"):
                    print(" ")
                    print("- You ask the dragon for a riddle, and then realize the dragon cannot speak English")
                    print(" ")
                  
                    
                elif (choice_f == "Wait"):
                    print(" ")
                    print("- You wait")
                    print(" ")
            
                    
                elif ((choice_f == "Yes") or (choice_f == "No")):

                    if (choice_f == "No"):
                        print(" ")
                        print("- Yes")
                        print(" ")
                        
                    elif (choice_f == "Yes"):
                        print(" ")
                        print("- No")
                        print(" ")
                        
                else:
                    
                    if (Help == False):
                        print(" ")
                        print("- Try using a previousely used input")
                        print(" ")
                        Help = True
                        
                    else:
                        print(" ")
                        print("- You hit your head on the wall")
                        print(" ")
                        
            
        else:
            print("I haven't coded this far yet")
            x = False

            
        
    


        count = count + 1
        #print (" ")
        #print(count)

print(" ")
print ("For the final time, the dragon falls through the wall, and with th e smell od a magnificent meadow, you know you are free")
print (" ")
print (color("You win","33"))
print (" ")


    
# Exiting loop ends it, maybe loops once but have new thing, try except line
# Joke making new option, say L for not picking it, force pick, there is nothing !!!
# Konami cheat code (Vorpereal sword to kill dragon)
# options to atk (attack), Duck => Duck, bash? !!!
# Cake
# Rock, paper, scissors !!!
# \noclip ends cycle
# Summoning key? Or varous popular cycles
# DOGG
# Roll a dice
# CHANGE INPUT TO BE UNIVERSAL
# 2nd year thought process (Build a bomb)
# Quick, type as fast as you can for 15 secound. i don't know how to time




   
