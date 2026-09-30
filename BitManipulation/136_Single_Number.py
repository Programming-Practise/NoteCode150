#? 额外开辟了hash_map这个字典，它的空间复杂度是O(n)不是O(1)
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map.update({num:1})
            else:
                hash_map[num] += 1
        for num, i in hash_map.items():
            if i == 1:
                return num

class Solution_XOR:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result