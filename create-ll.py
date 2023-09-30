class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# use dummy node approach, as it simplifies the insertion operation and allows us to automatically handle case of an empty input list of values


# create our dummy node
# create our tail to track insertion point, initializing it to dummy

# iterate over all of the values in the input list of vlaues
# create a new node with the current value
# set the tails next property to the new node
# update the tail to be the tails next property, tracking the insertion point

# return the dummy nodes next property, as that will point to the real head of the list


def create_linked_list(values):
    dummy = Node(None)
    tail = dummy

    for val in values:
        node = Node(val)
        tail.next = node
        tail = tail.next

    return dummy.next
