# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0

        while cur:
            cur = cur.next
            length += 1
        
        k = length - n
        dummy = ListNode(0, head)
        cur = dummy

        for i in range(k):
            cur = cur.next
            
        if cur.next is None:
            return None
        if cur.next.next is None:
            cur.next = None
        else:
            cur.next = cur.next.next
        
        return dummy.next