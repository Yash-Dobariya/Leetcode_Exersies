#  //Top K Frequent Elements?
nums = [1,2,2,3,3]
k = 2


class Solution:
    def topKFrequent(self, nums, k: int):
        d={}
        for each in range(len(nums)):
            if nums[each] not in d:
                d[nums[each]]=0
            d[nums[each]]+=1
        res=[]
        if len(d)==k:
            return d.keys()
        l=sorted(d.values(),reverse=True)
        for i in range(k):
            for k,v in d.items():
                if l[i]==v:
                    res.append(k)
                    d[k] = -1
        return res




        