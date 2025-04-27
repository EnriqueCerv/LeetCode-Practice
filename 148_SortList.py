
# %%
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def sortList( head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = head
        arr = []

        while cur:
            arr.append(cur.val)
            cur = cur.next
        arr.sort()

        head = ListNode()
        cur = head

        for ele in arr:
            # cur.val = ele
            cur.next = ListNode(val = ele)
            cur = cur.next
        
        return head.next
# %%
arr = [4,2,1,3]
dummyHead = ListNode()
cur = dummyHead
for ele in arr:
    cur.next = ListNode(ele)
    cur = cur.next
head = dummyHead.next

# %%
sortHead = sortList(head)