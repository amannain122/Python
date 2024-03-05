#Cleaning data for estimation by removing extremes(list, percentage)

from scipy import stats
list1=[]
for i in range(1,11):
    n=int(input("Guess the number of balls: "))
    list1.append(n)
print(list1)
list1.sort()
est=stats.trim_mean(list1,0.1)
print(est)