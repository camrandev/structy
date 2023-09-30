class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# create a new node
# handle edge case of inserting a at the start

# perform location search -> stop 1 index before
# handle edge case of inserting a new head

# only need to track the current node, we can save the next pointer as needed when inserting


def insert_node(head, value, index):
    curr = head
    count = 0
    new_node = Node(value)

    # handle edgecase of inserting a new head -> remember to return the head
    if index == 0:
        new_node.next = curr
        return new_node

    # navigate across the list to the POI -> stop 1 index before thetarget
    while count != index - 1:
        curr = curr.next
        count += 1

    # handle the insertion
    nxt = curr.next
    curr.next = new_node
    new_node.next = nxt

    # return the head
    return head


# O(n) time complexity as each node is only visited once at most, and O(1) space complexity as extra variables do not change in size relative to input
