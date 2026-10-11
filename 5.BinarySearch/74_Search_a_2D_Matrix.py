class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        up = 0
        down = len(matrix) - 1

        while up <= down:
            mid_row = (up + down) // 2

            if target < matrix[mid_row][0]:
                down = mid_row - 1
            else:
                up = mid_row + 1

        row = down

        if row < 0:
            return False

        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid_col = (left + right) // 2

            if target < matrix[row][mid_col]:
                right = mid_col - 1
            elif target > matrix[row][mid_col]:
                left = mid_col + 1
            else:
                return True

        return False
            
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows*cols - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // cols
            col = mid % cols
            if target < matrix[row][col]:
                right = mid - 1
            elif target > matrix[row][col]:
                left = mid + 1
            else:
                return True
        return False
