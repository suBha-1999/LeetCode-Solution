from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        def build(in_start: int, in_end: int, post_start: int, post_end: int) -> TreeNode:
            if in_start > in_end or post_start > post_end:
                return None

            root_val = postorder[post_end]
            root = TreeNode(root_val)
            
            root_in_index = inorder_map[root_val]
            left_size = root_in_index - in_start
            
            root.left = build(in_start, root_in_index - 1,
                              post_start, post_start + left_size - 1)
            
            root.right = build(root_in_index + 1, in_end,
                               post_start + left_size, post_end - 1)
            
            return root
        
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)


# --- Helper to print output in list form (like LeetCode format) ---
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
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


# --- Example Run ---
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

sol = Solution()
tree_root = sol.buildTree(inorder, postorder)

print(tree_to_list(tree_root))  # Output: [3, 9, 20, None, None, 15, 7]
