import collections
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q = collections.deque([root])

        while q:
            curr_level_nodes = []
            level_size = len(q)

            for _ in range(level_size):
                node = q.popleft()
                curr_level_nodes.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(curr_level_nodes)

        return ans[::-1]


# --- Helper: Build tree from list input ---
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    q = collections.deque([root])
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


# --- Example Run ---
# Input like LeetCode style
tree_values = [3,9,20,None,None,15,7]
root = build_tree(tree_values)

sol = Solution()
output = sol.levelOrderBottom(root)

print(output)  # Expected: [[15, 7], [9, 20], [3]]
