class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'}':'{', ']':'[', ')':'('}

        for bracket in s:
            if  stack and bracket in mapping:
                top_bracket = stack.pop()
                if top_bracket != mapping[bracket]:
                    return False
            else:
                stack.append(bracket)
            
        return len(stack) == 0
        