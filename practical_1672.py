# 1672. Richest Customer Wealth

accounts = [[1,2,3],[3,2,1]]
lenth=len(accounts)
row_lenth = len(accounts[0])
a=[]
for i in range(lenth):
    for j in range(row_lenth):
        s=sum(accounts[i])
        a.append(s)
print(max(a))

