class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return []
        
        nums.sort(reverse=True)
        
        cur_max = nums[0]
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] != cur_max:
                count += 1
                cur_max = nums[i]
            
            if count == 3:
                return nums[i]
            
        return nums[0]