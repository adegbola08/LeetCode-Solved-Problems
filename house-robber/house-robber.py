class Solution:
    def rob(self, nums: List[int]) -> int:
        opt1, opt2 = 0, 0
        for i in nums:
            temp = max(opt1+i, opt2)
            opt1 = opt2
            opt2 = temp
        return opt2
            