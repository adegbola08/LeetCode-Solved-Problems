class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        return min(count, key=count.get)
        
        
        """for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]"""
        