from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]

sol = Solution()

strs = ["dog","racecar","car"]
#strs = ["flower","flow","flight"]
result = sol.longestCommonPrefix(strs)
print(result)