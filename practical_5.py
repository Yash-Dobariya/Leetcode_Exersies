#  Longest Palindromic Substring

str1 =  "babad"


left = str1[0]
lenth = len(str1)
right = len(str1)-1

for i in range(lenth):

    if str1[i] != str1[right] :
        right -= 1

        print(str1[:right],end="")
        break