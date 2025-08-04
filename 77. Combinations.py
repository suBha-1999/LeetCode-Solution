from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        current_combination = [] 

        def backtrack(start_num):
            if len(current_combination) == k:
                result.append(list(current_combination))  
                return

            for i in range(start_num, n + 1):
                current_combination.append(i)
                backtrack(i + 1)  
                current_combination.pop() 
        backtrack(1)
        return result
    
sol = Solution()
n = 4
k = 2

print(sol.combine(n, k))