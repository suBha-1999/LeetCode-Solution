from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  
        last_index = len(nums) - 1

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= last_index:
                return True
        
        return True
    
sol = Solution()
nums = [2,3,1,1,4]

print(sol.canJump(nums))