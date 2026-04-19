class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        i = 0
        j = len(s)-1

        while i<j:
            while i<j and not s[i].isalnum():
                i = i+1
            while i < j and not s[j].isalnum():
                j = j-1
            if not i < j:
                break
            if s[i]!=s[j]:
                return False

            i = i+1
            j = j-1
        return True