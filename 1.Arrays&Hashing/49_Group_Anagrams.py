from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash_maps = defaultdict(list)
        for str in strs:
            key = tuple(sorted(self.build_hash(str).items()))
            hash_maps[key].append(str)

        return list(hash_maps.values())


    def build_hash(self, str):
        hash_map = defaultdict(int)
        for cha in str:
            hash_map[cha] += 1
        return hash_map