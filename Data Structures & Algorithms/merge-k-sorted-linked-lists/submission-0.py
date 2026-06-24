# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        stack = [lists[0]]

        for ll in lists[1:]:
            res = ListNode()
            while stack:
                top = stack.pop()
                temp = res

                while ll and top:
                    if ll.val <= top.val:
                        temp.next = ll
                        ll = ll.next
                    else:
                        temp.next = top
                        top = top.next
                    temp = temp.next
                
                if ll:
                    temp.next = ll
                elif top:
                    temp.next = top

            stack.append(res.next)

        return stack[-1]
        