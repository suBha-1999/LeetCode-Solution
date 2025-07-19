from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head  # Circle the list.

        t = length - k % length
        for _ in range(t):
            tail = tail.next
        newHead = tail.next
        tail.next = None

        return newHead
    

# Helper function to convert list to linked list
def list_to_linkedlist(items):
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for val in items[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to list (for displaying result)
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

    
sol = Solution()
head = [1,2,3,4,5]
k = 2

head_node = list_to_linkedlist(head)
rotated_head = sol.rotateRight(head_node, k)
print(linkedlist_to_list(rotated_head))

