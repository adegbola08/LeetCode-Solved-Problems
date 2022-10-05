class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        result = 0
        pos = len(s)-1
        
        while s[pos] != " " and pos >= 0:
            result += 1
            pos -= 1
            
        return result
        