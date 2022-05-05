class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        
        small = strs[0]
        result = ""
        
        for i in range(len(small)):
            
            for j in range(1,len(strs)):
                if small[i] != strs[j][i]:
                    return result
            else:
                result += small[i]
        
        return result
            
        
        