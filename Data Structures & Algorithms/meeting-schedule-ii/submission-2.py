"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # if len(intervals) == 1:
        #     return 1
        intervals.sort(key = lambda i:i.start)
        res , count = 0,0
        starttime = sorted([i.start for i in intervals])
        endtime = sorted([i.end for i in intervals])
        # print(starttime)
        # print(endtime)
        p,q = 0,0
        while p < len(intervals):
            # If a meeting starts before the previous one ends, need new room
            if starttime[p] < endtime[q]:
                count += 1
                p += 1
            else:
                # A meeting ended, free a room
                count -= 1
                q += 1
            # Track max rooms used
            res = max(res, count)

        return res