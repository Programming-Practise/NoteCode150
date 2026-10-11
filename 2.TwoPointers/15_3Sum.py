class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1, length-1):
                for k in range(j+1, length-1):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])
        return result


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for idx in range(len(nums) - 2):
            # 跳过重复的固定元素
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            left = idx + 1
            right = len(nums) - 1

            while left < right:
                total = nums[idx] + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    result.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # 跳过重复的左右元素
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result

