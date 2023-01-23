lists = [[1,4,5],[1,3,4],[2,6]]

merge_list=[element for nested_list in lists for element in nested_list]

sort_list=sorted(merge_list)
print(sort_list)
