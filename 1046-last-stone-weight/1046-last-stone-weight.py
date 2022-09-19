class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        
        while len(stones) > 1 :
            stones.sort(reverse=False)
            
            big = stones.pop(-1)
            small = stones.pop(-1)
            diff = big - small
            if diff > 0 or len(stones) == 0:
                stones.append(diff)
        
        return stones[0]