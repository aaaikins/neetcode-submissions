class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]

        maxProfit = -float('inf')

        for price in prices:
            if price < lowest:
                lowest = price
            profit = price - lowest
            maxProfit = max(profit, maxProfit)
        
        return maxProfit
        