#TRIMMED MEAN FOR ESTIMATION
#REMOVE 5-10% FROM EXTREMES
#THEN AVERAGE THE DATA FOR ESTIMATION
#USE STATS FOR MEAN FUNCTION
from statistics import mean
list1=[]
for i in range(1,11):
    n=int(input("Guess the number of balls: "))
    list1.append(n)
print(list1)
list1.sort()
print(list1)
trim=int(0.1*len(list1))
endtrim=int(len(list1)- trim)
list1=list1[trim:endtrim]
print(list1)
est=mean(list1)
print(est)

    
    