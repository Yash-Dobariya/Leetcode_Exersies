# 242. Valid Anagram

s = "nagaram"
t = "anagram"

"""First Method"""

for i in s:
    for j in t:
        pass

if i in j:
    print(True)
else:
    print(False)
    
"""Secound Method"""

if len(s) != len(t):
    print( False)
countS, countT = {}, {}
for i in range(len(s)):
    countS[s[i]] = 1 + countS.get(s[i], 0)
    countT[t[i]] = 1 + countT.get(t[i], 0)
print(countS == countT)