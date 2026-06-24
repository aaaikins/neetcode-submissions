# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        if not head:
            return
        dummy = ListNode(next=head)
        prev = dummy

        for _ in range(l-1):
            prev = prev.next

        start = prev.next

        for _ in range(r-l):
            temp = start.next
            start.next = temp.next
            temp.next = prev.next
            prev.next = temp


        return dummy.next