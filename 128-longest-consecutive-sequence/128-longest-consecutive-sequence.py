class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        nums_set = set(nums)
        
        result = 0
        
        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set:
                count = 0
                search = nums[i]
                while search in nums_set:
                    count += 1
                    search += 1
                result = max(result, count)
        
        return result
        
        
    