from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def has_sum(root, cur_sum):
            if not root:
                return False

            cur_sum += root.val

            # If leaf node, check sum
            if not root.left and not root.right:
                return cur_sum == targetSum

            # Recurse on children
            return has_sum(root.left, cur_sum) or has_sum(root.right, cur_sum)
        
        return has_sum(root, 0)


# ---------------- Helper Function ----------------
def build_tree(values):
    """Builds a binary tree from a list (LeetCode style)."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


# ---------------- Run Example ----------------
if __name__ == "__main__":
    # Example: Input [5,4,8,11,None,13,4,7,2,None,None,None,1], targetSum = 22
    values = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    targetSum = 22

    root = build_tree(values)

    sol = Solution()
    result = sol.hasPathSum(root, targetSum)
    print("Has Path Sum =", result)
