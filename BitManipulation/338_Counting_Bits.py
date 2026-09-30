class Solution:
    def countBits(self, n: int) -> list[int]:
        counts = []
        for num in range(n+1):
            count = 0
            while num:
                count += num & 1
                num >>= 1
            counts.append(count)

        return counts

# 没太理解，说是涉及DP
class Solution:
    def countBits(self, n: int) -> list[int]:
        counts = [0] * (n + 1)

        for i in range(1, n + 1):
            counts[i] = counts[i >> 1] + (i & 1)

        return counts