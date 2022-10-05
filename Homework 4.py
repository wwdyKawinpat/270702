import random

n = int(input("How many stick (N) in pile ?: "))
while n<0:
    if n<0:
        print("You cannot insert less than 0")
        n = int(input("How many sticks (N) in the pile: "))
    elif n>0:
        n = int(input("How many sticks (N) in the pile: "))
    
        
print("There are ",n," sticks in the pile")
name = input("What is your name: \n")
player = 0
com = 0
i = 0
cons = 0 # is conditions which fix Computer always win.


if (n%3)!=1:
    cons = 2
    print("Computer will go first\n") 
else:
    cons = 1
    print(name+" will go first\n") 
while n>0:        
    if cons==1:#Player pick
        player = int(input(name+", How many sticks you will take (1 or 2): ")) 
        if player == 1:
            print(name+" take",player," stick.")
            if player>= 3:
                print("No you cannot take more than 2 sticks!")
                n+=player #reture stick that is taken to x
                cons = 1
            elif player<1:
                print("No you cannot take less than 1 sticks!")
                n+=player #reture stick that is taken to x
                cons = 1        
            elif (player<=0) and i==1:
                print("No you cannot take more less than 1 stick!")
                n+=player #add minus value to x
                cons = 1  
            else:
                print(name+" take",player," sticks.")
        n -= player
        win = "Computer wins."
        cons = 2 
     
     
    elif cons == 2:#Computer pick
        print("There are",n,"left in pile.")
        if (n%3) == 2 or n == 1:
            com = 1          
        elif (n%3) == 0:
            com = 2
        else:
            com = random.randint(1,2)  
        n -= com
        print("Computer take",com,"stick.")
        win = name+" wins"
        cons = 1
            
    elif n<0:
     print("There are no enough sticks to take. Try again.")
     n+=player #reture stick that is taken to x
     cons = 1
    elif ((player or com)==1 or (player  or com)==2) and n ==0 :
     print(win)         
    elif ((player or com) ==2) and n <0 :
     print("Again pls\n")
     if player==2 and cons==2:
      print("Again pls\n")
      cons = 1
     elif com==2:
      print("Again pls\n")
      n+=com
      cons = 2  
    elif ((player or com)==1 or (player  or com)==2) and n >0:
     print("There are ",n,"in the pile now\n")
    i+=1


            
#print("OK. There is no stick left in the pile. You spent",count, "times.")
