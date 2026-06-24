class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x

        while l <= r:
            n = (l+r) // 2
            prod = n ** 2

            if prod == x:
                return n
            elif prod < x:
                l = n + 1
            else:
                r = n - 1
        
        return r