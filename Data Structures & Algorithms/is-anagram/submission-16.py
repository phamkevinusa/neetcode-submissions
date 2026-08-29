class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrS = list(s)
        arrT = list(t)

        arrS.sort()
        arrT.sort()

        return arrS == arrT