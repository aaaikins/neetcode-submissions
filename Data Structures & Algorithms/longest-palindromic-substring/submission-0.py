class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalindrome(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return l, r
        
        res = ""
        maxLen = float("-inf")
        l, r = 0, 0

        for i in range(len(s)):
            lo, ro = getPalindrome(s, i, i)
            if (ro -lo + 1) > maxLen:
                maxLen = (ro -lo + 1)
                l, r= lo, ro
            
            le, re = getPalindrome(s, i, i + 1)
            if (re -le + 1) > maxLen:
                maxLen = (re -le + 1)
                l, r= le, re

           
        
        return s[l+ 1: r]
