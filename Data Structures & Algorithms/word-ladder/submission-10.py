class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #turn words into adjacency list
        #do bfs passing in level until we find endword

        if endWord not in wordList:
            return 0

        adjList = defaultdict(list)
        def findWords(word):
            if adjList[word]:
                return adjList[word]

            res = []
            for a in wordList:
                if word == a:
                    continue
                d = 0
                for i in range(len(a)): 
                    if word[i] != a[i]: # keep track of different letters
                        d += 1
                if d == 1: #if one letter difference, add to output
                    res.append(a)
            adjList[word] = res
            return res
        

        visited = set([beginWord])
        
        queue = deque([(beginWord, 1)]) # word, depth
        while queue:
            node = queue.popleft()

            if node[0] == endWord:
                return node[1]

            for neighbor in findWords(node[0]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, node[1] + 1))
                
        return 0









