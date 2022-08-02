import random

x = int(input("How many stick (N) in pile ?: "))
while x<0:
    if x<0:
        print("You cannot insert less than 0")
        x = int(input("How many sticks (N) in the pile: "))
    elif x>0:
        x = int(input("How many sticks (N) in the pile: "))
    
        
print("There are ",x," sticks in the pile")
name = input("What is your name: \n")
y = 0
bot = 0
i = 0
cons = 0 # is conditions which fix Computer always win.


if (x%3)!=1:
    cons = 2
    print("Computer will go first\n") 
else:
    cons = 1
    print(name+" will go first\n") 
while x>0:        
    if cons==1:#Player pick
     y = int(input(name+", How many sticks you will take (1 or 2): ")) 
     if y == 1:
      print(name+" take",y," stick.")
     else:
      print(name+" take",y," sticks.")
     x -= y
     win = "Computer wins."
     cons = 2 
    elif cons == 2:#Computer pick
     print("There are",x,"left in pile.")
     if (x%3) == 2 or x == 1:
         bot = 1          
     elif (x%3) == 0:
         bot = 2
     else:
         bot = random.randint(1,2)  
     x -= bot
     print("Computer take",bot,"stick.")
     win = name+" wins"
     cons = 1
            
    if y>= 3:
     print("No you cannot take more than 2 sticks!")
     x+=y #reture stick that is taken to x
     cons = 1
    elif (y<=0) and i==1:
     print("No you cannot take more less than 1 stick!")
     x+=y #add minus value to x
     cons = 1
    elif x<0:
     print("There are no enough sticks to take. Try again.")
     x+=y #reture stick that is taken to x
     cons = 1
    elif ((y or bot)==1 or (y  or bot)==2) and x ==0 :
     print(win)         
    elif ((y or bot) ==2) and x <0 :
     print("Again pls\n")
     if y==2 and cons==2:
      print("Again pls\n")
      cons = 1
     elif bot==2 and z==1:
      print("Again pls\n")
      x+=bot
      cons = 2  
    elif ((y or bot)==1 or (y  or bot)==2) and x >0:
     print("There are ",x,"in the pile now\n")
    i+=1


            
#print("OK. There is no stick left in the pile. You spent",count, "times.")
