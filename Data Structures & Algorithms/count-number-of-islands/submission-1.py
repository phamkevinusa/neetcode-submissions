class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() #[r, c]
        rows, cols = len(grid), len(grid[0])
        count = 0

        if not grid:
            return 0
        def dfs(r, c):
            visited.add((r, c))
            moves = [[-1, 0],[1, 0], [0,-1], [0,1]]
            for dr, dc in moves:
                nr, nc = r+dr, c + dc
                if isValid(nr, nc):
                    if (nr, nc) not in visited and grid[nr][nc] == "1":
                        dfs(nr, nc)

        def isValid(r, c):
            return r >= 0 and r < rows and c >= 0 and c < cols

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c)
                    count += 1
        return count