from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            # if merged is empty OR no overlap, just add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # overlap exists, so merge with the last interval
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged

sol = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(sol.merge(intervals))