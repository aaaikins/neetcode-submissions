import random as rd

class Solution:

    def encode(self, strs):
        global code_map
        code_map = {}
        encoded = ""
        char = rd.randint(1, 1000)
        for word in strs:
            while char in code_map:
                char = rd.randint(1, 1000)
            code_map[char] = word
            encoded += str(char)
        
        return encoded

    def decode(self, s):
        return list(code_map.values())
