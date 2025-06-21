
from typing import List

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first_occurrence = self._find_occurrence(nums, target, True)
        if first_occurrence == -1:
            return [-1, -1]
        last_occurrence = self._find_occurrence(nums, target, False)
        return [first_occurrence, last_occurrence]

    def _find_occurrence(self, nums: list[int], target: int, find_first: bool) -> int:
        index = -1
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:  # nums[mid] == target
                index = mid
                if find_first:
                    end = mid - 1  # Search for an earlier occurrence
                else:
                    start = mid + 1 # Search for a later occurrence
        return index

Sol = Solution()
nums = [5,7,7,8,8,10]
target = 8
res = Sol.searchRange(nums, target)
print(res)
