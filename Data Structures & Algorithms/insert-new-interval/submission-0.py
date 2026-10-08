class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []


        for start, end in intervals:
            if end < newInterval[0]:
                res.append([start, end])
            elif start > newInterval[1]:
                res.append(newInterval)
                newInterval = [start, end]
            else:
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]
        
        res.append(newInterval)
        
        return res