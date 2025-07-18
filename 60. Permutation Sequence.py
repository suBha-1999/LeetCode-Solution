class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ''
        nums = [i + 1 for i in range(n)]
        fact = [1] * (n + 1)  # fact[i] := i!

        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i

        k -= 1  # Adjust k to be 0-indexed

        for i in range(n - 1, -1, -1):
            idx = k // fact[i]
            
            ans += str(nums[idx])
            
            nums.pop(idx)
            
            k %= fact[i]

        return ans

sol = Solution()
n = 3
k = 3
print(sol.getPermutation(n,k))