# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None


# Think of rerouting the next pointers
# edge cases:
# removing tail -> handled by basic algorithm
# removing head -> return head.next, must be handled explicitly

# track current node -> init to head
# track previous node -> init to Null

# handle edge case of removing first node:
# we know we are removing the first node when prev is none
# if prev is none and val is target, return curr.next

# handle the rest of the cases
# if target equals current
# set previous.next to current.next

# if not equals
# update prev to current
# update current to current.next

# return the head


def remove_node(head, target_val):
    curr = head
    prev = None

    # handle the iteration
    while curr:
        # handle first node edge cases
        if curr.val == target_val and not prev:
            return curr.next
        # handle the rest of the algorithm
        elif curr.val == target_val:
            prev.next = curr.next
            return head
        else:
            prev = curr
            curr = curr.next
