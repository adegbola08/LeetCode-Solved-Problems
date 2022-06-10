class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        needed = []
        
        for i in range(len(numbers)):
            if needed and numbers[i] in needed:
                return [needed.index(numbers[i])+1, i+1]
            needed.append(target-numbers[i])
            
        