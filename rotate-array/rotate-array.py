class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        rot_pos = k % n
        
        copy = nums[-rot_pos:]
        new = copy + nums[:n-rot_pos]
        
        for i in range(len(nums)):
            nums[i] = new[i]
            
        
        """
        Do not return anything, modify nums in-place instead.
        """
        