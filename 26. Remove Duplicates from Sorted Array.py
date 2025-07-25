
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for num in nums:
          if i < 1 or num > nums[i - 1]:
            nums[i] = num
            i += 1

        return i

sol = Solution()
nums = [1,1,2]
res = sol.removeDuplicates(nums)
print(res)