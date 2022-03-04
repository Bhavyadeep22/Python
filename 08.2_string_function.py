a='i love to watch family guy in my free time. This show is very funny.'

# string functions.
print(len(a))       #this give the length of the string
print(a.endswith('time'))    #this will give the output ture or false if the string ends with the correct value you added, here it ends with 'funny' giving output false. 
print(a.count('e'))          #this give the count or total number of occurence of any character in the string.
print(a.capitalize())        # this will make the first letter of the string capital. 
print(a.find('free'))        # this will find the word and gives the index of the first occurance of that word in the string.
print(a.replace('family guy','Suits'))  #this function will replace the old word with the new word.

# ESCAPE SEQUENCES
# \n for new line
# \t for a tab
# \' for a single quote
# \\ for a backslash

b='I paid $5 for a coffe at starbucks. \nI really \'liked the taste \t of \\it.'
print(b)

