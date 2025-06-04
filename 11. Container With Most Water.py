class Solution:
  def maxArea(self, height: list[int]) -> int:
    ans = 0
    l = 0
    r = len(height) - 1

    while l < r:
      minHeight = min(height[l], height[r])
      ans = max(ans, minHeight * (r - l))
      if height[l] < height[r]:
        l += 1
      else:
        r -= 1

    return ans

sol = Solution()

##driver Code
height = [1,8,6,2,5,4,8,3,7]
result = sol.maxArea(height)
print(result)