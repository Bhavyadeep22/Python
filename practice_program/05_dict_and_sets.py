# # wrp to create a dict of hindi words, provide user to look it up

# dict={
# 'hara':'Green',
# 'kala':'Black'
# }

# print('options are ', dict.keys())

# a=input("enter a word ")
# # print('the meaining of the word is: ', dict[a]) , this will give na error when the word entred by the user is not in the dict

# print('the meaining of the word is: ', dict.get(a)) # this will not give an error in the output but will return the none value keeping our
# # program error free because of get function


#WRP TO INPUT 8 NUMBERS FROM USER AND display all unique values.
# n1=int(input('enter a number 1: '))
# n2=int(input('enter a number 2: '))
# n3=int(input('enter a number 3: '))
# n4=int(input('enter a number 4: '))
# n5=int(input('enter a number 5: '))
# n6=int(input('enter a number 6: '))
# n7=int(input('enter a number 7: '))
# n8=int(input('enter a number 8: '))

# s={n1,n2,n3,n4,n5,n6,n7,n8}
# print(s)


s={20,20.0,'20'}
print(s)
print(len(s))

# Create an empty dict. allow 4 friends to enter their fav games as values and use keys as their names. Assume that their names are unique.

fav_games={}
a=input("enter your fav game John\n ")
b=input("enter your fav game Harry\n ")
c=input("enter your fav game Jack\n ")
d=input("enter your fav game Gezy\n ")

fav_games['john']=a
fav_games['harry']=b
fav_games['jack']=c
fav_games['gezy']=d

print(fav_games)

# if the names are the same it will overwrite the value with last input,
# whereas if the games are same it will give {'john': 'cricket', 'harry': 'basketball', 'jack': 'cricket', 'gezy': 'hockey'}
# Keys should be Unique but values can be same 
# we cannot add list in a set because lists are unhashable, can be changed. whereas we can add tuple in a set as tuples are immutable.