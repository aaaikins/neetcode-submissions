"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
            
        visited = {}

        temp = head

        while temp:
            visited[temp] = Node(temp.val)
            temp = temp.next

        temp = head 
        while temp:
            new_node = visited[temp]

            new_node.next = visited.get(temp.next)

            new_node.random = visited.get(temp.random)

            temp = temp.next

        return visited[head]
        