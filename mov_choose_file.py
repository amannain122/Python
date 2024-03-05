a=open("file1.txt",'r')
movies=a.readlines()

# movies=["Monty Python and the Holy Grail",'Cat on a Hot Tin Roof', 'On the Waterfront']
cmds={'list': "List Movies",'add':"Add a Movie", 'del':"Delete a Movie",'exit':"Exit the Program"}
print("Please choose from the following Commands\n\n",cmds)
cmd=input("Please Enter Command: ")

while cmd.lower()!="exit":
    if cmd.lower()=='list':
        number=[1,2,3,4,5]
        for numbers,items in zip(number,movies):
            print('\n',numbers,". ",items,'\n')
    elif cmd.lower()=='add':
        a=str(input("Please Enter the Movie Name: "))
        movies.append(a)
        print(a+" was added.\n")     
    elif cmd.lower()=='del':
        while True:
            try:
                b=int(input("Enter Movie Number to Delete: "))
                movie = movies.pop(b-1)
                print(movie, " was deleted\n")
                break
            except ValueError:
                print("Please try again entering a number")
    else:
        print("Please enter a correct input\n")
    cmd=input("Please Enter Command: ")

print("Thank you for interacting")

