class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        
        for ch in s:
            if ch.isalnum():
                word += ch.lower()
        
        l, r = 0, len(word)-1
        
        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        
        return True
        
        """return word == word[::-1]"""
        