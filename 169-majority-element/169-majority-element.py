class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        
        for elem in nums:
            if elem in count:
                count[elem] += 1
            else:
                count[elem] = 1
            if count[elem] >= len(nums)/2:
                return elem
        