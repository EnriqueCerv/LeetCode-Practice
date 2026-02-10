def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_head = Node(0)
        new_cur = new_head
        dummy = head
        cur = head

        while cur:
            new_cur.next = Node(cur.val)
            new_cur = new_cur.next
            cur = cur.next

        new_cur = new_head.next
        cur = head
        
        return new_head.next
