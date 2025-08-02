from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> List:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        
        ## for print the final result
        return nums
    
    
            
sol = Solution()
nums = [2,0,2,1,1,0]
print(sol.sortColors(nums))