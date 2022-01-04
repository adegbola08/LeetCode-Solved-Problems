class Solution:
    def rob(self, nums: List[int]) -> int:
        rob, rob1 = 0, 0
        for i in nums:
            temp = max(rob + i, rob1)
            rob = rob1
            rob1 = temp
        return rob1
            