from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            s_sort = sorted(s)
            key = tuple(s_sort)
            
            if key not in ans:
                ans[key] = [s]
            else:
                ans[key].append(s)

        return sorted(ans.values()) 
    
sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))