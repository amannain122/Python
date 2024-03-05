# break will exit loop whenever executed
x=0
while x<5:
    print('one time x and break')
    break

# continue doesn't allow to use next statement
while x<5:
    print("x is printed but not next print statement")
    x+=2
    continue
    print("This statement is not printing")

# Walrus operator
while (score:= input("Enter score: "))!=1:
    print("Score is: ",score)