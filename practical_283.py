# 283. Move Zeroes

nums = [0,1,0,3,12]
"""First Method"""
i = 0

for j in range(len(nums)):
    if nums[j] != 0:
        nums[i],nums[j] = nums[j], nums[i]
        i+= 1
print(nums)
    
"""Secound Method"""

count_zero = nums.count(0)
for i in range(count_zero):
    nums.remove(0)
    nums.append(0)
print(nums)