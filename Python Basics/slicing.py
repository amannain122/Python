#SLICING obj[from:upto:diff] // obj[slice(from,upto,diff)]

from data_sequence import *
aman='aman nain'
print(aman[1:])
print(list1[0:5:2])
print(aman[slice(1,5)])
print(tuple1[2:4])
#Set cannot be sliced
# print(set1[0:1])
#Dictinary can also not be sliced
# print(dict1[0:])
print(arr2[:2])
print(arr1[0:2:2])


#CONCATENATION  + or ,

print(aman+'','nain')
print(tuple1+tuple2)
print(tuple1,tuple2)
list1+=['nain']
print(list1+[1,2.3,'sam'])
#array should be of same typle i.e i or f to use +
print(arr1+ array('i',[1,2,3]))
print(arr1 , arr2)

#MULTIPLICATION JUST REPEATS THE DATA
print(tuple1[2:3]*5)
print(aman*2)

