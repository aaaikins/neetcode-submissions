# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # Step 1: Find the kth node
            kth = groupPrev
            for _ in range(k):
                if not kth:
                    break
                kth = kth.next
            if not kth:
                break

            # Step 2: Stop if fewer than k nodes remain
            groupNext = kth.next
            prev = groupNext
            curr = groupPrev.next

            # Step 3: Reverse the group
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Step 4: Reconnect the group
            oldHead = groupPrev.next
            groupPrev.next = prev
            groupPrev = oldHead
        
        return dummy.next