class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = defaultdict(list)

        for s in strs:
            wordMap[str(sorted(s))].append(s)
            # if sorted(s) in wordMap:
            #     wordMap[sorted(s)].append(s)
            # else:
            #     wordMap

        return list(wordMap.values())



        