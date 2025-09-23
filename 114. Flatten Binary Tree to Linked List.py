from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        stack = [root]
        prev = None

        while stack:
            curr = stack.pop()

            if prev:
                prev.right = curr
                prev.left = None  # Ensure left child is null

            # Push right child first, then left, so left is processed first
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

            prev = curr


# ---------------- Helper Functions ----------------
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from level-order list (LeetCode style)."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    q = deque([root])
    i = 1

    while q and i < len(values):
        node = q.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1

    return root


def print_flattened(root: Optional[TreeNode]) -> None:
    """Prints the flattened tree as a list (right-skewed)."""
    result = []
    while root:
        result.append(root.val)
        root = root.right
    print("Flattened:", result)


# ---------------- Example Run ----------------
if __name__ == "__main__":
    # Example: [1,2,5,3,4,None,6]
    values = [1, 2, 5, 3, 4, None, 6]
    root = build_tree(values)

    sol = Solution()
    sol.flatten(root)
    print_flattened(root)
