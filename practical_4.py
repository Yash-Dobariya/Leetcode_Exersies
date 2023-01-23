# Median of Two Sorted Arrays
import numpy as np

nums1 = [1, 2, 2, 3, 4, 3]
nums2 = []
nums3 = []

nums3 = nums1+nums2

sort_array = sorted(nums3)
lenth = len(sort_array)

if lenth % 2 == 0:

    median1 = (lenth)/2
    convert_int = int(median1)
    pri_median1 = sort_array[convert_int]

    median2 = (lenth-1)/2
    convert_int = int(median2)
    pri_median2 = sort_array[convert_int]

    median = (pri_median1+pri_median2)/2
    print(median)

elif lenth % 2 != 0:

    median = (lenth)/2
    convert_int = int(median)
    print(sort_array[convert_int])


"""Secound Method """


nums1.extend(nums2)

median = np.median(nums1)
print(median)