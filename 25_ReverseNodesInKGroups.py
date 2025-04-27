# %%
# # Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseKGroup(head, k):
    """
    :type head: Optional[ListNode]
    :type k: int
    :rtype: Optional[ListNode]
    """
    if head.next is None or k == 1:
        return head

    def reverseBetween(head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if head.next is None or left == right:
            return head

        # Create dummy head
        dummy = ListNode()
        dummy.next = head

        # Find the left - 1 node, i.e. last node before reversing
        pred = dummy
        for i in range(left - 1):
            pred = pred.next

        # First node to be reversed
        rev_start = pred.next
        cur = rev_start
        prev = None

        # Do the reversing
        for i in range(right - left + 1):
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp

        # Reconnect predecessor back to reversed list
        pred.next = prev
        # Reconnext the rest
        rev_start.next = cur

        cur = dummy.next
        while cur.next:
            cur = cur.next

        return cur

    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next

    left = 1
    right = left + k - 1
    dummy = ListNode()
    dummy.next = head
    cur_head = head

    while right <= n:
        rev_tail = reverseBetween(cur_head, left, right)
        left += k
        right += k
        cur_head = rev_tail.next

    return dummy.next
        


    
# %%
arr = [1,2,3,4,5]
dummy = ListNode()
cur = dummy
for ele in arr:
    cur.next = ListNode(ele)
head = dummy.next

k = 3

head = reverseKGroup(head, k)