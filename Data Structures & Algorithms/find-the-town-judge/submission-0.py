class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0] * (n+1)
        outdegree = [0] * (n + 1)

        for a, b in trust:
            indegree[b] += 1
            outdegree[a] += 1   

        for a in range(1, n+1):
            if outdegree[a] == 0 and indegree[a] == n-1:
                return a
        return -1



            


