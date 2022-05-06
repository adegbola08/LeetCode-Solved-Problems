class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]
        
        
        """nums.sort()
        
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                return nums[i-1]"""
        
        