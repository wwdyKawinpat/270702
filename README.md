# Stick In The Pile Game
Rule : Player who takes the last stick is a loser!!

## Game Start

First, Please input number of Stick in the pile.

``` sh
  stick_pile = int(input("How many stick (N) in pile ?: "))
    while stick_pile<0:
        if stick_pile<0:
            print("You cannot insert less than 0")
            stick_pile = int(input("How many sticks (N) in the pile: "))
        elif stick_pile>0:
            stick_pile = int(input("How many sticks (N) in the pile: "))
 ```
## Game Play
Player have to take turn picking until there is no stick left in the pile.
``` sh
    How many stick (N) in pile ?: 5
    There are  5  sticks in the pile
    What is your name: Kawinpat
    Kawinpat, How many sticks you will take (1 or 2): 1   
    Computer take  1  sticks.
    There are 3  left in the pile.

    Kawinpat, How many sticks you will take (1 or 2): 2   
    Computer take  1  sticks.
    Computer is Loser
``` 

## End Game.
Computer win the game.
``` sh
    print(player_name+ " take ",num_stick," sticks.")
    print(player_name+" is Loser")
```

Player win the game
``` sh
    print(bot_name+ " take ",bot_stick," sticks.")
    print(bot_name+" is Loser")
```

## Player Errors Conditons.
Take more that two sticks
``` sh
    if num_stick> 2:
        print("No you cannot take more than 2 sticks! \n")
```

Take less than one stick.
``` sh
    if num_stick<=0:
        print("No you cannot take more less than 1 stick! \n")
```

## Stick left in the pile Error Conditons.
Stick left in the pile cannot less than 0.
``` sh
    if stick_pile<0:
        print("There are no enough sticks to take. \n")
```

# Change Summary
Showing 1 changed file with 65 additions and 43 deletions.
