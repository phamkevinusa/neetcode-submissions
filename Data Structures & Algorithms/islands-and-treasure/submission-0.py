class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # use bfs starting from treasure chests
        # overwrite cell as long as it's less than
        # calculate neighboring cell as 1 + current node

        rows, cols = len(grid), len(grid[0])
        # need separate queue for every treasure chest

        def bfs(r, c):
            queue = deque([(r, c)])
            visited = set()

            while queue:
                r,c = queue.popleft()
                visited.add((r, c))
                # while node has neighbors
                moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in moves:
                    nr, nc = r + dr, c + dc

                    # check in bounds
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    
                    #check new cell not water, not treasure chest, is smaller distance, unvisited
                    if grid[nr][nc] == -1 or grid[nr][nc] <= grid[r][c] or (nr, nc) in visited:
                        continue
                    # process node

                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    bfs(r, c)
