from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash_map = defaultdict(int)
        for num in nums:
            hash_map[num] += 1

        result = sorted(hash_map.items(), key=lambda x:x[1], reverse=True)
        return [x[0] for x in result[0:k]]

        


