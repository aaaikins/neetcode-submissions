class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', '}':'{', ']':'['}

        stack = []

        for i in range(len(s)):
            # print(stack)
            if stack and s[i] in mapping:
                top = stack.pop()
                if mapping[s[i]] != top:
                    return False
            else:
                stack.append(s[i])

        return not stack
        
        