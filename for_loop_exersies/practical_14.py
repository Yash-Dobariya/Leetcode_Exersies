"""rite a Python program which accepts a sequence of comma separated 4 digit binary 
   numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence."""


user_input=input("Enter your string : ")
digit_count=0
digit_char=0
flag = True

for i in user_input:
    if i.isdigit():
        digit_count+=1

    elif i.isalpha():
        digit_char+=1

print("digit",digit_count)
print("string",digit_char)

