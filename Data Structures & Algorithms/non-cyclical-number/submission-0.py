class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(num):
            return sum(int(d) ** 2 for d in str(num))

        seen = set()

        while n != 1:
            n = next_num(n)

            if n in seen:
                return False

            seen.add(n)
        
        return True