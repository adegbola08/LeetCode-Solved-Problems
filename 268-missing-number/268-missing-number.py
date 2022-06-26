class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0
        total = 0
        
        for i in range(len(nums)):
            total += nums[i]
            count += 1
        return (count *(count+1)//2) - total
        