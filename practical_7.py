# Reverse Integer

x = -123
ans=0

while(x < 0):

    temp= x % 10
    ans=(ans * 10 )+ temp
    x = x// 10

print(ans)