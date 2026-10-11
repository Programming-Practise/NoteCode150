class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        length = len(cost)
        dp = [0] * (length + 1)
        dp[0] = dp[1] = 0
        for i in range(2, length+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[-1]
