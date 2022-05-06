class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        number = ""
        
        for i in range(len(digits)):
            number += str(digits[i])
        
        return list(str(int(number) + 1))
        