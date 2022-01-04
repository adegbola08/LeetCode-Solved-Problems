class Solution(object):
    def maxProfit(self, prices):
        if prices == sorted(prices,reverse=True):
            return 0
        profit = 0
        curMin = prices[0]
        Min = prices.index(min(prices))
        for i in range(len(prices)-1):
            if prices[i] <= curMin and i <= Min:
                curMin = min(curMin, prices[i])
                a = max(prices[i+1:])
                if prices[i] < a:
                    profit = max(a - prices[i], profit)
        return profit
            
        
        """
        :type prices: List[int]
        :rtype: int
        """
        