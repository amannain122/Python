# MAGIC SQUARE
# sum=n(n**2+1)/2
# 1 is located at right most coloumn in middle row(n/2,n-1) i.e (p,q)
# p is row && q i coloumn
# next number is at (p-1,q+1)
# if this pos. is acquired, new position is (p+1, q-2)
# if p is n//change to 0  OR is -1//change to n-1
# if p is -1//change to 0 && q is n//change to n-2

# =============================================================================
#n=3
            (q)
        
        0   1   2  
        
    0   x1  x2  x3

(p) 1   x4  x5  1

    2   x7  x8  x9
# =============================================================================

post of 1: (n//2,n-1)=(p,q)=(1,2)

post of 2:(p-1,q+1)=(0,3)=(0,0)

post of 3:(p-1,q+1)=(-1,1)=(3-1,1) = (2,1)

post of 4:(p-1,q+2)=(1,2)=post of 1
    :(p+1,q-2)=(1+1,2-2) = (2,0)
    
post of 5=(p-1,q+1)=(1,1)

post of 6=(p-1,q+1)=(0,2)

post of 7=(-1,3)=(0,1)

post of 8:(p-1,q+1)=(-1,2)=(2,2)

post of 9:(1,0)