class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        sequence = [i for i in range(1, n+1)]
        path = []
        result = []
        def backtracking(sequence, k, start_idx):
            if len(path) == k:
                result.append(path.copy())
                return None

            for idx in range(start_idx, len(sequence)):
                path.append(sequence[idx])
                backtracking(sequence, k, idx+1)
                path.pop()

        backtracking(sequence, k, 0)
        return result
            
