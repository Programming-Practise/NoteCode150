class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        if len(set_nums) < len(nums):
            return True
        else:
            return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct = set()
        for num in nums:
            if num in distinct:
                return True
            else:
                distinct.add(num)
        return False