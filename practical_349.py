# 349. Intersection of Two Arrays.
"""1 Question"""
nums1 = [1,2,2,1]
nums2 = [2,2]

"""2 Question"""
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]

list1=[]



for i in nums1:
    if i in nums2:
        list1.append(i)
lis=set(list1)
l=list(lis)
print(l)