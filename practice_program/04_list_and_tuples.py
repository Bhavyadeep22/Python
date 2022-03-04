# #write a prog to store 5 names of the fruits entered by the user.

# f1=input("enter fuit's name 1: ")
# f2=input("enter fuit's name 2: ")
# f3=input("enter fuit's name 3: ")
# f4=input("enter fuit's name 4: ")
# f5=input("enter fuit's name 5: ")

# list=[f1, f2, f3, f4, f5]
# print(list)
# wrp to count number of zeros in tuple
a=(1,4,5,3,7,2,1,35,6,67,1,1,1,1,1,1,1,1,11,3,55,789,9,666,3,2,5,1,1,1,1,1,1)
print(a.count(1))



a=[1,3,4,4,4,3,3,3,33,3,3,3,34,5,5,5,3,3,33,3,5,34,41,12,1,1,32,3,4,4,4,4,4,4,4,4,]    #wrp to sum the list 
print(sum(a))
# write a program to accept marks from 5 students and display in sorted manner

s2=int(input("entre your marks: "))                          #int will give the output in the integer form.
s3=int(input("entre your marks: "))
s4=int(input("entre your marks: "))
s5=int(input("entre your marks: "))
s1=int(input("entre your marks: "))

l1=[s1, s2, s3, s4, s5]
l1.sort()
print(l1)