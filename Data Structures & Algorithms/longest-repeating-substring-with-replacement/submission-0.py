class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxFreq = 0
        maxLen = 0
        for r, char in enumerate(s):
            count[char] = 1 + count.get(char, 0)

            maxFreq = max(maxFreq, count[char])

            if (r-l+1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
                
            maxLen = max(maxLen, r-l+1)

        return maxLen
        
        