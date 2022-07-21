class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        
        res = []
        start = intervals[0][0]
        stop = intervals[0][1]
        
        for i in range(len(intervals)):
            if intervals[i][0] <= stop:
                stop = max(intervals[i][1], stop)
            else:
                res.append([start, stop])
                start = intervals[i][0]
                stop = intervals[i][1]
        
        res.append([start, stop])
        return res
        
        
        
        
        
                
        