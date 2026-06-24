class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLen = 0
        hashSet = set()

        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
                
            maxLen = max(r-l+1, maxLen)
            hashSet.add(s[r])
        return maxLen
        