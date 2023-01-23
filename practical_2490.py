# 2490. Circular Sentence

user_input=(input("Enter your syntext : "))
first_char=user_input[0]
last_char=user_input[:-2:-1]

if first_char==last_char:
    print("True")
else:
    print("False")