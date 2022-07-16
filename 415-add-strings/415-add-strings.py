class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        res = ""
        
        i = 0
        carry = 0
        
        while i < len(num1) or i < len(num2) or carry:
            val1 = num1[i] if i < len(num1) else 0
            val2 = num2[i] if i < len(num2) else 0
            
            total = int(val1) + int(val2) + carry
            carry = total // 10
            res += str(total % 10)
            
            i += 1
        
        return res[::-1]
            
        