class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s2 = ')' + s
        dp = [0] * len(s2)

        for i in range(1, len(s2)):
            if s2[i] == ')' and s2[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2

        return max(dp)

sol = Solution()
s = ")()())"
res = sol.longestValidParentheses(s)
print(res)