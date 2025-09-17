from typing import Optional
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        # Count number of nodes
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        self.head = head  # store as instance variable

        def build_bst_recursive(start, end):
            if start > end:
                return None

            # pick right middle to match LeetCode's sample output
            mid = (start + end + 1) // 2

            # Build left subtree
            left_child = build_bst_recursive(start, mid - 1)

            # Root node
            root = TreeNode(self.head.val)
            root.left = left_child

            # Move linked list head
            self.head = self.head.next

            # Build right subtree
            root.right = build_bst_recursive(mid + 1, end)

            return root

        return build_bst_recursive(0, count - 1)

# ---------------------------
# Helper functions for testing
# ---------------------------

def create_linked_list(values):
    """Convert Python list -> Linked list"""
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def inorder_traversal(root):
    """Return inorder traversal of BST"""
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

def level_order(root):
    """Return level order (LeetCode style)"""
    if not root:
        return []
    ans = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            ans.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            ans.append(None)
    # Trim trailing None
    while ans and ans[-1] is None:
        ans.pop()
    return ans

# ---------------------------
# Example Run
# ---------------------------

head = create_linked_list([-10, -3, 0, 5, 9])
sol = Solution()
bst_root = sol.sortedListToBST(head)

print(level_order(bst_root))
