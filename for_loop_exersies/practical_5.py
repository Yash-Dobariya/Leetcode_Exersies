# Write a Python program that accepts a word from the user and reverse it

user_input=(input("Enter your string : "))

for char in range(len(user_input) - 1,-1,-1):
    print(user_input[char], end="")
    
    
    