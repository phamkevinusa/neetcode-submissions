class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def toDict(word):
            out = {}
            for l in word:
                out[l] = out.get(l,0) + 1

            return out

        sDict = toDict(s)
        tDict = toDict(t)

        return sDict == tDict

