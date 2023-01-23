#  Write a Python program to print alphabet pattern O.

result_str=""
for row in range(0,7):
    for column in range(0,7):
        if (((column == 1 or column == 5) and row != 0 and row != 6 ) or ((row == 0 or row == 6 )  and column > 1 and column < 5 )):  
            result_str+="*"
        else:      
            result_str+=" "
    result_str=result_str+"\n"
print(result_str)