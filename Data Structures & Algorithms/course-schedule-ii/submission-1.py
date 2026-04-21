class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
                
        graph = {i : [] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[a].append(b)
        
        visited = set()
        rec_stack = set()
        output = []
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
            output.append(node)
        for node in range(numCourses):
            if node in visited:
                continue
            if dfs(node) == False:
                return []
        return output
        