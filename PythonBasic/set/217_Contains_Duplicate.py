class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_ls = len(nums)
        num_set = len(set(nums))
        if num_ls == num_set:
            return False
        else:
            return True