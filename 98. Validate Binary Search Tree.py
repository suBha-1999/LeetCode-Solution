from typing import Optional, List
from collections import deque


#  Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))

        return True
    
# -------- Helper Functions to test like LeetCode --------
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build binary tree from level-order list (like LeetCode input)."""
    if not values:
        return None

    root = TreeNode(values[0])
    q = deque([root])
    i = 1

    while q and i < len(values):
        node = q.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1

    return root


# -------- Testing (like LeetCode) --------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: root = [2,1,3]
    tree1 = build_tree([2,1,3])
    print(sol.isValidBST(tree1))  # Expected True

    # Example 2: root = [5,1,4,None,None,3,6]
    tree2 = build_tree([5,1,4,None,None,3,6])
    print(sol.isValidBST(tree2))  # Expected False