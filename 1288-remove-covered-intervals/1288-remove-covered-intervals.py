class Solution(object):
    def removeCoveredIntervals(self, lst):
        lst.sort(key=lambda x:x[1])
        new = list(lst)
        new.sort(key=lambda x:x[1], reverse=True)
        count = 0
        
        for i in range(len(lst)):
            start = lst[i][0]
            stop = lst[i][1]
            new.remove(lst[i])
            
            for j in range(len(new)):
                if start >= new[j][0] and stop <= new[j][1]:
                    break
            else:
                count += 1
            new.append(lst[i])
            
        return count
        
        
        
        
        
        
        """
        lst.sort(key=lambda x:x[1])
        count = 1
        
        for i in range(len(lst)-1):
            start = lst[i][0]
            stop = lst[i][1]
            
            for j in range(i+1,len(lst)):
                if start >= lst[j][0] and stop < lst[j][1]:
                    break
            else:
                count += 1
        return count
                
        """        
        
        
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        