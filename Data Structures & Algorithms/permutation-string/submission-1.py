class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        
        c1 = Counter(s1)
        c2 = Counter(s2[:l1])

        if c1 == c2:
            return True

        for i in range(l1, l2):
            c2[s2[i]] += 1
            c2[s2[i - l1]] -= 1

            if c2[s2[i-l1]] == 0:
                del c2[s2[i-l1]]
        
            if c1 == c2:
                return True
        
        return False