"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort the start and ending times of the meetings
        time = []
        for interval in intervals:
            start, end = interval.start, interval.end
            time.append((start, 1))
            time.append((end, -1))
        time.sort(key=lambda x: (x[0], x[1]))

        days = 0
        max_days = 0
        for t in time:
            days += t[1]
            max_days = max(max_days, days)

        return max_days

        