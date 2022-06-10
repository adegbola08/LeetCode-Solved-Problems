class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]
        
        
        """needed = []
        
        for i in range(len(numbers)):
            if needed and numbers[i] in needed:
                return [needed.index(numbers[i])+1, i+1]
            needed.append(target-numbers[i])"""
            
        