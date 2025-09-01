class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: 0 nodes, 1 empty tree

        for i in range(1, n + 1):
            for j in range(i):  # j represents the number of nodes in the left subtree
                dp[i] += dp[j] * dp[i - j - 1]  # dp[j] for left, dp[i-j-1] for right

        return dp[n]
    
sol = Solution()
n = 3
print(sol.numTrees(n))