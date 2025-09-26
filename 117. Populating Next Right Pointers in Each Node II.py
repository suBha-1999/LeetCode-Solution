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

        queue = deque([root])

        while queue:
            level_size = len(queue)
            prev_node = None

            for _ in range(level_size):
                current_node = queue.popleft()

                if prev_node:
                    prev_node.next = current_node
                prev_node = current_node

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
        
        return root


# ---------------- Helper Functions ----------------
def build_tree(values):
    """Builds a binary tree (not necessarily perfect) from level-order input with None."""
    if not values or values[0] is None:
        return None

    nodes = [Node(val=v) if v is not None else None for v in values]
    q = deque([nodes[0]])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if not node:
            continue

        if i < len(values) and nodes[i] is not None:
            node.left = nodes[i]
            q.append(node.left)
        i += 1

        if i < len(values) and nodes[i] is not None:
            node.right = nodes[i]
            q.append(node.right)
        i += 1

    return nodes[0]


def serialize_with_next(root: 'Node'):
    """Serialize tree into LeetCode format with '#' markers for next pointers."""
    output = []
    level_start = root
    while level_start:
        current = level_start
        next_level = None
        while current:
            output.append(current.val)
            if not next_level:
                next_level = current.left or current.right
            current = current.next
        output.append("#")
        level_start = next_level
    return output


# ---------------- Example Run ----------------
if __name__ == "__main__":
    # Example: LeetCode 117 input
    values = [1,2,3,4,5,None,7]
    root = build_tree(values)

    sol = Solution()
    root = sol.connect(root)

    print("Output:", serialize_with_next(root))
