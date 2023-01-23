# 329. Longest Increasing Path in a Matrix

matrix = [[9, 9, 4],
          [6, 6, 8],
          [2, 1, 1]]
# m, n = len(matrix), len(matrix[0])

# def dfs(row, col, prev):

    # base condition : check "out of boundaries" situation and
    # also if "current <= previous" then these are invalid conditions. 

    # if row < 0 or col < 0 or row >= m or col >= n or matrix[row][col] <= prev:
    #     return 0 

#     # expand and look in all four directions using simple depth first search

#     left = dfs(row, col - 1, matrix[row][col])
#     print("left",left)
#     right = dfs(row, col + 1, matrix[row][col])
#     print("right",right)
#     top = dfs(row - 1, col, matrix[row][col])
#     print("top",top)
#     bottom = dfs(row + 1, col, matrix[row][col])
#     print("bottm",bottom)
#     print("prev",prev)
    
#     # return max depth of longest increasing path and 
#     # plus 1 to consider the current element.

#     return max(left, right, top, bottom) + 1
    
# # compute the longest increasing path for each element and
# # update the max value as answer.

# ans = -1
# for row in range(m):
#     for col in range(n):
#         ans = max(ans, dfs(row, col, 0))
        
#         print(ans)


row_len, col_len = len(matrix), len(matrix[0])
paths = [[0 for _ in range(col_len)] for _ in range(row_len)]

for row in range(row_len):
    for col in range(col_len):

        if row < 0 or col < 0:
            print(0) 
  
        if matrix[row][col] > matrix[row][col+1]: 
            paths[row][col] += 1
            print(paths[row][col])
    
        if matrix[row][col] > matrix[row+1][col]:
            paths[row][col] += 1
            print(paths[row][col])

        if matrix[row][col] > matrix[row][col+1]:
            paths[row][col] += 1
            print(paths[row][col])

        if matrix[row][col] > matrix[row-1][col]:
            paths[row][col] += 1
            print(paths[row][col])