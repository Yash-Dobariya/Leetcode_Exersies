# Binary Search

nums = [-1, 0, 3, 5, 9, 12]
target = 2
l = r = 0


while l <= r:
    m = (r-1)//10
    if nums[m] > target:
        r = m-1
    elif nums[m] < target:
        l = m+1
    else:
        print(m)
print(m)
