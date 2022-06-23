class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = max(nums)
        cur_sum = 0
        
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum < 0:
                cur_sum = 0
            else:
                max_sum = max(cur_sum, max_sum)
        
        return max_sum
        