class Solution:
    def sortColors(self, nums: List[int]) -> None:
        import collections
        
        count = collections.Counter(nums)
        start = 0
        
        for i in range(3):
            nums[start: start + count[i]] = [i]*count[i]
            start += count[i]
            
        return nums
        
        