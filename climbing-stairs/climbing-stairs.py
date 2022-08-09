class Solution:
    def climbStairs(self, n: int) -> int:
        pos1 = 1
        pos2 = 1
        result = 1
        
        for i in range(n-1):
            result = pos1 + pos2
            temp = pos1
            pos1 = result 
            pos2 = temp
            
        return result
        