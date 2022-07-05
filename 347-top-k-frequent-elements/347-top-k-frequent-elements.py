class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}
        
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        
        result = set()
        
        for i in range(k):
            temp = max(dic, key=dic.get)
            result.add(temp)
            dic.pop(temp)
        
        return result
            