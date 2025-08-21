from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_less = ListNode(0)
        dummy_greater = ListNode(0)
        tail_less = dummy_less
        tail_greater = dummy_greater
        
        current = head
        while current:
            if current.val < x:
                tail_less.next = current
                tail_less = tail_less.next
            else:
                tail_greater.next = current
                tail_greater = tail_greater.next
            current = current.next
            
        tail_less.next = dummy_greater.next
        tail_greater.next = None
        
        return dummy_less.next


# Helper: Convert Python list → Linked List
def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

# Helper: Convert Linked List → Python list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


sol = Solution()
head = build_linked_list([1,4,3,2,5,2])
x = 3
new_head = sol.partition(head, x)
print(linked_list_to_list(new_head))