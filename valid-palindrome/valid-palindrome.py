class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        
        for c in s:
            if c.isalnum():
                word += c.lower()
                
        if word == "".join(reversed(word)):
            return True
        return False