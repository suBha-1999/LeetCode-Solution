class Solution:
    def numDecodings(self, s: str) -> int:
        dp = 0
        dp2 = 0
        dp1 = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp = 0
            else:
                dp = dp1
                if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                    dp += dp2

            dp2, dp1, dp = dp1, dp, 0

        return dp1


sol = Solution()
s = "12"
print(sol.numDecodings(s))