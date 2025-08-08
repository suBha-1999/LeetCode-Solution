from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for num in nums:
            if i < 2 or num != nums[i - 2]:
                nums[i] = num
                i += 1

        return i
    
sol = Solution()
nums = [1,1,1,2,2,3]
print(sol.removeDuplicates(nums))