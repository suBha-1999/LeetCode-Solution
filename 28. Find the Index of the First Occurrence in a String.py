class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1

soll = Solution()
haystack = "sadbutsad"
needle = "sad"
res = soll.strStr(haystack, needle)
print(res)