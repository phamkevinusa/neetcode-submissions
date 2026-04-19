class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #implement iterative dfs with cycle detection
        graph = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            graph[crs].append(pre)

        visited = set()
        rec_stack = set()
        def dfs_cycle(node):
            if node in rec_stack:
                return False
            
            visited.add(node)
            rec_stack.add(node)

            for neighbor in graph.get(node,[]):
                if dfs_cycle(neighbor) == False:
                    return False
            rec_stack.discard(node)
            return True

        for node in range(numCourses):
            if node not in visited:
                if dfs_cycle(node) == False:
                    return False

        return True

