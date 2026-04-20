class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rowcount = [0] * rows
        colcount = [0] * cols
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    rowcount[row] += 1
                    colcount[col] += 1
        
        count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    if rowcount[row] > 1 or colcount[col] > 1:
                        count += 1

        return count

            