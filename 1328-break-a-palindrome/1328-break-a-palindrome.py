class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)//2
        
        for i in range(n):
            if palindrome[i] != "a":
                return palindrome.replace(palindrome[i],"a",1)
        result = palindrome[::-1]
        res = result.replace(palindrome[0],"b",1)
        return res[::-1] if len(palindrome) > 1 else ""
        