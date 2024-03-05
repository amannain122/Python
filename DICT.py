#DICTIONARIES
cmds={'list': "List Movies",'add':"Add a Movie", 'del':"Delete a Movie",'exit':"Exit the Program"}

a=cmds['list']
b=cmds.pop('exit')
c=cmds.get("add")
print(cmds)
del cmds['del']
print(a,'\n',b,'\n',c)

print(cmds)
cmds.clear()
print(cmds)