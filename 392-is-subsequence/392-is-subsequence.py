class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) < 1:
            return True
        if len(t) < 1:
            return False 
        
        pos = 0
        
        for i in range(len(t)):
            if t[i] == s[pos]:
                pos += 1
            if pos == len(s):
                return True
            
        return False if pos != len(s) else False
        