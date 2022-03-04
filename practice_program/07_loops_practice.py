############ write a program to print the table using for loop

# num=int(input('enter a number\n'))

# for i in range(1,11):
#     # print(str(num) +'X' + str(i) + '=' + str(i*num))
#     print(f'{num}X{i}={num*i}')    #this is called f string this helps in concatenating the strings easily.


##################### using WHILE loop
# num=int(input("Enter any number "))
# i=1
# while i<=10:
#     print(str(num)+"X"+str(i)+"="+str(i*num))
#     i=i+1


################ write a program to greet all the person names stored in a list and which starts with S

# l1=["Sachin", "Jack", "Sam","Suraj","sham", "Rahul"]

# for name in l1:
#     if name.startswith("S"):
#         print ("Hello " + name)


######################## write a program whether the given number is prime or not.

# num=int(input("Enter any number: "))
# prime=True
# for i in range(2,num):
#     if(num%i==0):
#         prime=False
#         break
# if prime:
#     print('the given number is a prime number')
# else:
#     print('this is not a prime number')


################## write a program to find the sum of first n natural number using while loop
# num = int(input("Enter a number: "))
# sum=0
# while(num > 0):
#        sum = num+sum
#        num =num- 1
# print("The sum is", sum)

# ################## write a program to calculate the factorial of a given number using for loop
# num=int(input("Enter any number: "))
# factorial=1
# for i in range(1, num+1):
#     factorial=factorial * i
# print(f'the factorial of {num} is : {factorial}')



################################# print table in a reverse order 

num = int(input("Enter Number: "))
for i in range (10,0,-1):
    print(f"{num} X {i} =  {num*i}")

