# Longest Common Prefix

strs = ["flower","flow","flight"]

lenth = len(strs[0])

for item in range( len(strs)):

    lenth = min(lenth, len(strs[item]))

    while lenth > 0 and strs[0][0:lenth] != strs[item][0:lenth]:

        lenth -= 1
print (strs[0][0:lenth])
    
    # break
    