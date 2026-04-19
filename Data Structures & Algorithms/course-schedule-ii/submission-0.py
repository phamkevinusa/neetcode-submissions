class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        graph = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        visited = set()
        rec_stack = set()
        output = []
        def dfs_cycle(node):
            if node in rec_stack:
                    return False

            if node not in visited:

                visited.add(node)
                rec_stack.add(node)

                for neighbor in graph.get(node,[]):
                    if dfs_cycle(neighbor) == False:
                        return False   

                rec_stack.discard(node)      
                output.append(node)

            return True

        for crs in range(numCourses):
            if crs not in visited:
                if dfs_cycle(crs) == False:
                    return []
        return output