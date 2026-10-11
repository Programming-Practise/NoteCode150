# time complexity O(nlogn) (sort)
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        for interval in intervals:
            if interval[0] > newInterval[-1]:
                result.append(interval)
            elif interval[-1] < newInterval[0]:
                result.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[-1], newInterval[-1])]
        result.append(newInterval)
        result.sort()
        return result

# time complexity O(n)
class Solution:
    def insert(self, intervals: list[list[int]],
               newInterval: list[int]) -> list[list[int]]:

        result = []
        i = 0
        n = len(intervals)

        # 第一阶段：添加左边的区间
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 第二阶段：合并重叠的区间
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # 添加合并后的新区间
        result.append(newInterval)

        # 第三阶段：添加右边剩余的区间
        while i < n:
            result.append(intervals[i])
            i += 1

        return result