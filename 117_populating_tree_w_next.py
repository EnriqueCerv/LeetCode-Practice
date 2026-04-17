"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        from collections import deque
        if not root:
            return

        dq = deque([root])

        while dq:
            level = len(dq)
            for idx in range(level):
                node = dq.popleft()

                if idx != level - 1:
                    node.next = dq[0]

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        
        return root
