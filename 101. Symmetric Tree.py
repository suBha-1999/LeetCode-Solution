from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True  # An empty tree is symmetric

        def isMirror(t1: TreeNode, t2: TreeNode) -> bool:
            if not t1 and not t2:
                return True  # Both are null, so they are mirror images
            if not t1 or not t2:
                return False  # One is null and the other is not
            if t1.val != t2.val:
                return False  # Values don't match

            # Recursively check outer and inner pairs
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        return isMirror(root.left, root.right)

# -----------------------------
# Helper: build tree from list
# -----------------------------
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# -----------------------------
# Test cases
# -----------------------------
if __name__ == "__main__":
    sol = Solution()

    # Symmetric tree: [1,2,2,3,4,4,3]
    root1 = build_tree([1,2,2,3,4,4,3])
    print(sol.isSymmetric(root1))  # True

    # Not symmetric: [1,2,2,None,3,None,3]
    root2 = build_tree([1,2,2,None,3,None,3])
    print(sol.isSymmetric(root2))  # False

    # Single node (symmetric by default): [1]
    root3 = build_tree([1])
    print(sol.isSymmetric(root3))  # True

    # Empty tree (symmetric)
    root4 = build_tree([])
    print(sol.isSymmetric(root4))  # True
