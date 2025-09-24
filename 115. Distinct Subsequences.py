from typing import List

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)

        dp[n] = 1  # base case: one way to form empty string
        for i in range(m - 1, -1, -1):
            prev = 1  # dp[n] (empty subsequence count)
            for j in range(n - 1, -1, -1):
                res = dp[j]
                if s[i] == t[j]:
                    res += prev
                prev = dp[j]
                dp[j] = res
        return dp[0]


# ---------------- Run Examples in VS Code ----------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    s, t = "rabbbit", "rabbit"
    print("Example 1:")
    print("Input:", s, t)
    print("Output:", sol.numDistinct(s, t))  # Expected 3
    print()

    # Example 2
    s, t = "babgbag", "bag"
    print("Example 2:")
    print("Input:", s, t)
    print("Output:", sol.numDistinct(s, t))  # Expected 5
    print()

    # Custom Example
    s, t = "abcd", "abc"
    print("Custom Example:")
    print("Input:", s, t)
    print("Output:", sol.numDistinct(s, t))  # Expected 1
