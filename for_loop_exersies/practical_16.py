""" Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. 
    The numbers obtained should be printed in a comma-separated sequence."""

even_list=[]

for i in range(100,401,2):
    a=str(i)
    even_list.append(a)
print(','.join(even_list))

