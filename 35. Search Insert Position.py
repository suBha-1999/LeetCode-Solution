
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            elif target < nums[mid]:
                r = mid

            else:
                l = mid + 1

        return l

sol = Solution()
nums = [1,3,5,6]
target = 5
res = sol.searchInsert(nums, target)
print(res)
