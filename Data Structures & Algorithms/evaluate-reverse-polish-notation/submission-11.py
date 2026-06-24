class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'/', '+', '*', '-'}

        for elem in tokens:
            if elem not in operators:
                stack.append(int(elem))
            else:
                right= stack.pop()
                left = stack.pop()

                if elem == "+":
                    stack.append(left + right)
                elif elem == "*":
                    stack.append(left * right)
                elif elem == "-":
                    stack.append(left - right)
                elif elem == "/":
                    stack.append(int(left / right))
                    
        return stack.pop()

        