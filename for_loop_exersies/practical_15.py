# Write a Python program to check the validity of password input by users.

import re

user_input=input("Enter your password : ")
x = True

while x:
    
    if (len(user_input) <6 or (len(user_input)>12) ):
        print("please enter minimum 6 lenth and maximum 12")
        break
    elif not re.search("[a-z]", user_input):
        print("please enter lower case")
        break
    elif not re.search("[A-Z]",user_input):
        print("please enter upper case ")
        break
    elif not re.search("[$#@]",user_input):
        print("please enter($#@) charcater ")
        break
    elif not re.search("[0-9]",user_input):
        print("plese enter (0-9) character ")
        break
    else:
        print(" valid password ")
        x=False
        break

if x :
    print("Not valid password")
     