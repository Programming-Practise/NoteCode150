class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = {}
        for cha in s:
            if cha in hash_map:
                hash_map[cha] += 1
            else:
                hash_map[cha] = 1

        for cha in t:
            if cha not in hash_map:
                return False
            else:
                hash_map[cha] -= 1

        for _, v in hash_map.items():
            if v != 0:
                return False
        return True