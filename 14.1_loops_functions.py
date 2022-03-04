# Range function
# it is used to genrate a sequence of numbers

# for i in range(7):     # print till n-1
#     print(i)
# print('Done')




# for i in range(1,7):    # range starts from 1
#     print(i)
# print('Done')


# for i in range(1,7,2):    # range starts from 1, loop stops at 7 and  2 is the step size
#     print(i)
# print('Done')





# BREAK STATEMENT- It basically breaks the loop.

# for i in range(1,7):    # range starts from 1
#     print(i)
#     if i == 3:
#         break 
# else:                        
#      print('Done')
# this will not print 'done' because it is not a successfull termination of the loop.
# else function with for only works when the loop is completed successfully, If the loop is executed completely then print else otherwise if the loop is stopped by break dont execute else

# CONTINUE STATEMENT- it basically skips the value 

# for i in range(1,7):    
#     if i == 3:
#         continue
#     print(i)


# PASS STATEMENT- it is a null statement, means do nothing

# i=9
# if i>10:
#     pass                                          # this will pass the condition and print hello world
# print('hello world')

###################################3 writa a program to print table in a reverse order.

num = int(input("Enter Number: "))
for i in range (10,0,-1):
    print(f"{num} X {i} =  {num*i}")