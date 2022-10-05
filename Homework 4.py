import random

n = int(input("How many stick (N) in pile ?: "))
while n<0:
    print("You cannot insert less than 1 stick.")
    n = int(input("How many sticks (N) in the pile: "))
    
name = input("What is your name: \n")
player = 0 
com = 0
turn = 0
    
while n>=0:     
    if turn%2 != 0:
        player = int(input(name+", How many sticks you take (1 or 2):"))
        print(name , ' takes ', player , ' sticks.')
        n -= player
        if n == 0:
            print('\n',name , 'takes a last stick.')
            print('Computer wins')
            break
        if player >= 3:
            print("You cannot take more than 2 sticks.")
            n+=player #return sticks that is taken from player.
            turn -= 1
        elif player<1:
            print("You cannot take less than 1 stick.")
            n+=player #return sticks that is taken from player.
            turn -= 1
        elif player > n and n < 0:
            print("No enough sticks in the pile.")
            n+=player #return sticks that is taken from player.
            turn -= 1
        turn += 1
  
    elif turn%2 == 0:
        print(n," sticks in the pile.\n")
        if n%3 == 2 :#Computer pick
            com = 1 
            n -= com 
            print("Computer take",com,"stick.")
            print('There are ', n , ' sticks left in the pile.\n')
            turn+=1 
            if com == 0:
                print('Player wins')
                break               
        elif n%3 == 0:
            com = 2
            n -= com
            print("Computer takes ",com," sticks.")
            print('There are ', n , ' sticks left in the pile.\n')
            turn+=1
            if n == 0:
                print('Computer take a last stick.\n')
                print(name,' wins')
                break
        else:
            com = random.randint(1,2)  
            n -= com
            turn+=1
            print("Computer take",com,"stick.")
            print('There are ', n , ' sticks left in the pile.\n')