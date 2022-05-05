class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_count = nums.count(0)
        
        for i in range(zero_count):
            nums.remove(0)
            nums.append(0)
        
        
        
        """
        Do not return anything, modify nums in-place instead.
        """
        