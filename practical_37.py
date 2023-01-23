from dokusan import generators
import numpy as np

# arr=np.array(list(str(generators.random_sudoku(avg_rank=150))))
# print(arr.reshape(9,9))

suduku = []
# user_input=int(input("Enter your value : "))
for i in range(0,9):

    row = list(input("Enter Element of row {} without any spaces : ".format(i+1)))
    row = [int(i) for i in row]
    suduku.append(row)
print("Enter suduku :")
print(np.matrix(suduku))
print("Your Suduku :")
try:
    def possible(row, col, n):

        global suduku
        for i in range(0,9):
            if suduku[row][i] == n:
                return False

        for i in range(0,9):
            if suduku[i][col] == n:
                return False
        box_y = (row//3)*3
        box_x = (col//3)*3
        for i in range(0,3):
            for j in range(0,3):
                if suduku[box_y+i][box_x+j] == n:
                    return False
        return True 

    def solve():
        for row in range(0,9):
            for col in range(0,9):
                if suduku[row][col] == 0:
                    for n in range(1, 10):
                        if possible(row, col, n):
                            suduku[row][col] = n
                            solve()
                            suduku[row][col] = 0
                    return False
        print(np.matrix(suduku)) 
    solve()
except :
    print(" Please Enter vaild suduko!! ")