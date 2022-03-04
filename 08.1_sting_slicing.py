a="hello "
name= "James "    
b= "How are you?"
print(type(name))
print(a + name+ b )      #concatenation strings
                         #or c=a+name+b
                         #print(c)


print(name[4])       #name[4]=a-- cant change, does not work.
print(name[0:4])      #0:4 means 0,1,2,3 vale from the string will be printed, in this case JAME. 
                        #this is called STRING SLICING.
print(name[:4])      #same as name[0:4]
print(name[0:])      # will give value till last. same as name[0:5]
print(name[-4:-1])    #same as name[1:4]
print(name[-1])    #negative indices, this is used to find the last value of string, in this case its blank space.
print(name[1:4:2])

