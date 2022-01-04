class Solution(object):
    def frequencySort(self, s):
        res = ''
        sList = list(set(s))
        dic, lst = {}, []
        for i in sList:
            if i not in dic:
                dic[i] = s.count(i)
        for k,v in dic.items():
            new = []
            new.append(k)
            new.append(v)
            lst.append(new)
        lst.sort(key=lambda x: x[1], reverse=True)
        for i in lst:
            res += i[0]*i[1]
        return res
            
                
        
        
        """
        :type s: str
        :rtype: str
        """
        