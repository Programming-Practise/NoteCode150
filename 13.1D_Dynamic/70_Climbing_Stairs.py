class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        if n >= 3:
            dp = [0] * (n + 1)
            dp[1] = 1
            dp[2] = 2
            for i in range(3, n+1):
                dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2 = 1  # dp[1]
        prev1 = 2  # dp[2]

        for i in range(3, n + 1):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur

        return prev1
        