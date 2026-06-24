class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        i, j = 0, 0
        res = ""

        while i < len(w1) and j < len(w2):
            c1 = w1[i]
            c2 = w2[j]
            res += c1 + c2
            i += 1
            j += 1

        if i < len(w1):
            res += w1[i:]
        if j < len(w2):
            res += w2[j:]
        
        return res

        