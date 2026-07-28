class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyprice = prices[0]
        maxprofit = 0

        for i in range(len(prices)):
            if prices[i] < buyprice:
                buyprice = prices[i]
            else:
                profit = prices[i] - buyprice
                maxprofit = max(maxprofit, profit)
        return maxprofit
