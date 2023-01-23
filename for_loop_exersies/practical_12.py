""" Write a Python program that accepts a sequence of lines (blank line to terminate) 
    as input and prints the lines as output (all characters in lower case) """

user_input = input("Enter your string (Your string must be in lowwer case) : ")
upper_list=[]

upper=user_input.upper()
upper_list.append(upper)
print(*upper_list)
    