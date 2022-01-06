class Solution(object):
    def isPalindrome(self, s):
        c = ''
        for i in s:
            if i.isalnum():
                c += i
        y = (''.join(reversed(c)))
        if y.lower() == c.lower():
            return True
        return False
        
        
        
        
        """
        :type s: str
        :rtype: bool
        """
        