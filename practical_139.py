# Word break

s="le"
word=["le","code"]

n = len(s)
r = [[False for _ in range(n+1)] for _ in range(n)]
for i in range(0, n):

    for j in range(i+1, n+1):

        if i == 0:

            r[i][j] = s[:j] in word
            # print(s[:j], s[:j] in word
            continue

        elif s[i:j] in word:
            
            r[i][j] = r[i-1][i] or r[i-1][j]
            print(r[i-1][i])
          
        else:
            r[i][j] = r[i-1][j]
            print(r[i-1][j])

# print(r[i][j])
print (r[n-1][n])
