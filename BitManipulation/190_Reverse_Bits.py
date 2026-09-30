class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []

        for _ in range(32):
            bits.append(n & 1)
            n >>= 1

        result = 0

        for i, bit in enumerate(bits):
            result += bit * (2 ** (31 - i))

        return result