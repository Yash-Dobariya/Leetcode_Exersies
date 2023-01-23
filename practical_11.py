# Container With Most Water

height = [1,8,6,2,5,4,8,3,7]
l=0
r = len(height)-1
arealist = []

while l != r :
    
    area = (r-l) * min(height[l] , height[r])
    arealist.append(area)

    if height[l] < height [r]:
        l += 1

    else:
        r -= 1
print(arealist)        
print(max(arealist))