class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            area = 0
            container_height = min(height[left], height[right])
            area = container_height * (right - left)
            max_area = max(max_area, area)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return max_area

