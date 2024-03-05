#EXTERNAL FILES
#open('filename', 'mode'): MODE- R/READ, W/WRITE, R+/READ AND WRITE
# RANDOM 
#random.RANDOM NUMBER B/W 0-1
#random.randrange/randint CHOOSE RANDOM from SEQ--list,tuple
import random


def evolve(x):
    ind=random.randint(0,len(x)-1)
    p=random.randint(1,100)
    if (p==1):
        if(x[ind]=='0'):
            x[ind]=='1'
        else:
            x[ind]=='0'
    return(x)

with open("dna.txt") as dna:
    x=dna.read()
    x=list(x) 
    
# =============================================================================
# import pandas as pd
# x=pd.read_table('dna.txt',na_values='??')
# x=list(x)
# =============================================================================
    
for i in range(1,10000):
    evolve(x)    
print(x)