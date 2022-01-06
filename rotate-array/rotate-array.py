class Solution(object):
    def rotate(self, nums, k):
        if k < len(nums):
            a = len(nums) - k
            last = nums[0:a]
            first = nums[a:]
            nums[0:k] , nums[k:]= first,last
            return nums
        for i in range(k):
            temp = nums[-1]
            for j in range(len(nums)-1,-1,-1):
                nums[j] = nums[j-1]
            nums[0] = temp
        

        
        
        """
        for i in range(1,k+1):
            nums.insert(0,nums.pop(-1))
            i+=1
        """
        
        
        
        """i = 1
        while i <= k:
            nums.insert(0,nums[-1])
            nums.pop(-1)
            i+=1"""

        
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        