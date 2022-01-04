class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[pos] = nums[i]
                count += 1
                pos += 1
        return pos
                
            
                