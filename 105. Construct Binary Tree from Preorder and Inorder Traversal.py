from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = inIdx = 0

        def dfs(limit):
            nonlocal preIdx, inIdx
            if preIdx >= len(preorder):
                return None
            if inorder[inIdx] == limit:
                inIdx += 1
                return None
            
            root = TreeNode(preorder[preIdx])
            preIdx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root

        return dfs(float('inf'))


# Helper: Level-order traversal to list (for printing the tree)
def treeToList(root: Optional[TreeNode]) -> List[Optional[int]]:
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
    # remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result


# Example usage
if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    sol = Solution()
    root = sol.buildTree(preorder, inorder)

    print("Tree as list (level-order):", treeToList(root))
