############################### Star pattern
row=4
for i in range(4):    # 4 here represents the number of rows. number of times the loop will run
    print('*'*(i+1))
########################################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

rows = 6                   # if you want user to enter a number, uncomment the below line
                           # rows = int(input('Enter the number of rows'))
                           # outer loop

for i in range(rows):
                                # nested loop
    for j in range(2*i-1):      # this will print odd number os stars in a pattern
                                # display number
        print("*", end=' ')
                                # new line after each row
    print('')

############################################################################################################