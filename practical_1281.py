# 1281. Subtract the Product and Sum of Digits of an Integer

n = [2,3,4]
lenth = len(n)
mul_count=1
sum_count=0
for i in range(lenth):

    mul_count *= n[i]
    sum_count += n[i]
    
result = mul_count - sum_count
print(result)