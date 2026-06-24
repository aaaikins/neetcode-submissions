class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]

        maxProfit = -float('inf')

        for price in prices:
            lowest = min(price, lowest)
            profit = price - lowest
            maxProfit = max(profit, maxProfit)
        
        return maxProfit
        