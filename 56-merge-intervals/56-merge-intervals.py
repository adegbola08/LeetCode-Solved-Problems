class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
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
        
        