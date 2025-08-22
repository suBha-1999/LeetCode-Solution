import collections, functools

class Solution:
    @functools.lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        if collections.Counter(s1) != collections.Counter(s2):
            return False

        n = len(s1)
        for i in range(1, n):
            # No swap
            if (self.isScramble(s1[:i], s2[:i]) and
                    self.isScramble(s1[i:], s2[i:])):
                return True
            # Swap
            if (self.isScramble(s1[:i], s2[n - i:]) and
                    self.isScramble(s1[i:], s2[:n - i])):
                return True
        return False
    
sol  = Solution()
s1 = "great"
s2 = "rgeat"

print(sol.isScramble(s1, s2))