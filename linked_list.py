# %%
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

# %%
# Create linked list from array
arr = [1,3,2,5,3,7,4,7,5,8,2]

head = ListNode(arr[0])
temp_node = head

for ele in arr[1:]:
    temp_node.next = ListNode(ele)
    temp_node = temp_node.next


# %%
# Sorting numbers from a linked list
arr = []

temp_node = head
while temp_node:
    arr.append(temp_node.val)
    temp_node = temp_node.next

arr.sort()
temp_node = head
for ele in arr:
    temp_node.val = ele
    temp_node = temp_node.next
# %%
# Insert sort directly on the list in O(1) memory

def sorted_insert(sorted_head, new_node):
    if sorted_head is None or new_node.val < sorted_head.val:
        new_node.next = sorted_head
        return new_node

    curr = sorted_head

    while curr.next and curr.next.val < new_node.val:
        curr = curr.next

    new_node.next = curr.next
    curr.next = new_node

    return sorted_head

def insertion_sort(head):
    sorted_head = None
    curr = head

    while curr:
        next_insert = curr.next 
        sorted_head = sorted_insert(sorted_head, curr)
        curr = next_insert

    return sorted_head
        
    

