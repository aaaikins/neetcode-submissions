class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0

        for r in range(1, len(prices)):
            curProfit = prices[r] - prices[l]
            maxProfit = max(curProfit, maxProfit)

            while l < r and prices[r] < prices[l]:
                l += 1
            
        
        return maxProfit

        