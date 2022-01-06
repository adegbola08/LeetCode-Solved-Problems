class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.find(needle)
        elif needle not in haystack:
            return -1
        else:
            return 0
        
        
        
        
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        