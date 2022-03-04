
b=set()
# Adding values to an empty set using .add method
b.add(4)
b.add(5)
b.add(4)     # adding same value more than once does not change a set. It will take only single value.
b.add(5)
# b.add([1,2,3,4])   ...... Cannot add list in the sets as list and dictionarycan be changed (both are unhashable) whereas we can add tuple into the sets because tupes are immutable, cant be changed.
b.add((1,2,3))
print(b)

# properties of sets
# unordered- elements order doesnt matter
# unindexed- cannot access elements by index
# unchangeable, no duplicate values. 


#LENGTH OF THE SET
print(len(b))     # PRINTS THE LENGTH OF THE SET.

# REMOVAL OF AN ITEM FROM THE SET
b.remove(5)       #removes the value(5) from the set.

# REMOVES TGE ELEMENT FROM THE SET AND RETURNS THE SET
b.pop()

# EMPTIES THE SET
# b.clear()

# INTERSECTION RETURS THE COMMON ITEMS FROM BOTH THE SETS
# b.intersection()

# UNION RETURNS THE NEW SET WITH ALL THE ITEMS FROM BOTH SETS
# b.union()
print(b)