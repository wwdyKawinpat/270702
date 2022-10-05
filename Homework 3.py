import random
#Give conditions stick in the pile cannot less than 0
stick_pile = int(input("How many stick (N) in pile ?: "))
while stick_pile<0:
    if stick_pile<0:
        print("You cannot insert less than 0")
        stick_pile = int(input("How many sticks (N) in the pile: "))
    elif stick_pile>0:
        stick_pile = int(input("How many sticks (N) in the pile: "))

print("There are ",stick_pile," sticks in the pile")
# Retrieved player_name.
player_name = input("What is your name: ")
bot_name = 'Computer'
# Insert number of sticks player take.
num_stick = int(input(player_name+", How many sticks you will take (1 or 2): ")) #Player can take only 1 or 2 stick.
count = 0

# Create bot to take a stick with random number of 1 or 2
for i in range(10):
    bot_stick = random.randint(1,2)

# Setting Condition, take until stick in the pile is 0
while stick_pile>0:
    # For each turn player cannot take more than 2 sticks or less than 0 stick.
    if num_stick> 2:
        print("No you cannot take more than 2 sticks! \n")
        num_stick = int(input(player_name+", How many sticks you will take (1 or 2): "))

    elif num_stick<=0:
        print("No you cannot take more less than 1 stick! \n")
        num_stick = int(input(player_name+", How many sticks you will take (1 or 2): "))
    # Setting break, Player lose condition.
    if stick_pile==1 and num_stick==stick_pile:
        bot_stick==0
        print(player_name+ " take ",num_stick," sticks.")
        print(player_name+" is Loser")
        break
    
    if stick_pile-num_stick == 0:
        print(player_name+ " take ",num_stick," sticks.")
        print(player_name+" is Loser")
        break
     # Setting lose condition to bot.   
    if stick_pile<= 3:
        bot_stick=stick_pile-num_stick
        print(bot_name+ " take ",bot_stick," sticks.")
        print(bot_name+" is Loser")
        break
    
    elif stick_pile-bot_stick == 0:
        print(bot_name+ " take ",bot_stick," sticks.")
        print(bot_name+" is Loser")
        break

    # Calculation stick left in the pile.
    elif 0<num_stick<=2:
        for i in range(10):
            bot_stick = random.randint(1,2)
        stick_pile=stick_pile-num_stick-bot_stick     
        print(bot_name+ " take ",bot_stick," sticks.")
        count += 1
        # Repeat statement to play until stick in the pile is 0.
        if stick_pile>0:
            print("There are", stick_pile," left in the pile. \n")
            num_stick = int(input(player_name+", How many sticks you will take (1 or 2): "))
        # Setting condition, player or bot cannot take more than stick left in the pile.
        elif stick_pile<0:
            print("There are no enough sticks to take. \n")
            num_stick = int(input(player_name+", How many sticks you will take (1 or 2): "))
            



#print("OK. There is no stick left in the pile. You spent",count, "times.")
