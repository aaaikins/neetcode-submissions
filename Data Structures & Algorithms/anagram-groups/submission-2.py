class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for s in strs:
            count_s = [0] * 26
            for c in s:
                count_s[ord(c) - ord('a')] += 1
            anagramMap[tuple(count_s)].append(s)
        
        return list(anagramMap.values())