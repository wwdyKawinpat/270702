# Create empty list
x = []
# Retrieved number of number and Checking minus number.
n = int(input("How many numbers do you want? :"))
while len(x) < n:
    if len(x) < n:
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

# Join number in list.
result=''.join(x)
# Print Largest number form.
print(result)
print(x)

