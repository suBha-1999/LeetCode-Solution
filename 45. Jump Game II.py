from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        end = 0
        farthest = 0

        # Start an implicit BFS.
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                ans += 1
                break
            if i == end:      # Visited all the items on the current level.
                ans += 1        # Increment the level.
                end = farthest  # Make the queue size for the next level.
        return ans
    
sol = Solution()
nums = [2,3,1,1,4]
print(sol.jump(nums))