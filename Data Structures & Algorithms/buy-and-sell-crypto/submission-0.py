class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bestBuy = prices[0]
        for i in range(1,len(prices)):
            if prices[i] > bestBuy:
                profit = max(profit , prices[i]-bestBuy)
            bestBuy = min(bestBuy , prices[i])
            
        return profit