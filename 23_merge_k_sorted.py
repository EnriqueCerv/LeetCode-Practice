# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        lists = [l for l in lists if l]

        if not lists:
            return None
        
        def merge2Lists(head1, head2):
            dummy = ListNode()
            curr = dummy
            while head1 and head2:
                if head1.val < head2.val:
                    curr.next = head1
                    head1 = head1.next
                else:
                    curr.next = head2
                    head2 = head2.next
                curr = curr.next
            curr.next = head1 or head2
            return dummy.next
        
        while len(lists) > 1:
            head1 = lists.pop()
            head2 = lists.pop()

            new_head = merge2Lists(head1, head2)
            lists.append(new_head)
        
        return lists[0]