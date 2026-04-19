class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #running dfs on a node in a component will mark the whole component as visited
        #count how many times you can start dfs on a new component (head node is not visited)


        graph = {i : [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)


        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph.get(node, []):
                dfs(neighbor)
            
        numComponents = 0
        for node in range(n):
            if node not in visited:
                numComponents += 1
                dfs(node)
        
        return numComponents
