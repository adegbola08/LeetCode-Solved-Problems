class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        
        for c in s:
            if c.isalnum():
                word += c.lower()
           
        l, r = 0, len(word)-1
        
        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        
        return True
        
        """if word == word[::-1]:
            return True
        return False"""