class Solution(object):
    def isValid(self, s):
        lst = []
        dic = {")":"(", "}":"{","]":"["}
        for c in s:
            if c in dic:
                if lst and lst[-1] == dic[c]:
                    lst.pop(-1)
                else:
                    return False
            else:
                lst.append(c)
        return True if not lst else False
    
        """
        :type s: str
        :rtype: bool
        """
        