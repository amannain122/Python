#LIST CAN BE OF ANY DATA TYPE INSIDE []
list1=[1,2,'sma',5]
print(list1)
print(list1[-1])

#TO USE ARRAY - FIRST IMPORT
from array import *

#ARRAY IS COMBINATION OF SAME DATA TYPE WITH ('i,u,f',[])
#ARRAY NEED ('I'- FOR INTEGER; 'U'- FOR UNICODE & 'F'- FOR FLOAT)
arr1=array('i',[1,2])
print(arr1)
arr2=array('f',[3.0,5.5,2.5])
for x in arr1:
    print(x)    
print(arr2)
for y in arr2:
    print(y)
        

#TUPLE IS LIST WITH/ WITHOUT (((parentheses)))        
tuple1=(1,'aman',2,'nain')
tuple2=1,2,'nain','krishna'
print(tuple1[1], tuple2[2])   

#DICTIONARY IS LIST HOLDING KEY-PAIRS in {like-set}
dict1={1:'first',2:"second",'three':3}
dict2=dict([(1,'Aman'),( 'Nain',2),( 3,'Kumar')])
print(dict1)
print(dict2)

#SETS are same as mathematical sets inside {} and can contain all data types
set1={1,87.5,'nain','krishna'}
print(set1)

#RANGE(a,b,c)-->(a,b-1) is limit while "c" is difference
range1=range(1,15)
for z in range1:
    print(z)  


