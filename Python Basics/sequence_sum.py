#Loops
first=int(input("Enter starting number: "))
last=int(input("Enter last number till you want sum: "))
choice=int(input("Enter 1 for OddSum and 2 for EvenSum: "))
sum=0

if(choice==1 and first%2==1):
    for i in range(first,last+1,2):
        print(i)
        sum=sum+i
if(choice==1 and first%2!=1):
    for i in range(first+1,last+1,2):
        print(i)
        sum=sum+i
if(choice==2 and first%2==0):
    for i in range(first,last+1,2):
        print(i)
        sum=sum+i
if(choice==2 and first%2!=0):
    for i in range(first+1,last+1,2):
        print(i)
        sum=sum+i 
if(choice!=1 and choice!=2):
    for i in range(first, last+1):
        print(i)
        sum=sum+i
        
print("Your sum is: ",sum)