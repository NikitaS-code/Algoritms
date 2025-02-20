from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        output = [intervals[0]]

        for idx in range(1, len(intervals)):
            start, end = intervals[idx]
            last_interval = output[-1]
            last_end = last_interval[1]

            if start > last_end:
                output.append(intervals[idx])

            else:
                last_interval[1] = max(last_end, end)

        return output