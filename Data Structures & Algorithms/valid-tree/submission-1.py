class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #check for cycles but don't count directly previous node as a cycle
        #define curr node at the top of every call before recursing

        if len(edges) != n - 1:
            return False
        graph = {i : [] for i in range(n)}

        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)


        rec_stack = set()


        def dfs_cycle(node, par):

            if node in rec_stack:
                return False

            rec_stack.add(node)
            for neighbor in graph.get(node, []):
                if neighbor == par:
                    continue
                if dfs_cycle(neighbor, node) == False:
                    return False

            return True


        return dfs_cycle(0,-1) and len(rec_stack) == n
