class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for elem in tokens:
            if elem not in '/+*-':
                stack.append(int(elem))
            else:
                print(stack)
                prev = stack.pop()
                if elem == "+":
                    stack[-1] = stack[-1] + prev
                elif elem == "*":
                    stack[-1] = stack[-1] * prev
                elif elem == "-":
                    stack[-1] = stack[-1] - prev
                elif elem == "/":
                    stack[-1] = int(stack[-1] / prev)
                    # if stack[-1] < 0:
                    #     stack[-1] = 0
        return stack[-1]

        