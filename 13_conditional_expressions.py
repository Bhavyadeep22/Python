
# if the first condition is staisfied it will not run the other conditions.
# From the whole elseif ladder if the first condition is satisfied the other conditions will not run. it will come out of the loop

# a=24

# if(a>3):
#     print('the value of a is greater than 3')                     
# elif(a>9):
#     print('the value of a is greater than 9')
# elif(a>11):
#     print('the value of a is greater than 11')
# elif(a>15):
#     print('the value of a is greater than 15')
# elif(a>19):
#     print('the value of a is greater than 19')
# else:
#     print('the value of a is less than 3,9,11,15 and 19')

# print("done")
#     # the above program will only run the firsr condition as it is satisfied. 



a=24

if(a>3):
    print('the value of a is greater than 3')                     
if(a>9):
    print('the value of a is greater than 9')
if(a>11):
    print('the value of a is greater than 11')

if(a>15):
    print('the value of a is greater than 15')
elif(a>19):
    print('the value of a is greater than 19')
else:
    print('the value of a is less than 3,9,11,15 and 19')

print("done")

a=22
if(a>9):
    print("greater")
else:
    print('lesser')


age=int(input("enter your age "))
if(age>18):
    print('yes')
else:
    print('no')