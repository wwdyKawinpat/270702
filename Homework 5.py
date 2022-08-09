x = []
while len(x) < 4:
    if len(x) < 4:
        num = int(input("Enter your number :"))
        if num >= 0:
            x.append(num)
        elif num < 0:
            print("You cannot enter minus number, Please enter again.")

for i in range(len(x)):
        x[i]=str(x[i]) #Convert array in to str.

for i in range(len(x)):
        for j in range(1+i,len(x)):
            if x[j]+x[i]>x[i]+x[j]:
            #Checking Possible Largest number by index by index
            #if [1]+[0] > [0]+[1] swap [1] and [0]
            #finding maximun value in each pair.
                x[i],x[j]=x[j],x[i] 

result=''.join(x)
print(result)
print(x)

