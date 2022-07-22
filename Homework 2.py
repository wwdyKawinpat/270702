while x<0:
    if x<0:
        print("You cannot insert less than 0")
        x = int(input("How many sticks (N) in the pile: "))
    elif x>0:
        x = int(input("How many sticks (N) in the pile: "))

print("There are ",x," sticks in the pile")
name = input("What is your name: ")
y = int(input(name+", How many sticks you will take (1 or 2): "))
count = 0

while x>0:
    if y> 2:
        print("No you cannot take more than 2 sticks!")
        y = int(input(name+", How many sticks you will take (1 or 2): "))
    elif y<=0:
        print("No you cannot take more less than 1 stick!")
        y = int(input(name+", How many sticks you will take (1 or 2): "))
    elif y<=2:
        x=x-y
        count += 1
        if x>0:
            print("There are", x," left in the pile.")
            y = int(input(name+", How many sticks you will take (1 or 2): "))
        elif x<0:
            print("There are no enough sticks to take.")
            y = int(input(name+", How many sticks you will take (1 or 2): "))
        elif x==0: 
            break
print("OK. There is no stick left in the pile. You spent",count, "times.")

