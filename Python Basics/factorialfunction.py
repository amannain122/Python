def factorial(n):
    if n<=0:
        return(1)
    else:
            fact=(n*factorial(n-1))
    return(fact)
n=int(input("Enter number: "))
print(factorial(n)) 
