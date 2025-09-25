from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        # Start with the leftmost node of the current level
        leftmost = root

        while leftmost.left:  # While there's a next level to process
            current = leftmost
            while current:
                # Connect left child to right child
                current.left.next = current.right

                # Connect right child to the left child of the next node (if it exists)
                if current.next:
                    current.right.next = current.next.left
                
                current = current.next  # Move to the next node at the current level
            
            leftmost = leftmost.left  # Move to the next level's leftmost node
        
        return root


# ---------------- Helper Functions ----------------
def build_perfect_tree(values):
    """Builds a perfect binary tree from a list of values (level order)."""
    if not values:
        return None
    
    nodes = [Node(val=v) if v is not None else None for v in values]
    n = len(values)

    for i in range(n):
        if nodes[i]:
            left_idx, right_idx = 2 * i + 1, 2 * i + 2
            if left_idx < n:
                nodes[i].left = nodes[left_idx]
            if right_idx < n:
                nodes[i].right = nodes[right_idx]
    return nodes[0]


def serialize_with_next(root: 'Node'):
    """Serialize tree into LeetCode format with '#' markers for next pointers."""
    output = []
    level_start = root
    while level_start:
        current = level_start
        while current:
            output.append(current.val)
            current = current.next
        output.append("#")
        level_start = level_start.left
    return output


# ---------------- Example Run ----------------
if __name__ == "__main__":
    values = [1,2,3,4,5,6,7]
    root = build_perfect_tree(values)

    sol = Solution()
    root = sol.connect(root)

    print("Output:", serialize_with_next(root))
