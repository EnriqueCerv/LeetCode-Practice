# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()

        remainder = 0
        cur = head

        while l1 or l2 or remainder:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + remainder
            if val > 9:
                remainder = 1
                val -= 10
            else: 
                remainder = 0
            cur.next = ListNode(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
        
        return head.next
        
        