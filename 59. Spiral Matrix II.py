from typing import List


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        count = 1

        while top <= bottom and left <= right:
            # Move Right
            for col in range(left, right + 1):
                matrix[top][col] = count
                count += 1
            top += 1

            # Move Down
            for row in range(top, bottom + 1):
                matrix[row][right] = count
                count += 1
            right -= 1

            # Move Left
            if top <= bottom: # Check to avoid single row/column issues
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = count
                    count += 1
                bottom -= 1

            # Move Up
            if left <= right: # Check to avoid single row/column issues
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = count
                    count += 1
                left += 1
        
        return matrix
    
sol = Solution()
n = 3
print(sol.generateMatrix(n))