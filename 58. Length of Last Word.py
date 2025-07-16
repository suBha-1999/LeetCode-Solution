class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])
    

sol = Solution()
s = "Hello World"
print(sol.lengthOfLastWord(s))