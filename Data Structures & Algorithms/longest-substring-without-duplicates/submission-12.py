class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        hasSet = set()

        l = 0 

        for r in range(len(s)):
            while s[r] in hasSet:
                hasSet.remove(s[l])
                l += 1
            maxLen = max(maxLen, r-l + 1)
            hasSet.add(s[r])
        
        return maxLen