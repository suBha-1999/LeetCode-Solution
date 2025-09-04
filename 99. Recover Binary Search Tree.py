from typing import Optional,List
from collections import deque



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        prev = None
        first = None
        second = None

        while curr:
            if not curr.left:
                if prev and curr.val < prev.val:
                    if not first:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    if prev and curr.val < prev.val:
                        if not first:
                            first = prev
                        second = curr
                    prev = curr
                    curr = curr.right

        first.val, second.val = second.val, first.val


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


# ---------- Example Test ----------

# Input: [1,3,None,None,2]
root = build_tree([1,3,None,None,2])

Solution().recoverTree(root)

print(tree_to_list(root))