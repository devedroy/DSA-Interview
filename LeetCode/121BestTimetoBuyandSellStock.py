class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1
        maxProfit = 0
        
        while s < len(prices):
            if prices[b] < prices[s]:
                profit = prices[s] - prices[b]
                maxProfit = max(profit, maxProfit)
            else:
                b = s
            s += 1
        return maxProfit