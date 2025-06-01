class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#'.join('@' + s + '$')
        p = self._manacher(t)
        maxPalindromeLength, bestCenter = max((extend, i) for i, extend in enumerate(p))
        l = (bestCenter - maxPalindromeLength) // 2
        r = (bestCenter + maxPalindromeLength) // 2
        return s[l:r]

    def _manacher(self, t: str) -> list[int]:
        p = [0] * len(t)
        center = 0
        for i in range(1, len(t) - 1):
            rightBoundary = center + p[center]
            mirrorIndex = center - (i - center)
            if rightBoundary > i:
                p[i] = min(rightBoundary - i, p[mirrorIndex])
            # Try to expand the palindrome centered at i.
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1
            # If a palindrome centered at i expands past `rightBoundary`, adjust
            # the center based on the expanded palindrome.
            if i + p[i] > rightBoundary:
                center = i
        return p



sol = Solution()

s = "cbbd" #"babad"
result = sol.longestPalindrome(s)
print(result)