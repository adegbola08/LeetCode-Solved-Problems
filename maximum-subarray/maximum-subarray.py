class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        ans = 0
        for i in nums:
            if ans < 0:
                ans = 0
            ans += i
            res = max(res, ans)
        return res
            