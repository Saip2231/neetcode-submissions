class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key = lambda i:i[0])
        lastend = intervals[0][1]
        for start , end in intervals[1:]:
            if start >= lastend:
                #overlapping
                lastend = end
            else:
                #remove one of the intervals
                count = count + 1
                lastend = min(end , lastend)
        return count
