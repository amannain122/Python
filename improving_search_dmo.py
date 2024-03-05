import numpy as np
p=0
for i in np.arange(-5000,5000,1):
    for x2 in np.arange(-5000,5000,1):
        a=(60/1+(i+1)**2 + (x2-3)**2)+(20/1+(i-1)**2 + (x2-3)**2)+(30/1+(i)**2 + (x2+4)**2)
        
        if p>a:
            p=a

print(p)