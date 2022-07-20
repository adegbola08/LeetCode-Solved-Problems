class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        
        l,r = 0, len(nums)-1
        
        while l <= r:
            mid = (l + r)//2
            
            if nums[mid] == target:
                while mid-1 >= 0 and nums[mid-1] == target:
                    mid -= 1
                first = mid
                break
            elif nums[mid] > target:
                r = mid -1
            else:
                l = mid + 1
            
        
        if first != -1:
            new = first
            while new+1 < len(nums) and nums[new+1] == target:
                new += 1
            print(new)
            last = new
        
        return [first, last]
        