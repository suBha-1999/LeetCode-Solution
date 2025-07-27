class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left, right = 1, x
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid <= x:
                ans = mid  
                left = mid + 1 
            else:
                right = mid - 1 
        
        return ans
    
sol = Solution()
x = 36 # 2 100 144
print(sol.mySqrt(x))