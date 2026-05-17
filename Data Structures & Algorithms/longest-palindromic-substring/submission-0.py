class Solution:
    def longestPalindrome(self, s: str) -> str:
        #traverse left to right
        #from each letter, check the next left and right letters to see if the same and palindromic
        #also consider palindromes of even length
        res = ""
        resLen = 0
        for i in range(len(s)):

            #odd length
            l, r = i, i #initialize r and l on string
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            l, r = i, i+1 #initialize r and l on string
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
 
 
        return res
