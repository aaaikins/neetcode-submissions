class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        i, j = 0, x
        while i <= j:
            mid = (i + j) // 2

            if mid ** 2 == x:
                return mid
            elif (mid**2) > x:
                j = mid - 1
            else:
                i = mid + 1
            print('i', i)
            print('j', j)

        return j