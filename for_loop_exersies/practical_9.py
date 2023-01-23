# Write a Python program to get the Fibonacci series

# series=10
# n1, n2 = 0, 1
# for i in range(1,series+1):

#     # fibonacci = (i-1)+(i-2)
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")

def recursive(n):
    if n ==1 :
        return 0
    elif n== 2:
        return 1
    else:
        return recursive(n-1) + recursive(n-2)
   
        
ans=recursive(3)
print(ans)

# 0,1,1,2,3,5,8,13,21

