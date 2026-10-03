# 左闭右闭 [left, right]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        # 右边是闭区间，所以最后一个有效索引是 len(nums) - 1
        while left <= right:
            # [1, 1] 是合法区间，因此需要允许 left == right
            mid = (left + right) // 2
            # Python 中 // 表示整除，结果向下取整
            if nums[mid] > target:
                right = mid - 1
                # mid 已经确定不可能是 target
                # 下一轮搜索区间仍然保持左闭右闭
            elif nums[mid] < target:
                left = mid + 1
                # mid 已经确定不可能是 target
                # 下一轮搜索区间仍然保持左闭右闭
            elif nums[mid] == target:
                return mid
        return -1

# 左闭右开 [left, right)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        # 右边是开区间，所以 right 可以取 len(nums)
        # 搜索区间 [0, len(nums)) 正好覆盖整个数组
        while left < right:
            # [1, 1) 是空区间，因此当 left == right 时搜索结束
            mid = (left + right) // 2
            # Python 中 // 表示整除，结果向下取整
            if nums[mid] > target:
                right = mid
                # mid 已经确定不可能是 target
                # 由于右边是开区间，直接将 right 设为 mid
                # 下一轮搜索区间为 [left, mid)
            elif nums[mid] < target:
                left = mid + 1
                # mid 已经确定不可能是 target
                # 因此排除 mid，下一轮从 mid + 1 开始
                # 下一轮搜索区间为 [mid + 1, right)
            elif nums[mid] == target:
                return mid
        return -1
