class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while True:
            
            new = 0
            while n != 0:
                new += ((n%10)**2)
                n = (n//10)
            
            if new == 1:
                return True
            if new in seen:
                return False
            else:
                n = new
                seen.add(new)
        
        