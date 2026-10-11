# time complexity is O(n^2)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        longest = 1
        slow = 0
        for fast in range(1,len(s)):
            if s[fast] in s[slow:fast]:
                while s[slow] != s[fast]:
                    slow += 1
                slow += 1
            else:
                longest = max(longest, fast-slow+1)
        return longest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        longst = 1
        hash_map = {}
        slow = 0
        for idx, cha in enumerate(list(s)):
            if cha in hash_map and hash_map[cha]>=slow:
                slow = hash_map[cha] + 1
                
            hash_map[cha] = idx
            longst = max(longst, idx - slow  + 1)
        return longst
