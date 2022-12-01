# Easy

# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend
# all meetings.
#
#
#
# Example 1:
#
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false

# Constraints:
#
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti < endi <= 106

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x : x[0])

        for i, pair in enumerate(intervals):
            start, end = pair
            if i < len(intervals) - 1 and end > intervals[i + 1][0]:
                return False
        return True
## T = O(nlog(n));  S = O(1)