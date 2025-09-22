from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, current_sum, current_path):
            if not node:
                return

            current_sum += node.val
            current_path.append(node.val)

            # If it's a leaf and sum matches targetSum
            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(current_path))  # copy path

            # Recurse left & right
            dfs(node.left, current_sum, current_path)
            dfs(node.right, current_sum, current_path)

            # Backtrack
            current_path.pop()

        dfs(root, 0, [])
        return result


# ---------------- Helper Functions ----------------
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a level-order list (LeetCode style)."""
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


# ---------------- Example Run ----------------
if __name__ == "__main__":
    # Example 1
    values = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    targetSum = 22
    root = build_tree(values)

    sol = Solution()
    print("Paths:", sol.pathSum(root, targetSum))
