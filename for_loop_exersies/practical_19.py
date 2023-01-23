#  Write a Python program to print alphabet pattern p.

pattern_str=""
for row in range(0,7):
    for col in range(0,7):
        if ((col == 1 or col == 6)and row!=0 and col==6 )or ((row == 0 or row == 3)and col > 2 and col < 5):
            pattern_str+="*"
        else:
            pattern_str+=" "
    pattern_str+="\n"
print(pattern_str)