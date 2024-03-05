#PLOTTING plt.plot(x,y,"TYPES")
#TYPES- r/red line, ro/red dot, bs/blue square, g^/green triangles, r--/dashed
#IMPORT MATPLOTLIB AND STATISTICS FOR GRAPHS
import matplotlib.pyplot as plt
import statistics

list1=[]
for i in range(1,9): 
    n=int(input("Guess the number of balls: "))
    list1.append(n)
list1.sort()
trim=int(0.1*len(list1))
endtrim=int(len(list1)- trim)
list1=list1[trim:endtrim]
print(list1)

xlist=[]    
for i in range(len(list1)):
    xlist.append(5)
    

plt.plot(list1,xlist,'r--')
plt.ylabel('Random')
plt.plot([statistics.mean(list1)],[5],'g^')
plt.plot(statistics.median(list1), [10],'bs')
