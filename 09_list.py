# lists are created using []
a=[1,2,3,3,4,5]
print(a)
# lists can be accssed using index a[0], a[2]...
print(a[3])    #this will give the value from the list with index value 3 (starting from 0)

# we can change the value of the list using following.
a[0]=9912
print(a)


# list can be created with items of different types
c=['xyz', 78, True, False, 9.99]
print(c)

# list slicing
fruits=['apple', 'banana', 'grapes', 'kiwi']

print(fruits[0:2])
fruits.append ('mango') 
print(fruits)