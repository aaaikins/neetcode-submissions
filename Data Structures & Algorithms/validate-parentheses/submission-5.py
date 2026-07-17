class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for c in s:
            if stack:
                if c in brackets and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        
        return len(stack) == 0
        