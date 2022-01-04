class Solution(object):
    def topKFrequent(self, nums, k):
        lst = []
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = nums.count(i)
        for t,v in dic.items():
            new = []
            new.append(t)
            new.append(v)
            lst.append(new)
        lst.sort(key=lambda x: x[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(lst[i][0])
        return ans
           
        
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        