# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None


# set a variable to track the first value
# set a variable to track the current node

# start at the heads next value, see if that value is equal to the tracked value
# if not, return False

# return true


def is_univalue_list(head):
    ref = head.val
    curr = head.next

    while curr:
        if curr.val != ref:
            return False
        curr = curr.next

    return True
