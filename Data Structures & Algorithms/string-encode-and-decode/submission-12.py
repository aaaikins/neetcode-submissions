class Solution:
    def __init__(self):
        self.message = []

    def encode(self, strs: List[str]) -> str:
        self.message = strs
        code = ""
        # for s in strs:
        #     temp = str(len(s)) + "#" + s
        #     code += temp
        return code

    def decode(self, s: str) -> List[str]:
        message = self.message
        return message