class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Initialize DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize first row and column
        for i in range(m + 1):
            dp[i][0] = i  # i deletions to convert word1[:i] to empty string
        for j in range(n + 1):
            dp[0][j] = j  # j insertions to convert empty string to word2[:j]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],      # Deletion
                                       dp[i][j - 1],      # Insertion
                                       dp[i - 1][j - 1])  # Replacement
        
        return dp[m][n]

sol = Solution()
word1 = "horse"
word2 = "ros"

print(sol.minDistance(word1, word2))