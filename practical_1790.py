# 1790. Check if One String Swap Can Make Strings Equal

s1 = "kelb"
s2 = "kelb"

for i in range(len(s2)):
    
    if s2[i] in s1  :
       print(True)

    elif s2[i] == s1:
        print(True)
    
    else:
        print(False)
    break