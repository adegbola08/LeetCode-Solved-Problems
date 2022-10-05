class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = 0
        count = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pos], nums[i] = nums[i], nums[pos]
                count += 1
                pos += 1
            
        return count
        