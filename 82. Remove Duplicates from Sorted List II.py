from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            if prev.next == head:
                prev = prev.next
            else:
                prev.next = head.next
            head = head.next

        return dummy.next
    
# Helper: convert Python list to linked list
def list_to_linkedlist(lst):
    dummy = ListNode()
    curr = dummy
    for num in lst:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# Helper: convert linked list to Python list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage
sol = Solution()
head = list_to_linkedlist([1, 2, 3, 3, 4, 4, 5])
result_head = sol.deleteDuplicates(head)
print(linkedlist_to_list(result_head))
