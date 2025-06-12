
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            nxtPair = curr.next.next
            second = curr.next

            # Reverse this pair
            second.next = curr
            curr.next = nxtPair
            prev.next = second

            # Update pointers
            prev = curr
            curr = nxtPair

        return dummy.next


# Helper to convert list of values into a linked list
def build_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper to print linked list
def print_linked_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res



sol = Solution()

head = [1,2,3,4]
linked_lists = build_linked_list(head)

result = sol.swapPairs(linked_lists)
print(print_linked_list(result))