class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hash_map = {}
        for idx, number in enumerate(numbers):
            if number in hash_map:
                return [hash_map[number],idx]
            else:
                hash_map[target-number] = idx

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1
