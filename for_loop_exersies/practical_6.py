# Write a Python program to count the number of even and odd numbers from a series of numbers.\

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
count_even=0
count_odd=0

for i in numbers:
    if i %  2 == 0:
        count_even+=1
    else:
        count_odd+=1
print("even number : ",count_even)
print("odd  number : ",count_odd)

    
    
    
    
    
    # if i % 2 == 0:
    #     even_num=numbers.count(i)
    #     print(even_num)
    # else:
    #     odd_num=numbers.count(i)
    #     print(odd_num)

    