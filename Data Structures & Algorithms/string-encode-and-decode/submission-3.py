import random as rd

class Solution:

    def encode(self, strs: List[str]) -> str:
        global code_map
        code_map = {}
        rand_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h','i', 'j'
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
        encoded = ""
        char = rd.choice(rand_char)
        for word in strs:
            while char in code_map:
                char = rd.choice(rand_char)
            code_map[char] = word
            encoded += char
        
        return encoded

    def decode(self, s: str) -> List[str]:
        print(code_map)
        return list(code_map.values())
