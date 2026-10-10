class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for i in range(1, n):
            pre_interval = res[-1]
            cur_interval = intervals[i]

            if (pre_interval[1] >= cur_interval[0]):
                pre_interval[1] = max(pre_interval[1], cur_interval[1])
            else:
                res.append(cur_interval)

        return res