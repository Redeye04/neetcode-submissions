class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        profit = 0
        l = len(prices)
        for i in range(1, l):
            sell = prices[i]
            if buy > prices[i]:
                buy = prices[i]
            elif sell < prices[i]:
                sell = prices[i]
            curr = sell - buy
            if curr > profit:
                profit = curr
        
        if profit <= 0:
            return 0

        return profit
