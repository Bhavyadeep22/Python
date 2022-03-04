a={
    "pen":"a tool to write",
    "watch": "a tool that tells time",
    'suresh': 24.5, 
    'harman':{'maths':99}, 
    'dhoni':183,
    1:292
}

print(list(a.keys()))       # print the keys of the dictionary.
print(a.values())           # print the values in the dictionary.
print(a.items())            # print a list of (key, value) tuples.
print(a)

# to update dictionary by adding new key value pair from the update_a
update_a={'lion':'king'}
a.update(update_a)
print(a)


# important, could be an interview question 
print(a.get("pen")) # this will print the value associated with "pen"
print(a['pen'])   # this method will print the value associated with "pen"......THIS IS THE SIMILARITY IN THESE TWO METHODS

# WHEREAS THE DISSERENCE BETWEEN .GET AND [] METHOD IS THE FOLLOWING

print(a.get("pen2")) # this will return none if the key is not present in the dictionary,
print(a['pen2'])   # this method will give an error  if the key is not present in the dictionary.
