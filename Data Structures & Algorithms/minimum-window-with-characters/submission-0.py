class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return t
        if len(s) < len(t):
            return ""

        need = Counter(t)
        missing = len(t)

        l = 0
        minLen = float("inf")
        start = 0

        for r, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            print("missing ", missing)
            while missing == 0:
                if (r - l + 1) < minLen:
                    minLen = (r - l + 1)
                    start = l
                need[s[l]] += 1
                if need[s[l]] > 0:
                    missing += 1
                l += 1
            
            print("left ", l)

        return "" if minLen == float("inf") else s[start:start + minLen]





        