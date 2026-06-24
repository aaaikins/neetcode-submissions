class Solution:
    def __init__(self):
        self.message = []
    def encode(self, strs: List[str]) -> str:
        self.message = strs
        code = ""
        for s in strs:
            temp = str(len(s)) + "#" + s
            code += temp
        return code

    def decode(self, s: str) -> List[str]:
        message = self.message
        # i = 0

        # while i < len(s):
        #     j = i
        #     while s[j] != '#':
        #         j += 1
        #     length = int(s[i:j])
        #     i = j + 1
        #     j = i + length
        #     message.append(s[i:j])
        #     i = j

        return message