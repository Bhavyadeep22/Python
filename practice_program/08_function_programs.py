# def greatest(a,b,c):
#     if a>b:
#         print(str( a ) +' is the greates')
#     elif c>b:
#         print(str(c ) +' is the greatest')
#     else:
#        print(str(b ) + ' is the greatest')

# a=int(input('enter a number: '))
# b=int(input('enter a number: '))
# c=int(input('enter a number: '))

# greatest(a,b,c)

# def farh(cel):
#     return(cel* (9/5)) +32

# c=int(input("enter the temp you want to convert: "))
# f= farh(c)
# print("the temp in fahr is " + str(f))


# def multiply(num):
#     i = 1
#     return (num*i)

# num = int(input("Enter the number: "))
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i} ")

i = 1
def multiply(num):
    for i in range(1,11):
        return (f"{num} X {i} = {num*i} ")

num = int(input("Enter the number: "))
t= multiply(num)
print('the table is ' + str(t))
