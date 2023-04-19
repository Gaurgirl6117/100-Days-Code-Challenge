# Github: Gaurgirl6117
# DAY 6 of DAY 100
# Merge Intervals - GeeksorGeeks
# https://leetcode.com/problems/merge-intervals/description/

class Solution(object):
    def merge(self, intervals):
   
        intervals=sorted(intervals)
        res=[intervals[0]]
        for start,end in intervals[1:]:
            lastEnd=res[-1][1]
            if lastEnd>=start:
                res[-1][1]=max(lastEnd,end)
            else:
                res.append([start,end])
