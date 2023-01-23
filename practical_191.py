n = "0000000100000000000001"
lenth=len(n)
count = 0

for i in range(lenth):
    if n[i] ==  "1":
        count+=1        
print(count)

    