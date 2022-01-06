class Solution(object):
    def longestCommonPrefix(self, strs):
        first = min(strs, key=len)
        res = ''
        for i in range(len(first)):
            for j in range(len(strs)):
                p = strs[j]
                if first[i] == p[i]:
                    j+=1
                else:
                    return res
            res += first[i]
            i+= 1
        return res
                
                
        
       
        """
        :type strs: List[str]
        :rtype: str
        """
        