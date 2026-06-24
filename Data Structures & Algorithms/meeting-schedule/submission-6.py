"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        if not intervals:
            return True

        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            top = stack[-1]
            cur = intervals[i]

            if cur.start < top.end:
                return False
            
            stack.append(cur)
            
        return True

        print(intervals)

        return True

