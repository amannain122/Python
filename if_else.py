 # SFEMS PRINCIPLES FOR PYTHON USE
code=input("Enter type code r/w: ")

if code.lower()=='r':
    invoice_total=int(input("Enter invoice total: "))
    if invoice_total>=250:
        dis_per=0.2
    elif invoice_total>=100:
        dis_per=0.1
    elif invoice_total<100:
        dis_per=0
    print("Discount Percent is: ",dis_per)
    
elif code.lower()=='w':
    invoice_total=int(input("Enter invoice total: "))
    if invoice_total>=500:
        dis_per=0.5
    elif invoice_total<500:
        dis_per=0.4
    print("Discount Percent is: ",dis_per)
    
else:
    print("Please enter only 'r' or 'w'")
    



