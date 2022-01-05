class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before, after = 1, 1
        res = []
        for i in nums:
            res.append(before)
            before *= i
        for i in range(len(nums)-1,-1,-1):
            res[i] = after * res[i]
            after *= nums[i]
        return res
            
            
            
               
            