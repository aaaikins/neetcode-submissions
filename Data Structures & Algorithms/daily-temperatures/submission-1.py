class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            print(t, res)
            while stack and t > stack[-1][1]:
                stackInd, stackTemp = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((i, t))

        return res