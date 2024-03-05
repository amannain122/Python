h=int(input("Enter hour: "))
m=int(input("Enter minutes: "))

hours=(h*60+m)*0.5
min=m*6

angle= abs(hours-min)
if (360-angle)<angle:
    angle=360-angle
print(angle)