a=input("Enter String: ")
counter=0
c=len(a)
s=''
j=1
for i in range(c):
    if a[i] == a[c-j]:
        s+=a[i]
        counter+=1
    j+=1

print(s)
print(counter)  
