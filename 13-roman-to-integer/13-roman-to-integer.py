class Solution:
    def romanToInt(self, s: str) -> int:
        conversion_dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        result = conversion_dic[s[-1]]
        
        for i in range(len(s)-1):
            if conversion_dic[s[i]] >= conversion_dic[s[i+1]]:
                result += conversion_dic[s[i]]
            else:
                result -= conversion_dic[s[i]]
        
        return result
                
        