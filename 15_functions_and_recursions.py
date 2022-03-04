##### a function is group of statements that perform specific tasks 

# two tyes: built in and user defined. 

# def greet(name):
#     print("hello " + name +' how are you?')

# # name=input('entre your name: ')   
# greet(name)




def greatest(a,b,c):
    if a>b:
        print(str( a ) +' is the greates')
    elif c>b:
        print(str(c ) +' is the greatest')
    else:
       print(str(b ) + ' is the greatest')

a=int(input('enter a number: '))
b=int(input('enter a number: '))
c=int(input('enter a number: '))

greatest(a,b,c)