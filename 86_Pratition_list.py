class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        new_head = ListNode()
        new_tail = ListNode()
        cur, cur_head, cur_tail = head, new_head, new_tail

        while cur:
            if cur.val < x:
                cur_head.next = ListNode(cur.val)
                cur_head = cur_head.next
            else:
                cur_tail.next = ListNode(cur.val)
                cur_tail = cur_tail.next
            cur = cur.next
        
        cur_head.next = new_tail.next
        return new_head.next