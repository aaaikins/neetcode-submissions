class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # count = Counter(s)
        # print(count)
        l = 0
        res = 0
        maxF = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxF = max(maxF, count[s[r]])

            while (r-l+1) - maxF > k:
                count[s[l]] -= 1
                l += 1

            res = max(r-l+1, res)

        return res
        