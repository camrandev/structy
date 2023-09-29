# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# save the current node
# save the previous node


# starting at the current node and contining until we hit a null value

# save the next node
# update the next pointer to the saved previous node
# update the previous node to the current node
# update the current node to the saved next node

# return the prev pointer, as it will be now pointing to the new head


def reverse_list(head):
    curr = head
    prev = None

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev
