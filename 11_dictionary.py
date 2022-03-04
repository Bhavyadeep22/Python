# a collection of key value pair
# unordered
# mutable
# cannot have duplicate keys, if you do it will overwrite the key. 

mydict={
    "pen":"a tool to write",
    "watch": "a tool that tells time"
}

print (mydict['watch'])
print (mydict['pen'])


marks={'suresh': 24.5, 
'harman':{'maths':99}, 
'dhoni':183}


print(marks['dhoni'])
print(marks['suresh'])
print(marks['harman']['maths'])