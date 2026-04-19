class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix)-1
        while top <= bot:
            mid = (top+bot) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:

                l, r = 0, len(matrix[mid]) - 1

                while l <= r:
                    c = (l + r) // 2
                    if matrix[mid][c] == target:
                        return True
                    elif matrix[mid][c] < target:
                        l = c + 1
                    else:
                        r = c - 1
                return False
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                bot = mid - 1
        return False