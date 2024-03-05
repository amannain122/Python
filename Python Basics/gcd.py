#Euclid Algorithm for GCD
def gcd(m,n):
        if m<n:
        (m,n)=(n,m)
        if (m%n)==0:
            return(n)
        else:
            diff=m-n
        return(gcd(max(n,diff),min(n,diff)))            
    
 #List Algorithm for gcd
    def gcd1(m,n):
        
        cf = []
        for i in range(1, min(m,n)+1):
            if (m%i)==0 and (n%i)==0:
                cf.append(i)
                return(cf[])
         
#NEW ALG's
def h(x):
    (d,n)=(1,0)
    while d<=x:
        (d,n)=(d*3,n+1)
    return(n)                

def g(n):
    s=0
    for i in range(2,n):
        if n%i==0:
            s+=1
    return(s)

def foo(m):
    if m == 0:
      return(0)
    else:
      return(m+foo(m-1))
  
def f(n): 
    s=0
    for i in range(1,n+1):
        if n//i == i and n%i == 0:
           s = 1
    return(s%2 == 1)

