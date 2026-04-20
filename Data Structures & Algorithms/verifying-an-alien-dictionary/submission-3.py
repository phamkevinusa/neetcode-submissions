class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # sorted first letter, then second letter, etc

        # need to make sure prefix word comes first
        # abc, abcd
        # need to make sure the letter after the prefix comes first
        # abca, abcd

        #
        chardict = {c : i for i , c in enumerate(order)}

        for i in range(len(words)-1):
            a = words[i]
            b = words[i+1]
            minLen = min(len(a), len(b))
            #find index of first differing letter so we can slice the words
            index = -1 #if no diff letter found
            for j in range(minLen): 
                if a[j] != b[j]:
                    index = j
                    break

            #prefix coming after edgecase
            if index == -1:
                if len(a) > len(b):
                    return  False
                else:
                    continue
            
            if not chardict[a[index]] < chardict[b[index]]:
                return False
        return True 


