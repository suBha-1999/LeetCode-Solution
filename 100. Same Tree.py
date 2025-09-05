from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            nodeP = q1.popleft()
            nodeQ = q2.popleft()

            if nodeP is None and nodeQ is None:
                continue
            if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                return False

            q1.append(nodeP.left)
            q1.append(nodeP.right)
            q2.append(nodeQ.left)
            q2.append(nodeQ.right)

        return not q1 and not q2   # ensure both queues are empty


# ---------- Helper functions for testing ----------

def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a list (level order, with None as empty)."""
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    q = deque([root])
    i = 1
    while q and i < len(nodes):
        node = q.popleft()
        if node:
            if i < len(nodes) and nodes[i] is not None:
                node.left = TreeNode(nodes[i])
            q.append(node.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                node.right = TreeNode(nodes[i])
            q.append(node.right)
            i += 1
    return root

def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Converts a binary tree to list (level order) with None as empty."""
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)
    # trim trailing None
    while result and result[-1] is None:
        result.pop()
    return result


# ---------- Example Test Cases ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: both trees same
    p1 = build_tree([1, 2, 3])
    q1 = build_tree([1, 2, 3])
    print(sol.isSameTree(p1, q1))  # True

    # Example 2: different structure
    p2 = build_tree([1, 2])
    q2 = build_tree([1, None, 2])
    print(sol.isSameTree(p2, q2))  # False

    # Example 3: different values
    p3 = build_tree([1, 2, 1])
    q3 = build_tree([1, 1, 2])
    print(sol.isSameTree(p3, q3))  # False
