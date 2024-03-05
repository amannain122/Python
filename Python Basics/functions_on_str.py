# FUNCTIONS
# find functions on a specific data type
# print(dir(data-type))

from slicing import * 
print(aman)
print(aman.count('n'))
print(aman.capitalize())
print(aman.find('i'))
print(aman.title())
print(aman[3:6])
print(aman.swapcase())
print(aman.replace('nain', 'nain1'))
print(aman.isalnum())
print(len(aman))

# FORMATTING
a='aman'
b='kumar'
c='nain'
name='{} {} {}'.format(a,b,c)
print(name.title())
print(" length of different data sequences are:")
length='list={} string={} array={} dict={} range={} tuple={} set={}'.format(len(list1),len(aman),len(arr2),len(dict1),len(range1),len(tuple1),len(set1))
print(length) 

#MORE METHODS
list1.sort()#to sort
list1.reverse()#to reverse the sorted/unsorted list
#CLEAR FUNCTION
list1.clear()
set1.clear()
dict1.pop(1)
set1.remove(89)
del list1[:]

#INSERT list/array.insert(index,"value")
list1.insert(0,"krishna")
set1.update([89])
dict1[1]='first'

