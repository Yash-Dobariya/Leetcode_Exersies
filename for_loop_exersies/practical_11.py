"""Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
   The element value in the i-th row and j-th column of the array should be i*j."""


rows=3
columns=4
mul_list=[[ 0 for j in range(columns) ] for i in range(rows)]

for i in range(rows):
    for j in range(columns):
        mul_list[i][j]= i * j
print(mul_list)