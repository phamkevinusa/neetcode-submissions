class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i : [] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[a].append(b)
        
        visited = set()
        rec_stack = set()
        def dfs(node):
            if node in rec_stack:
                return False
            if node in visited:
                return True

            rec_stack.add(node)
            visited.add(node)
            for neighbor in graph.get(node, []):
                if dfs(neighbor) == False:
                    return False
            
            rec_stack.discard(node)

        for node in range(numCourses):
            if node in visited:
                continue
            if dfs(node) == False:
                return False

        return True