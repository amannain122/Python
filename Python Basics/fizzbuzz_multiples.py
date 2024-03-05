n=int(input('Enter number to start: '))
b=int(input('Enter number to end: '))
for i in range(n,b+1):
    if(i%3==0 and i%5!=0):
        print('Fizz')
    elif (i%5==0 and i%3!=0):
        print('buzz')
        
    elif(i%3==0 and i%5==0):
        print('Fizzbuzz')
    else:
        print(i)
        