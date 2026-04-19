class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        sMap = {}
        seen = {}
        for s in s1:
            sMap[s] = 1 + sMap.get(s,0)

        l = 0
        for r in range(len(s2)):
            char = s2[r]
            seen[char] = 1 + seen.get(char,0) #add char to seen
            if r - l + 1 > len(s1):
                left_char = s2[l]
                seen[left_char] -= 1
                if seen[left_char] == 0:
                    del seen[left_char]
                l += 1
            if seen == sMap:
                return True

        return False

