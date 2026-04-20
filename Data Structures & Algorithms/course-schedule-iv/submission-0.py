class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {i : [] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[a].append(b)

        def bfs(start, end):
            visited = set([start])
            queue = deque([start])

            while queue:
                node = queue.popleft()

                if node == end:
                    return True
                
                for neighbor in graph.get(node, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            return False
        

        return [bfs(start, end) for start, end in queries]
             