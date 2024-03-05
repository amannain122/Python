#% LISTS - MUTABLE
li1=[2,3,4,'aman','isha']
li=[]

#%% Append to add in list
for i in range(5):
    li.append(li1[i])

#%% POP to remove last item by default or at a particular index
pop1=li.pop()
pop2=li.pop(2)

#%% INSERT to insert value at particular index
li.insert(0, 'nain')
print(li)

#%% REMOVE to delete particular item in list rather than index
li.remove('nain')
print(li)

#%% INDEX to get index of particular item
li.index(2)

#%% 'in' keyword to check item in list just like i in range()
if 'aman' in li:
    li.remove('aman')
    print(li)

a,b=0,0
for i in li:
    a+=i
print(a)

i=0
while i<len(li):
    b+=li[i]
    i+=1
print(b)

#%% ENUMERATE FUNCTION to print items in list while in loop
table=['a','b','c','d','e','f']
for i, letters in enumerate(table,start=1):
    print(i,":",letters)
    
#%% ZIP FUNCTION to form list with two lists
number=[1,2,3,4,5]
for numbers,letter in zip(number,table):
    print(numbers,":",letters)
    
#%% SLICING
table[0:2]
table[:4]
table[1:6:2]
table[::-1]

#%% SORTING as per ASCII VALUES and COUNT tells the no. of occurences
li1.sort()
li.count(5)

#%% COPYING in Lists
#Shallow Copy menas only accessing and changing value in list 2 will change in list1
li2=li1  

#DeepCopy means actual copy
li2=li1.copy()

#%% OTHER FUNCTIONS
import random
random.shuffle(li1) 
random.choice(li1)
max(li)
min(li)
sum(li)

def add_squares(total,current):
    return total+(current*current)
li(add_squares)
import functools
functools.reduce(add_squares, list)
filter(add_squares, iterable)
map(add_squares, iter1)








