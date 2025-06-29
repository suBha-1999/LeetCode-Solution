
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap_elements(index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]
        list_length = len(nums)
      
        for i in range(list_length):
            while 1 <= nums[i] <= list_length and nums[i] != nums[nums[i] - 1]:
                swap_elements(i, nums[i] - 1)
              
        for i in range(list_length):
            if i + 1 != nums[i]:
                return i + 1
      
        return list_length + 1
    
sol = Solution()
nums = [1,2,0]

res = sol.firstMissingPositive(nums)
print(res)