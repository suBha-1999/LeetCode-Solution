
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0

        for num in nums:
            if num != val:
                nums[i] = num
                i += 1

        return i

sol = Solution()
nums = [3,2,2,3]
val = 3
res = sol.removeElement(nums, val)
print(res)