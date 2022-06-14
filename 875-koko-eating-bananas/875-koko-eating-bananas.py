class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = -1
        
        while l <= r:
            mid = (l + r)//2
            
            hours = 0
            for i in piles:
                temp = i / mid
                hours += math.ceil(temp)
                    
            if hours <= h:
                if k == -1:
                    k = max(mid, k)
                else:
                    k = min(mid, k)
            
                r = mid - 1
            else:
                l = mid + 1
                
        return k
        