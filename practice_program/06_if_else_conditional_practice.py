# write a progeram to find the greatest of four numbers entered by the user.

# a1=int(input('enter a number: '))
# a2=int(input('enter a number: '))
# a3=int(input('enter a number: '))
# a4=int(input('enter a number: '))

# if(a1>a4):
#     n1=a1 
# else:
#     n1=a4
# if(a2>a3):
#     n2=a2
# else:
#     n2=a3
# if(n1>n2):
#     print('the greatest number is: ', n1)
# else:
#     print('greatest number is: ', n2)



# write a program to find out whether a student is pass or fail if it requires total 40% and least 33% in each subject to pass. Assume 3 subjects and take ,marks  as an input from the user.

# m1=int(input('enter marks of subject 1: '))
# m2=int(input('enter marks of subject 2: '))
# m3=int(input('enter marks of subject 3: '))

# f1=(m1+m2+m3)/3

# if(m1<33 or m2<33 or m3<33):
#     print('you are fail')

# elif(f1 <40):
#     print('you are fail due to total percentage is less tha 40')
# else:
#     print('congrats! you passed')



# write a program to check the text entered by user is spam or not


# text=input('enter the text\n')

# if('make a lot of money'in text):
#     spam=True
# elif('buy now' in text):
#     spam=True
# elif('click this' in text):
#     spam= True

# else:
#     spam=False

# if(spam):
#     print('this text is a spam')
# else:
#     print('this text is not a spam')



# #  write a program to find whether a given username contains less than 10 character or not.
# a=input('enter your username\n')
# ln=len(a)

# if(ln>10):
#     print("user name too long")
# else:
#     print('your user name is :', a)

# a=["john", "cena", "jose", "jessica"]
# b=input('enter your name: ')

# if(b in a):
#     print('you are in the list')
# else:
#     print('you are not in the list')






text=input('enter the text\n')

if('John'in text):
    print('test is talking anout john')
elif('john' in text):
    print('test is talking anout john')
elif('JOHN' in text):
    print('test is talking anout john')
elif('jOHN' in text):
    print('test is talking anout john')
elif('JOHN' in text):
    print('test is talking anout john')

else:
    print('there is no reference of john in the text')