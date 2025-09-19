from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        # If only one child exists, the path must go through that child
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1

        # If both children exist, take the minimum depth of the two subtrees
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# ---------------- Helper Functions ----------------
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
    # Example: Input [3,9,20,None,None,15,7]
    values = [3, 9, 20, None, None, 15, 7]
    root = build_tree(values)

    sol = Solution()
    result = sol.minDepth(root)
    print("Minimum Depth:", result)
