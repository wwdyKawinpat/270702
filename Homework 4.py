import random

n = int(input("How many stick (N) in pile ?: "))                   # Retrieved number of sticks in pile
while n<=0:                                                         # Checking pile cannot less than 0
    print("You cannot insert less than 1 stick.")
    n = int(input("How many sticks (N) in the pile: "))
    
name = input("What is your name: \n")                              # Input player name
player = 0                                                         # Create player
com = 0                                                            # Create Computer
turn = 0
    
while n>=0:                                                        # Iteration conditions
    if turn%2 != 0:                                                # Setting turn. There are 2 players, player who take 1st turn always %2 = 0, the other one always %2 != 0.
        player = int(input(name+", How many sticks you take (1 or 2):"))
        print(name , ' takes ', player , ' sticks.')               # Printing Player action
        n -= player
        if player >= 3:
            print("You cannot take more than 2 sticks.")
            n+=player                                              # Return sticks that is taken from player.
            turn -= 1                                              # Condition to return player turn
        elif player<1:
            print("You cannot take less than 1 stick.")
            n+=player                                              # Return sticks that is taken from player.
            turn -= 1                                   
        elif player > n and n < 0 or com > n and n < 0:
            print("No enough sticks in the pile.")
            n+=player                                              # Return sticks that is taken from player.
            turn -= 1
        if n == 0:                                                 # Setting codition to player to take stick and setting Ending game condition
            print('\n',name , 'takes a last stick.')               # Printing Player action
            print('Computer wins!!')                               # Annoucement Game winner !!
            break                                                  # Ending iteration command            
        turn += 1                                                  # Giving turn to next player (Computer)
  
    elif turn%2 == 0:                                              # 1st turn playing condition, using %2 = 0 to set 1st player becasue there are 2 players.
        print('There are',n," sticks in the pile.\n")
        if n%3 == 2 :                                              # Computer picking condition
            com = 1             
            n -= com 
            print("Computer take",com,"stick.")                    # Printing Computer action
            print('There are ', n , ' sticks left in the pile.\n') # Showing sticks left in the pile
            turn+=1 
            if n == 0:                                             # Setting Ending game condition for computer
                print('Computer takes the last stick.')              
                print('Player wins!!')                             # Annoucement Game winner !!
                break                                              # Ending iteration command
        elif n%3 == 0:                                             # Computer picking condition
            com = 2
            n -= com
            print("Computer takes ",com," sticks.")
            print('There are ', n , ' sticks left in the pile.\n')
            turn+=1
            if n == 0:                                             # Setting Ending game condition for computer
                print('Computer takes the last stick.')              
                print('Player wins!!')                             # Annoucement Game winner !!
                break                                              # Ending iteration command
        elif n%3 == 1:
            com = random.randint(1,2)                              # Random number condition
            n -= com            
            print("Computer take",com,"stick.")
            print('There are ', n , ' sticks left in the pile.\n')
            if n == 0:                                            # Setting Ending game condition for computer
                print('Computer takes the last stick.')              
                print('Player wins!!')                            # Annoucement Game winner !!
                break                                             # Ending iteration command
            elif n < 0:
                com = 1
                n -= com
            turn+=1