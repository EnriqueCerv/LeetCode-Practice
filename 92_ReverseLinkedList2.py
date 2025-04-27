#%%
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    """
    :type head: Optional[ListNode]
    :type left: int
    :type right: int
    :rtype: Optional[ListNode]
    """
    arr = []
    cur = head
    while cur:
        arr.append(cur.val)
        cur = cur.next
    
    new_arr = arr[:left - 1] + arr[left - 1 : right][::-1] + arr[right :]
    new_head = ListNode()
    cur = new_head
    for ele in new_arr:
        cur.next = ListNode(ele)
        cur = cur.next
    
    return new_head.next
# %%
arr = [1,2,3,4,5]
left, right = 2, 4
dummy = ListNode()
cur = dummy
for ele in arr:
    cur.next = ListNode(ele)
    cur = cur.next

head = reverseBetween(dummy.next, left, right)
