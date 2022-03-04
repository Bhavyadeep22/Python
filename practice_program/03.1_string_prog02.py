#write a program to detect double spacs in the string.

a= 'The Python programming language has a wide range of  syntactical constructions.'

doublespaces=a.find('  ')     # this will find the spaces and give the index value of it as an output

print(doublespaces)


# write a peogram to replace the double spaces with the single spaces


a= 'The Python programming  language has a  wide  range of  syntactical constructions.'

a=a.replace('  ',' ')          #this will find the double spaces in the string and replace it with the single space.

print(a)