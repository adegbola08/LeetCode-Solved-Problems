class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] <= cur_min:
                cur_min = prices[i]
            else:
                profit = max(profit, (prices[i] - cur_min))
        
        return profit
        
        
        
        