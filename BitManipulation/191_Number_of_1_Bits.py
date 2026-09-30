# the space complexity is O(n), and it can be further optimized
class Solution:
    def hammingWeight(self, n: int) -> int:
        ls = []
        while n > 0:
            ls.append(n % 2)
            n = n // 2 
        return sum(ls)

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n % 2
            n = n // 2 
        return count

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            count += n & 1
            n >>= 1

        return count