class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        
        while len(stones) > 1 :
            
            big = max(stones)
            stones.remove(big)
            small = max(stones)
            stones.remove(small)
            
            diff = big - small
            if diff > 0 or len(stones) == 0:
                stones.append(diff)
        
        return stones[0]