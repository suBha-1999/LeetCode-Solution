from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def generateTrees(mn: int, mx: int) -> List[Optional[TreeNode]]:
            if mn > mx:
                return [None]

            ans = []
            for i in range(mn, mx + 1):
                for left in generateTrees(mn, i - 1):
                    for right in generateTrees(i + 1, mx):
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        ans.append(root)
            return ans

        return generateTrees(1, n)


# Helper: serialize tree into LeetCode list format
def serialize(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    output = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            output.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            output.append(None)
    # Trim trailing None’s
    while output and output[-1] is None:
        output.pop()
    return output


# -------------------
# Main Test Code
# -------------------
if __name__ == "__main__":
    n = 3
    sol = Solution()
    trees = sol.generateTrees(n)

    result = [serialize(t) for t in trees]
    print(result)
