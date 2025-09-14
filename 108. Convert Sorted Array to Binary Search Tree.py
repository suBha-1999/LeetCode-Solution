from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, values: List[int]) -> Optional[TreeNode]:
        def construct_bst(start, end):
            if start > end:
                return None

            mid = (start + end) // 2  # pick the middle element
            node = TreeNode(values[mid])
            node.left = construct_bst(start, mid - 1)
            node.right = construct_bst(mid + 1, end)
            return node

        return construct_bst(0, len(values) - 1)


# Helper function to print tree in level order
from collections import deque

def level_order(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result


# Example usage
nums = [-10, -3, 0, 5, 9]
root = Solution().sortedArrayToBST(nums)
print(level_order(root))
