class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        mergeList = []
        mergeList.append(intervals[0])

        for start, end in intervals[1:]:
            lastEnd = mergeList[-1][1]
            if start <= lastEnd:
                mergeList[-1][1] = max(lastEnd, end)
            else:
                mergeList.append([start, end])

        return mergeList
        
        