class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_needed = []
        
        for i in range(len(nums)):
            if nums[i] in nums_needed:
                return [nums_needed.index(nums[i]), i]
            nums_needed.append(target-nums[i])
        
        
        """for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums and nums.index(temp) != i:
                return [i, nums.index(target-nums[i])]"""
        