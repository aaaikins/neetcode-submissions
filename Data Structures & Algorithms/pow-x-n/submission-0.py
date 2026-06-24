class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            half = pow(x, n//2)
            if n % 2 == 0:
                return half * half
            else:
                return x * half * half

        if n < 0:
            n = -n
            x = 1/x


        return helper(x, n) 