class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = float('-inf')
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit = max(profit, prices[j]-prices[i])
        return profit if profit>0 else 0

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        i = 0
        for j in range(1, len(prices)):
            if prices[j] < prices[i]:
                i = j
            profit = max(profit, prices[j] - prices[i])
        return profit
