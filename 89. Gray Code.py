from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = []
        for i in range(1 << n):  # Iterate from 0 to 2^n - 1
            ans.append(i ^ (i >> 1))
        return ans
    
sol = Solution()
n = 2
print(sol.grayCode(n))