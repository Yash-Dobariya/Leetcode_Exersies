# 350. Intersection of Two Arrays II.
"""1 Question"""
nums1 = [1,2,2,1]
nums2 = [2,2]

"""2 Question"""
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

l=[]

for i in nums1:
    if i in nums2:
        l.append(i)
print(l)