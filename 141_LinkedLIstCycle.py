def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
        
def hasCycle(self, head):
        seen = set()
        cur = head
        pos = 0
        while cur is not None:
            if cur not in seen:
                seen.add(cur)
                pos += 1
            else:
                return pos
            cur = cur.next
        return 0