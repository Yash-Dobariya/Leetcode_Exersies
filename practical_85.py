# 85. Maximal Rectangle

matrix = [[1, 0, 1, 0, 0],
          [1, 0, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 0, 0, 1, 0]]

num_col = len(matrix[0])
num_row = len(matrix)
max_rec=[]
sum_matrix = []

for row in range(num_col):
    sum = 0
    left = 0
    right = num_col-1

    for col in range(num_row):

        if matrix[col][row] == 0:

            sum =0
        sum += matrix[col][row]
    sum_matrix.append(sum)
    print(sum_matrix)

    while left != right:

        area=(left - right) * min(sum_matrix[left] , sum_matrix[right])
        max_rec.append(area)

        if (sum[left] < sum[right]):
 
            left += 1
        else:

            right -= 1
        
    print(max(max_rec))     
print(sum_matrix)