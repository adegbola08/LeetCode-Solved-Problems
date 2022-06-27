class Solution:
    def findMinDifference(self, time: List[str]) -> int:
        
        for i in range(len(time)):
            if time[i] == "00:00":
                time[i] = "24:00"
            pos = time[i].find(":")
            time[i] = 60*int(time[i][:pos]) + int(time[i][pos+1:])
            
        time.sort()
        
        res = -1
        for i in range(1,len(time)):
            temp = time[i] - time[i-1]
            if res == -1:
                res = temp
            else:
                res = min(res, temp)
        diff = time[0] - time[-1] + 1440
        return min(res,diff)
            
        
        
            
        