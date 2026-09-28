class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                result.append(curStr)
                return

            for ch in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + ch)
                
        if digits:
            backtrack(0, "")

        return result