class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        power = 2**31
        
        while n:
            res += (n%2*power)
            n = n >> 1
            power = power // 2
            
        return res
             
        