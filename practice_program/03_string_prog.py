# write a prog. to display  a user name followed by good afternoon using input function.

from sqlite3 import Date


a=input('enter your name\n')
print("Good Afternoon, "+a  )


# Write a program to fill in a letter template givenbelow with name and date.
letter='''Dear <|NAME|>,

You are selected!

Date:<|DATE|>
'''
name=input('Enter your name\n')
date=input('Enter Date\n')
letter=letter.replace('<|NAME|>', name)
letter=letter.replace('<|DATE|>', date)

print(letter)