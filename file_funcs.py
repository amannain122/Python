a=open("abc.text",r)
with open("abc.txt",w) as file:
    file.read()
    file.readlines()# open file as list
    file.readline()# read single line of file
    for line in file:
        line=line.replace("aman", "nain")# change content of line
        file.append(line)#update the changes
        